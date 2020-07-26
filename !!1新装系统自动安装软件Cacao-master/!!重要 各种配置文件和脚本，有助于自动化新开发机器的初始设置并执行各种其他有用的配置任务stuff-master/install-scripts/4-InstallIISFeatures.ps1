#IIS stuff
$iisFeatures = ("IIS-WebServerRole","IIS-WebServer","IIS-CommonHttpFeatures","IIS-HttpErrors","IIS-HttpRedirect",
        "IIS-ApplicationDevelopment","IIS-NetFxExtensibility45","IIS-HealthAndDiagnostics",
        "IIS-HttpLogging","IIS-LoggingLibraries","IIS-RequestMonitor","IIS-HttpTracing","IIS-Security",
        "IIS-URLAuthorization","IIS-RequestFiltering","IIS-IPSecurity","IIS-Performance","IIS-HttpCompressionDynamic",
        "IIS-WebServerManagementTools","IIS-ManagementScriptingTools","IIS-Metabase",
        "IIS-StaticContent","IIS-DefaultDocument","IIS-DirectoryBrowsing","IIS-WebSockets","IIS-ApplicationInit",
        "IIS-ASPNET45","IIS-CGI","IIS-ISAPIExtensions","IIS-ISAPIFilter",
        "IIS-ServerSideIncludes","IIS-CustomLogging","IIS-BasicAuthentication","IIS-HttpCompressionStatic",
        "IIS-ManagementConsole","IIS-ManagementService","IIS-WMICompatibility","IIS-LegacyScripts",
        "IIS-LegacySnapIn","IIS-CertProvider","IIS-WindowsAuthentication","IIS-DigestAuthentication",
        "IIS-ClientCertificateMappingAuthentication","IIS-IISCertificateMappingAuthentication");

foreach ($feature in $iisFeatures)
{
    if((Get-WindowsOptionalFeature -Online -FeatureName $feature).State -eq "Disabled")
    {
        write-host "Enabling $feature"
        Enable-WindowsOptionalFeature -Online -FeatureName $feature -NoRestart -All;
    }
    else
    {
        write-host "$feature already enabled"
    }
}

