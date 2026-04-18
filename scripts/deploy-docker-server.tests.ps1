$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$scriptPath = Join-Path $PSScriptRoot 'deploy-docker-server.ps1'
. $scriptPath

$failures = [System.Collections.Generic.List[string]]::new()

function Assert-Equal {
    param(
        [Parameter(Mandatory = $true)]
        $Actual,

        [Parameter(Mandatory = $true)]
        $Expected,

        [Parameter(Mandatory = $true)]
        [string] $Message
    )

    if ($Actual -ne $Expected) {
        $failures.Add("$Message`nExpected: $Expected`nActual:   $Actual")
    }
}

function Assert-SequenceEqual {
    param(
        [Parameter(Mandatory = $true)]
        [string[]] $Actual,

        [Parameter(Mandatory = $true)]
        [string[]] $Expected,

        [Parameter(Mandatory = $true)]
        [string] $Message
    )

    $actualJoined = [string]::Join('|', $Actual)
    $expectedJoined = [string]::Join('|', $Expected)
    Assert-Equal -Actual $actualJoined -Expected $expectedJoined -Message $Message
}

function Assert-Contains {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Actual,

        [Parameter(Mandatory = $true)]
        [string] $ExpectedSubstring,

        [Parameter(Mandatory = $true)]
        [string] $Message
    )

    if (-not $Actual.Contains($ExpectedSubstring)) {
        $failures.Add("$Message`nMissing substring: $ExpectedSubstring")
    }
}

$expectedPaths = @(
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

Assert-SequenceEqual `
    -Actual (Get-DeployableRelativePaths) `
    -Expected $expectedPaths `
    -Message 'Deploy script should sync the expected Docker build inputs.'

Assert-SequenceEqual `
    -Actual (Get-DefaultVerifyPaths) `
    -Expected @('/', '/blog') `
    -Message 'Deploy script should verify the root page and blog index by default.'

$rebuildCommand = Get-RemoteRebuildCommand `
    -RemoteDir '/home/justin/deploy/cardinalsixcyber' `
    -ImageName 'jbegarek/cardinalsixcyber:latest' `
    -ContainerName 'cardinalsixcyber'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring 'docker buildx build --load --no-cache -t jbegarek/cardinalsixcyber:latest .' `
    -Message 'Deploy script should force a fresh buildx image load on the server.'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring 'docker compose up -d --force-recreate --no-build' `
    -Message 'Deploy script should recreate the running container from the freshly loaded image.'

$statusLine = Parse-HttpStatusLine '  HTTP/1.1 200 OK'
Assert-Equal -Actual $statusLine.StatusCode -Expected 200 -Message 'HTTP status parser should extract numeric status codes.'

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Host 'All deploy script tests passed.'
