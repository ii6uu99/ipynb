echo ...... Configuring shared folder in VirtualBox
"%VBOX_PATH%\VBoxManage.exe" sharedfolder add "%MACHINE_NAME%" --automount --name %SHARE_ID% --hostpath %SHARED_FOLDER_PATH%
echo ...... Done!