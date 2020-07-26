#Requires -RunAsAdministrator
$ErrorActionPreference = "Inquire"

function Write-Heading
{
    $NL = [System.Environment]::NewLine
    Write-Host -ForegroundColor Blue "$NL $args $NL"
}

Write-Heading "Running tasks..."
$tasks = @(
    [pscustomobject]@{name="ahk shortcuts"; exec = "~\stuff\Matt's Shortcuts.ahk"},
    [pscustomobject]@{name="easywindowdrag"; exec = "~\stuff\EasyWindowDrag_(KDE).ahk"}
);

foreach ($task in $tasks)
{
    write-host "    Starting $($task.name)";
    . $task.exec
}

#clear scratch dir
Write-Heading "Clearing scratch dir..."
Remove-Item C:\scratch\* -Recurse -Force

#remove outlook reply sig
Write-Heading "Removing outlook reply sig..."
$profilesLocation = "HKCU:\Software\Microsoft\Office\16.0\Outlook\Profiles\"
$settings = (Get-ChildItem -Path $profilesLocation -Recurse | where {$_.GetValue("Account Name") -eq "Matt.Wanchap@cpal.com.au"})
$settings | Set-ItemProperty -Name "Reply-Forward Signature" -Value "(none)"

#kill exclaimer
Write-Heading "Killing exclaimer..."
Get-Process exsync -ErrorAction SilentlyContinue | Stop-Process -Force;

#kill osquery
Write-Heading "Killing osquery..."
Get-Service osqueryd -ErrorAction SilentlyContinue | Stop-Service
Get-Process osqueryd -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Heading "Copying spotlight images as wallpapers..."
& "~\stuff\Scripts\Windows Spotlight Wallpapers.ps1"

#check for outdated packages
Write-Heading "Checking for outdated packages..."
. choco upgrade all -y

Write-Heading "Done"
Read-Host "Press return to finish"
