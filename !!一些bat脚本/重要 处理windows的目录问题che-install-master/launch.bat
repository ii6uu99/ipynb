@ECHO OFF 
REM 获取当前目录并转换为Unix格式
set f=%~dp0:\=/%&set h=%g::=%&set i=/%h%

REM 在目录名称末尾修剪空格
for /l %%a in (1,1,100) do if "!i:~-1!"==" " set i=!i:~0,-1!

docker run -v %i%:/che local

bin\test.bat