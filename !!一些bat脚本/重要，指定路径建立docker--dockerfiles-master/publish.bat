@ECHO OFF
IF [%1] == [] GOTO error

setLocal
FOR %%F in (%1) DO SET REPO=%%~nxF
FOR /f %%i in ('powershell.exe . .\version.ps1 -Repository %REPO% -Next') DO SET VERSION=%%i

ECHO BUILDING %REPO%:%VERSION% ...
docker build -t dirty49374/%REPO%:%VERSION% %1
docker build -t dirty49374/%REPO%:latest %1

ECHO PUSHING %REPO%:%VERSION% ...
docker push dirty49374/%REPO%:%VERSION%
docker push dirty49374/%REPO%:latest

ECHO %REPO%:%VERSION% pushed
GOTO done

:error
ECHO publish.bat {path}

:done
