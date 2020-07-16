@echo off
cls
REM cd lyDoc
set/p str="输入提交信息(回车结束):"
@echo "%str%"
git pull
git add .
git commit -m "%str%"
git push
pause
