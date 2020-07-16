echo ...... Creating bash script that configures shared folder on docker-machine
echo #!/bin/bash > %BASH_SCRIPT_NAME%
echo echo "mkdir -p %SHARED_FOLDER_MOUNT% && mount -t vboxsf -o uid=1000,gid=50 %SHARE_ID% %SHARED_FOLDER_MOUNT%" ^| sudo tee -a /mnt/sda1/var/lib/boot2docker/profile >> %BASH_SCRIPT_NAME%
echo exit >> %BASH_SCRIPT_NAME%
echo ...... Done!
