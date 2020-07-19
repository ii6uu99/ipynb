# 安卓termux折腾手记：安装python库+tasker调用



# 1.termux简介

##  1.1 简介

termux是安卓手机上的一款软件，相当于在安卓上搭建了一个Linux平台，所以在Linux上能干的事情很多在手机上也都办得到，比如本文就是介绍与python相关的内容。

实际上，得益于安卓平台的开放性，类似termux的手机神器着实不少。不说各类强大的编程IDE，单是termux这样的Linux平台类软件就很多，如GnuRoot系列，LinuxDisplay系列等。这其中termux很受人欢迎，对于我来说，其主要优点一是体积小，二是不需要root，三是网上能找到很多相关资源。

除了termux之外，它还有一大群兄弟姐妹们（各种插件）可供大家挑选使用，如下所示。

[![安卓termux折腾手记：安装python库+tasker调用_第1张图片](https://img.it610.com/image/info10/7554d9e54cea4966906f829dd368bce1.jpg)](https://img.it610.com/image/info10/7554d9e54cea4966906f829dd368bce1.jpg)

termux插件

## 1.2下载

官方给出了两个地址，一是Google Play，二是Fiord。

这两个地方略有区别，安装包的签名是不同的。所以如果要和termux家族的其他软件联合使用的话，最好在同一个来源下载。其次在Google play有些额外的软件是付费应用，而上可以免费下载。

##  1.3 termux 初体验

打开termux后的界面如下，包括两部分。

[![安卓termux折腾手记：安装python库+tasker调用_第2张图片](https://img.it610.com/image/info10/7804074e62c943628d8c19e305595df5.jpg)](https://img.it610.com/image/info10/7804074e62c943628d8c19e305595df5.jpg)

termux首界面

\1. 第一部分是termux官方网站和相关资源，实际上还有Github和Google Group。有啥问题到这些地方可以找到答案，像github和官方wiki就有很多资源可供进一步学习。

\2. 第二部分介绍了个包管理器命令pkg，给出了四个命令。最后的help是通用的，前面分别是搜索/安装/升级包。我理解跟linux的apt/apt-get, python的pip差不多，实际上直接用apt命令也可以的。

#  2 安装python模块

我们开始在termux上配置python编程环境了。

##  2.1 安装python

\1. 安装python前首先更新安装包

> apt update
>
> apt upgrade

\2. 安装python，目前模式最新版3.6.4。

python-dev也装上，主要是有些第三方模块用得着。假如安装python2的话，把python改成python2就可以了。

> pkg install python, python2
>
> pkg install python-dev, python2-dev

**Note：**这里用的是pkg，按道理apt也可以，不过这次一开始我用apt报错了。

##  2.2 安装科学计算包

作为爱学习的孩子，我们用python当然要搞一搞当前最热门的数据分析跟机器学习了。

###  2.2.1 jupyter, numpy，matplotlib和pandas

方法来自这篇文章：Running Jupyter and the Scipy stack on Android

\1. 安装这四个包，首先安装下依赖。

> apt install python python-dev clang fftw libzmq libzmq-dev freetype freetype-dev libpng libpng-dev pkg-config

\2. 正式安装包

这四个包安装方法类似，不过实际中安装时很多人会踩坑，其中jupyter是最容易安装的，一般没问题。安好了就可以拥有ipython和jupyter notebook两大神器了。

> LDFLAGS=" -lm -lcompiler_rt" pip install jupyter

这里pip之前加了东西，看到网上说是链接到数学库编译的意思。

剩下三个其中numpy是基础包，是pandas和matplotlib的依赖包，方法类似。

> LDFLAGS=" -lm -lcompiler_rt" pip install numpy matplotlib pandas

**Note：** 第一次一起安装，结果matplotlib部分报错。后来是先装numpy,再一起装pandas和matplotlib（termux可以开多个界面）成功了。

**ipython和matplotlib**

用ipython写代码可以使用各种魔法操作，termux里的界面看着也很漂亮，如下图所示

[![安卓termux折腾手记：安装python库+tasker调用_第3张图片](https://img.it610.com/image/info10/13d28aa494a5490e9ad77a9eab682d3b.jpg)](https://img.it610.com/image/info10/13d28aa494a5490e9ad77a9eab682d3b.jpg)

termux/ipython界面

不过可以看到里面```import matplotlib.pyplot```报错了，主要是缺后端绘图界面支持。命令行作图确实也不大现实。但我们还是可以在手机上使用matplotlib的，毕竟还有jupyter notebook嘛。

在jupyter notebook作图如下：

[![安卓termux折腾手记：安装python库+tasker调用_第4张图片](https://img.it610.com/image/info10/8b0d6cae701c41a691cc16e37185a1c4.jpg)](https://img.it610.com/image/info10/8b0d6cae701c41a691cc16e37185a1c4.jpg)



###  2.2.2 安装numpy，matplotlib可能遇到的问题

numpy，matplotlib可能在安装时可能会有问题，这个跟各个模块的版本号有关系。

安装报错不妨多试几个版本。就是在最后加上版本号信息诸如``pip install numpy==1.12.1``` ```pip install matplotlib==1.2.0```

当然如果你还要一起安装下面两个模块的话，还可以有别的解决方法。

###  2.2.3 安装scipy和scikit-learn

这里安装后一个scikit-learn需要先安装scipy。安装时要用到gcc来编译，不过从某版本开始termux官方版把gcc去除了。

参照官方wiki和Github的大致安装方法如下：

\1. 安装curl. 

> pkg install curl

\2. 命令行输入以下命令

> $ curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh

这里安装了一个叫gnupg的东西，链接到了termux社区一位贡献者(its-pointless)编译的源中，其中把numpy和scipy都包括进去了。也就是说这俩直接编译好了，只需要```pkg

install numpy, scipy``` 即可。

Github里原话是这样的

> This script essentially installs gnupg on your device and downloads and adds a public key to your apt keychain ensuring that all subsequent downloads are from the same source.

\3. 上面已经说了，就是```pkg install numpy, scipy```

4.最后安装scikit-learn就很简单了，直接```pip install scikit-learn```就行。

>  假如前面那个方法按照numpy报错，可以采用该方法

##  2.3 爬虫模块安装

常见的几个比如requests，BeautifulSoup4，lxml，scrapy。

前两个很简单，直接pip安装就行。后两个有一些依赖，而且安装scrapy前必须要先装lxml。

###  2.3.1 lxml，scrapy安装

**lxml**

> apt-get install libxml2 libxml2-dev libxslt libxslt-dev
>
> pip install lxml

**scrapy**

> apt install python python-dev clang libffi libffi-dev openssl openssl-dev libxml2 libxml2-dev libxslt libxslt-dev
>
> pip install scrapy

#  3.termux/Tasker联合使用

前面提到有个apk叫termux-task可以用。

按照这个apk应用即可，具体使用方法：

\1. Tasker任务里添加插件>termux:task，然后添加用termux编写的脚本了。

\2. 脚本放置位置是有要求的，就是要放到```~/.termux/tasker```文件夹里。需要在termux里创建该目录（如下代码所示），然后放入脚本就行。

> mkdir -p .termux/tasker

\3. 这个跟文件系统有关系。比如```~/.termux```. ~ 表示 $HOME, 对于termux来说也就是这个路径 "/data/data/com.termux/files/home".手机未root时 这个目录只有termux才有权限访问。

\4. 实际测试时发现，termux中的可执行程序开头必须加上声明行才可以使用，不然都是当成sh脚本运行的。比如对于python文件，开头要加上一行：

> \#!/data/data/com.termux/files/usr/bin/python

\5. python程序中有文件操作时，没办法直接写一个相对路径，写上绝对路径是可以的。

比如之前提到的```.termux/tasker```文件夹中的xxx.py，

假如程序中有个写入文件```data/xxx.csv```，要换成下面的绝对路径：

> /data/data/com.termux/files/home/.termux/tasker/data/xxx.csv

如下图，为Tasker中添加Termux脚本的界面，这里添加了一个py脚本，选择在termux中运行

[![安卓termux折腾手记：安装python库+tasker调用_第5张图片](https://img.it610.com/image/info10/720061a531ac4b0ab9de663e6d9381db.jpg)](https://img.it610.com/image/info10/720061a531ac4b0ab9de663e6d9381db.jpg)

Tasker添加termux脚本

下图即为脚本执行界面

[![安卓termux折腾手记：安装python库+tasker调用_第6张图片](https://img.it610.com/image/info10/ac54d822a5b64c00b8db31f3768d9b42.jpg)](https://img.it610.com/image/info10/ac54d822a5b64c00b8db31f3768d9b42.jpg)

脚本运行结果

# 4.相关资源

Termux Wiki

termux in Github