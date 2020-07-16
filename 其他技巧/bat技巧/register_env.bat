@echo off

echo add sg generator evn

::输出空行

echo: 
set generator_home=%cd%
echo SG_GENERATOR_HOME %generator_home%
echo:

::/M表示设置到全局的环境变量

setx SG_GENERATOR_HOME "%generator_home%" /M
call register_user_path.bat %SG_GENERATOR_HOME%\bin
echo Congratulations, your setup was successful
echo:
echo At the end of the operation, press enter to exit...

pause>nul

register_user_path.bat

:: PATH-ADD - add a path to user path environment variable
@echo off
setlocal
:: set user path
set ok=0
for /f "skip=2 tokens=3*" %%a in ('reg query HKCU\Environment /v PATH') do if [%%b]==[] ( setx PATH "%%~a;%1" && set ok=1 ) else ( setx PATH "%%~a %%~b;%1" && set ok=1 )
if "%ok%" == "0" setx PATH "%1"
:end
endlocal
echo.
