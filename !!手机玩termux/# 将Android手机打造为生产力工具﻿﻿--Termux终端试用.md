# 将Android手机打造为生产力工具﻿﻿--Termux终端试用



两年前第一次接触termux，当时很兴奋，下班没事就折腾一番，试着装各种软件，记忆比较深刻的是在上面装了一套fedora，成功跑起来了，但是运行速度很慢。那时候版本还不太成熟，安装软件很不顺畅，各种问题，国内用户比较少，百度一下大概能搜到零星的三，五篇中文资料，经常为了装个软件查不少英文资料，有些还要下载源码在termux里重新编译。去年有一段时间为了了解些大数据，人工智能的东西，左termux上装numpy，pandas时，感觉有了很大的改善，不过jupyter当时装上没跑起来。这次更新了一下版本，jupyter跑起来了，一时难抑心中激动，写下这篇文章推荐给大家。

另外，现在国内用户很多了，百度能搜到很多这方面的中文资料，也充分说明termux足够成熟了。

## 简介

Termux是一个Android的高级终端模拟器, 安装后可以在Android手机上搭建一个完整的Linux环境，开源且支持apt管理软件包，十分方便安装各类软件, 完美支持Python,PHP,Ruby,Go,Nodejs,MySQL等等。

Termux有官方的软件源，网速不快，国内用户下载安装termux后可以修改配置使用清华软件源，安装更新各类软件速度很快，上面的软件基本与Linux软件源保持同步。

不需要root权限Termux就可以正常运行，不过需求多的用户能root自然是最好，很多需要root权限的命令就可以执行了，包括文件管理上也会很方便。

## 安装

推荐通过官网安装，地址：

https://termux.com

本人是通过的F-Droid安装的，搜索，选择“Termux Terminal emulator with packages”，当前版本是0.67。

近半年视力有些下降了，可能用手机太多，为了少用手机保护视力换了个老人机，所以本文的所有截图都是在华为可通话平板上操作的，所用Android版本为7.0。

安装后，启动运行的界面是这样的：



[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第1张图片](https://img.it610.com/image/info10/1ab29aebfe0f4f459e21bc32ca25a02b.jpg)](https://img.it610.com/image/info10/1ab29aebfe0f4f459e21bc32ca25a02b.jpg)

图片发自App

## 基本操作

### 长按屏幕

显示菜单项（包括复制、粘贴、更多），此时屏幕出现可选择的复制光标

  长按屏幕

  ├── COPY:复制

  ├── PASTE:粘贴

  ├── More:更多

   ├── Select URL: 选择网址

   └── Share transcipt: 分享命令脚本

   └── Reset: 重置

   └── Kill process: 杀掉当前终端会话进程

   └── Style: 风格配色

   └── Help: 帮助文档

### 从左向右滑动

从左向右滑动，显示隐藏式导航栏，可以新建、切换、重命名会话 session 和调用弹出输入法。



[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第2张图片](https://img.it610.com/image/info10/5230d16388934e66a98182888509f8ad.jpg)](https://img.it610.com/image/info10/5230d16388934e66a98182888509f8ad.jpg)

图片发自App



显示扩展功能按键

扩展功能键是什么? 就是 PC 端常用的按键如: ESC，CTR，TAB, 但是手机上难以操作的一些按键.

效果图



[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第3张图片](https://img.it610.com/image/info10/b7efbdc7cdac47c3afbbdfcaf3f9063b.jpg)](https://img.it610.com/image/info10/b7efbdc7cdac47c3afbbdfcaf3f9063b.jpg)

图片发自App

方法一

从左向右滑动, 显示隐藏式导航栏, 长按左下角的KEYBOARD.

方法二

使用Termux快捷键:音量++Q键

### 常用快捷键

Ctrl键是终端用户常用的按键，但大多数触摸键盘都没有这个按键。为此，Termux 使用音量减小按钮来模拟Ctrl键。

例如，在触摸键盘上按音量减小+ L发送与在硬件键盘上按Ctrl + L相同的输入。

  Ctrl+A -> 将光标移动到行首

  Ctrl+C -> 中止当前进程

  Ctrl+D -> 注销终端会话

  Ctrl+E -> 将光标移动到行尾

  Ctrl+K -> 从光标删除到行尾

  Ctrl+L -> 清除终端

  Ctrl+Z -> 挂起（发送 SIGTSTP 到）当前进程

音量加键也可以作为产生特定输入的特殊键.

  音量加+E -> Esc 键

  音量加+T -> Tab 键

  音量加+1 -> F1（和音量增加 + 2→F2 等）

  音量加+0 -> F10

  音量加+B -> Alt + B，使用 readline 时返回一个单词

  音量加+F -> Alt + F，使用 readline 时转发一个单词

  音量加+X -> Alt+X

  音量加+W -> 向上箭头键

  音量加+A -> 向左箭头键

  音量加+S -> 向下箭头键

  音量加+D -> 向右箭头键

  音量加+L -> | （管道字符）

  音量加+H -> 〜（波浪号字符）

  音量加+U -> _ (下划线字符)

  音量加+P -> 上一页

  音量加+N -> 下一页

  音量加+. -> Ctrl + \（SIGQUIT）

  音量加+V -> 显示音量控制

  音量加+Q -> 显示额外的按键视图

### 目录环境结构

$ echo $HOME

/data/data/com.termux/files/home

这个目录不用多介绍了，你自己的东西都放这吧。

$ echo $PREFIX

/data/data/com.termux/files/usr

软件通常都装在这里。

就这两个目录，另外提醒下，用空间清理时小心些，尽量把有价值的东西先备份，我就是前些天用空空间清理时清了termux，当时清出来2G还挺高兴，结果进去一看什么都没有了，全新安装的一样干净，连装的软件都没了。

## 配置使用

### 编辑安装源

方法一 执行命令:

export EDITOR=vi   # 将 vi 设为默认编辑器

apt edit-sources   # 打开源列表

将原来的https://termux.net官方源替换为http://mirrors.tuna.tsinghua.edu.cn/termux

保存并退出

方法二 直接编辑源文件:

vi $PREFIX/etc/apt/sources.list

修改如下内容:  

\# The termux repository mirror from TUNA:

deb [arch=all,aarch64] https://mirrors.tuna.tsinghua.edu.cn/termux stable main

### 安装基本工具

（1）更新包，安装基本工具

经常用Linux的用户应该很熟悉，命令行直接执行：

apt update

apt upgrade

apt install vim-python curl wget git unzip unrar

(2)管理员身份

手机没有 root

利用proot工具来模拟某些需要 root 的环境

apt install proot

然后终端下面输入:

termux-chroot

即可模拟root环境

在这个proot环境下面, 相当于是进入了home目录, 可以很方便地进行一些配置.

在管理员身份下，输入exit可回到普通用户身份。

### 配置python开发环境

（1）安装Python，个人觉得python2可以不装了

apt install python python-dev

要装python2的话，命令如下

apt install python2 python2-dev

这里安装python-dev是因为后面有些包安装时需要引用一些头文件，如果不装dev会安装失败。

输入python --version 看下版本，确认安装成功

（2）安装必要的软件

•clang和g++——这两个不是Python模块，是编译器，下面的安装有些需要用到。（g++需要的时间挺久，下载包就有200M+）

apt install clang

apt install g++

apt install vim-python

vim，神之编辑器，这是用于python的。

apt install emacs

emacs，编辑器之神，不解释了，不会用也装上。

编辑器这我想多说几句，虽然很多人知道编辑器分三类，一类是vim，一类是emacs，一类是其他编辑器。但咱们开发人员通常都只用第三类，并且一般只用第三类里的IDE，以前我也是这样的，但是我建议至少学学vi怎么用，能用它作一些简单的编辑，会移动光标，修改，插入，删除，查找，保存，退出这些基本操作命令能记住，这样偶尔需要你去在linux系统里做一些操作的话，不至于束手无策，因为vi很可能是你能用的唯一编辑器。

（3）安装python包

•lxml——比标准库里xml模块性能更强大的xml处理模块

这个模块依赖的包很多，需要先安装：

apt install libcrypt libcrypt-dev

apt install libxml2 libxml2-dev libxslt libxslt-dev

接下来就可以安装了：

pip install lxml

•scrapy——专业爬虫库，依赖于lxml

先安装依赖项：

apt install openssl openssl-tool openssl-dev libffi libffi-dev

再安装：

pip install scrapy

•BeautifulSoup4——专业爬虫库

pip install BeautifulSoup4

pip install requests

•numpy——数学计算库

LDFLAGS=“-lm -lcompiler_rt” pip install numpy

•matplotlib——绘图模块

LDFLAGS=“-lm -lcompiler_rt” pip install matplotlib

•pandas——数据分析模块

LDFLAGS=“-lm -lcompiler_rt” pip install pandas

•Jupyter Notebook——超级好用的交互式记事本

apt install libzmq libzmq-dev --依赖包

LDFLAGS="-lm -lcompiler_rt" pip install jupyter

## 试用jupyter

1 启动

jupyter notebook &

或

jupyter notebook



[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第4张图片](https://img.it610.com/image/info10/3647eb0db9514bf993d84fd163e007ba.jpg)](https://img.it610.com/image/info10/3647eb0db9514bf993d84fd163e007ba.jpg)

图片发自App

把最后那行http地址复制到手机浏览器地址栏，即进入jupyter notebook编辑python代码。



[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第5张图片](https://img.it610.com/image/info10/aca8efed30024e09beb37808d4287807.jpg)](https://img.it610.com/image/info10/aca8efed30024e09beb37808d4287807.jpg)

图片发自App



新建一个文件，键入一段代码画个正弦波，看下效果：



[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第6张图片](https://img.it610.com/image/info10/b761c7fc8ed54ae9bf3020d0c4bbad19.jpg)](https://img.it610.com/image/info10/b761c7fc8ed54ae9bf3020d0c4bbad19.jpg)

图片发自App



效果很炫酷吧？这里需要说明下，我本机默认的浏览器不能用，我用的是Firefox。

## 安装mysql

在termux上是不能直接安装mysql的，需要安装他的替代品mariadb，是mysql的一个分支，使用方法是一样的:

apt install mariadb

数据库初始化：

mysql_install_db

启动：

mysqld &

效果图：

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第7张图片](https://img.it610.com/image/info10/3b7426428a3841989654cf9b39ff256c.jpg)](https://img.it610.com/image/info10/3b7426428a3841989654cf9b39ff256c.jpg)

图片发自App

修改密码：

mysql_secure_installation

输入当前root密码

因为是空密码, 这里默认 回车

Enter current password for root (enter for none):

设置新密码

这里设置新的 root 密码

  Set root password? [Y/n] y

  New password:

  Re-enter new password:

其他设置

下面根据个人偏好来进行设置, 没有绝对的要求

  Remove anonymous users? [Y/n] y     #是否移除匿名用户

  Disallow root login remotely? [Y/n] y     #是否不允许root远程登录

  Remove test database and access to it? [Y/n] y #是否移除test数据库

  Reload privilege tables now? [Y/n] y     #是否重新加载表的权限

执行sql脚本，建库，建表，初始化数据。

mysql -uroot -p123456 init.sql

脚本内容如下：

--1 建库

CREATE DATABASE `heLocalDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

--2 建表

USE heLocalDB;

CREATE TABLE IF NOT EXISTS Contact(

  name varchar(20) NOT NULL default '',

  email varchar(30),

  telCell varchar(20),

  telWork varchar(20),

  telHome varchar(20),

  c_group varchar(100) ,

  PRIMARY KEY (name)

);

--3 初始化数据

INSERT INTO Contact (name,telCell) VALUES ('test1', '12345678');

INSERT INTO Contact (name,telCell) VALUES ('test2', '22345678');

使用密码登录数据库

  $ mysql -uroot -p

  Enter password: ******

查询验证：

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第8张图片](https://img.it610.com/image/info10/29895e7748fb4bba93e5831bd2d36629.jpg)](https://img.it610.com/image/info10/29895e7748fb4bba93e5831bd2d36629.jpg)

图片发自App

## 试用python操作mysql

使用Python进行MySQL的底层库主要有两个，Python-MySQL（更熟悉的名字可能是MySQLdb），PyMySQL。和SQLAlchemy。

Python-MySQL资格最老，核心由C语言打造，接口精炼，性能最棒，缺点是环境依赖较多，安装复杂，近两年已停止更新，只支持Python2，不支持Python3。

PyMySQL为替代Python-MySQL而生，纯python打造，接口与Python-MySQL兼容，安装方便，支持Python3。

在上层还有些其他工具，比如SQLALchem，这是一个ORM框架，它并不提供底层的数据库操作，而是借助于MySQLdb、PyMySQL等第三方库来完成，目前SQLALchemy在Web编程领域应用广泛。目前pandas可以借助SQLALchem直接操作数据库，使用很简单，下面分别用pymysql和pandas示范操作mysql的方法。

第一种 使用pymysql

vim testMysql.py

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第9张图片](https://img.it610.com/image/info10/768b7e433bf643489841954fb633fd5d.jpg)](https://img.it610.com/image/info10/768b7e433bf643489841954fb633fd5d.jpg)

图片发自App

执行，查看结果：

python testMysql.py

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第10张图片](https://img.it610.com/image/info10/e1ab6d3d064f4cea94c7c3341300bf9c.jpg)](https://img.it610.com/image/info10/e1ab6d3d064f4cea94c7c3341300bf9c.jpg)

图片发自App

代码如下：

import pymysql

\#打开数据库连接

db=pymysql.connect(host='1.1.1.1',port=3306,user='root',passwd='123123',db='test',charset='utf8')

cursor=db.cursor()#使用cursor()方法获取操作游标

sql = "select * from test0811"

cursor.execute(sql)

info = cursor.fetchall()

db.commit()

cursor.close() #关闭游标

db.close()#关闭数据库连接

第二种 使用pandas

先安装sqlalchem包：

pip install sqlalchemy

代码如下：

vim testPandas.py

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第11张图片](https://img.it610.com/image/info10/a149f45675d7460187f5c37e723015ab.jpg)](https://img.it610.com/image/info10/a149f45675d7460187f5c37e723015ab.jpg)

图片发自App

执行结果：

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第12张图片](https://img.it610.com/image/info10/6b9ef19dc1174946b99fa1b9e8065208.jpg)](https://img.it610.com/image/info10/6b9ef19dc1174946b99fa1b9e8065208.jpg)

图片发自App

注:上两张图是使用蓝牙键盘，横放的截屏效果。

代码:

import pandas as pd

from sqlalchemy import create_engine

from sqlalchemy.types import CHAR,INT

connect_info = 'mysql+pymysql://username:passwd@host:3306/dbname?charset=utf8'

engine = create_engine(connect_info) #use sqlalchemy to build link-engine

sql = "SELECT * FROM test0811" #SQL query

df = pd.read_sql(sql=sql, con=engine) #read data to DataFrame 'df'

\#write df to table 'test1'

df.to_sql(name = 'test1',

con = engine,

if_exists = 'append',

index = False,

dtype = {'id': INT(),

'name': CHAR(length=2),

'score': CHAR(length=2)

}

)

pandas的DataFrame数据格式有行索引和列索引，使用DataFrame来存储数据库表中的数据会十分方便。使用pandas中的read_sql和to_sql函数从MySQL数据库中读写数据，此处不多做介绍了，有兴趣可以去了解下pandas资料。

## 附1：访问手机存储

在termux中可以访问手机存储的，执行命令如下:

termux-setup-storage

会弹出一个开通权限的窗口，确认后，在$HOME目录会出现一个storage文件夹内容如下:

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第13张图片](https://img.it610.com/image/info10/aee17924346541e0a5600a1a1e7a71cb.jpg)](https://img.it610.com/image/info10/aee17924346541e0a5600a1a1e7a71cb.jpg)

图片发自App

这里shared对应手机存储根目录，其他是些软链接，对应音频，视频，图片等，自己去研究吧。

## 附2:其他

termux也支持ssh，git，node.js，nginx等等，听说有人在上面跑过websphere，总之把它当成linux系统，能想到什么都可以上去试试，有问题问百度。

另外推荐一个软键盘，Hacker's Keyboard。

　　这个键盘提供了Tab/Ctrl/Esc和方向键等很多功能键，专为没有实体键，又要操作ConnectBot的人士设计。

上面是百度百科对这个工具的介绍，connectbot是一款安卓上通过ssh连接操作服务器的软件，不多介绍了，实际上有了termux不需要它。

使用效果图

[![将Android手机打造为生产力工具﻿﻿--Termux终端试用_第14张图片](https://img.it610.com/image/info10/0fe0d2f99dc144a6a84e68185091163c.jpg)](https://img.it610.com/image/info10/0fe0d2f99dc144a6a84e68185091163c.jpg)

图片发自App