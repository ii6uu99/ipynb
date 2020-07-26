# Disable UAC for unattended install
Disable-UAC

# Get the base URI path from the ScriptToCall value
$bstrappackage = "-bootstrapPackage"
$helperUri = $Boxstarter['ScriptToCall']
$strpos = $helperUri.IndexOf($bstrappackage)
$helperUri = $helperUri.Substring($strpos + $bstrappackage.Length)
$helperUri = $helperUri.TrimStart("'", " ")
$helperUri = $helperUri.TrimEnd("'", " ")
$helperUri = $helperUri.Substring(0, $helperUri.LastIndexOf("/"))
$helperUri += "/scripts"
write-host "helper script base URI is $helperUri"

function executeScript {
    Param ([string]$script)
    write-host "executing $helperUri/$script ..."
	iex ((new-object net.webclient).DownloadString("$helperUri/$script"))
}

executeScript "SystemConfig.ps1";
executeScript "FileExplorerSettings.ps1";
executeScript "Browsers.ps1";
executeScript "WindowsExtras.ps1";
executeScript "CommonDevTools.ps1";
executeScript "SqlTools.ps1";
executeScript "AzureClient.ps1";
executeScript "VisualStudio.ps1";
executeScript "Utilities.ps1";

# Powershell install at the end so that it doenst cause issues with the rest of the script
choco install -y powershell-core

# Enable critical items 
Enable-UAC
Enable-MicrosoftUpdate
Install-WindowsUpdate -acceptEula
