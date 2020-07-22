PowerShell在Ubuntu系统的使用
2018.2.17
版权声明：本文为博主chszs的原创文章，未经博主允许不得转载。
本文主要介绍如何在Ubuntu 16.04 LTS上安装和使用PowerShell。要知道，PowerShell Core是微软公司推出的一个跨平台（Windows，Linux和macOS）自动化和配置工具/框架，可与现有工具很好地配合使用，并对结构化数据（如JSON， CSV，XML等），REST API和对象模型的处理做了优化。PowerShell包括一个命令行shell，一个相关的脚本语言和一个处理cmdlet的框架。

下面先介绍在Ubuntu 16.04（Xenial Xerus）服务器上逐步安装Microsoft PowerShell的过程。

在Ubuntu 16.04 LTS上安装PowerShell
步骤1：首先在终端中运行以下apt-get命令，确保所有系统软件包都是最新的。

# sudo apt-get update
# sudo apt-get upgrade

步骤2：在Ubuntu 16.04上安装PowerShell。有两种方法。

方法1：使用Debian软件包安装
首先，将Debian软件包下载到你的Ubuntu服务器上：

# wget https://github.com/PowerShell/PowerShell/releases/download/v6.0.1/powershell_6.0.1-1.ubuntu.16.04_amd64.deb
# dpkg -i powershell_6.0.1-1.ubuntu.16.04_amd64.deb

使用以下命令安装PowerShell：

# apt-get install -f

方法2：基于微软提供的软件仓库安装
使用官方的Ubuntu安装PowerShell Microsoft Repository：

# curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/microsoft.list

然后在终端中执行以下操作：

# apt-get update
# apt-get install -y powershell

安装后，就可以运行powershell，只需在提示符下输入以下命令“pwsh”即可：

# pwsh
1
此时已成功安装PowerShell。

PowerShell介绍
Windows PowerShell是专门为系统管理员设计的Windows命令行Shell。Windows PowerShell包含了可以单独或组合使用的交互提示和脚本编写环境。
与大多数Shell（它们接受和返回文本）不同，Windows PowerShell是在dotNET Framework公共语言运行时（CLR）和dotNET Framework的基础上生成的，它接受和返回dotNET Framework对象。环境中的这一基本更改为Windows的管理和配置带来了全新的工具和方法。

Windows PowerShell引入了cmdlet（读作“command-let”）的概念，它是内置于Shell的简单的单一函数命令行工具。可以分别使用每个cmdlet，但只有组合使用这些简单的工具来执行复杂的任务时，你才会意识到它们的强大功能。Windows PowerShell包含了一百多个基本核心cmdlet，你可以编写自己的cmdlet并与其他用户共享。Windows PowerShell旨在通过消除长期存在的问题和添加新功能改进命令行和脚本环境。

PowerShell v6.0.1版的变化主要如下：

使用的dotNet Core Runtime和包升级到2.0.5版
修复了数个安全问题
PowerShell的基本操作：

更改计算机状态
收集有关计算机的信息
兼容性别名
创建自定义PowerShell快捷方式
创建dotNET和COM对象（New-Object）
创建自定义输入框
创建图形日期选取器
获取WMI对象（Get WmiObject）
管理当前位置
使用Process Cmdlet管理进程
管理服务
管理Windows PowerShell驱动器
直接操作项
多选列表框
其他有用的脚本对象
执行网络任务
使用Out Cmdlet重定向数据
从管道中删除对象（Where对象）
为多个对象重复执行任务（ForEach 对象）
从列表框中选择项
选择对象部件（Select对象）
对对象进行排序
使用格式命令更改输出视图
使用静态类和方法
查看对象结构（Get Member）
使用文件和文件夹
使用文件、文件夹和注册表项
使用对象
使用打印机
使用注册表条目
使用注册表项
使用软件安装
————————————————
版权声明：本文为CSDN博主「chszs」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/chszs/article/details/79332551