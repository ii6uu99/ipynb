@echo off

REM The basis script

SET WK_DIR=%cd%
SET SCRIPT_PATH=%~dp0
SET MOUNT_POINT=/app

echo "Starting Ubuntu docker via %SCRIPT_PATH%ubuntu.cmd in the working Directory"

docker run ^
	--rm ^
	--name ubuntu ^
	-it ^
	-v %WK_DIR%:%MOUNT_POINT% ^
	--workdir %MOUNT_POINT% ^
	gerardnico/ubuntu:latest ^
	bash ^
	%*

