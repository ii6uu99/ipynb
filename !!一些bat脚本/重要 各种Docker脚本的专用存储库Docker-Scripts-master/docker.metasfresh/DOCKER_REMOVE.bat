@echo off

SET MACHINE=metasfresh
IF NOT "%1"=="" SET MACHINE=%1

docker-machine rm %MACHINE%

:Exit
ECHO Done. Press any key.
pause > nul
