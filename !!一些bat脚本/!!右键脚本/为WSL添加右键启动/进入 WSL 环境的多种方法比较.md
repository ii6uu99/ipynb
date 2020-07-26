# [进入 WSL 环境的多种方法比较](http://www.mocihan.ml/archives/53/)

- 2016-08-16 10:18:00
-  

- [技术](http://www.mocihan.ml/category/IT/)
-  

- [暂无评论](http://www.mocihan.ml/archives/53/#comments)
-  

- 86 次阅读
-  

- 

Windows 10 中包含了一个 WSL（Windows Subsystem for Linux）子系统，我们可以在其中运行未经修改过的原生 Linux ELF 可执行文件。利用它我们可以做很多事情，对开发人员和普通用户都是如此。当然对开发人员的吸引力更大一些，因为这意味着在一些情况，不再需要使用 Linux 虚拟机、双系统、Cygwin/MSYS2 了。

当前版本（14901.1000）Windows 10 中的 WSL 功能已经比较完善了，和刚出来时不可同日而语，也不再是一个没有实用价值的玩具了（最初的版本连 zsh 和 tmux 等最基本的工具都无法运行，基本没有可用性。但如果现在依然说 WSL 不可用，就有失偏颇了）。但对不想折腾的普通用户来说，用户体验并不好。其实我们可以做一些优化，最终效果是在仅损失少量可接受的代价的前提下，达到接近完美的体验。本文主要将进入 WSL 环境的多种方式，以及简单比较不同方式之间的优缺点。

## 直接运行 bash

最简单直接的方法是 `Win + R` 输入 bash 直接进入。但这样右键（很可能）不可用，复制粘贴很麻烦（需要在标题栏右键菜单中选择编辑）。而先进入 cmd 或者 powershell 后，再运行 bash，这样复制和粘贴进方便了很多。尤其是先进入 powershell 再运行 bash，可以鼠标选择复制，右键直接粘贴。我们可以直接 `Win + R` 输入 `powershell -c bash ~` 进入。但从 powershell 进入会有额外的问题，一些程序的显示可能会出现异常。

直接运行 bash 的好处是性能最好，资源占用最低，交互（比如在资源管理器打开 bash 并定位到当前目录，或者直接双击 .sh 脚本用 bash 运行等）也更容易实现。但有一个严重的问题，就是无法输入中文，显示中文也会出现重叠或者截断的情况。此外还有复制粘贴麻烦，而且只支持 16 种颜色等问题。可定制性也很弱，这样的终端用户体验上很差的。如果只给我这样一个环境使用，即使所有的 Linux 软件都能正常运行，我也是没办法接受的。这恐怕也是 WSL 最让人诟病的地方，第一印象就不是很好。

## 使用 wsl-terminal

wsl-terminal 是专门为 WSL 准备的终端模拟器，主体是 mintty，另外整合了一些工具，使用起来非常方便，也是目前用户体验最好的，大小也只有 1M 多，推荐使用。使用方法见官方主页，地址：https://github.com/goreliu/wsl-terminal。

实现方面，这个方法是由在 WSL 里启动 sshd，然后使用 ssh 客户端登录的方法改进的。它的运行机制和 ssh 有很大的的区别。mintty 会运行 wslbridge，wslbridge 包含两个程序，wslbridge.exe 和 wslbridge-backend。从文件名可以看出来，前者是 Windows 程序，后者是 Linux 程序。wslbridge.exe 会在一个隐藏窗口运行 bash.exe 进入 WSL 环境，在其中运行相同目录下的 wslbridge-backend。wslbridge.exe 和 wslbridge-backend 之间会建立三个 tcp 连接，也就是将 stdin、stdout、stderr 分别通过三个 tcp 连接联系起来，连接建立后就不再监听任何端口了。而 mintty 就是一个终端模拟器，对它来说 wslbridge 和 ssh 没有什么区别。

性能上，在我这里用 wslbridge 和 ssh 执行命令的速度是差不多的，前者稍微快一点，不明显。资源占用上，前者占优。

使用的方便程度上，明显 wslbridge 占优。不再需要启动 sshd，配置信任关系等。另外 wslbridge 会自动将当前路径传递进去，不需要自己转换路径然后拼接 cd 命令，这样方便了许多。而且可以直接通过参数传递环境变量。我之前写的几个脚本减少了数十行。

## 使用 ConEmu 等终端模拟器

ConEmu（包括基于 ConEmu 修改的 cmder） 等终端模拟器也已经开始适配 WSL 环境，使用它复制粘贴更加方便（可以鼠标选择时直接复制，右键直接粘贴），也能输入中文了。但中文显示还是有问题（但比直接运行 bash.exe 要好一些），比如一个中文字符要比两个英文字符宽（在 vim 等地方），输入中文然后退格删除会删除到前边的字符（在 bash、zsh 等地方）。另外 ConEmu 更漂亮，界面上的功能更多（比如支持标签页，可以配置很多东西等）。除此之外和直接运行 bash 是一样的，比如颜色支持上。另外这个环境对 Linux 命令输出显示的兼容性不如直接运行 bash，某些命令的输出是有问题的（比如 top 命令中的反色显示会丢失）。

另外和 ConEmu 类似的是使用 Cygwin/MSYS2 的 mintty -e winpty bash。这个和 ConEmu 的问题类似，中文显示输入、颜色等地方同样存在问题。并且我实际测试时发现 mintty -e winpty bash 比 mintty -e ssh 127.0.0.1 还要慢，基本上没有什么优势。winpty 和 wslbridge 是同一个人写的，不需要考虑使用 winpty 了。

## 在 WSL 中开启 sshd，ssh 上去使用

（和 mintty + wslbridge 相比，在本机访问的话，ssh 基本上已经没有什么优势了。把 Cygwin/MSYS2 裁剪成 ssh 客户端，也不需要折腾了，相关内容我就不删了。）

还有一种办法是在 WSL 中开启 sshd，使用 ssh 客户端登录上去使用，就像使用本地 Linux 虚拟机或者 VPS 那样。

目前 ssh 上去的环境是没有任何问题的，包括中文显示输入、颜色、命令输出等。但这样也有一些问题，比如需要一个常驻的 sshd（可以使用更轻量级的 dropbear），并且使用起来不是很方便，尤其是在涉及交互的场景（比如在资源管理器创建一个 .sh 脚本，然后用 WSL 执行），需要写若干辅助的脚本。启动速度也比直接运行 bash 要慢，但如果选择轻量级的 ssh 客户端的话，使用起来还是比较容易接受的。

在 ssh 客户端的选择上，首先如果不是一直开着，secureCRT、XShell 之类比较重量级的 ssh 客户端是不大合适了，启动比较慢，体积比较大，资源占用也多，有点大材小用了。PuTTY 是一个选择，在启动速度、资源占用、文件体积上都比较出色，但功能上就存在一些问题。比如我想在资源管理器任意一个目录运行 PuTTY，并且在 WSL 中定位到当前目录，或者执行一个临时拼凑出的命令，就比较难实现（也不是完全实现不了，比如可以每次都修改一次注册表，或者通过临时文件传递路径和命令）。另外 PuTTY 的官方版本不支持 24-bit 颜色，虽然有其他版本支持，但 PuTTY 的修改版很混乱，很难找一个各方面都很出色的版本。PuTTY 的易用性也存在问题，比如会话的载入和保存功能，很多人都会在这上面吃亏，丢失了已经填好的配置，配置信任关系比较麻烦，，基本上不上网搜索是很难仅从设置界面看明白是怎么用的，加密方法的支持也不完善。

其实还有一个容易被大家忽略的选择，是在 Cygwin/MSYS2 中的 mintty 使用 ssh。不过也难怪，安装 Cygwin 或者 MSYS2 都是比较麻烦的，而且至少会占用几百兆空间。但其实如果只裁剪一个最小的环境当成 ssh 客户端使用，仅需要不到 10M 的空间（压缩后只有 3M 左右，其中还包括了维护用的 dash、ls、cat、rm 等命令），比起 PuTTY 的 500K 自然大了不少，但比起 secureCRT、XShell 等还是要轻量级一些的。mintty 界面简洁，配置方便，中文显示输入、颜色支持上没有任何问题。更重要的是直接用 ssh 命令非常灵活，可以临时拼凑命令然后执行， 使用和 Linux 下相同的方式建立信任关系等。并且 mintty 启动快，资源占用少，虽然每次都要运行 ssh 登陆，但速度也是可以接受了。不支持标签页的问题，可以用在 WSL 里运行 tmux 来解决，这样启动 mintty 还会更快一些，而且 mintty 退出后环境还在保持。

裁剪 Cygwin/MSYS2 的办法：

这里以 MSYS2 为例，简单讲下如何把几百兆的 MSYS2 裁剪成不到 10M 的 ssh 客户端。

安装 MSYS2 后，用 `pacman -S openssh` 安装 openssh，其他的基本不需要额外安装了。

然后再另一个目录（这里以 `c:\sshclient` 为例，这个目录在哪不重要，使用的时候是可以随意移动的）下创建 5 个目录：dev、etc、tmp、usr、home。

将 MSYS2 中 `/etc/passwd` 文件放置到 `c:\sshclient\etc` 下，可以修改下这个文件，只保留直接当前使用的用户名，shell 也改成自己用的 shell（比如最轻量的 dash），home 目录也设置好。

在 `c:\sshclient\usr` 目录下创建 `bin`，然后把 MSYS2 中 `/usr/bin` 里的这些文件复制过去：

```
cat.exe
cygwin-console-helper.exe
dash.exe
ls.exe
mintty.exe
msys-2.0.dll
msys-asn1-8.dll
msys-com_err-1.dll
msys-crypt-0.dll
msys-crypto-1.0.0.dll
msys-gcc_s-seh-1.dll
msys-gssapi-3.dll
msys-heimbase-1.dll
msys-heimntlm-0.dll
msys-hx509-5.dll
msys-iconv-2.dll
msys-intl-8.dll
msys-krb5-26.dll
msys-roken-18.dll
msys-sqlite3-0.dll
msys-ssp-0.dll
msys-wind-0.dll
msys-z.dll
rm.exe
ssh.exe
```

需要记的只有 mintty.exe、ssh.exe、dash.exe、cygwin-console-helper.exe，这些 dll 文件可以根据错误提示来拷贝，其他命令根据自己的喜好。

在 `c:\sshclient\home\username\.ssh` 里写好 ssh 的配置文件，就大功告成了。运行 mintty，输入 /usr/bin/ssh 127.0.0.1 即可。但要想好用还需要写一些额外的工具，比如用右键菜单在指定的目录打开 、将 .sh 脚本的打开方式改成 mintty、用 WSL 里的 vim 编辑资源管理器中选定的文件等。

最后截图纪念一下。显示的是 Arch Linux 系统，因为我把默认的 Ubunt 14.04 的文件全部换成 Arch Linux 的了，而且运行良好（安装方式：https://github.com/Microsoft/BashOnWindows/issues/8#issuecomment-240026910）。另外可以注意到左下角的窗口，wcmd 可以直接运行 Windows 的 ipconfig 命令，这得益于 [cbwin](https://github.com/xilun/cbwin) 项目，虽然是使用的是在 Windows 运行一个守护进程，监听 127.0.0.1 的某一个端口，然后 WSL 中的 wcmd、wrun、wstart 命令通过 TCP 发送命令和采集结果，速度上还是可以接受的，运行命令或者图形界面软件都没有问题。在微软官方没有支持在 WSL 里直接运行 Windows 软件的情况下，是一个不错的替代方式。它要明显比在 Windows 下开 SSH Server 要快，而且使用起来更方便。

![image](http://www.mocihan.ml/usr/uploads/manual/028.png)

标签: none