

# WSL 修改默认登录用户为root（转）

# [https://www.cnblogs.com/edhg/p/11563387.html](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fedhg%2Fp%2F11563387.html) 





[WSL 修改默认登录用户为root](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fedhg%2Fp%2F11563387.html)

C:\Users\用户名\AppData\Local\Microsoft\WindowsApps\ubuntu1804.exe config --default-user root



如

C:\Users\Administrator\AppData\Local\Microsoft\WindowsApps\ubuntu.exe config --default-user root



在管理员cmd中运行net stop lxssmanager

net stop LxssManager
net start LxssManager

再次打开wsl, 即可看到默认登录用户为root

因为修改了默认用户, 默认进入的目录也变了, 可以通过在Linux中运行此命令修改默认进入的目录

echo "cd ~用户名" >> ~/.bashrc