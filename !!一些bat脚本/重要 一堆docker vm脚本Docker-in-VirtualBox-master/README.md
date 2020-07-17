# Docker-in-VirtualBox

https://github.com/harmless-tech/Docker-in-VirtualBox





## 对于Windows

### 1.安装VirtualBox。

- [https://www.virtualbox.org/wiki/下载](https://www.virtualbox.org/wiki/Downloads)
- [确保在BIOS中启用了虚拟化。](https://www.howtogeek.com/213795/how-to-enable-intel-vt-x-in-your-computers-bios-or-uefi-firmware/)

### 2.安装Docker Desktop（或仅安装Docker Machine）。

- https://www.docker.com/products/docker-desktop
- https://github.com/docker/machine/releases
- 确保在启动时禁用Docker Desktop。
- 忽略有关容器和hyper-v的警告。
- 从任务栏退出Docker Desktop。

### 3.在VirtualBox中创建一个Docker Machine。

- 运行命令 `docker-machine create --driver=virtualbox Docker`
- 确保允许它创建网络适配器。

### 4.完成后，您现在将在VirtualBox中拥有一个Docker Machine。

## 访问Docker机器

### 1.下载docker vm脚本并将其[添加到您的路径。](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)

- 运行`dvm-start`以启动dvm。
- 运行`dvm-restart`以重新启动dvm。
- 运行`dvm-stop`以停止dvm。
- `dvm`在cmd中运行以添加dvm变量。
- `dvmp`在powrshell中运行以添加dvm变量。
- 运行`dvm-cmd`以使用dvm变量打开cmd。
- 运行`dvm-pshell`以使用dvm变量打开powershell。

## [转发端口](https://www.howtogeek.com/122641/how-to-forward-ports-to-a-virtual-machine-and-use-it-as-a-server/)