# Creates an Azure virtual machine and enables WinRM / CredSSP for use with Ansible
# You should probably disable unencrypted HTTP auth too, but I haven't here

Import-Module Az.Compute, Az.Accounts
Connect-AzAccount
write-host "Enter VM creds"
$creds = Get-Credential -Message "Enter VM creds"
$vmname = Read-Host -Prompt "Enter VM name"

$vm = New-AzVm `
        -Name $vmname `
        -Location "AustraliaEast" `
        -Credential $creds `
        -Size "Standard_DS3_v2" `
        -OpenPorts 3389,5986 # change the ports for whatever you need

$fqdn = $vm.FullyQualifiedDomainName;
write-host "Created VM, domain name is: $fqdn"
$username = $creds.UserName;
"full address:s:$fqdn" | out-file "~\desktop\$vmname.rdp";
"username:s:$vmname\$username" | out-file "~\desktop\$vmname.rdp" -Append;
write-host "Created RDP file on the desktop called $vmname.rdp"

# download the Ansible config script
Invoke-WebRequest https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1 -OutFile ConfigureRemotingForAnsible.ps1

# execute the Ansible config script on the VM
$vm | Invoke-AzVMRunCommand -CommandId 'RunPowerShellScript' -ScriptPath 'ConfigureRemotingForAnsible.ps1' -Parameter @{EnableCredSSP=1; DisableBasicAuth=1} -AsJob
