Import-Module 'C:\tools\poshgit\dahlbyk-posh-git-9bda399\src\posh-git.psd1'

# ALIASES
Set-Alias csi "C:\Program Files (x86)\Microsoft Visual Studio\2019\**\MSBuild\Current\Bin\Roslyn\csi.exe"
Set-Alias hex "C:\Program Files\HxD\HxD.exe"
Set-Alias sf 'force'
Set-Alias sfdx 'C:\Program Files\Salesforce CLI\bin\sfdx.cmd'
Set-Alias stree "C:\Program Files (x86)\Atlassian\Sourcetree\SourceTree.exe"

Clear-Host

[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12

function prompt
{
  #$p = Split-Path -leaf -path (Get-Location) #just gets last part of path
  $origLastExitCode = $LASTEXITCODE
  Write-Host $ExecutionContext.SessionState.Path.CurrentLocation -NoNewline
  Write-VcsStatus
  $LASTEXITCODE = $origLastExitCode
  "`n$('>' * ($nestedPromptLevel + 1))"
}

function search
{
    #todo: need a way to exclude binary files
    param
    (
        [string]$filePattern="*.*",
        [string]$searchStr
    )

    get-childitem $filePattern -Recurse | sls $searchStr -Context 1,1
}

function Obliterate
{
    remove-item $args -force -recurse -confirm
}

function SFFields
{
    (force describe -n="$($args[0])" -t=sobject | ConvertFrom-Json).Fields | Sort-Object name | Select-Object -ExpandProperty name
}

function SFUser
{
    <#
    .SYNOPSIS
        Opens the Salesforce user profile page for the first user returned by a query for a partial username match
    .EXAMPLE
        SFUser matt.wanchap
    .PARAMETER
        The only parameter is the username, which does not need to be complete.  The query uses LIKE so only part of the name needs to be provided.
    #>
    [CmdletBinding()]
    param
    (
        [Parameter(Mandatory)]
        [string]$username
    )

    $users = (force query --format csv "select id from user where username like '%$username%' and isactive=true" | convertfrom-csv)
    
    if($users.Count -eq 0)
    {
        Write-Host "No users found";
        return;
    }
    else
    {
        foreach($user in $users)
        {
            Start-Process -filepath "https://cpal.my.salesforce.com/$($user.Id)?noredirect=1&isUserEntityOverride=1" 
        }
    }
}

function SFUserID
{
    (force query "SELECT Id FROM User WHERE Name LIKE '%$($args[0])%' LIMIT 1" --format:csv | ConvertFrom-Csv).Id
}

function SFQuery
{
    force query --format json $args[0] | ConvertFrom-Json
}

function SFUpdate
{
    Param($Type, $Where, $Update)
    #eg: SFUpdate -Type Contact -Where "OwnerId='$(sfuserid Kirsty)'" -Update "OwnerId:$(sfuserid Isabelle)"
    force query "select Id FROM $Type WHERE $Where" --format:csv | ConvertFrom-Csv | % {force record update $Type $_.Id $Update }
}

function SFRecTypes
{
    force describe -t=sobject -n="$($args[0])" | convertfrom-json | Select-Object -ExpandProperty recordTypeInfos
}

# Chocolatey profile
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
