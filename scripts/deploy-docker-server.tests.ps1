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

function Assert-NotContains {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Actual,

        [Parameter(Mandatory = $true)]
        [string] $UnexpectedSubstring,

        [Parameter(Mandatory = $true)]
        [string] $Message
    )

    if ($Actual.Contains($UnexpectedSubstring)) {
        $failures.Add("$Message`nUnexpected substring: $UnexpectedSubstring")
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
    -ImageName 'cardinalsixcyber:local' `
    -ContainerName 'cardinalsixcyber'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring 'docker compose build --no-cache app' `
    -Message 'Deploy script should force Compose to build the service image on the server.'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring "docker image inspect cardinalsixcyber:local --format 'built image {{.Id}} created {{.Created}}'" `
    -Message 'Deploy script should inspect the newly built service image before recreating the container.'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring "docker ps -a --format '{{.Names}}' | grep -Fxq 'cardinalsixcyber'" `
    -Message 'Deploy script should detect an existing fixed-name container before replacement.'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring 'docker rm -f cardinalsixcyber' `
    -Message 'Deploy script should remove the existing fixed-name container before starting the rebuilt app.'

Assert-Contains `
    -Actual $rebuildCommand `
    -ExpectedSubstring 'docker compose up -d --no-deps app' `
    -Message 'Deploy script should start the app from the image Compose just built.'

Assert-NotContains `
    -Actual $rebuildCommand `
    -UnexpectedSubstring 'docker push' `
    -Message 'Deploy script should not depend on Docker Hub publishing for the production server rebuild.'

Assert-NotContains `
    -Actual $rebuildCommand `
    -UnexpectedSubstring 'jbegarek/cardinalsixcyber' `
    -Message 'Deploy script should not reference the Docker Hub registry image because Watchtower can replace local builds with stale registry content.'

$statusLine = Parse-HttpStatusLine '  HTTP/1.1 200 OK'
Assert-Equal -Actual $statusLine.StatusCode -Expected 200 -Message 'HTTP status parser should extract numeric status codes.'

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Host 'All deploy script tests passed.'
