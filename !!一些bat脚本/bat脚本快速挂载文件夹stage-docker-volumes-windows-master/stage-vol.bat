::  
:: Stage directory to docker volume
::
::	Example:
::		stage-vol.bat volumeName c:\full\path\to\deploy\dir
::
::	Output:
::		docker volume ls:
::			DRIVER              VOLUME NAME
::			local               volumeName
:: 
::
::	How to use the resulting volume:
::
::		docker run --rm -it --name test-volume-transfer -v volumeName:/data alpine sh
::
::		# Within the shell you can do ls /data to see your folder
::		/ # ls /data
::		content1 content2 subfolder1 subfolder2
::
@ECHO OFF
IF NOT "%~2"=="" IF "%~3"=="" GOTO START
ECHO( 
ECHO This script requires 2 parameters: Docker volume name and path to directory to copy to volume
ECHO	Example:
ECHO		stage-vol.bat volumeName c:\full\path\to\deploy\dir
ECHO(
ECHO		`docker volume ls` output:
ECHO			DRIVER              VOLUME NAME
ECHO			local               volumeName
ECHO(
ECHO(
ECHO	How to use the resulting volume:
ECHO(
ECHO		docker run --rm -it --name test-volume-transfer -v volumeName:/data alpine sh
ECHO(
ECHO		# Within the shell you can do ls /data to see your folder
ECHO		/ # ls /data
ECHO		content1 content2 subfolder1 subfolder2
ECHO(
ECHO(
GOTO :EOF
:START
set volname=%1
set datadir=%2
echo %volname%
echo %datadir%
docker volume create %1
FOR /F %%i IN ('docker run --rm -d --name volume-stager -v %volname%:/data alpine sleep 1000') DO set "ctr=%%i"
docker cp %datadir%\. %ctr%:/data
docker stop %ctr%
echo "script end"

:EOF
