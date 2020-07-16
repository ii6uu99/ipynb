@echo off

set ABS_PATH=%~dp0
call %ABS_PATH%..\config.bat

echo ...... Stopping docker-machine
docker-machine stop %MACHINE_NAME%
echo ...... Done!
