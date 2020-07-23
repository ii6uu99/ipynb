@echo off

::设置本地为延迟扩展
setlocal EnableDelayedExpansion

git config --global core.autocrlf false


echo 对当前文件夹下的所有git存储库执行git push

::遍历当前文件夹，并进入文件夹
FOR /D %%d IN (*) DO (
  cd %%d

::执行主体命令
::取得文件名和github的仓库名一致
for /F "delims=?" %%i in ("%cd%") do set folder=%%~nxi
set url=git@github.com:ii6uu99/%folder%.git

if exist .git (
git add .
git commit -m "Auto Update"
:: origin master
git pull

) else (


git init
git remote add github %url%
git pull origin master
git add .
git commit -m init
type nul>README.md
)
git push -u origin master 

::执行主体命令完成，返回路径上一层，继续执行
  cd ..
)

pause