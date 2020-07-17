param ([switch]$Next = $false, [string]$Repository)

$db = Get-Content version.db
$line = $db | Select-String "${Repository}:"

if ($line -match '(\d+)\.(\d+)\.(\d+)') {
    if ($Next) {
        $ver = "$($Matches[1]).$($Matches[2]).$([int]::Parse($Matches[3])+1)"
        $db = $db.Replace($line, "${Repository}:${ver}")
    } else {
        $ver = $Matches[0]
    }
} else {
    if ($Next) {
        $ver = "0.0.1"
        $db = $db + "${Repository}:${ver}" + [Environment].NewLine
    } else {
        $ver = "0.0.0"
    }
}

if ($Next) {
    $db | Set-Content version.db
}

Write-Host $ver
