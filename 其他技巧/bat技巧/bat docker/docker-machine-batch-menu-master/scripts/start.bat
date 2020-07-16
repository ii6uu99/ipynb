@echo off

set ABS_PATH=%~dp0
call %ABS_PATH%..\config.bat

echo ...... Starting docker-machine
docker-machine start %MACHINE_NAME%
echo ...... Done!

call %ABS_PATH%_configureEnv.bat
call %ABS_PATH%_postStart.bat
