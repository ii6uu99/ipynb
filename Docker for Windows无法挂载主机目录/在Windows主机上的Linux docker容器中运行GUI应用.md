# 在Windows主机上的Linux docker容器中运行GUI应用

[＃码头工人](https://dev.to/t/docker) [＃软件](https://dev.to/t/software) [＃个应用](https://dev.to/t/apps) [＃桂](https://dev.to/t/gui)

[![darksmile92头像](https://res.cloudinary.com/practicaldev/image/fetch/s--v8J8QiF4--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/41170/c66534e9-5530-418d-8cd1-9fbf48fa5681.jpeg)罗宾·克雷茨马尔](https://dev.to/darksmile92)五月22 ・ 3分钟阅读



https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde



# 这是什么意思

Docker具有许多优势，因此能够通过隔离在Docker容器中的GUI使用应用程序就是其中之一。例如您的浏览器，TextEditor或其他。

毫不夸张地说，这将使您能够在Windows主机上使用linux / macOS软件，而不会遇到一些麻烦。同样，这将防止您的机器在删除应用程序时具有剩余的依赖项，因为所有这些都保留在docker容器中。

# 为什么有人甚至会尝试这样做？

我在家中的私人计算机上使用Arch Linux，而在工作中使用Windows 10。我希望能够在Windows机器上使用Evolution邮件客户端和其他方便的linux应用程序。

因此，有许多关于如何从Linux主机与Linux容器共享X11-Session的教程。但：

# 如何从Windows主机共享显示？

## 安装VcXsrv并对其进行配置

首先，安装[VcXsrv Windows X Server](https://sourceforge.net/projects/vcxsrv/)。我们也可以使用Xming，但是Windows软件包自2013年以来就没有更新。最简单的方法是使用[Chocolatey](https://chocolatey.org/)，这是我最喜欢的Windows软件包管理器！
因此，启动一个PowerShell会话并运行：

```
choco install vcxsrv
```

然后从开始菜单运行**Xlaunch**并执行初始配置步骤：**确保在单击完成之前保存到配置文件！** 将其保存到以下位置之一：
[![设置1](https://res.cloudinary.com/practicaldev/image/fetch/s--MCnNoPwj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/g3roivsrapgy69mqkhpc.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--MCnNoPwj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/g3roivsrapgy69mqkhpc.png)
[![设置2](https://res.cloudinary.com/practicaldev/image/fetch/s--9T2fJDCh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/5l5fil0nongqswsc5qx5.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--9T2fJDCh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/5l5fil0nongqswsc5qx5.png)
[![设置3](https://res.cloudinary.com/practicaldev/image/fetch/s--1fOShFRZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/3eh1lry7125modpdj6a2.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--1fOShFRZ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/3eh1lry7125modpdj6a2.png)
[![设置4](https://res.cloudinary.com/practicaldev/image/fetch/s--GFylK6hC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/48tl3o3pv99vbhk06188.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--GFylK6hC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/48tl3o3pv99vbhk06188.png)



- %appdata%\Xming
- %userprofile%\Desktop
- %userprofile%

## 创建一个Dockerfile

要使用一个简单的示例，请创建一个新文件夹并在其中放置以下内容的*Dockerfile*：

```
FROM ubuntu:14.04
RUN apt-get update && apt-get install -y firefox
CMD /usr/bin/firefox
```

## 生成并运行容器

对于高级Docker用户，请使用以下快速命令：

```
docker build -t firefox .
set-variable -name DISPLAY -value YOUR-IP:0.0
docker run -ti --rm -e DISPLAY=$DISPLAY firefox
```

### 有一些解释：

现在构建新容器并将其标记为*firefox*：

```
docker build -t firefox .
```

因为容器具有其自己的localhost接口，所以我们需要使用网络适配器的IP地址。
找出您的IP地址

```
ipconfig
```

设置环境变量（用您的替换IP）：

```
set-variable -name DISPLAY -value 10.11.128.118:0.0
```

在cmd上运行容器：

```
docker run -ti --rm -e DISPLAY=$DISPLAY firefox
```

现在，您应该看到一个Firefox窗口：
[![火狐浏览器](https://res.cloudinary.com/practicaldev/image/fetch/s--d_jpgRzm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/zbbfl8ytpwmd9erj9hxh.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--d_jpgRzm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/zbbfl8ytpwmd9erj9hxh.png)

这将适用于大多数其他应用。

## 持久数据

要持久保存数据（例如Evolution邮件），请通过docker卷安装正确位置的容器。

找出所有位置，您的应用程序在其中存储要保留的数据并进行装载：

```
docker run -v c:/docker/evolutionmail/home/user/.local/share/evolution:/root/.local/share/evolution -v c:/docker/evolutionmail/home/user/.config/evolution:/root/.config/evolution -ti --rm -e DISPLAY=$DISPLAY evolution
```

## 用于演化邮件的示例Dockerfile

如果有人需要，这是我的演变Dockerfile：

```
FROM debian
# Setup enviroment variables
ENV DEBIAN_FRONTEND noninteractive

# Installing fuse filesystem is not possible in docker without elevated priviliges
# but we can fake installling it to allow packages we need to install for GNOME
RUN apt-get install libfuse2 -y && \
cd /tmp ; apt-get download fuse && \
cd /tmp ; dpkg-deb -x fuse_* . && \
cd /tmp ; dpkg-deb -e fuse_* && \
cd /tmp ; rm fuse_*.deb && \
cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && \
cd /tmp ; dpkg-deb -b . /fuse.deb && \
cd /tmp ; dpkg -i /fuse.deb

# Upstart and DBus have issues inside docker.
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

# Install GNOME
RUN apt-get update && apt-get install -y xorg gnome-core gnome-session-fallback
# Pull in the hack to fix keyboard shortcut bindings for GNOME 3 
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/gnome-keybindings.pl /usr/local/etc/gnome-keybindings.pl
RUN chmod +x /usr/local/etc/gnome-keybindings.pl

# Add the script to fix and customise GNOME for docker
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/gnome-docker-fix-and-customise.sh /usr/local/etc/gnome-docker-fix-and-customise.sh
RUN chmod +x /usr/local/etc/gnome-docker-fix-and-customise.sh

RUN apt-get update -y && apt-get install -y dbus-x11 gnome-keyring evolution evolution-data-server seahorse sudo
RUN apt-get install -y libnotify-cil-dev
CMD ["evolution"]
```

我很好奇，看到您在评论中使用了docker化！

〜干杯





接触powershell权限

我注意到Windows防火墙可以阻止与容器的连接。您可以通过“ VcXsrv Windows xserver”的防火墙设置允许此访问。另外，如果只想授予xserver专用网络访问权限，则可以使用：

```
Set-NetConnectionProfile -interfacealias "vEthernet (DockerNAT)" -NetworkCategory Private
```



