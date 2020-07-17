
set name=kaijigit.bat
set autofile=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
::判断开机自启动文件夹是否存在有文件
if exist %name% (
   echo "已经存在有该文件"
) else (
xcopy ./%name% %autofile% /s /e
)

pause