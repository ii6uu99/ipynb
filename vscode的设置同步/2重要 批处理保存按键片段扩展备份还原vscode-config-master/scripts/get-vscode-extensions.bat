@echo off

:: use vscode to list all installed extensions
:: pipe to xargs to construct commands
:: output to bat file
(code --list-extensions | xargs -L 1 echo call code --install-extension) > install-vscode-extensions.bat
