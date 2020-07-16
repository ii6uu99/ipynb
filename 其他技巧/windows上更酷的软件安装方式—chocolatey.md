# windows上更酷的软件安装方式—chocolatey

[Chocolatey](https://link.jianshu.com/?t=https%3A%2F%2Fchocolatey.org%2F)是一款Windows环境下的包管理工具。其依赖于微软旗下的Nuget项目及其核心，可以将其视为Windows的apt-get。

## 安装Chocolatey

推荐使用win8/win10操作系统。

以管理员身份运行CMD，执行以下脚本：



```sh
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
```

如果你习惯用PowerShell.exe，也可以使用管理员身份运行PowerShell后执行：



```sh
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

## 初次使用

举个栗子，你如果想安装7Zip，你可以在命令行输入：



```undefined
cinst 7Zip
```

就会自动安装这个压缩软件。

安装go语言,输入：



```undefined
cinst golang
```

安装Visual Studio 2013 Ultimate这个巨无霸也是可以的：



```undefined
cinst VisualStudio2013Ultimate
```

软件列表，可以在Chocolatey的软件索引查到。

## 命令列表

Chocolatey在命令行里的命令是`choco`,具体的命令如下：



```sh
 * list - lists remote or local packages
 * search - searches remote or local packages (alias for list)
 * info - retrieves package information. Shorthand for choco search pkgname --exact --verbose
 * install - installs packages from various sources
 * pin - suppress upgrades for a package
 * outdated - retrieves packages that are outdated. Similar to upgrade all --noop
 * upgrade - upgrades packages from various sources
 * uninstall - uninstalls a package
 * pack - packages up a nuspec to a compiled nupkg
 * push - pushes a compiled nupkg
 * new - generates files necessary for a chocolatey package from a template
 * sources - view and configure default sources (alias for source)
 * source - view and configure default sources
 * config - Retrieve and configure config file settings
 * feature - view and configure choco features
 * features - view and configure choco features (alias for feature)
 * apikey - retrieves or saves an apikey for a particular source
 * setapikey - retrieves or saves an apikey for a particular source (alias for apikey)
 * unpackself - have chocolatey set it self up
 * version - [DEPRECATED] will be removed in v1 - use `choco outdated` or `cup <pkg|all> -whatif` instead
 * update - [DEPRECATED] RESERVED for future use (you are looking for upgrade, these are not the droids you are looking for)
```

其中的 `choco install` 可以简化为 `cinst`

## 添加seuic源

**理想是美好的，然后现实里那无所不在的墙会让你崩溃，所以我们要使用一个私有源来解决这个尴尬的问题。**

首先我们来看一下默认的源：



```sh
 $  choco source list
chocolatey - https://chocolatey.org/api/v2/ | Priority 0.
```

可以看到系统中只有一个官方的源，注意一下其中的Priority，来看看官方怎么解释的。

> --priority=VALUE
> Priority - The priority order of this source as compared to other
> sources, lower is better. Defaults to 0 (no priority). All priorities
> above 0 will be evaluated first, then zero-based values will be
> evaluated in config file order. Available in 0.9.9.9+.

我们要的目的是加一个seuic内部源，并且让我们的源优先级高于官方源，let's go！好奇宝宝难道不问下为什么要内部源优先？这里主要是要解决choco安装依赖的问题。举栗子：比如安装android-sdk依赖jdk8，指定android-sdk在内部源查找，但是依赖的jdk8则会按照优先级挨个源去找。



```sh
 $  choco source add -n=seuic -s"http://choco.seuic.info/nuget/" 
 $  choco source remove -n=chocolatey
 $  choco source add -n=chocolatey -s"https://chocolatey.org/api/v2/"  --priority=3
```

让我们来检查一下吧。



```sh
 $  choco source list
chocolatey - https://chocolatey.org/api/v2/ | Priority 3.
seuic - http://choco.seuic.info/nuget/ | Priority 0.
```

可以用下面的命令来看看我们seuic源上的东西：



```cpp
choco list -s"seuic"
```

# 一些有用的包

### Cmder：



```sh
 $  cinst cmder -y -s"seuic"
```

cmder是windows下替代cmd的神器，多说无益，一用就知道。安装完后win+R输入cmder即可使用。



![img](https://upload-images.jianshu.io/upload_images/47177-9ccc2f2c295ac9dd.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/909/format/webp)

Cmder

### 安装androidstudio、android-sdk、jdk8三件套：



```sh
 $  cinst androidstudio -y -s"seuic"
 $  cinst android-sdk -y -s"seuic"
$  cinst jdk8 -y -s"seuic"
```

androidstudio依赖android-sdk和jdk8，android-sdk依赖jdk8。choco安装时会自动安装依赖，所以三件套都装的话只要cinst androidstudio -y -s"seuic"即可。这些东西不是要翻墙就是要去oracle网站死磕，现在只要一行命令轻松搞定。

### 安装vagrant+virtualbox：



```sh
 $  cinst vagrant -y -s"seuic"
 $  cinst virtualbox -y -s"seuic"
```

vagrant更适合给开发大爷们创造一个统一的开发、测试、接近于完全隔离的环境，以及提高对高配机的闲置利用。docker更方便地解决了同一机器上的环境隔离，以及提高运维锅们解决部署时环境依赖的效率。