::移动文件到自启动文件夹C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

set autogitfile=C:\Users\Administrator\cmder\autoupdate.cmd
::隐藏窗口
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin

::定时
:start

::存放执行命令

call %autogitfile%

::15分钟执行一次
choice /t 5 /d y /n >nul

goto start

pause