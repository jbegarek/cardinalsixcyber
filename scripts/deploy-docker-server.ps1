[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string] $SourceDir,
    [string] $HostName = 'justin@192.168.0.240',
    [string] $RemoteDir = '/home/justin/deploy/cardinalsixcyber',
    [string] $ImageName = 'jbegarek/cardinalsixcyber:latest',
    [string] $ContainerName = 'cardinalsixcyber',
    [string[]] $VerifyPaths,
    [string] $PublicBaseUrl
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -ErrorAction SilentlyContinue) {
    $PSNativeCommandUseErrorActionPreference = $false
}

function Get-DeployableRelativePaths {
    @(
        'src',
        'public',
        'data',
        'nginx',
        'astro.config.mjs',
        'tsconfig.json',
        'package.json',
        'package-lock.json',
        'Dockerfile',
        'compose.yaml',
        '.dockerignore'
    )
}

function Get-DefaultVerifyPaths {
    @('/', '/blog')
}

function Parse-HttpStatusLine {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Line
    )

    if ($Line -match 'HTTP\/\d+(?:\.\d+)?\s+(?<StatusCode>\d{3})(?:\s+(?<Reason>.*))?$') {
        $reason = ''
        if ($Matches.ContainsKey('Reason') -and $null -ne $Matches.Reason) {
            $reason = $Matches.Reason.Trim()
        }

        [pscustomobject]@{
            StatusCode = [int] $Matches.StatusCode
            Reason = $reason
            Raw = $Line.Trim()
        }
        return
    }

    throw "Could not parse HTTP status line: $Line"
}

function Get-RemoteRebuildCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string] $RemoteDir,

        [Parameter(Mandatory = $true)]
        [string] $ImageName,

        [Parameter(Mandatory = $true)]
        [string] $ContainerName
    )

@"
set -euo pipefail
cd $RemoteDir
docker buildx build --load --no-cache -t $ImageName .
docker push $ImageName
docker compose up -d --force-recreate --no-build
docker ps --filter name=$ContainerName --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'
"@
}

function Invoke-NativeCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string] $FilePath,

        [Parameter(Mandatory = $true)]
        [string[]] $ArgumentList
    )

    $stdoutPath = [System.IO.Path]::GetTempFileName()
    $stderrPath = [System.IO.Path]::GetTempFileName()

    try {
        $process = Start-Process `
            -FilePath $FilePath `
            -ArgumentList ($ArgumentList | ForEach-Object { ConvertTo-NativeArgument $_ }) `
            -NoNewWindow `
            -Wait `
            -PassThru `
            -RedirectStandardOutput $stdoutPath `
            -RedirectStandardError $stderrPath

        $output = @()
        foreach ($path in @($stdoutPath, $stderrPath)) {
            if ((Test-Path $path) -and (Get-Item $path).Length -gt 0) {
                $output += (Get-Content $path)
            }
        }

        [pscustomobject]@{
            ExitCode = $process.ExitCode
            Output = [string[]] $output
        }
    } finally {
        Remove-Item $stdoutPath, $stderrPath -ErrorAction SilentlyContinue
    }
}

function ConvertTo-NativeArgument {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Value
    )

    if ($Value -eq '') {
        return '""'
    }

    if ($Value -notmatch '[\s"]') {
        return $Value
    }

    $escaped = $Value -replace '(\\*)"', '$1$1\"'
    $escaped = $escaped -replace '(\\+)$', '$1$1'
    return '"' + $escaped + '"'
}

function Assert-CommandSucceeded {
    param(
        [Parameter(Mandatory = $true)]
        $Result,

        [Parameter(Mandatory = $true)]
        [string] $Label
    )

    if ($Result.ExitCode -ne 0) {
        $joinedOutput = $Result.Output -join [Environment]::NewLine
        throw "$Label failed with exit code $($Result.ExitCode).`n$joinedOutput"
    }
}

function Join-UrlPath {
    param(
        [Parameter(Mandatory = $true)]
        [string] $BaseUrl,

        [Parameter(Mandatory = $true)]
        [string] $Path
    )

    $trimmedBase = $BaseUrl.TrimEnd('/')
    $normalizedPath = if ($Path.StartsWith('/')) { $Path } else { "/$Path" }
    "$trimmedBase$normalizedPath"
}

function Invoke-DockerServerDeploy {
    param(
        [Parameter(Mandatory = $true)]
        [string] $SourceDir,

        [Parameter(Mandatory = $true)]
        [string] $HostName,

        [Parameter(Mandatory = $true)]
        [string] $RemoteDir,

        [Parameter(Mandatory = $true)]
        [string] $ImageName,

        [Parameter(Mandatory = $true)]
        [string] $ContainerName,

        [Parameter(Mandatory = $true)]
        [string[]] $VerifyPaths,

        [string] $PublicBaseUrl
    )

    foreach ($tool in @('ssh', 'scp')) {
        if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
            throw "Required tool not found in PATH: $tool"
        }
    }

    if ($PublicBaseUrl -and -not (Get-Command 'curl.exe' -ErrorAction SilentlyContinue)) {
        throw 'Public verification requires curl.exe to be available in PATH.'
    }

    $resolvedSourceDir = (Resolve-Path $SourceDir).Path
    $deployableItems = Get-DeployableRelativePaths
    $sourcePaths = foreach ($item in $deployableItems) {
        $fullPath = Join-Path $resolvedSourceDir $item
        if (-not (Test-Path $fullPath)) {
            throw "Deployable path missing from source directory: $fullPath"
        }

        $fullPath
    }

    Write-Host "Deploy source: $resolvedSourceDir"
    Write-Host "Remote target: ${HostName}:$RemoteDir"

    if ($PSCmdlet.ShouldProcess($HostName, "Ensure remote directory $RemoteDir exists")) {
        $mkdirResult = Invoke-NativeCommand -FilePath 'ssh' -ArgumentList @($HostName, "mkdir -p $RemoteDir")
        Assert-CommandSucceeded -Result $mkdirResult -Label 'Remote directory creation'
    }

    if ($PSCmdlet.ShouldProcess($HostName, 'Sync deployable files')) {
        # Delete managed directories on the remote before copying so removed local files don't persist.
        $dirItems = $deployableItems | Where-Object {
            (Get-Item (Join-Path $resolvedSourceDir $_)) -is [System.IO.DirectoryInfo]
        }
        $rmTargets = ($dirItems | ForEach-Object { "$RemoteDir/$_" }) -join ' '
        $rmResult = Invoke-NativeCommand -FilePath 'ssh' -ArgumentList @($HostName, "rm -rf $rmTargets")
        Assert-CommandSucceeded -Result $rmResult -Label 'Remote directory wipe'

        # Fresh copy of all deployable paths.
        $scpArgs = @('-r') + $sourcePaths + @("${HostName}:${RemoteDir}/")
        $scpResult = Invoke-NativeCommand -FilePath 'scp' -ArgumentList $scpArgs
        Assert-CommandSucceeded -Result $scpResult -Label 'File sync'
    }

    if ($PSCmdlet.ShouldProcess($HostName, 'Rebuild Docker image and recreate container')) {
        $remoteRebuildCommand = Get-RemoteRebuildCommand -RemoteDir $RemoteDir -ImageName $ImageName -ContainerName $ContainerName
        $rebuildResult = Invoke-NativeCommand -FilePath 'ssh' -ArgumentList @($HostName, $remoteRebuildCommand)
        Assert-CommandSucceeded -Result $rebuildResult -Label 'Remote Docker rebuild'
        $rebuildResult.Output | ForEach-Object { Write-Host $_ }
    }

    foreach ($verifyPath in $VerifyPaths) {
        if (-not $verifyPath.StartsWith('/')) {
            throw "Verify path must start with '/': $verifyPath"
        }

        if ($PSCmdlet.ShouldProcess($HostName, "Verify internal route $verifyPath")) {
            $verifyCommand = "docker exec $ContainerName wget -q -O /dev/null -S http://127.0.0.1$verifyPath 2>&1 | grep 'HTTP/'"
            $verifyResult = Invoke-NativeCommand -FilePath 'ssh' -ArgumentList @($HostName, $verifyCommand)
            Assert-CommandSucceeded -Result $verifyResult -Label "Internal route verification for $verifyPath"

            $statusLine = ($verifyResult.Output | Where-Object { $_ -match 'HTTP\/' } | Select-Object -Last 1)
            if (-not $statusLine) {
                throw "No HTTP status line returned for internal route $verifyPath"
            }

            $parsedStatus = Parse-HttpStatusLine $statusLine
            if ($parsedStatus.StatusCode -ne 200) {
                throw "Internal route verification failed for $verifyPath with status $($parsedStatus.StatusCode)"
            }

            Write-Host "Verified internal route: $verifyPath -> $($parsedStatus.StatusCode)"
        }

        if ($PublicBaseUrl -and $PSCmdlet.ShouldProcess($PublicBaseUrl, "Verify public route $verifyPath")) {
            $publicUrl = Join-UrlPath -BaseUrl $PublicBaseUrl -Path $verifyPath
            $curlResult = Invoke-NativeCommand -FilePath 'curl.exe' -ArgumentList @('-L', '-s', '-o', 'NUL', '-w', '%{url_effective} %{http_code}\n', $publicUrl)
            Assert-CommandSucceeded -Result $curlResult -Label "Public route verification for $publicUrl"

            $statusSummary = ($curlResult.Output | Select-Object -Last 1).Trim()
            if ($statusSummary -notmatch '\s200$') {
                throw "Public route verification failed for ${publicUrl}: $statusSummary"
            }

            Write-Host "Verified public route: $statusSummary"
        }
    }
}

if (-not $VerifyPaths -or $VerifyPaths.Count -eq 0) {
    $VerifyPaths = Get-DefaultVerifyPaths
}

if ($VerifyPaths.Count -eq 1 -and $VerifyPaths[0] -match ',') {
    $VerifyPaths = $VerifyPaths[0].Split(',', [System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { $_.Trim() }
}

if (-not $SourceDir) {
    $SourceDir = if ($PSScriptRoot) {
        Split-Path -Parent $PSScriptRoot
    } else {
        (Get-Location).Path
    }
}

if ($MyInvocation.InvocationName -ne '.') {
    Invoke-DockerServerDeploy `
        -SourceDir $SourceDir `
        -HostName $HostName `
        -RemoteDir $RemoteDir `
        -ImageName $ImageName `
        -ContainerName $ContainerName `
        -VerifyPaths $VerifyPaths `
        -PublicBaseUrl $PublicBaseUrl
}
