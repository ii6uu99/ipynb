
call code --list-extensions > list.txt

REM @echo off

echo FOR /D %%%%p IN ("%%USERPROFILE%%\.vscode\extensions\*.*") DO rmdir "%%%%p" /s /q> install-extensions.cmd
(for /f "delims=" %%L in (list.txt) do @echo call code --install-extension %%L)>> install-extensions.cmd

echo rm -rf ~/.vscode/extensions> install-extensions.sh
(for /f "delims=" %%L in (list.txt) do @echo code --install-extension %%L)>> install-extensions.sh

del list.txt