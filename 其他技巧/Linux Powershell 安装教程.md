# [Linux Powershell 安装教程](https://www.linuxprobe.com/linux-powershell-installation.html)

[![img](https://www.linuxprobe.com/imgs/peixun.jpg)](https://www.linuxprobe.com/training)

**Linux系统技术交流QQ群（340829）验证问题答案：刘遄**[![Linux就该这么学](https://www.linuxprobe.com/wp-content/uploads/2018/02/QQ%E7%BE%A4.png)](https://qm.qq.com/cgi-bin/qm/qr?k=WdT99acUoOwt80KJFX6Xg0f6DyOxuo1Q&jump_from=webapi)

| 导读 | **在微软爱上 [Linux](https://www.linuxprobe.com/) 之后，Power[Shell](https://www.linuxcool.com/) 这个原本只是 Windows 才能使用的组件，于 2016 年 8 月 18 日 开源并且成为跨平台软件：https://linux.cn/article-7699-1.html ，登陆了 Linux 和 macOS。** |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/083959vbbegoma8emdggkb.jpg)

**PowerShell** 是一个微软开发的自动化任务和配置管理系统。它基于 .NET 框架，由[命令](https://www.linuxcool.com/)行语言解释器（shell）和[脚本](https://www.linuxcool.com/)语言组成。

PowerShell 提供对 **COM** (组件对象模型Component Object Model) 和 **WMI** (Windows 管理规范Windows Management Instrumentation) 的完全访问，从而允许系统管理员在本地或远程 Windows 系统中 执行管理任务，以及对 WS-Management 和 CIM（公共信息模型Common Information Model）的访问，实现对远程 Linux 系统和网络设备的管理。

通过这个框架，管理任务基本上由称为 **cmdlets**（发音 command-lets）的 .NET 类执行。就像 Linux 的 shell [脚本](https://www.linuxcool.com/)一样，用户可以通过按照一定的规则将一组 **cmdlets** 写入文件来制作脚本或可执行文件。这些脚本可以用作独立的[命令](https://www.linuxcool.com/)行程序或工具。

**在 Linux 系统中安装 PowerShell Core 6.0**

要在 Linux 中安装 **PowerShell Core 6.0**，我们将会用到微软软件仓库，它允许我们通过最流行的 Linux 包管理器工具，如 apt-get、yum 等来安装。

**在 Ubuntu 16.04 中安装**

首先，导入该公共仓库的 **GPG** 密钥，然后将 Microsoft Ubuntu 仓库注册到 **APT** 的源中来安装 **PowerShell**：

```
$ curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
$ curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/microsoft.list
$ sudo apt-get update
$ sudo apt-get install -y powershell
```

**在 Ubuntu 14.04 中安裝**

```
$ curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
$ curl https://packages.microsoft.com/config/ubuntu/14.04/prod.list | sudo tee /etc/apt/sources.list.d/microsoft.list
$ sudo apt-get update
$ sudo apt-get install -y powershell
```

**在 [CentOS](https://www.linuxprobe.com/) 7 中安裝**

首先，将 **Microsoft RedHat** 仓库注册到 YUM 包管理器仓库列表中，然后安装 **PowerShell**：

```
$ sudo curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/microsoft.repo
$ sudo yum install -y powershell
```

**如何在 Linux 中使用 PowerShell Core 6.0**

在这一节中，我们将会简单介绍下 **PowerShell**；我们将会看到如何启动 PowerShell，运行一些基础命令，操作文件、目录和进程。然后学习怎样列出所有可用的命令、显示命令帮助和别名。

输入以下命令来启动 PowerShell：

```
$ powershell
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084024du81euye77bsusii-1.png)

在 Linux 中启动 PowerShell

你可以通过以下命令来查看 PowerShell 版本：

```
$PSVersionTable
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084025ckdzp5tfm6tcc5cp-1.png)

查看 PowerShell 版本

在 Linux 中运行基本的 PowerShell 命令。

```
get-date          [# 显示当前日期]
get-uptime        [# 显示开机时间]
get-location      [# 显示当前工作目录]
```

**在 PowerShell 中操作文件和目录**

1、 可以通过两种方法创建空文件：

```
new-item  tecmint.tex
或者
"">tecmint.tex
```

然后往里面添加内容并查看文件内容。

```
set-content tecmint.tex -value "TecMint Linux How Tos Guides"
get-content tecmint.tex
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084025lvi4q45pzfv98v88-1.png)

在 PowerShell 中创建新文件

2、 在 PowerShell 中删除一个文件

```
remove-item tecmint.tex
get-content tecmint.tex
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084026pshkk774r8k6kvee-1.png)

在 PowerShell 中删除一个文件

3、 创建目录

```
mkdir  tecmint-files
cd  tecmint-files
“”>domains.list
ls
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084026d94zz0gpg1gkgg1p-1.png)

在 PowerShell 中创建目录

4、 执行长格式的列表操作，列出文件／目录详细情况，包括模式（文件类型）、最后修改时间等，使用以下命令：

```
dir
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084026ambbskbqhh9mhqbn-1.png)

Powershell 中列出目录长列表

5、 显示系统中所有的进程：

```
get-process
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084027rba9tystlwkk9aot-1.png)

在 PowerShell 中显示运行中的进程

6、 通过给定的名称查看正在运行的进程/进程组细节，将进程名作为参数传给上面的命令，如下：

```
get-process apache2
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084027tfb66w2yzf22z6bb-1.png)

在 PowerShell 中查看指定的进程

输出中各部分的含义：

- NPM(K) – 进程使用的非分页内存，单位：Kb。
- PM(K) – 进程使用的可分页内存，单位：Kb。
- WS(K) – 进程的工作集大小，单位：Kb，工作集由进程所引用到的内存页组成。
- CPU(s) – 进程在所有处理器上所占用的处理器时间，单位：秒。
- ID – 进程 ID (PID).
- ProcessName – 进程名称。

7、 想要了解更多，获取 PowerShell 命令列表：

```
get-command
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084028o4jtwhzzywjj6f6p-1.png)

列出 PowerShell 的命令

8、 想知道如何使用一个命令，查看它的帮助（类似于 Unix/Linux 中的 man）；举个例子，你可以这样获取命令 **Describe** 的帮助：

```
get-help Describe
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084028o6z08ttgt8t06wo0-1.png)

PowerShell 帮助手册

9、 显示所有命令的别名，輸入：

```
get-alias
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084029g4kmmzokrb4wn4oo-1.png)

列出 PowerShell 命令别名

10、 最后，不过也很重要，显示命令历史记录（曾运行过的命令的列表）：

```
history
```

![Linux Powershell 安装教程Linux Powershell 安装教程](https://www.linuxprobe.com/wp-content/uploads/2017/03/084029rixqy93zi60v3ozi-1.png)

显示 PowerShell 命令历史记录

就是这些了！在这篇文章里，我们展示了如何在 Linux 中安装**微软的 PowerShell Core 6.0**。在我看来，与传统 Unix／Linux 的 shell 相比，PowerShell 还有很长的路要走。目前看来，PowerShell 还需要在命令行操作机器，更重要的是，编程（写脚本）等方面，提供更好、更多令人激动和富有成效的特性。

查看 PowerShell 的 GitHub 仓库：https://github.com/PowerShell/PowerShell。

------

作者简介：

Aaron Kili 是一个 Linux 和 F.O.S.S 狂热爱好者，将来的 Linux 系统管理员、web 开发者，目前是 TecMint 的内容编辑，是一个热爱研究计算机与坚定的分享知识的人。