Android搭建私人Git服务！(Termux + MySQL + Gogs 的搭建，运行，Frp内网穿透)

 发表于 2019-07-30| 更新于 2020-02-26

字数总计:1.5k|阅读时长: 5 分钟

|阅读量:316

> 此教程将教你如何在Android端搭建Gogs服务端(使用MySQL数据库)
> **原文已修改，此教程并不针对无基础的新手**

# 0x00 前言

## 什么是Gogs

Gogs 是一款极易搭建的自助 Git 服务。

## 开发目的

Gogs 的目标是打造一个最简单、最快速和最轻松的方式搭建自助 Git 服务。使用 Go 语言开发使得 Gogs 能够通过独立的二进制分发，并且支持 Go 语言支持的 所有平台，包括 Linux、Mac OS X、Windows 以及 ARM 平台。

------

# 0x01 准备工作

## ① Termux

Termux是一款非常强大的终端模拟软件，拥有真实的Linux指令，并且有apt软件包管理程序，可以说没有桌面linux系统，它就是最好的替代品(当然我们这次在手机上，当然没有桌面linux系统)！

### 传送门：

[Termux(CoolApk, v0.65)](https://www.coolapk.com/apk/com.termux)
[Termux(Google Play, v0.73)](https://play.google.com/store/apps/details?id=com.termux)

## ② Gogs二进制程序

核心部件，包括可执行二进制文件gogs，用于开启本地git服务。

### 传送门：

[linux_armv5.zip(Github, v0.11.86)](https://github.com/gogs/gogs/releases/download/v0.11.86/linux_armv5.zip)，或者



Bash



```
wget https://github.com/gogs/gogs/releases/download/v0.11.86/linux_armv5.zip
```

## ③ Frp二进制程序 (可选)

可选部件，当你想公布你的git服务到互联网但由于NAT层导致无法端口映射时用到。

### 传送门

ARM32：[frp_0.27.0_linux_arm.tar.gz(OfficialWebsite, v0.27.0)](http://diannaobos.iok.la:81/frp/frp-v0.27.0/frp_0.27.0_linux_arm.tar.gz)，或者：



Bash



```
wget http://diannaobos.iok.la:81/frp/frp-v0.27.0/frp_0.27.0_linux_arm.tar.gz
```

ARM64：[frp_0.27.0_linux_arm64.tar.gz(OfficialWebsite, v0.27.0)](http://diannaobos.iok.la:81/frp/frp-v0.27.0/frp_0.27.0_linux_arm64.tar.gz)，或者：



Bash



```
wget http://diannaobos.iok.la:81/frp/frp-v0.27.0/frp_0.27.0_linux_arm64.tar.gz
```

------

# 0x02 详细过程

## Ⅰ. Termux环境配置

[![Termux](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img1.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img1.jpg)

在Termux中：



Bash



```
pkg install -y unstable-repo
pkg install -y mariadb git wget tar unzip zip neofetch nano
```

## Ⅱ. 解压缩下载的文件

> 注意：如果你已在termux外部下载gogs(和frp)的压缩包的话，请使用`mv`指令将其移动到`/data/data/com.termux/files/home/`(这个路径可以简写成英文波浪号”~”)
> 如果想从termux内部下载，请使用”准备工作”中的`wget`指令下载gogs(和frp)

### 在Termux中：

解压Gogs：



Bash



```
#解压缩
unzip linux_armv5.zip
#删除压缩包
rm linux_armv5.zip
```

[![gogs压缩包中的内容](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img2.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img2.jpg)

解压Frp：



Bash



```
#解压缩
tar -xvzf frp_0.27.0_linux_arm64.tar.gz
#更改成好记的文件夹名
mv frp_0.27.0_linux_arm64 frp
#删除压缩包
rm frp_0.27.0_linux_arm64.tar.gz
```

[![Frp压缩包中的内容](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img10.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img10.jpg)

## Ⅲ. MySQL Database(数据库)配置

> 注意：可能稍微有些难度，本人也是菜鸡
> ~~已经会mysql的大神请灵活变通~~

### ① 查看当前用户名：

在Termux中：



Bash



```
neofetch
```

[![neofetch](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img3.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img3.jpg)

得知我们当前用户名为`u0_a284`

### ② 启动本地MySQL服务

在Termux中：



Bash



```
mysqld
```

[![MySQL服务端启动成功](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img4.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img4.jpg)

### ③ 添加当前账户并给予数据库操作权限 && 创建Gogs数据库

首次初始化MySQL服务器时会创建名字为root的账户

在Termux中：



Bash



```
mysql -u root -p
```

输入密码为：`root`

> 注：输入时不显示，输入完按回车就行

[![成功登入MySQL数据库管理控制台](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img5.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img5.jpg)

在MySQL控制台中添加我们从`neofetch`指令中查询到的用户并授予数据库最高操作权限



Code



```
CREATE USER '用户'@'localhost' IDENTIFIED BY '密码'; # 创建用户
GRANT ALL ON *.* TO '用户'@'localhost'; # 授予该用户最高权限
CREATE DATABASE 数据库名称; #用来存放gogs账户信息的数据库，名称随意
exit # 退出MySQL控制台
```

> 注：① 这样创建的用户只能从本地访问这个数据库(因为设定的localhost)
> ② 注意是否有单引号
> ③ 数据库名称要记住，之后要用

每次操作出现`Query OK, x rows affected (x.xxxx sec)`就代表该操作成功！

## Ⅳ. 安装Gogs

### ① 创建一个文件夹用来存放gogs里的用户创建的repo

在Termux中：



Bash



```
cd ~
mkdir gogs-repo
```

### ② 启动Gogs Web Server端

在Termux中：



Bash



```
./gogs/gogs web
```

[![Gogs服务端启动成功](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img6.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img6.jpg)

### ③ **安装Gogs！**

浏览器进入`http://localhost:3000`

请**仔细**按照图中标识的项目设置
[![Setup 1](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img7.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img7.jpg)
[![Setup 2](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img8.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img8.jpg)

配置完成后点击安装
稍等片刻安装，完成后出现登录界面
[![Gogs登录界面](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img9.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img9.jpg)

至此，Gogs服务端(本地)已安装完成

## Ⅴ. 使用Frp将gogs公布到互联网上

> 由于我本人没有Frp服务器，所以用的Frp官网上免费的frp服务器，token请从[中文官网](https://diannaobos.com/frp/)加群获取
> 如果你有自己的服务商，你可以使用你自己的
> ~~讲真这不是广告，谁让我没钱2333~~

### ① **配置frpc.ini**

使用`nano`(或者其他)编辑文件frpc.ini

如何编辑，请看图。
[![frpc.ini配置](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img11.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img11.jpg)

### ② `custom_domains`和`subdomain`配置问题

二级域名有两种配置方式：

1. 自定义一个以服务商域名为基础的域名，该域名会解析到服务商的主服务器。
2. 直接定义二级域名。

> 可以通过访问frps dashboard查看其他人的配置来确定服务商指定的方式(默认xxx.xxx.xxx:7500查看)，或直接由服务商告知
> 默认用户名和密码都是`admin`

例如：

该服务商采用的第一种方法定义二级域名
[![第一种方式](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img12.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img12.jpg)



Code



```
#subdomain = 
custom_domains = gogs.frpzj.kskxs.com
```

该服务商采用的第二种方法定义二级域名
[![第二种方式](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img13.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img13.jpg)



Code



```
subdomain = gogs
#custom_domains =
```

### ③ 启动Frp客户端

在Termux中：



Bash



```
./frpc -c frpc.ini
```

[![成功运行frpc](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img14.jpg)](https://cdn.jsdelivr.net/gh/StageGuard/stageguard.github.io/img/run-gogs-img/img14.jpg)

直接访问定义的二级域名即可`http://gogs.frpzj.kskxs.com:8081/`

> 注意端口，在上上图能看到，提供第一种方式的服务商提供的端口为`8081`，第二种方式的服务商提供的端口为`7000`

------

# 0x03 终止服务：

> 终止frp客户端快捷键：`CTRL + C`
> 终止gogs web端快捷键：`CTRL + C`
> 终止mysql 数据库指令：`killall -SIGTERM mysqld`
> ~~或者直接硬核清理Termux进程~~

------

# 0x04 常见问题：

## dial tcp: lookup xxx.xxx.xxx on [::1]:53: read udp [::1]:xxxxx->[::1]:53: read: connection refused

解决：dns解析问题，在frpc.ini的common项中添加：



Code



```
dns_server = 1.1.1.1
```

## **欢迎在评论区补充其他问题:)**

------

教程终于肝地差不多了呢
这是我第一次正式写博客，有点激动！！
如果你觉得对你有用的话，也可以考虑捐赠一波(你在想peach)

参考资料：

https://gogs.io/docs

**文章作者:** [StageGuard](mailto:undefined)

**文章链接:** https://stageguard.top/2019/07/30/run-gogs-on-android/

**版权声明:** 本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。转载请注明来自 [StageGuard](https://stageguard.top/)！