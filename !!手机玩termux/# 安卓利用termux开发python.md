# 安卓利用termux开发python



[![安卓利用termux开发python_第1张图片](https://img.it610.com/image/info10/556438ac32a145b79c2e6f1a610b93c5.jpg)](https://img.it610.com/image/info10/556438ac32a145b79c2e6f1a610b93c5.jpg)

htop任务管理

## 一 介绍

termux 是一个安卓平台下的app, 它能够在安卓上实现一个微型的linux,具有命令行界面,可以以apt方式简单的安装软件.本人主要是利用termux开发python软件.在安卓下开发python软件有多种方案,比较简单的就是qpython和termux.qpython提供了安卓下Python的IDE,但对python3支持有限.相对于qpython而言,termux默认下载的python版本是python3,对python3及其相关模块支持良好,且可termux可支持vim,通过openssh和xshell组合能够"爽快"地在电脑端编写代码,在手机端执行.

## 二 安装

1. 从任意一个安卓市场下载安装包（搜索termux或高级终端）,安装即可.
2. 进入app后先输入apt upgrade和apt update 检查更新.
3. 现在就可以apt安装各种应用了.

## 三 使用

#### 3.1 首先列出本人安装的软件包

- apt install python 默认安装的是Python3,毕竟python3是未来啊

- apt install clang 大名鼎鼎的c++ 编译器,用来编译c或c++程序

- apt install vim termux自带vi,如果想使用vim(毕竟神之编辑器),则必须安装,且默认安装vim 8.0 版本, 配合.vimrc,bundle和git 可以完美配置python开发环境,体验几乎和ubuntu的终端无异.

- apt install git 这个码农都懂的

- apt install htop 任务管理器

- apt install tree 目录树

- apt install irssi irc客户端,命令行聊天软件

- apt install sl 跑火车

- apt install openssl ssh远程连接,后期会用到

  [![安卓利用termux开发python_第2张图片](https://img.it610.com/image/info10/9e72e22d62504ecb8561491b6dedf5ba.jpg)](https://img.it610.com/image/info10/9e72e22d62504ecb8561491b6dedf5ba.jpg)

  vim8.0安装插件后效果

### 3.2 未root手机openssh连接xshell

1. xshell下设置连接属性。选择连接选项：名称随意添，主机填写手机的ip地址，端口是

   8022

   .如图：

   [![安卓利用termux开发python_第3张图片](https://img.it610.com/image/info10/aedb834a652c438eacd8d8bebdf02bd3.jpg)](https://img.it610.com/image/info10/aedb834a652c438eacd8d8bebdf02bd3.jpg)

   image.png

2. xshell，该窗口下，选择用户身份验证。用户名在手机上输入命令whoami即可。点击浏览按钮，进入“用户密匙”窗口，点击“生成”按钮。然后按照提示下一步即可，最后生成密匙如图三，将其拷贝即可。

   [![安卓利用termux开发python_第4张图片](https://img.it610.com/image/info10/049bf6b3e3be42368a0e3ff7ede1e19c.jpg)](https://img.it610.com/image/info10/049bf6b3e3be42368a0e3ff7ede1e19c.jpg)

   2.1 输入用户名

   [![安卓利用termux开发python_第5张图片](https://img.it610.com/image/info10/d8ac80ec7dd642e78173c6555df14567.png)](https://img.it610.com/image/info10/d8ac80ec7dd642e78173c6555df14567.png)

   2.2 密匙生成

   [![安卓利用termux开发python_第6张图片](https://img.it610.com/image/info10/22b5aafed85d4f4fa320f975cf61765f.jpg)](https://img.it610.com/image/info10/22b5aafed85d4f4fa320f975cf61765f.jpg)

   2.3 生成密匙

   3 用微信或者qq将拷贝的字符串发送到手机。在手机上复制，然后termux里进入~/.ssh/目录 下。即cd ~/.ssh/ 然后输入命令echo, 之后长按屏幕，直到出现图3.1的画面，按下paste粘贴后在其尾部输入>>authorized_keys即可。

   [![安卓利用termux开发python_第7张图片](https://img.it610.com/image/info10/9b67436e9e584520be2e0b3e9c4010eb.jpg)](https://img.it610.com/image/info10/9b67436e9e584520be2e0b3e9c4010eb.jpg)

   3.1 termux复制

3. 在xshell下登陆，密匙选择刚才生成的即可。

### 3.3 root后openssh连接xshell

毕竟手机还是不适合生产环境,要想撸代码还得是ssh+vim啊.

1. 在termux上打开ssh服务.输入sshd

2. 用re文件管理器将home目录下.ssh文件夹内的id_rsa.pub文件(这个是ssh连接的公匙)复制到手机sd卡,并将其传至电脑.

3. 电脑上打开xshell建立新连接,名称随意添,ip地址可在termux上输入命令ifconfig查看(手机和电脑在同一局域网下).端口8022.

4. xshell用户身份认证选择public key,用户名在termux上运行whoami命令即可.选择浏览,导入刚才复制的密匙.

   [![安卓利用termux开发python_第8张图片](https://img.it610.com/image/info10/d7a5bfe228ba4950ba7d200364c55015.jpg)](https://img.it610.com/image/info10/d7a5bfe228ba4950ba7d200364c55015.jpg)

   xshell导入密匙

5. 选择连接即可登录手机,编写,调试代码.