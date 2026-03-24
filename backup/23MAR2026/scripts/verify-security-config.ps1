$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$dockerfilePath = Join-Path $repoRoot "Dockerfile"
$composePath = Join-Path $repoRoot "compose.yaml"
$nginxConfigPath = Join-Path $repoRoot "nginx\default.conf"

$failures = [System.Collections.Generic.List[string]]::new()

foreach ($requiredPath in @($dockerfilePath, $composePath, $nginxConfigPath)) {
    if (-not (Test-Path $requiredPath)) {
        $failures.Add("Missing required file: $requiredPath")
    }
}

if (Test-Path $dockerfilePath) {
    $dockerfile = Get-Content $dockerfilePath -Raw

    if ($dockerfile -notmatch "COPY\s+nginx/default\.conf\s+/etc/nginx/conf\.d/default\.conf") {
        $failures.Add("Dockerfile must copy nginx/default.conf into the image.")
    }
}

if (Test-Path $composePath) {
    $compose = Get-Content $composePath -Raw

    if ($compose -match "(?ms)services:\s+app:.*?^\s+ports:") {
        $failures.Add("compose.yaml must not publish ports for the app service.")
    }

    if ($compose -notmatch "(?ms)services:\s+app:.*?^\s+networks:\s*$") {
        $failures.Add("compose.yaml must attach the app service to a Docker network.")
    }

    if ($compose -notmatch "(?m)^\s*proxy-net:\s*$") {
        $failures.Add("compose.yaml must define the proxy-net network.")
    }

    if ($compose -notmatch "(?m)^\s*external:\s*true\s*$") {
        $failures.Add("compose.yaml must use the existing external proxy network.")
    }
}

if (Test-Path $nginxConfigPath) {
    $nginxConfig = Get-Content $nginxConfigPath -Raw

    foreach ($requiredDirective in @(
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    )) {
        if ($nginxConfig -notmatch [regex]::Escape($requiredDirective)) {
            $failures.Add("nginx/default.conf must set $requiredDirective.")
        }
    }
}

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Host "Security config verification passed."
