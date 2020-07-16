@echo off
git config --global core.autocrlf false
git add .
git commit -m "Auto Update"
git push -u origin master
pause