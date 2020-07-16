ECHO OFF
:MENU
CLS
ECHO.
ECHO    ..............................................................
ECHO       PRESS 1, 2, 3, 4, 5, 6 to select your task, or 0 to EXIT
ECHO    ..............................................................
ECHO.
ECHO      1 - Init Docker Machine
ECHO      2 - Start Docker Machine
ECHO      3 - Stop Docker Machine
ECHO      4 - Restart Docker Machine
ECHO      5 - Regenerate Certs
ECHO      6 - Remove Docker Machine
ECHO.
ECHO      0 - EXIT
ECHO.
SET /P M=Type 1, 2, 3, 4, 5, 6, or 0 then press ENTER :
IF %M%==1 GOTO INIT
IF %M%==2 GOTO START
IF %M%==3 GOTO STOP
IF %M%==4 GOTO RESTART
IF %M%==5 GOTO REGENERATE
IF %M%==6 GOTO RM
IF %M%==0 GOTO EOF
GOTO :MENU

:INIT
CLS
call scripts\init.bat
pause
GOTO MENU

:START
CLS
call scripts\start.bat
pause
GOTO MENU

:STOP
CLS
call scripts\stop.bat
pause
GOTO MENU

:RESTART
CLS
call scripts\restart.bat
pause
GOTO MENU

:REGENERATE
CLS
call scripts\regenerate-certs.bat
pause
GOTO MENU

:RM
CLS
call scripts\rm.bat
pause
GOTO MENU

:EOF
