全平台的备份指南，让你从此重装不再难

每次需要重置手机、重装电脑，或者配置公司的办公电脑，大概都会非常烦恼。这篇文章，我会提纲掣领地分享一下我的重装手册。如果你也正好想要写一份，或许可以给你一些帮助。

为了操作方便，下面过程中会经常使用终端工具。当我写了一段代码时，通常意味着你需要打开 Windows 的「命令提示符」，或者 macOS 的「终端」，并把代码粘贴到终端工具中执行。

此外，我还可能涉及许多「正则表达式」的使用，比较现代的文本编辑器（如 Notepad++、Sublime Text、Visual Studio Code 等）都支持正则表达式的全局替换，你可以任意选择。我所用的代码均使用 Visual Studio Code 测试。

## Windows 操作系统的备份与导入

### Windows 账户同步

由于 Windows 10 现在已经支持微软账户登录与同步，当我们登录微软账户后，可以在「设置」中打开「同步设置」。这样，系统的大部分设置都会自动同步到微软的云端。

![img](https://cdn.sspai.com/2019/08/23/5c24fe7f42a25bd6fcba63d84c5d1059.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)同步 Windows 设置

### 导出 Chocolatey 软件列表

为了更方便地管理软件，也为了更快捷地在系统重置之后重新安装，我推荐使用 Chocolatey 、Scoop 或两者结合来管理程序。

对 Chocolatey 而言，备份时可以这样导出所安装的软件列表：

```
choco list -l --idonly > choco.txt 
```

这里的参数 `-l` 是小写字母 l 而不是数字 1。

打开当前目录，就可以看到 `choco.txt` 已经生成。所在目录以命令提示符前缀为准，如下图中，`choco.txt` 会生成于 `C:\workspace` 中。

![img](https://cdn.sspai.com/2019/08/23/6a15f6b9a0f39a5faf727828ef99684e.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)导出 Chocolatey 已安装列表

### 导出 Scoop 软件列表

备份 Scoop 的方式为：

```
scoop export > scoop.txt 
```

可以对 Scoop 的导出列表进行额外处理，以方便后续安装。使用 VSCode 打开 `scoop.txt` 文件，以正则表达式搜索：

```
(.*?) .*
```

并全部替换成：

```
$1
```

注意正则式中包含空格，请完整复制。

![img](https://cdn.sspai.com/2019/08/23/210c05aea82bfae57e8b6981b47411c6.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)VSCode 中的正则式替换

### 应用商店安装的应用列表

对于应用商店中的软件，我们可以使用 Geek Uninstaller 这款软件查看所有软件的列表。在「查看」菜单中选择「Windows Store Apps」之后，点击 `ctrl+s` 就可以把列表保存下来了。

![img](https://cdn.sspai.com/2019/08/23/d58c1b46352de588cf092dd60cf0d13b.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)使用 Geek Uninstaller 查看商店应用

不过由于应用商店的已安装应用中实际上包含了大量系统级别的预装应用，所以我建议直接手动记录下来——从应用商店安装的应用应该不多，我只有五个。

### 手动安装的软件列表

手动安装的软件列表可以借助 Chocolatey 来导出：

```
choco list -li 
```

执行之后，终端中会显示 `applications not managed with Chocolatey` 这样的提示，此上的列表就是手动安装的部分了。

### 导入备份的设置和软件

对于前面讲的几种备份，导入的方式并没有什么特别之处。Windows 账户登录后，系统设置等许多内容会直接同步过来，稍等即可。

Chocolatey 和 Scoop 都是使用 `install` 命令来安装，直接在后面跟上所有想要的程序名称：



```
choco install -y 软件1 软件2 软件3
scoop install 软件1 软件2 软件3
```

应用商店的部分直接在应用商店中搜索并安装，余下手动安装的几个就只能去官网下载安装包并逐一安装了。使用 Chocolatey 和 Scoop 管理程序后，手动安装的部分应当仅有极少数。

## macOS 操作系统的备份与导入

### 导出 Homebrew 和 App Store 的软件列表

与 Windows 类似，在 macOS 中我也建议使用出色的 Homebrew 来安装和管理应用程序。

感谢评论区的分享。借助 Homebrew Bundle，我们可以非常简洁地导出所安装的 Homebrew、Homebrew Cask 和 Mac App Store 应用。为了处理 Mac App Store 应用，首先需要安装一个依赖：



```
brew install mas
```

然后就可以执行：

```
brew bundle dump
```

这样，在当前的目录下就自动生成了一个名为 `Brewfile` 的文本文件。打开之后可以看到，里面包含了：



- tap
- brew
- cask
- mas

对于 brew，它导出的列表已经剔除了自动安装的依赖项，而只留下了我们手动安装的部分。对于 mas，它导出的列表包含了程序名称，以及用于后续安装的 app ID。



### 导出 Launchpad 中的软件列表

Launchpad 也就是「启动台」中的软件列表与「应用程序」文件夹内可以认为一致。如果需要，可以备份这个软件列表。

1. 打开「应用程序」文件夹
2. 全选、复制
3. 打开 VSCode 并粘贴

这样，软件列表就会以文本的形式得以保存了。

### 导入备份的软件

同样，借助 Homebrew Bundle，我们可以一键安装 Homebrew、Homebrew Cask 和 Mac App Store 应用。

将需要安装的软件按格式放到 `Brewfile` 中，并执行：

```
brew bundle
```

稍等之后，列表中的软件就已经安装完成了。

## Android 操作系统的备份

### 系统自带的同步功能

无论是原生 Google 账号的数据同步功能，还是国内外一众定制 UI 的云服务，Android 操作系统在登录系统账号并开启同步的情况下，可以自动同步联系人、短信、通话记录甚至相册、Wi-Fi 密码、系统设置、应用列表等内容，按需开启即可。

在新的手机上登录账号后，数据会自动同步下来。

### 导出应用列表

Android 上用于导出应用列表的工具有很多，我一直在使用 List My Apps 这个应用，非常高效，还可以直接导出成 Markdown 格式，并自动附上 Google Play 链接，方便后续安装和查看。



[![img](https://cdn.sspai.com/2019/08/22/application/af45e2547bd804683dd50f2e0991059b.jpg?imageMogr2/auto-orient/quality/95/thumbnail/!100x100r/gravity/Center/crop/100x100/interlace/1)](https://sspai.com/app/List My Apps)[List My Apps](https://sspai.com/app/List My Apps)[相关文章](https://sspai.com/app/List My Apps)

导出之后的结果是这样的格式：

![img](https://cdn.sspai.com/2019/08/23/0c4ecc30ca51c0d7615089c8c689873c.jpeg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)使用 List My Apps 导出应用列表

当然，你也可以选择使用 HTML 或者文本格式。

## iOS 操作系统的备份

### iCloud 云同步

登录 Apple ID 后，使用 iCloud 就可以同步照片、通讯录、日历等内容。

### 导出应用列表

备份 iOS 的应用列表可以使用 Mac 上的 Apple Configurator 2 工具。



[![img](https://cdn.sspai.com/2017/09/16/e08ebf4fd40e0b53d293d549854b27a6.png?imageMogr2/auto-orient/quality/95/thumbnail/!100x100r/gravity/Center/crop/100x100/interlace/1)](https://sspai.com/app/Apple Configurator 2)

[Apple Configurator 2](https://sspai.com/app/Apple Configurator 2)

[相关文章](https://sspai.com/app/Apple Configurator 2)



把 iOS 设备连接到电脑后，依次选择 Apple Configurator 2 菜单中的「操作」、「导出」、「信息」。







![img](https://cdn.sspai.com/2019/08/23/188436a33edc9213956f6854fade913b.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)导出 iOS 设备信息

之后勾选「已安装的应用」，则可以导出为 csv 逗号分隔文件。





![img](https://cdn.sspai.com/2019/08/23/40af097e94021a6af22e8d53b659f473.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)导出应用列表

使用 Excel 打开后，可以看到这个文件一共分为 3 列：

```
UDID,应用名称,销售商
```

为了使文件内容更清晰，我们借助 Excel 进行调整。首先删除第 1 列和第 3 列，只留下「应用名称」这一列。

接下来继续使用 Excel 移除应用名称中的版本号：

1. 打开 Excel 的「替换」对话框
2. 查找 `(*)`
3. 替换内容设置为空
4. 点击全部替换

这样，文件中就只剩下单纯的「应用名称」了。



## 桌面程序的配置备份与导入

为了在程序安装好之后直接配置成自己顺手的样子，许多程序都自带或者可以通过第三方程序实现配置的备份。这里我只举几个 Windows 上的例子，你可以试着在自己常用的程序中找找「设置导出」的选项，或许有惊喜。

### 导出浏览器扩展列表

借助 CCleaner，我们可以导出 Mozilla Firefox 和 Google Chrome 浏览器中的扩展列表。

![img](https://cdn.sspai.com/2019/08/23/19a8857e990fa8e6f95adf30036d23da.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)CCleaner 中的浏览器扩展列表

依次选择「工具」、「浏览器插件」，并选择相应的浏览器，最后点击右下角「保存为文本文件」，就可以导出扩展列表了。

当然，对浏览器来说，最方便的自然是直接登录 Firefox 和 Google 的账户，设置和扩展会自动进行同步。

### 备份和恢复 Bandizip 设置

按 F5 打开设置后，选择「其他设置」并点击「导出 Bandizip 设置」，所有设置会以注册表项的形式导出。



![img](https://cdn.sspai.com/2019/08/23/bdf50ed587788991161939d6ce9d48f8.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)Bandizip 导出设置

需要导入时，直接双击导出的 reg 文件即可。

### 备份和恢复 DNSJumper 设置

DNSJumper 中的设置项以及配置的 DNS 列表都保存在程序目录下的 `DnsJumper.ini` 文件中，直接备份这个文件就行。

导入时，先找到配置文件的位置，然后使用备份的文件直接覆盖后，打开程序就可以看到备份的 DNS 列表了。

如果找不到配置文件，可以使用 Everything 搜索文件名。

### 定位 Snipaste 设置文件

知名贴图工具 Snipaste 的配置文件名字是 `config.ini`，非常普通。如果通过 Windows 应用商店来安装，会很难找到。

建议使用 Everything 来搜索 `splog.txt`，Snipaste 的配置文件会与这个文件在同一目录下。

### 备份和恢复 VSCode 扩展列表

虽然现在也有 [扩展](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) 可以直接进行设置和扩展的同步，但我依然喜欢手动导出列表，这样更加自由，也更加可靠。

导出扩展列表时，在终端中执行：

```
code --list-extensions > ext-list.txt 
```

对这个文件稍作修改，进行正则替换：

```
(.*)\r?\n
```

替换成

```
--install-extension $1
```

最后在文件开头加上 `code`。这样，整个文件类似于：

```
code --install-extension 扩展1 --install-extension 扩展2 
```

复制整个文件，直接在终端中粘贴并运行，就可以把所有扩展自动装上了。

## 终端配置的备份

准确地说，我们备份的是 Shell 的配置。

如果你经常使用 macOS 的终端、Windows 的 WSL（微软版 Linux）或者是一个 Linux 使用者，那么你很可能需要备份 Shell 的配置，使得重新安装系统或者更换电脑后，可以直接获得舒适的终端体验。

以 zsh 为例，备份 Mac 上的配置文件：

```
cp ~/.zshrc zshrc-mac.conf 
```

备份远程 Linux 服务器上的配置文件：

```
scp user@remote-server:~/.zshrc zshrc-vps.conf 
```

如果觉得不够清晰，还可以使用 VSCode 进行一番正则替换，来把注释和空行移除。

## 那么，如何保存和查阅？

现在，我们已经有了大量的文本文件。可能你还写了几份笔记，记录了自己的重装过程中的操作过程，以便下一次快速搭建。操作过程越详细，装机的时间就会越短。

我使用 Markdown 的格式记录操作步骤，并把大多数导出的文本配置的文件改成了 md 格式。与此同时，我使用 [docsify](https://docsify.js.org/) 搭建了一个简单的网站，放在了自己的 VPS 上。这样，所有的文档和配置就可以随时随地查询啦。

我还把所有的这些文件建立起了一个 Git 仓库，并托管在 Gitlab 上。使用 Git 的好处是，当你调整了软件列表，你可以直接看到增加和删除了哪些软件和配置，还可以对以往的版本进行备份，方便随时回滚。当然，你也可以把文件放在 NAS 上，并使用 Beyond Compare 等工具来检查、修改。

最后形成的文件结构大致是这样的：

```
重装指南
├── 目录.md
├── Google Chrome 扩展
│   ├── 如何备份.md
│   ├── Proxy SwitchyOmega.bak
│   └── 扩展列表.md
├── 桌面程序
│   ├── 如何备份.md
│   ├── Bandizip
│   │   └── Bandizip Settings.reg
│   ├── Directory Opus
│   │   └── Opus Config.ocb
│   ├── DnsJumper
│   │   └── DnsJumper.ini
│   ├── Everything
│   │   └── Everything.ini
│   ├── Listary
│   │   └── Preferences.json
│   ├── Snipaste
│   │   └── config.ini
│   └── VSCode
│       ├── 扩展列表.md
│       ├── 键位绑定.json
│       ├── 全局设置.json
│       └── 代码片段
│           ├── c.json
│           ├── ...
│           └── markdown.json
├── Linux 安装指南
│   ├── CentOS.md
│   ├── 软件列表.md
│   └── WSL.md
├── Mac 安装指南
│   ├── 如何备份.md
│   ├── brew bundle.md│   ├── 应用程序.md
│   └── 手动安装.md
├── 手机应用列表
│   ├── 如何备份.md
│   ├── Android.md
│   └── iPhone.md
├── oh-my-zsh
│   ├── 如何备份.md
│   ├── zshrc-mac.md
│   ├── zshrc-vps.md
│   └── zshrc-wsl.md
└── Windows 安装指南
    ├── 如何备份.md
    ├── 第一次配置.md
    └── 软件列表.md
```