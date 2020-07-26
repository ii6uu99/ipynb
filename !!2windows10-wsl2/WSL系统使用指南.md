# WSL系统使用指南

[![img](https://upload.jianshu.io/users/upload_avatars/2875616/a806c90b-f8a9-4665-81a7-82096df4b2b8.png?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp)](https://www.jianshu.com/u/f9e2d952e70a)

[肆不肆傻](https://www.jianshu.com/u/f9e2d952e70a)关注

0.9122018.09.09 13:40:24字数 1,491阅读 17,813

2016年上半年的时候，微软在推出的windows 10 内部预览版中搭载了用户期待已久的windows subsystem for linux （WSL）服务，用户只要开启这项服务就能够在windows系统上体验原生的Linux bash指令操作。下面我们就介绍下在使用这项服务的经验：

## 一：安装WSL子系统

尽管微软有志于将Linux命令行操作体验整合到Windows系统下来，WSL也作为一项独立的windows服务引进，但这项服务默认是不开启的，要体验Linux需先开启该服务。你有两种方式开启这项服务：

1. 控制面板->程序和功能->添加Windows功能和服务->勾选Windows subsystem for Linux
2. Powershell命令行 `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`

至此，你的电脑已经在策略上允许使用Linux子系统了，但是这项服务本身并不包含Linux子系统本身，你需要额外安装相应的Linux系统才行。你有三种途径安装Linux子系统：

1. 从Windows Store下载相应的发行版
2. 通过命令行安装
3. 下载发行版，然后手动解压安装

#### 1.1 从Windows Store 安装

> 参考：[Windows 10 Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

打开Windows Store 搜索Linux，Store会为你推荐目标答案：



![img](https://upload-images.jianshu.io/upload_images/2875616-965d6bcba42172ad.png?imageMogr2/auto-orient/strip|imageView2/2/w/1155/format/webp)

Windows Store Linux子系统



点击“Get the apps”进入以下页面：



![img](https://upload-images.jianshu.io/upload_images/2875616-a8c33445e8d68b22.png?imageMogr2/auto-orient/strip|imageView2/2/w/1150/format/webp)

Windows Store Linux子系统


展示了目前支持的几个发行版，均以windows metro 应用的方式发布。选择相应的版本安装即可。

#### 1.2 命令行安装

> 参考：[Manually download WSL distro packages](https://docs.microsoft.com/en-us/windows/wsl/install-manual)

从Windows Store安装Linux简单方便，但不适用于所有情况，比如系统版本低于16215 Windows Store不提供可直接下载安装的发行版或者Windows Server版中Windows Store因安全因素考虑被禁止使用，这时候用户可以手动下载这些Linux 发行版APP进行安装。
**下载地址如下：**
[Ubuntu 18.04](https://aka.ms/wsl-ubuntu-1804)：https://aka.ms/wsl-ubuntu-1804
[Ubuntu 18.04 ARM](https://aka.ms/wsl-ubuntu-1804-arm)：https://aka.ms/wsl-ubuntu-1804-arm
[Ubuntu 16.04](https://aka.ms/wsl-ubuntu-1604)：https://aka.ms/wsl-ubuntu-1604
[Debian GNU/Linux](https://aka.ms/wsl-debian-gnulinux)：https://aka.ms/wsl-debian-gnulinux
[Kali Linux](https://aka.ms/wsl-kali-linux)：https://aka.ms/wsl-kali-linux
[OpenSUSE](https://aka.ms/wsl-opensuse-42)：https://aka.ms/wsl-opensuse-42
[SLES](https://aka.ms/wsl-sles-12)：https://aka.ms/wsl-sles-12
我们以安装 Ubuntu 16.04 为例讲解如何通过命令行安装WSL。

##### 1.2.1 下载Linux发行版

下载方式有很多，你可以选择自己喜欢的任何方式下载。



```shell
# PowerShell 中使用Invoke-WebRequest 指令
Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1604 -OutFile Ubuntu.appx -UseBasicParsing
```

或



```shell
# CMD 中使用curl指令，该指令Windows 10 2018春季版及以后可使用
curl.exe -L -o ubuntu-1604.appx https://aka.ms/wsl-ubuntu-1604
```

或 直接点击链接下载或将连接复制到下载器中下载。下载文件保存为 xxx.appx即可。

##### 1.2.2 安装下载的appx文件



```shell
# PowerShell 
add-appxpackage /path/to/xxx.appx
```

或解压下载的xxx.appx后从解压文件手动安装，参加小节1.3.

#### 1.3 手动解压安装

在我们使用1.2.1中的方法下载Linux发行版后，得到文件xxx.appx。这时候我们可以通过解压appx文件来安装应用，具体：

1. 重命名xxx.appx文件为xxx.zip, `Rename-Item /path/to/xxx.appx /path/to/xxx.zip`。
2. 解压zip文件，`Expand-Archive /path/to/xxx.zip /path/to/xxx`，确保`/path/to/xxx`在系统盘。
3. 进入解压目录运行发行版加载程序，如`ubuntu.exe`，完成安装。

- **几点注意事项**：

1. 从Windows Store 安装Linux子系统需要windows版本在16215及以后。
2. WSL只能运行在系统盘，默认是C盘，请确保WSL安装在C盘。如果你在设置中更改了APP的默认安装位置，则在通过Windows Store安装WSL之前需先将默认安装位置改为系统盘，以便Linux发行版能正确安装在系统盘。
3. 命令行环境，包括：CMD、Powershell 和 WSL 不允许在Windows 10 S 上运行。

## 二：修改WSL默认登陆用户

安装完WSL，用户即可运行程序来实例化一个Linux运行环境。首次启动应用程序时，需要等待程序完成一些初始化操作，之后程序将会向用户要求设置一个用户名，这个用户名是用来登陆WSL的默认用户。每次启动程序，将自动使用该用户登陆，不需要用户输入密码，用户只有在执行`sudo`等高权限指令的时候才会被要求输入密码。

用户可以修改默认登陆用户，例如对于Ubuntu发行版， `ubuntu config --default-user root`可设置默认使用root身份登陆WSL。这是很有用的，当你忘记了普通用户的密码后，可以通过这种方式进入root模式来修改或重置普通用户的登陆口令。

## 三： 其他

#### 1. 修改Ubuntu终端默认字体

WSL默认字体根据系统版本和区域语言设置各有不同，用户可以按下图中终端默认字体设置过程调整终端使用的默认字体和字体大小。修改默认字体后，下次打开终端会自动应用设置的默认字体。



![img](https://upload-images.jianshu.io/upload_images/2875616-0c35037af5db0861.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/1138/format/webp)

修改终端默认字体和系统语言设置

如果默认字体设置无效，重启终端设置丢失，可能是字符编码的问题：你的终端包含了当前字符编码不支持的字符。可通过设置默认字符编码解决。
window 命令行默认的字符编码格式在 我的系统上是 UFT-8，可以如下图所示查看：

![img](https://upload-images.jianshu.io/upload_images/2875616-c19ec33511ac7a8c.png?imageMogr2/auto-orient/strip|imageView2/2/w/730/format/webp)

查看当前终端使用的字符编码格式


也可使用命令行指令：`cmd /C chcp` 查看。
还可以通过修改注册表键值的方法更改默认字符编码：

![img](https://upload-images.jianshu.io/upload_images/2875616-8e977bd3ea2c19a9.png?imageMogr2/auto-orient/strip|imageView2/2/w/778/format/webp)

注册表修改Ubuntu终端默认字符编码



设置后，自定义配置应该不会丢失。为保证较好的兼容性，我们开启windows **区域和语言设置** 中的 非unicode 程序语言，使用unicode utf-8 提供全球语言支持，有效减少字符与编码的不兼容导致的问题。典型案例就是Tmux自定义主题中状态栏多行（不能一行显示）的问题。