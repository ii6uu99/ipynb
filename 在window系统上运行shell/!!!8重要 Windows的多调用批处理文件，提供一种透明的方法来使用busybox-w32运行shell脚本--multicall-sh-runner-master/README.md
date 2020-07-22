https://github.com/mr-south-guo/multicall-sh-runner

# 多呼Sh跑步者

## 描述

shell脚本文件   名.sh文件，修改为 名.cmd,以普通用户运行调用shell脚本文件

修改为.admin.cmd ，以管理用户运行调用shell脚本文件





甲多重呼叫Windows批处理文件（*流道*），以提供一个透明的方法来运行一个sh脚本（使用[busybox的-W32](http://frippery.org/busybox/)），在Windows命令提示或从其他批处理文件。

## 特征

- **多通话。**重命名*亚军*以匹配目标SH-脚本，它会自动地运行SH-脚本。
- **自动以管理员身份运行。**附加`.admin`到*跑步*者的名称，它将以admin身份运行sh脚本。
- **传递参数。**所有参数传递给*跑步者*通过传递到SH-脚本。
- **随身携带。**没有要安装的东西，也没有留下任何东西。

## 文件和用法

### 主要档案

- ```
    sh-runner.cmd
    ```

    - 的*亚军*。它必须与目标sh脚本位于同一目录中。
    - 复制/硬链接并重命名它以匹配您的目标sh脚本。举些例子：
        - 要`abc.sh`以当前用户身份运行，请将*跑步者*重命名为`abc.cmd`。
        - 要`abc.sh`以管理员身份运行，请将*跑步者*重命名为`abc.admin.cmd`。
    - 符号链接不要做工作，作为*亚军*将解决它的名字链接目标。（NTFS符号链接的许多丑陋特性之一。）

- ```
    sh.exe
    ```

    - 它已重命名`busybox64.exe`（64位）以执行sh脚本。
    - 您可以从[busybox-w32](http://frippery.org/busybox/)下载最新版本或32位版本。
    - http://frippery.org/busybox/
    - busybox-w32是BusyBox到Microsoft Windows WIN32 API的端口。它在单个独立的本机可执行文件中将BusyBox功能的子集引入Windows
- 
    - 此文件是**必填**文件，du。
    - 它可以在同一个目录下*亚军*，还是在`PATH`。
    
- ```
    elevate.exe
    ```

    - 一个微小的开源工具来以管理员身份运行命令，从[这里](http://code.kliu.org/misc/elevate/)。
    - 该文件是**可选的**。如果您不打算使用“以管理员身份自动运行”功能，则不需要它。（您可以随时启动*亚军*手动为管理员。）
    - 它可以在同一个目录下*亚军*，还是在`PATH`。

- ```
    hardlink-runner.cmd
    ```

    - 实用程序脚本硬连接一个*亚军*到多个*选手*为一组SH-脚本，让你不必做一个接一个。
    - 如果不带参数运行它，它会创建*选手*在同一个目录中所有的SH-脚本，通过硬连接`sh-runner.cmd`。
    - 使用选项`-h`显示帮助消息以获取更多用法详细信息。
    - 该文件是**可选的**。

### 示例文件

- ```
    sh-hello.sh
    ```

    - 一个hello-world示例sh-script。

- ```
    sh-hello.cmd
    ```

    - 所述*转轮*，重命名为运行示例SH-脚本作为当前用户（开始用户*浇道*）。

- ```
    sh-hello.admin.cmd
    ```

    - 该*转轮*，重新命名，并附加`.admin`，作为管理员自动运行示例SH-脚本。

## 常问问题

### 这可以与WSL，Cygwin，MSYS等一起使用吗？

我不知道。也许您可以尝试一下并让我知道？

### 为什么要像单线工作一样进行此项目`busybox.exe sh <sh-script>`？

有几个原因：

- 我喜欢在各处以相同方式运行sh脚本，即称呼它们的名称。是在busybox shell中还是在命令提示符下。
- 我喜欢以管理员身份始终启动一些sh脚本，而无需手动执行。
- 我喜欢双击以启动一些sh脚本，而无需编写任何启动代码。
- 一般来说，我很懒，好吗？

### 为什么仍要在Windows上使用sh-script？我知道批处理脚本很糟糕，但是PowerShell脚本不够好吗？

这只是一个偏好问题。我的主要个人原因是

- sh-script功能强大，可以在Linux，Android和现在的Windows上随处找到。
- busybox-w32很小巧，功能强大，可移植，而且简直很棒。