# 最新termux安装 msf教程

- [笔记](https://www.it610.com/search/笔记/1.htm)

## 最新Termux安装metasploit教程

本文发表于2020.03.08

网上教程都很多了，不过有些已经过时了，现在官方已经在官方源中添加了metasploit包，安装只需要两条命令,但还是很难安装！这里说下捣腾时的一些经验。

首先安装前最好是干净的环境，把Termux程序的数据清除，因为安装过软件的termux可能会有依赖版本或者其他问题导致msf安装时数据库设置出错，导致启动不了数据库，本人小白，处理不了那些 问题，只能重装，经过多次重装后，发现原始环境更容易一次成功。另外失败的原因是，国外源，大家懂的，安装时最好挂梯子。安装msf时最好不要换源。

```java
#安装前先更新一下源
pkg update && pkg upgrade

pkg install unstable-repo
#先安装repo再安装msf
pkg install metasploit
```

另外如果安装失败重新安装的话，最好是清理一下数据或者卸载msf再重新安装（卸载安装各种玄学问题，推荐清理应用数据）：

```java
#卸载并清除配置文件
apt-get purge metasploit
```

[![最新termux安装 msf教程_第1张图片](https://img.it610.com/image/info8/16faa2eefc3f488e9368847f96d290d0.jpg)](https://img.it610.com/image/info8/16faa2eefc3f488e9368847f96d290d0.jpg)

#### 补充一点

如果安装好后，可能过段时间会出现数据库没有启动。
启动下数据库即可，数据库启动方法在安装msf成功后会有提示，类似以下格式：

```bash
#停止
pg_ctl -D /data/data/com.termux/files/usr/var/lib/postgresql -l logfile stop
#启动
pg_ctl -D /data/data/com.termux/files/usr/var/lib/postgresql -l logfile start
```

如果启动不了，请检查是否处于proot模式，经测试，proot模式下启动不了postgresql数据库。

另外推荐几个不错的教程，新手，不会排版，将就下吧。
Termux 高级终端安装使用配置教程

pip速度慢，更新失败，请换源