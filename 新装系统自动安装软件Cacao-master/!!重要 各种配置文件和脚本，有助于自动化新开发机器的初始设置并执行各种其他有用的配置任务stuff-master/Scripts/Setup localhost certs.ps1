Import-Module WebAdministration

#check that the cert doesn't already exist
$currentCert = (Get-Childitem Cert:\CurrentUser\Root\ | where Subject -eq CN=*.localhost.com)

if($currentCert -ne $null)
{
    Write-Error "Root localhost cert is already installed.  Open Certificate management and delete it, then re-run this script"
    return;
}

$domain = "*.localhost.com", "localhost"
Write-Host "Creating self-signed cert for $domain"
$cert = New-SelfSignedCertificate -DnsName $domain -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5)
$thumb = $cert.Thumbprint

Write-Host "Updating existing cert bindings used by IIS Express with new self-signed cert"

foreach ($port in 44300..44399) {
    # silence the success output spam with  & { } 1 > $null
    & { netsh http delete sslcert ipport=0.0.0.0:$port } 1 > $null
    & { netsh http add sslcert ipport=0.0.0.0:$port certhash=$thumb appid=`{214124cd-d05b-4309-9af9-9caa44b2b74a`} } 1 > $null
}

Write-Host "Adding self-signed cert to root cert authority so it's always trusted"
$StoreScope = 'LocalMachine'
$StoreName = 'root'
$Store = New-Object  -TypeName System.Security.Cryptography.X509Certificates.X509Store  -ArgumentList $StoreName, $StoreScope
$Store.Open([System.Security.Cryptography.X509Certificates.OpenFlags]::ReadWrite)
$Store.Add($cert)
$Store.Close()

# update all existing SSL bindings to use the new cert
Get-WebBinding -protocol https | Foreach-Object { $_.AddSslCertificate($thumb, "My") }
Write-Host "Completed self-signed cert setup"
