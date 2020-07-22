if([IntPtr]::Size -eq 4)
{
    write-error "You're using a 32-bit (x86) powershell instance, which is going to break things later on. Ensure you're running the 64-bit version!"
    return
}

"Step 1 at $((Get-Date).ToLongTimeString())" >> progress.txt
. ~\stuff\install-scripts\1-InstallImportantThingsWithChoco.ps1

"Step 2 at $((Get-Date).ToLongTimeString())" >> progress.txt
. ~\stuff\install-scripts\2-ScheduleTasks.ps1

Start-Sleep -Seconds 5

"Restarting at $((Get-Date).ToLongTimeString())" >> progress.txt
Restart-Computer
