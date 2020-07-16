@echo off

set ABS_PATH=%~dp0
call %ABS_PATH%..\config.bat

echo ...... Certificates regeneration
docker-machine rm -f %MACHINE_NAME%
echo ...... Done!
