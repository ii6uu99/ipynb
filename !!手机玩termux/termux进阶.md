#### 基本命令

`Termux`除了支持`apt`命令外,还在此基础上封装了`pkg`命令,`pkg`命令向下兼容`apt`命令.`apt`命令大家应该都比较熟悉了,这里直接简单的介绍下`pkg`命令:

```
pkg search          搜索包
pkg install       安装包
pkg uninstall     卸载包
pkg reinstall     重新安装包
pkg update                 更新源
pkg upgrade                升级软件包
pkg list-all               列出可供安装的所有包
pkg list-installed         列出已经安装的包
pkg shoe  显示某个包的详细信息 pkg files  显示某个包的相关文件夹路径
```

#### 目录环境结构

```
~ > echo $HOME /data/data/com.termux/files/home
~ > echo $PREFIX /data/data/com.termux/files/usr
~ > echo $TMPPREFIX /data/data/com.termux/files/usr/tmp/zsh 
```

长期使用Linux的朋友可能会发现，这个HOME路径看上去可能不太一样,为了方便,`Termux` 提供了一个特殊的环境变量:`PREFIX`

[![Android应用神器：高级终端Termux_第3张图片](https://img.it610.com/image/info8/326d0408ed454fb3be6e7aac5da4e808.jpg)](https://img.it610.com/image/info8/326d0408ed454fb3be6e7aac5da4e808.jpg)

#### 更换国内源

##### 一键 更换`Termux`清华大学源,加快软件包下载速度.

```
sed -i 's@https://termux.net@https://mirrors.tuna.tsinghua.edu.cn/termux@' $PREFIX/etc/apt/sources.list
pkg up
```

##### 手动：

**设置默认编辑器**  export EDITOR=vi 

**编辑源文件** apt edit-sources 

**将原来的 https://termux.net 官方源替换为 http://mirrors.tuna.tsinghua.edu.cn/termux** 

在vi编辑器里，输入第一个`i`进入编辑模式（插入），下面会给出提示“INSERT”，此时再打字就是在光标左边插入字符。等修改完毕后，按住音量上，同时输入`e`，即可退出编辑模式。再输入`:wq`保存并退出vi。

[![img](https://img.it610.com/image/info8/9e2b0c3868c04ed6ac84d30622e1ecaa.jpg)](https://img.it610.com/image/info8/9e2b0c3868c04ed6ac84d30622e1ecaa.jpg)
保存并退出

##### 或者直接编辑源文件

上面是官方推荐的方法,其实还有更简单的方法,类似于Linux下直接去编辑源文件:

```
vi $PREFIX/etc/apt/sources.list 
```

### 安装基本工具

```
pkg install vim curl wget git unzip unrar 
```

## Termux优化

### 添加一行导航栏

原本只有一行，连左右移动光标都没有

```
1 # 如果.termux目录不存在 请自己建立这个目录
2 mkdir .termux
3 # 写入：
4 vim ~/.termux/termux.properties 
5 extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']] 
6 # 保存并关闭 vim命令：“:wq” （去掉双引号），退出termux命令： exit ，重新打开
```

[![Android应用神器：高级终端Termux_第4张图片](https://img.it610.com/image/info8/3573a9a104364ab781aea9776dba00b4.jpg)](https://img.it610.com/image/info8/3573a9a104364ab781aea9776dba00b4.jpg)

### 终端配色

主要使用了 zsh 来替代bash作为默认shell.使用一键安装脚本来安装,一步到位,顺便启动了外置存储,可以直接访问SD卡下的目录.

执行下面这个命令确保已经安装好了curl

```
pkg install curl
sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)" 
```

[![Android应用神器：高级终端Termux_第5张图片](https://img.it610.com/image/info8/c37d6309f162421094b5a9529bb16649.jpg)](https://img.it610.com/image/info8/c37d6309f162421094b5a9529bb16649.jpg)
Android6.0以上会弹框确认是否授权,`允许`授权后`Termux`可以方便的访问SD卡文件. 
脚本允许后先后有如下两个选项:

```
Enter a number, leave blank to not to change: 14 Enter a number, leave blank to not to change: 6 
```

分别选择`背景色`和`字体` 
想要继续更改挑选配色的话,继续运行脚本来再次筛选:

```
$ ~/termux-ohmyzsh/install.sh 
```

 exit 重启`sessions`会话生效配置

### 访问外置存储优化

执行过上面的`zsh`一键配置脚本后,并且授予文件访问权限的话,会在家目录生成`storage`目录，并且生成若干目录，软连接都指向外置存储卡的相应目录

[![Android应用神器：高级终端Termux_第6张图片](https://img.it610.com/image/info8/7cae63e3b54f4e6d83e4619c5b630ec9.jpg)](https://img.it610.com/image/info8/7cae63e3b54f4e6d83e4619c5b630ec9.jpg)

### oh my zsh主题配色

编辑`.zshrc`配置文件

```
$ vim .zshrc
```

第一行可以看到,默认的主题是**`agnoster`**主题:

[![img](https://img.it610.com/image/info8/69862a1d0b204ce8b9ae472660757f60.jpg)](https://img.it610.com/image/info8/69862a1d0b204ce8b9ae472660757f60.jpg)

在 .oh-my-zsh/themes 目录下放着 oh-my-zsh 所有的主题配置文件. 

**agnoster**

[![Android应用神器：高级终端Termux_第7张图片](https://img.it610.com/image/info8/138cedc220014bdfa1659c1b0bc8dd00.jpg)](https://img.it610.com/image/info8/138cedc220014bdfa1659c1b0bc8dd00.jpg)

robbyrussell

[![img](https://img.it610.com/image/info8/6cbbd590c6f74ca7a92b51c7d4ef6081.jpg)](https://img.it610.com/image/info8/6cbbd590c6f74ca7a92b51c7d4ef6081.jpg)

jaischeema

[![img](https://img.it610.com/image/info8/45ac6fd2e2e04e08aed15726f10ec26a.jpg)](https://img.it610.com/image/info8/45ac6fd2e2e04e08aed15726f10ec26a.jpg)

re5et

[![Android应用神器：高级终端Termux_第8张图片](https://img.it610.com/image/info8/6dc5bfe11b584bd4ac71800aad1bebab.jpg)](https://img.it610.com/image/info8/6dc5bfe11b584bd4ac71800aad1bebab.jpg)

junkfood

[![Android应用神器：高级终端Termux_第9张图片](https://img.it610.com/image/info8/2bd304e316544f94897f58d75d8f3163.jpg)](https://img.it610.com/image/info8/2bd304e316544f94897f58d75d8f3163.jpg)

cloud

[![Android应用神器：高级终端Termux_第10张图片](https://img.it610.com/image/info8/046ff8a0d8a4422287804028e27ca8d9.jpg)](https://img.it610.com/image/info8/046ff8a0d8a4422287804028e27ca8d9.jpg)

random

当然如果你是个变态的话,可以尝试`random`主题,每打开一个会话配色主题都是随机的.

```
ZSH_THEME="random" 
```

### 修改启动问候语

默认的启动问候语如下:

[![Android应用神器：高级终端Termux_第11张图片](https://img.it610.com/image/info8/e9f30f4a3447425e8faa0f3c4bb52285.jpg)](https://img.it610.com/image/info8/e9f30f4a3447425e8faa0f3c4bb52285.jpg)
这个对于初学者有一定的帮助在前期,随着对`Termux`的熟悉,这个默认的问候语就会显得比较臃肿. 
编辑问候语文件直接修改问候语:

```
1 vim $PREFIX/etc/motd 
```

修改完的效果如下:

[![Android应用神器：高级终端Termux_第12张图片](https://img.it610.com/image/info8/9f0fb54ab8474323a199bd845042823f.jpg)](https://img.it610.com/image/info8/9f0fb54ab8474323a199bd845042823f.jpg)
这样启动新的会话的时候看上去就会简洁很多.

## 管理员身份

### 手机没有root

利用`proot`工具来模拟某些需要root的环境

```
1 pkg install proot 
```

然后终端下面输入:

```
1 termux-chroot
```

即可模拟`root`环境 
在这个`proot`环境下面,相当于是进入了`home`目录,可以很方便地进行一些配置.

[![Android应用神器：高级终端Termux_第13张图片](https://img.it610.com/image/info8/95c4725b20f64c8489cfeb0b1efa3c04.jpg)](https://img.it610.com/image/info8/95c4725b20f64c8489cfeb0b1efa3c04.jpg)
在管理员身份下，输入 exit 可回到普通用户身份。

### 手机已经root

安装`tsu`,这是一个`su`的termux版本,用来在termux上替代`su`:

```
1 pkg install tsu
```

然后终端下面输入:

```
1 tsu
```

即可切换`root`用户,这个时候会弹出`root`授权提示,给予其`root`权限,效果图如下:

[![Android应用神器：高级终端Termux_第14张图片](https://img.it610.com/image/info8/7de359ebd7be40aa9e18274af008563a.jpg)](https://img.it610.com/image/info8/7de359ebd7be40aa9e18274af008563a.jpg)
在管理员身份下，输入 exit 可回到普通用户身份。

## 信息安全

因为`termux`可以很好的支持`Python`,所以几乎所有用`Python`编写的安全工具都是可以完美的运行使用的. 总的来说可玩性还是比较高的.

### Metasploit

安装Ｍetasploit

Termux官方提供的自动话脚本安装方法如下:

```
1 cd ～
2 pkg install wget
3 wget https://Auxilus.github.io/metasploit.sh
4 bash metasploit.sh 
```

> 注　在x86平台下自动化安装失败，想在x86平台下安装的参考 官方的文档 手动去安装．

这个过程平均耗时大约3分钟左右（使用国内的清华源的情况下）．

配置msf数据库缓存

意外发现数据库居然都配置好了，启动`msfconsole会`自动连接数据库了．

[![Android应用神器：高级终端Termux_第15张图片](https://img.it610.com/image/info8/81f8c791412c46a3ba5a6454676606e9.jpg)](https://img.it610.com/image/info8/81f8c791412c46a3ba5a6454676606e9.jpg)

接下来重建数据库缓存

```
1 msf > db_rebuild_cache
```

这个时候立刻去搜索发现缓存依然没有建立，只能使用慢速搜索，这里其实是这个缓存建立需要时间，只要稍微等待一下就可以了．

> 国光以前这里做过测试，缓存建立的平均时间是3分钟左右．

然后就可以实现`msf`秒搜索的效果了，无需等待，感觉比电脑上还要快呐

[![Android应用神器：高级终端Termux_第16张图片](https://img.it610.com/image/info8/6fd6dae82d074867a3f6e255ed8ec3a4.jpg)](https://img.it610.com/image/info8/6fd6dae82d074867a3f6e255ed8ec3a4.jpg)

### Nmap

端口扫描必备工具

```
1 pkg install nmap
```

[![Android应用神器：高级终端Termux_第17张图片](https://img.it610.com/image/info8/c56d904fb51640a0921c59e8ed10c4fa.jpg)](https://img.it610.com/image/info8/c56d904fb51640a0921c59e8ed10c4fa.jpg)

### hydra

Hydra是著名的黑客组织THC的一款开源暴力破解工具这是一个验证性质的工具，主要目的是：展示安全研究人员从远程获取一个系统认证权限。

```
1 pkg install hydra
```

[![Android应用神器：高级终端Termux_第18张图片](https://img.it610.com/image/info8/51dc4e23a8f942ed824829537f1a56a5.jpg)](https://img.it610.com/image/info8/51dc4e23a8f942ed824829537f1a56a5.jpg)

### sslscan

SSLscan主要探测基于ssl的服务，如https。SSLscan是一款探测目标服务器所支持的SSL加密算法工具。 
SSlscan的代码托管在Github

```
1 pkg install sslscan
```

 

 

 

[![Android应用神器：高级终端Termux_第19张图片](https://img.it610.com/image/info8/819680afa5204fa4a1ef012010e56006.jpg)](https://img.it610.com/image/info8/819680afa5204fa4a1ef012010e56006.jpg)

### whatportis

whatportis是一款可以通过服务查询默认端口，或者是通过端口查询默认服务的工具，简单易用。在渗透测试过程中，如果需要查询某个端口绑定什么服务器，或者某个应用绑定的默认端口，可以使用whatportis查询。

```
1 pip2 install whatportis
```

[![Android应用神器：高级终端Termux_第20张图片](https://img.it610.com/image/info8/669ccc250a624955af159480dc0c0df9.jpg)](https://img.it610.com/image/info8/669ccc250a624955af159480dc0c0df9.jpg)

### SQLmap

SQLmap是一款用来检测与利用SQL注入漏洞的免费开源工具 官方项目地址

直接`git clone`源码

```
git clone https://github.com/sqlmapproject/sqlmap.git cd sqlmap
python2 sqlmap.py 
```

[![Android应用神器：高级终端Termux_第21张图片](https://img.it610.com/image/info8/761a5f56ddbb44f9915c2db051f1fef2.jpg)](https://img.it610.com/image/info8/761a5f56ddbb44f9915c2db051f1fef2.jpg)

### RouterSploit

RouteSploit框架是一款开源的路由器等嵌入式设备漏洞检测及利用框架。

```
1 pip2 install requests
2 git clone https://github.com/reverse-shell/routersploit
3 cd routersploit
4 python2 rsf.py
```

[![Android应用神器：高级终端Termux_第22张图片](https://img.it610.com/image/info8/6b24fe3afbc240a6b936c3328c0df6bc.jpg)](https://img.it610.com/image/info8/6b24fe3afbc240a6b936c3328c0df6bc.jpg)

### Slowloris

低带宽的DoS工具

```
1 git clone https://github.com/gkbrk/slowloris.git cd slowloris
2 chmod +x slowloris.py
```

[![Android应用神器：高级终端Termux_第23张图片](https://img.it610.com/image/info8/0eff6f845bb64b14b50ab3bfa0cec368.jpg)](https://img.it610.com/image/info8/0eff6f845bb64b14b50ab3bfa0cec368.jpg)

### RED_HAWK

一款采用PHP语言开发的多合一型渗透测试工具，它可以帮助我们完成信息采集、SQL漏洞扫描和资源爬取等任务。

```
1 pkg install php
2 git clone https://github.com/Tuhinshubhra/RED_HAWK.git cd RED_HAWK
3 php rhawk.php 
```

[![Android应用神器：高级终端Termux_第24张图片](https://img.it610.com/image/info8/e23ea091442b4382ae6279613e356554.jpg)](https://img.it610.com/image/info8/e23ea091442b4382ae6279613e356554.jpg)

### Cupp

Cupp是一款用Python语言写成的可交互性的字典生成脚本。尤其适合社会工程学，当你收集到目标的具体信息后，你就可以通过这个工具来智能化生成关于目标的字典。

```
git clone https://github.com/Mebus/cupp.git cd cupp
python2 cupp.py 
```

[![Android应用神器：高级终端Termux_第25张图片](https://img.it610.com/image/info8/28fc45823d9d4fc7aa57dfe699e6993c.jpg)](https://img.it610.com/image/info8/28fc45823d9d4fc7aa57dfe699e6993c.jpg)

### Hash-Buster

Hash Buster是一个用python编写的在线破解Hash的脚本，官方说5秒内破解,速度实际测试还不错哦~

```
1 git clone https://github.com/UltimateHackers/Hash-Buster.git cd Hash-Buster
2 python2 hash.py
```

[![Android应用神器：高级终端Termux_第26张图片](https://img.it610.com/image/info8/760939bdbdb64b499c21449b2a0a860f.jpg)](https://img.it610.com/image/info8/760939bdbdb64b499c21449b2a0a860f.jpg)

### D-TECT

D-TECT是一个用Python编写的先进的渗透测试工具,

- wordpress用户名枚举
- 敏感文件检测
- 子域名爆破
- 端口扫描
- Wordperss扫描
- XSS扫描
- SQL注入扫描等

```
git clone https://github.com/shawarkhanethicalhacker/D-TECT.git cd D-TECT
python2 d-tect.py 
```

[![Android应用神器：高级终端Termux_第27张图片](https://img.it610.com/image/info8/a84b657e04e54668a3ad667806018074.jpg)](https://img.it610.com/image/info8/a84b657e04e54668a3ad667806018074.jpg)

### WPSeku

WPSeku 是一个用 Python 写的简单的 WordPress 漏洞扫描器，它可以被用来扫描本地以及远程安装的 WordPress 来找出安全问题。被评为2017年最受欢迎的十大开源黑客工具.

```
git clone https://github.com/m4ll0k/WPSeku.git cd WPSeku
pip3 install -r requirements.txt
python3 wpseku.py 
```

[![Android应用神器：高级终端Termux_第28张图片](https://img.it610.com/image/info8/796f2e96d066494b9811a657cc7ddfba.jpg)](https://img.it610.com/image/info8/796f2e96d066494b9811a657cc7ddfba.jpg)

### XSStrike

XSStrike是一种先进的XSS检测工具。它具有强大的模糊测试引擎.

```
git clone https://github.com/UltimateHackers/XSStrike.git cd XSStrike
pip2 install -r requirements.txt
python2 xsstrike 
```

[![Android应用神器：高级终端Termux_第29张图片](https://img.it610.com/image/info8/85e40cd4df0c4f34a755191c7c958ed2.jpg)](https://img.it610.com/image/info8/85e40cd4df0c4f34a755191c7c958ed2.jpg)

### 小结

因为Termux完美的支持`Python`和`Perl`等语言,所以有太多优秀的信息安全工具值得大家去发现了,这里我就不一一列举了.

## Python环境部署

### 安装python2.7

```
pkg install python2 
```

安装完成后,使用`python2`命令启动`python 2.7.14`环境.

[![Android应用神器：高级终端Termux_第30张图片](https://img.it610.com/image/info8/21f7ea46a9b34fd98d6bad46b242ad69.jpg)](https://img.it610.com/image/info8/21f7ea46a9b34fd98d6bad46b242ad69.jpg)

### 安装python3

```
pkg instll python 
```

安装完成后,使用`python`命令启动`python 3.6.5`环境.

[![Android应用神器：高级终端Termux_第31张图片](https://img.it610.com/image/info8/d5761a4fd7b640bbb4e2ad7d290e41df.jpg)](https://img.it610.com/image/info8/d5761a4fd7b640bbb4e2ad7d290e41df.jpg)

### 升级pip版本

```
python2 -m pip install --upgrade pip  python -m pip install --upgrade pip 
```

这两条命令分别升级了`pip2`和`pip3`到最新版. 
pip版本查看

[![img](https://img.it610.com/image/info8/562667afe35e4f6a9e5ccf36e923c439.jpg)](https://img.it610.com/image/info8/562667afe35e4f6a9e5ccf36e923c439.jpg)

### ipython

ipython是一个python的交互式shell，支持变量自动补全，自动缩进，支持bash shell命令，内置了许多很有用的功能和函数。学习ipython将会让我们以一种更高的效率来使用python。先安装`clang`,否则直接使用`pip`安装`ipython`会失败报错.

```
1 pkg install clang
2 pip install ipython
3 pip3.6 install ipython 
```

 

然后分别使用`ipython`和`ipython2`进入`py2`和`py3`控制台:

[![Android应用神器：高级终端Termux_第32张图片](https://img.it610.com/image/info8/9b5cac9f66dd4c4ab660ff39bb0b8d4e.jpg)](https://img.it610.com/image/info8/9b5cac9f66dd4c4ab660ff39bb0b8d4e.jpg)

### 编辑器

终端下有`vim`神器,并且官方也已经封装了`vim-python`,对`vim`进行了Python相关的优化.

```
pkg install vim-python 
```

解决termux下的vim汉字乱码

在家目录下,新建`.vimrc`文件

```
vim .vimrc 
```

添加内容如下:

```
set fileencodings=utf-8,gb2312,gb18030,gbk,ucs-bom,cp936,latin1 set enc=utf8 set fencs=utf8,gbk,gb2312,gb18030 
```

然后`source`下变量:

```
source .vimrc 
```

效果图

[![Android应用神器：高级终端Termux_第33张图片](https://img.it610.com/image/info8/0e579b9cb5b142b8aae232dfa033ecd5.jpg)](https://img.it610.com/image/info8/0e579b9cb5b142b8aae232dfa033ecd5.jpg)

## php

```
termux`封装的php版本是`php 7.2.5
```

### 安装PHP

```
pkg install php
```

**查看下版本**

![img](https://img.it610.com/image/info8/cb88f4cd14b84b5cb41d9be18ad26af9.jpg)

 

> 自`PHP5.4`之后 PHP内置了一个Web 服务器,来在`termux`下尝试下PHP Web Server的简单使.

### 编写测试文件

在家目录下建一个`www`文件夹: mkdir www 
在`www`文件夹下新建一个`index.php`文件,其内容为

![img](https://img.it610.com/image/info8/c2c022ab3bd349559ed512f434df6ef1.jpg)

### 启动WebServer

```
php -S 127.0.0.1:8080 -t www/
```

浏览器访问效果如下:

[![Android应用神器：高级终端Termux_第34张图片](https://img.it610.com/image/info8/5aec0486b55140ae8c07684f3d1f5451.jpg)](https://img.it610.com/image/info8/5aec0486b55140ae8c07684f3d1f5451.jpg)

## termux ssh 连接电脑

有时候要操作电脑,这个时候有了`termux`,躺在床上就可以操作电脑了,岂不是美滋滋~~
安装`openssh`

```
pkg install openssh
```

然后就可以直接ssh连接你的电脑了

> 前提是电脑安装了ssh服务

```
$ ssh sqlsec@192.168.1.8
```

手机连接操作电脑效果图:

![img](https://img.it610.com/image/info8/564ea1ac81ab4c03b207e4f08b269fd7.jpg)

 

## 电脑ssh连接Termux

**安装openssh**

同样也需要`openssh`才可以

```
pkg install openssh
```

**启动sshd**

安装完成后,`sshd`服务默认没有启动,所以得手动启动下:

```
sshd
```

因为手机上面低的端口有安全限制,所以这里的`openssh`默认的`sshd`默认的服务是`8022`端口上的.
`ssh`的用户名用`whoami`命令看下.

![img](https://img.it610.com/image/info8/c3fe485000bb4389ae282dbecd6573f5.jpg)


可以看到`sshd`启动后,端口才可以看到.

**PC端生成公钥**

`ssh`登录是key公钥模式登录,首先在PC端生成秘钥:

```bash
sqlsec@ubuntu:-> ssh-keygen -t rsa
```

执行完成后，会在家目录下创建3个文件
`id_rsa`, `id_rsa.pub` , `known_hosts`

![img](https://img.it610.com/image/info8/c06173ed2c1240eb82f40d1e5ab74249.jpg)

 

**拷贝公钥到手机**

然后把公钥`id_rsa.pub`拷贝到手机的`data\data\com.termux\files\home\.ssh`文件夹中.

**将公钥拷贝到验证文件中**

在`Termux`下操作

```bash
cat id_rsa.pub > authorized_keys
```

 

![img](https://img.it610.com/image/info8/169c6a98c0c24ae3a248afcc376c19cd.jpg)

 

**PC端连接手机termux**

```bash
sqlsec@ubuntu-> ssh -p8022 u0_a119@192.168.1.3
```

**效果图**

![img](https://img.it610.com/image/info8/efe2e59e8e3644999fa157cc82232f47.jpg)

###  pc端连接手机termux 真心鸡肋呀~(忍不住自己吐槽下自己

## 一些无聊的尝试

一些无聊有趣的版块,如果你是一个正经讲究人,可以跳过这个板块以节约你的阅读时间.

### nyancat 彩虹猫

**彩虹貓**（英语：**Nyan Cat**）是在2011年4月上传在Youtube 的视频，并且迅速爆红于网络，並在2011年YouTube浏览量最高的视频中排名第五.

```bash
pkg install nyancat
nyancat
```

 

![img](https://img.it610.com/image/info8/84c9e26cd3f74c599fddd12d76c87a11.jpg)

 

什么鬼~完全Get不到国外人的趣味点~

### 终端二维码

Linux 命令行下的二维码,主要核心是这个网址:`http://qrenco.de/`

```bash
echo "http://www.sqlsec.com" |curl -F-=\<- qrenco.de 
```

 

![img](https://img.it610.com/image/info8/7bd39e78509a43dbbe0a7e73aa098a2d.jpg)

###  如果你不嫌无聊的话还可以扫描这个二维码,然后就打开我的博客了.

 

### 终端地图

一个基于`nodejs`编写的命令行下的地图.

```
npm install mapscii -g
mapscii
```

进入终端地图

![img](https://img.it610.com/image/info8/5e3258dba6f4430ab459a58ccfa3f70e.jpg)

###  **操作方法**

 

- 方向键 移动
- `a`和`z`键 放大缩小
- `q`键 退出

终端下的地图!讲究人~ 如果你足够无聊的话,还可以尝试能不能在这个地图上找到自己所在的位置.

 

### 安装Linux

甚至还可以在`Termux`里面在安装其他的`Linux`发行版.

由于本文篇幅已经过长了,这里不在叙述了,感兴趣,能折腾的自己去找一些资料.下面列出目前网友们用`Termux`可以成功安装的发行版:

- Ubuntu
- Arch
- Fedora
- Kali Nethunter

Ubuntu

[![Android应用神器：高级终端Termux_第35张图片](https://img.it610.com/image/info8/b25c24c9368d42f9bf94533fcf522ae8.jpg)](https://img.it610.com/image/info8/b25c24c9368d42f9bf94533fcf522ae8.jpg)

Fedora

[![Android应用神器：高级终端Termux_第36张图片](https://img.it610.com/image/info8/9b5a24700aa64de8abc6f6ff159579a3.jpg)](https://img.it610.com/image/info8/9b5a24700aa64de8abc6f6ff159579a3.jpg)

### 内网穿透

使用`ngrok`或者`frp`可以将`Termux`上面搭建的网站映射到外网上去,`手机建站`也不是不可能了.

### Python Jupyter Notebook

Jupyter notebook（又称IPython notebook），支持运行超过40种编程语言。Python的一个强大的模块,成功安装的话可以实现比`caddy`的效果,支持`web`下的终端操作,支持代码高亮运行.由于这里需要安装大量文件,加上用户需求比较少,这一块感兴趣的话可以自己去探索.

[![Android应用神器：高级终端Termux_第37张图片](https://img.it610.com/image/info8/0e18e53b1fce46fd957dee737e2d8df5.jpg)](https://img.it610.com/image/info8/0e18e53b1fce46fd957dee737e2d8df5.jpg)

## 总结

相对来说 国外的Termux DIY的氛围比国内好很多,Youtube上的视频都有很高的播放量:

[![Android应用神器：高级终端Termux_第38张图片](https://img.it610.com/image/info8/a613b2ca2ce0423d967875479e38b500.jpg)](https://img.it610.com/image/info8/a613b2ca2ce0423d967875479e38b500.jpg)

 

###  

 

 

------

 

参考资料来源：

[1] 国光

[2] Termux官方网站

[3] 清华大学开源软件镜像站

转载于:https://www.cnblogs.com/csgo/p/10880746.html