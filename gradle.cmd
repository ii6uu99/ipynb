
echo 隐藏窗口
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin

:start
cd /d C:\Users\Administrator\cmder
call autoupdate.cmd
choice /t 20 /d y /n >nul
goto start

pause