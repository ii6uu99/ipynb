@echo off

:: remove existing config
rmdir /S /Q "%appdata%\Code\User"

:: make junction
mklink /J "%appdata%\Code\User" "%~dp0..\User"

