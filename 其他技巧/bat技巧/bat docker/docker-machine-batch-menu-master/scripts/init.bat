@echo off

set ABS_PATH=%~dp0
call %ABS_PATH%..\config.bat

call %ABS_PATH%_createDockerMachine.bat
call %ABS_PATH%_createBashScript.bat
call %ABS_PATH%_configureSharedFolderOnDockerMachine.bat
call %ABS_PATH%stop.bat
call %ABS_PATH%_configureSharedFolderOnVirtualBox.bat
call %ABS_PATH%start.bat
