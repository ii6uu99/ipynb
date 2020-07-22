Import-Module ScheduledTasks

function ScheduleStartupTask
{
    param
    (
        [string]$TaskName,
        [string]$TaskDescription,
        [string]$ExecPath,
        [Microsoft.PowerShell.Cmdletization.GeneratedTypes.ScheduledTask.RunLevelEnum]$RunLevel,
        $ExecArgs
    )

    $oldTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

    if ($oldTask -ne $null)
    {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false 
    }

    $actionParams = @{ Execute = $ExecPath }

    if ($ExecArgs)
    {
        $actionParams.Add("Argument", $ExecArgs)
    }

    $action = New-ScheduledTaskAction @actionParams
    $trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -RunLevel $RunLevel
    $settings = New-ScheduledTaskSettingsSet
    $settings.DisallowStartIfOnBatteries = $false
    $settings.StopIfGoingOnBatteries = $false
    $newTask = New-ScheduledTask -Action $action -Principal $principal -Trigger $trigger -Settings $settings -Description TaskDescription
    Register-ScheduledTask -TaskName $TaskName -InputObject $newTask
}

ScheduleStartupTask -TaskName "startup tasks" -TaskDescription "Runs startup tasks script" -ExecPath "powershell" -ExecArgs "-NoProfile -Command "". '~\stuff\startup tasks.ps1'""" -RunLevel Highest;
ScheduleStartupTask -TaskName "continue setup - install other things 1" -TaskDescription "runs the next steps in parallel" -ExecPath "powershell" -ExecArgs "-NoProfile -Command "". '~\stuff\install-scripts\3-InstallOtherSoftware.ps1'""" -RunLevel Highest;
ScheduleStartupTask -TaskName "continue setup - install other things 2" -TaskDescription "runs the next steps in parallel" -ExecPath "powershell" -ExecArgs "-NoProfile -Command "". '~\stuff\install-scripts\4-InstallIISFeatures.ps1'""" -RunLevel Highest;

