@echo off
git config --global core.autocrlf false
for /F "delims=?" %%i in ("%cd%") do set folder=%%~nxi
set url=git@github.com:ii6uu99/%folder%.git

if exist .git (
git add .
git commit -m submit-auto
git pull github master

) else (


git init
git remote add github %url%
git pull github master
git add .
git commit -m init
)
git push github master -u

pause