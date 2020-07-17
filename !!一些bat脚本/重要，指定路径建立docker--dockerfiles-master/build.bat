@ECHO OFF
IF [%1] == [] GOTO error

setLocal
FOR %%F in (%1) DO SET REPO=%%~nxF

docker build -t dirty49374/%REPO%:latest %1
GOTO done

:error
ECHO build.bat {path}

:done
