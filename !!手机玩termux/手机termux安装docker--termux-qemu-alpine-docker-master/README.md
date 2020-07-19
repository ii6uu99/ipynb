# Termux + Qemu + Alpine + Docker + VNC

https://github.com/diogok/termux-qemu-alpine-docker



这是用于通过Termux在android上运行docker的设置，并在qemu中运行alpine并在Alpine上启用docker。

仅在Samsung S10e上测试过。

## [安装Termux](https://termux.com/)

并开始。

## 设置VNC + Fluxbox

第一步是设置VNC和Fluxbox，遵循[termux VNC指南](https://wiki.termux.com/wiki/Graphic_Environment)非常容易：

启用x11存储库，安装tiger-vnc和fluxbox：

```
pkg install x11-repo
pkg install tigervnc fluxbox
```

他们启动vncserver，它将要求您设置密码和其他选项，只需按照屏幕上的说明进行操作：

```
vncserver
```

Xvnc将它们在后台运行。我们现在可以启动fluxbox：

```
DISPLAY=":1" fluxbox
```

这将在Xvnc服务器上启动fluxbox，并锁定当前终端。您也可以在该命令上附加一个“＆”以在后台启动它。

您可以在远程桌面上停止fluxbox。

您可以停止vnc：

```
vncserver -kill :1
```

要访问VNC服务器，请选择RDP客户端（例如Ubuntu上的Vinagre或Android上的VNC Viewer），然后在端口5901上连接到您的电话IP（用于显示：1）。

要在wifi上找到您的手机IP：

```
ip addr show wlan0
```

在Fluxbox内部，您可以右键单击桌面以获取菜单并启动“ aterm”之类的东西。

## 设置QEMU

Qemu的安装非常容易，只是需要注意的一点是，我不得不使用x11-repo中的qemu来代替不稳定的无头镜头，并且不知道为什么。

安装Qemu：

```
pkg install unstable-repo
pkg install qemu-system-x64_64 qemu-utils
```

这就对了。

## 准备在Qemu上安装Alpine

您将需要Alpine *虚拟* ISO，可以从[alpine网站](https://alpinelinux.org/)下载。将其另存为alpine.iso以便于键入：

```
pkg install curl
curl http://dl-cdn.alpinelinux.org/alpine/v3.10/releases/x86_64/alpine-virt-3.10.1-x86_64.iso -o alpine.iso
```

他们将需要一个映像磁盘来进行高山安装：

```
qemu-img create -f qcow2 alpine.img 5g
```

## 在QEMU上开始Alpine安装

他们可以启动Alpine的Qemu安装。如果您正在进行XVNC会话，它将启动QEMU窗口。

```
qemu-system-x86_64 -hda alpine.img -cdrom alpine.iso -boot d -m 512
```

如果要保留在同一终端上（不启动新窗口），则可以在最后一个命令后附加“ -nographic”。

如果在QEMU窗口上，则可以单击它以获取焦点，并可以按CTRL + ALT + G释放焦点。您也可以按CTRL + ALT + F进入全屏模式。

在终端上，您可以停止使用CTRL + A + X进行仿真。还有其他几个Ctrl + A命令。

高山启动需要一些时间，但是他们会为您提供一个“登录：”终端，只需输入“ root”即可启动。

## 在Qemu的Alpine上建立网络

这是我遇到的麻烦，在开始在Alpine内部进行安装之前，应先设置正确的网络。

首先，通过编辑*/ etc / network / interfaces*使其具有以下内容来设置接口：

```
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet dhcp
```

保存它，然后重新启动高山网络：

```
/etc/init.d/networking restart
```

您应该从Qemu用户网络获得IP。请注意，在此设置上*ping*不起作用。

仅通过它们，还需要通过将*/etc/resolv.conf*编辑为以下内容来添加DNS服务器：

```
nameserver 8.8.8.8
```

您可以通过尝试仅设置存储库进行测试：

```
setup-apkrepos
```

如果这为您提供了可供选择的存储库列表（大约40多个），它们就可以了。

## 安装高山

要开始安装：

```
setup-alpine
```

只需注意屏幕指示即可。提示时，请确保选择在磁盘“ sda”上安装。

安装完成后，通过发出停止命令来关闭Alpine。

```
halt
```

当它说系统停止运行时，退出Qemu（通过CTRL + Alt + g和关闭窗口，或在终端上通过ctrl + a + x退出）。

## 在Qemu上运行已安装的Alpine

要开始高山运动，只需运行：

```
qemu-system-x86_64 -hda alpine.img -boot c -m 512
```

这将花费一些时间，并为您设置的root用户提供登录提示。

## 在Alpine上安装Docker

我全部安装的原因是要[在alpine](https://wiki.alpinelinux.org/wiki/Docker)上[运行docker](https://wiki.alpinelinux.org/wiki/Docker)。

在高山上，编辑/ etc / pkg / repositories和取消注释社区存储库，它们安装docker：

```
apk update
apk add docker
```

启动服务并在启动时启用它：

```
service start docker
update-rc enable docker
```

测试一下

```
docker info
docker run alpine echo hello
```

## 有多慢？

在我的机器上，一个简单的hello world需要1s来回显，而在此设置下则需要25s。好吧，至少它能起作用...