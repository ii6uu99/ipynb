像程序员一样安装程序：Chocolatey 初见



### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

------

你一定会觉得很酷！今天，我们会尝试用一种非常程序员的方式在 Windows 上安装、卸载、管理程序。

来动手试一试吧，毕竟，这可能是你接近编程的一次美好体验。

## 神奇！

要是你 [在少数派上](https://sspai.com/post/35358) 看到了一款很好用的文件压缩工具 [Bandizip](https://cn.bandisoft.com/bandizip/)，你会怎么来安装它呢？

- 通过文章内的链接或搜索引擎找到它的官网，点击官网的下载按钮安装
- 要是你使用百度，你可以在百度搜索页直接点击第三方软件下载站的按钮下载
- 借助各大厂家的电脑管家来搜索、下载
- 向身边的好友或在论坛、交流群中索要安装包

但是，今天我们会尝试一种更加有趣、方便而又可靠的方式：

![img](https://cdn.sspai.com/2019/06/20/663e95cb67980a8a24b7a6dd1c090a67.gif)使用 Chocolatey 安装 Bandizip

没错，**只需要输入一行命令**，稍等几分钟，Bandizip 已经在你的系统中装好啦。

## 安装 Chocolatey

要想这样通过命令行来一键安装程序，我们借助的是 [Chocolatey](https://chocolatey.org/) 这款软件包管理器。它事实上是为了习惯于 Linux 的程序员们准备的，因为在 Linux 中安装程序，通常都只需要一条安装命令就可以完成。不过，**这丝毫不影响每一个人来尝试一下**。

![img](https://cdn.sspai.com/2019/06/20/6f90d5fde5db602d920bdb5416944a12.gif)安装 Chocolatey



Chocolatey 自身的安装很方便，一共有三步：

1. 开始菜单中搜索 `cmd`，选择「命令提示符」

2. 右键菜单或在右边菜单选择「以管理员身份运行」

3. 复制下面这段内容，回车执行

   ```
   @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
   ```

OK 准备就绪。

前面的安装命令来自 [官网的安装界面](https://chocolatey.org/install)，如果有更新，还是以官网的为准。

## 第一次尝试

接下来，我们可以继续在这个窗口中，尝试安装我们的第一个程序。输入：

```
choco install --yes Bandizip
```



稍等片刻，Bandizip 程序就安装好了。你可以在桌面上看到它的快捷方式。

## 装机从此不再难

每次拿到一台新的电脑，**快速安装上所有自己需要的程序**是一件非常非常耗时间的事情。

如果去国内各大第三方下载站，或者电脑管家、百度的安装工具，它们很多都会把原生的安装包进行修改，加入自己的广告或其他私货；总之，**下载软件还是最好去各自的官网**，这样才能最好地避免病毒、保护隐私。

然而，要一个个软件分别去官网下载，既无聊，又费心。下载安装包之后，还需要手动一次次地点击「下一步」，直到全部安装完成。

Chocolatey 就可以比较好地解决这些烦恼。因为你可以：

```
choco install --yes bandizip firefox potplayer teamviewer
```

把你想要安装的程序一起写上，十个，二十个，都没有关系。把它丢在一边跑着，你可以出去吃个冰淇淋，回来就都装上了。

## 还有一些命令

在安装的过程中，你应该已经发现 **Chocolatey 的命令非常语义化**。

先以 `choco` 开头，告诉系统我要使用 Chocolatey 了，然后用 `install` 表明我要安装一个程序，最后跟上需要安装的程序名称即可。中间的 `--yes` 意味着对 Chocolatey 安装过程的认可，如果不加，Chocolatey 会在安装的每一个步骤前停下来问你是否同意继续。

![img](https://cdn.sspai.com/2019/06/20/36246ba1a4334bf22f17c6d33717a567.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)用于安装的命令

所以，这个命令理解下来就是：「召唤」Chocolatey，请执行「安装」，我「同意」你的一切行为，安装的内容是「Bandizip 和 Firefox」。

除了安装，你肯定还关心怎么卸载。要是想要**卸载**一个已经安装的程序，只需要执行：

```
choco uninstall bandizip
```

为了便于管理，我们有时候需要查看所有程序的**列表**。想知道自己用 Chocolatey 装了哪些程序，可以这样写：

```
choco list --local
```



需要更新程序时，可以先**检查**一下哪些应用需要更新，使用 `outdated` 命令：

```
choco outdated
```

这样就会把所有「过期」的应用全部列出来，可以按需更新。**升级**与安装的命令格式相似：

```
choco upgrade --yes Bandizip
```

你也可以尝试**一键升级**所有程序，命令同样非常语义化，执行「升级」、「允许」操作、「所有」应用：

```
choco upgrade --yes all
```



现在，你可以不必担心每一个程序是否是最新版，因为你可以时不时运行一下更新命令；你也不用担心程序卸载不干净了，使用 Chocolatey 安装的程序，就可以用 Chocolatey 卸载。

## 知其所以然

前面安装的时候提到过，Chocolatey 跟其他第三方软件管理器不同之处在于，其他软件管理器经常修改原来的安装包，从而可以夹带自己的广告，并且经常安装好之后发现并不是最新版本。但是 Chocolatey 不但**使用官网链接下载**，而且会在下载完成后使用数字摘要技术**检查安装包是否跟官网上的完全一致**，所以，你使用 Chocolatey 安装的就是最新纯净官网版本。

此外，通过使用 `info` 命令，你还可以查看程序的详细信息，便于你确认是否需要使用 Chocolatey 来安装这个程序：

```
choco info tim
```

得到 Tim 的详细信息如下：

![img](https://cdn.sspai.com/2019/06/20/a8887313f2bf1d734a34db0311c38679.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)Tim 软件包信息



在这里列出了 Tim 的软件描述、更新时间、用户协议、官网链接、下载数、用于完整性检查的数字摘要，以及软件包的认证状态和测试状态。这些信息可以用来确认 Chocolatey 上的这个软件包是否可靠。

## 它包揽了一切

现在，我的 Windows 软件基本上全靠 Chocolatey 管理了。每隔一段时间，我会用 `list` 命令导出一下已安装的软件，需要配置新电脑的时候，只要把这份导出的列表稍作整理，就可以用 `install` 命令一下子全部装上了。这样也可以让公司和家里的 Windows 电脑保持一致的使用手感。

不过，仍有一些软件没有在 Chocolatey 上提供。我需要手动安装的软件包括：

- QQ（不过有 Tim）
- 微信
- 搜狗输入法
- 火绒安全
- Visual Studio
- Office

此外，还有一些软件需要从微软应用商店下载，自然也不会出现在 Chocolatey 中。无论如何，Chocolatey 绝对是一种值得尝试的软件管理方式。