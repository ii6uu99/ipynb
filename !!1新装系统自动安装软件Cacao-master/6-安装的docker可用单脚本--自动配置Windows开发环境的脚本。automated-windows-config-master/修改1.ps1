# Installs Chocolately onto your machine
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

#安装 git
choco install git -y
choco install vscode -y 
choco install docker-desktop -y 
choco install f.lux -y
choco install wox -y
choco install typora -y

#choco install kubernetes-cli -y
#choco install kubernetes-helm -y
choco install 7zip.install -y
choco install vagrant -y

#https://blog.csdn.net/ChinarCSDN/article/details/82914429
#热键设置
#安装 AutoHotkey (Portable)
choco install autohotkey.portable -y

#安装 python
choco install python -y

#Google Chrome (64-bit only)
choco install google-chrome-x64 -y

#安装 firefox
choco install firefox -y

#安装 notepad++
choco install notepadplusplus.install -y

#截图软件
choco install ShareX -y

#wsl的gui工具
choco install vcxsrv -y

#KDiff3官方版是一款小巧专业的实用型文件合并以及目录比较工具
choco install KDiff3 -y