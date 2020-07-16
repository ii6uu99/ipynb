pip install nbopen
python -m nbopen.install_win
assoc .whl=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"
assoc .md=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"
assoc .py=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"
