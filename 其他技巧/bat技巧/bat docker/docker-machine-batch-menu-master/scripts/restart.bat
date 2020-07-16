@echo off

set ABS_PATH=%~dp0
call %ABS_PATH%..\config.bat

echo ...... Restarting docker-machine
docker-machine restart %MACHINE_NAME%
echo ...... Done!

call %ABS_PATH%_postStart.bat
