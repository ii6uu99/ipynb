Android运行Docker！(Termux + QEMU + linux_alpine, qemu网络映射)

 发表于 2019-08-15| 更新于 2020-02-26

https://stageguard.top/2019/08/15/run-docker-on-qemu-alpine/#·-测试

> 此教程将教你如何在Android端搭docker

# 1. Docker

Docker是一个开放源代码软件项目，让应用程序部署在软件货柜下的工作可以自动化进行，借此在Linux操作系统上，提供一个额外的软件抽象层，以及操作系统层虚拟化的自动管理机制。

(来自https://zh.m.wikipedia.org/wiki/Docker)

### **· 为什么在android不能使用docker**

众多厂商阉割掉了cgroup和namespace等docker需要的功能

### **· 你为什么还说要在android运行docker，标题党！**

……
所以我们这次用QEMU虚拟机模拟x86_64的linux系统

### **· 效率怎样**

**非常低**，在我骁龙625设备上运行docker指令大概需要15秒才有反应(alpine standard版)

### **· 那些有啥用啊**

~~没什么用，就是折腾，看着别人抱怨android不能运行docker而我能运行的感觉很爽，至少能运行~~

(废话连篇)

------

# 2. 准备工作

## ①. Termux

### 请看上一篇文章：[准备工作 Termux](https://stageguard.github.io/2019/07/30/run-gogs-on-android/#①-Termux)

## ②. Alpine Linux系统镜像

### **Small. Simple. Secure.**

### Alpine Linux is a security-oriented, lightweight Linux distribution based on musl libc and busybox.

(来自https://alpinelinux.org/)

使用Alpine的原因：

- 体积占用小，完全安装后的镜像不到1gb
- 安装快(废话)
- 内存占用小，idle状态仅占用30多MB内存

### 传送门：

standard-x86_64: [alpine-standard-3.10.1-x86_64.iso(v3.10.1, OfficialSite)](http://dl-cdn.alpinelinux.org/alpine/v3.10/releases/x86_64/alpine-standard-3.10.1-x86_64.iso)，或者在Termux中：



Bash



```
wget http://dl-cdn.alpinelinux.org/alpine/v3.10/releases/x86_64/alpine-standard-3.10.1-x86_64.iso
```

virtual-x86_64: [alpine-virt-3.10.1-x86_64.iso(v3.10.1, OfficialSite)](http://dl-cdn.alpinelinux.org/alpine/v3.10/releases/x86_64/alpine-virt-3.10.1-x86_64.iso)，或者在Termux中：



Bash



```
wget http://dl-cdn.alpinelinux.org/alpine/v3.10/releases/x86_64/alpine-virt-3.10.1-x86_64.iso
```

> 官网上写到visual版与standard版相似但对虚拟机有特殊优化。
> standard版我已测试成功，这次使用visual版。

## ③. VNC Viewer (可选)

用来连接qemu虚拟机的”显示器”，还可以连接蓝牙/OTG鼠标和键盘，非常强大

> 为什么是可选，因为qemu有不输出图像模式(-nographic)，直接在termux控制台输出，不需要”显示器”，但是有可能翻车。

### 传送门：

[VNC Viewer(GooglePlay)](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android)

------

# 3. 详细过程

## Ⅰ. 安装依赖

在Termux中：



Bash



```
pkg install x11-repo unstable-repo
pkg install qemu-utils qemu-system-x86_64
```

## Ⅱ. 创建虚拟镜像(硬盘)

在Termux中：



Bash



```
qemu-img create -f qcow2 virt-alpine.img 5g
```

[![创建镜像](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img1.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img1.jpg)

> 参数中`5g`代表创建一个最大容量为5g的镜像，可调节，最少2g以保证docker能正常安装。

## Ⅲ. 启动虚拟机

在Termux中：



Bash



```
qemu-system-x86_64 -hda virt-alpine.img -cdrom alpine-virt-3.10.1-x86_64.iso -boot d -m 512 -nographic
```

参数解释：

- `-hda` : 启动的虚拟硬盘
- `-cdrom` : 启动的光盘镜像文件(相当于用光盘安装windows)
- `-boot` : 启动槽位，选d ~~(我也不是太清楚)~~
- `-m` : 内存大小，单位mb
- `-nographic` : 无图像模式，直接在控制台输出
- `--vnc :1` : 以vnc为图像模式输出到”显示器”，并占用vnc 1端口

> 先使用`-nographic`模式启动，若长时间没出现alpine bootlog这界面，则先按`CTRL+X+A`结束进程(或用`htop`杀掉qemu进程)，再用`--vnc :1` vnc图像模式启动
> [![alpine bootlog](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img2.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img2.jpg)
> **如何连接：**

1. 打开VNC Viewer

2. 点击右下角加号(+)

3. Address填`localhost:1`(`--vnc`占用的端口)，name随意

4. 点击CREATE→CONNECT，就可以连接了

   (用VNC Viewer操作可能会麻烦，建议用蓝牙/OTG鼠标键盘)
   [![用VNC连接qemu"显示器"](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img3.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img3.jpg)

## Ⅳ. 安装Alpine到虚拟硬盘

### · 使用root账户登录：

[![登录到alpine](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img4.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img4.jpg)

### · 配置网络：

在alpine中，使用vi编辑器：



Bash



```
vi /etc/network/interfaces
```

添加如下配置



Code



```
auto lo
iface lo inet loopback
auto eth0
iface eth0 inet dhcp
```

保存后重启网络：



Bash



```
/etc/init.d/networking restart
```

[![网络重启成功](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img5.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img5.jpg)
这样alpine就能访问互联网了

### · 设置软件源：



Bash



```
setup-alpine
```

选择21(清华大学源)，等待更新即可

### · 安装：



Bash



```
setup-alpine
```

**详细配置：**

1. `Select keyboard layout: cn` (选择CN键盘布局)
2. `Select variant` (cn)
3. `Enter system hostname: stageguard` (输入hostname名称，随意)
4. `Which one do you want to initialize? (or '?' or 'done') [eth0]`
5. `Ip address for eth0? (or 'dhcp', 'none', '?') [10.0.2.15] dhcp` (选dhcp)
6. `Changing password for root` (修改root用户密码)
7. `Which timezone are you in? ('?' for list) [UTC] Asia/Shanghai` (时区填Asia/Shanghai)
8. `HTTP/FTP proxy URL? (e.g. 'http://proxy:8080', or 'none') [none]` (代理地址，默认none)
9. `Enter mirror number (1-47) or URL to add (or r/f/e/done) [f]: 21` (选择软件源，21(清华源))
10. `Which SSH server? ('openssh', 'dropbear' or 'none') [openssh]` (SSH服务器，选择openssh(默认))
11. `Which disk(s) would you like to use? (or '?' for help or 'none') [none]sda` (安装在何处，选sda)
12. `How would you like to use it? ('sys', 'data', 'lvm' or '?' for help) [?] sys` (安装方式，选sys)
13. `WARNING: Erase the above disk(s) and continue? [y/N]: y` (清除整个硬盘，y(是))

> 若出现网络问题：
> [![网络问题](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img6.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img6.jpg)
> 应该是默认dns服务器异常。
> 编辑`/etc/resolv.conf`
> 将`10.0.2.3`改为`8.8.8.8`即可
> `bash vi /etc/resolv.conf`

```
Installing system on /dev/sda3:`
`initramfs: creating /boot/it.....`
`Installation is complete. Please reboot.
```

安装完成，现在关闭虚拟机



Bash



```
poweroff
```

## Ⅴ. 启动Alpine并安装docker

### · 启动qemu虚拟机

在Termux中：



Bash



```
qemu-system-x86_64 -hda virt-alpine.img -boot c -m 512 -netdev user,id=nde1,hostfwd=tcp::2222-:22 -device e1000,netdev=nde1,id=d-net1 -nographic
```

参数解释：

- `-hda` : 启动的虚拟硬盘
- `-boot` : 启动槽位，选c ~~(我也不是太清楚)~~
- `-m` : 内存大小，单位mb
- `-netdev` : 网络配置，详情请看[QEMU_Wiki:Documentation/Networking](https://wiki.qemu.org/Documentation/Networking)
- `-device` : 设备配置(当前指向网络设备)
- `-nographic` : 无图像模式，直接在控制台输出
- `--vnc :1` : 以vnc为图像模式输出到”显示器”，并占用vnc 1端口

> `-netdev`参数中的`hostfwd`可以映射网络，当前配置会将虚拟机中22(SSH默认)端口映射到物理网络的2222端口上。

### · 配置SSHD(可选)

在Alpine中：



Bash



```
vi /etc/ssh/sshd_config
```

取消注释PermitRootLogin并修改为yes
[![修改sshd_config](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img7.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img7.jpg)
重启sshd

现在外部ssh就可以登录alpine的root账户了
在Termux中：



Bash



```
ssh root@localhost -p 2222
```

### · 添加community源

在alpine中，docker在其comminuty源里



Bash



```
vi /etc/apk/repositories
```

取消注释comminuty源
[![alpine源](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img8.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img8.jpg)
修改完成后，执行：



Bash



```
apk update
```

### · 安装docker



Bash



```
apk add docker
```

[![安装完成](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img9.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img9.jpg)

### · 修改docker为开机(虚拟机)启动，启动docker



Bash



```
#使docker开机启动
rc-update add docker
#开启docker服务
service docker start
#后台启动
setsid containerd
setsid dockerd
```

[![docker启动完成](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img10.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img10.jpg)

### · 测试



Bash



```
docker info
```

[![docker info](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img11.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-docker-img/img11.jpg)

# ***DOCKER 安装完成！\***

参考资料：

https://github.com/diogok/termux-qemu-alpine-docker/blob/master/README.md
https://stageguard.gitee.io/2019/07/30/run-gogs-on-android/

**文章作者:** [StageGuard](mailto:undefined)

**文章链接:** https://stageguard.top/2019/08/15/run-docker-on-qemu-alpine/

**版权声明:** 本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。转载请注明来自 [StageGuard](https://stageguard.top/)！