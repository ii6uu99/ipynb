::PRE INSTALLER
echo installing limit disabler
START .\downloads\crack.exe
echo setting up ckis updater
START .\downloads\ckis-updater-master\build\bypass.bat


::DEV INSTALLER
echo Starting installation for db Browser
START .\downloads\DB.Browser.for.SQLite-3.11.2-win32.msi
PAUSE 20
echo Starting installation for git 
START .\downloads\Git-2.23.0-32-bit.exe
PAUSE 20
echo Starting installation for melon player
START .\downloads\Melon4Setup.exe
PAUSE 20
echo Starting installation for python3
START .\downloads\python-3.7.4.exe
PAUSE 20
echo Starting installation for vs code
START .\downloads\VSCodeUserSetup-ia32-1.38.0.exe
PAUSE 20
