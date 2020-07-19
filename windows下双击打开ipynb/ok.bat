pip install nbopen
python -m nbopen.install_win
assoc .whl=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"
rem assoc .md=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"
rem assoc .py=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"

pause
