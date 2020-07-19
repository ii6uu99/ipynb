# 详细 termux 开启ssh

- [实用](https://www.it610.com/search/实用/1.htm)
-  

- [解决方案](https://www.it610.com/search/解决方案/1.htm)
-  

- [linux](https://www.it610.com/search/linux/1.htm)
-  

- [Android](https://www.it610.com/search/Android/1.htm)

## **通过ssh让手机端认识（信任）pc端————————SSH是什么？**

**简要原理分析：**

这里涉及到加密算法，为了简化小白的操作不展开来说，大体就是pc端生成自己的公钥，然后让手机端认识公钥，然后用私钥连接手机ssh服务端

## 为什么要用SSH—————————————————为什么用SSH？

1.安全，所有传输的命令都会加密，防止窃听等

2.方便，不需要输入密码，配置一次，以后再使用的使用直接使用ssh登录

3.装逼。

## **概要步骤————————————————————怎么用SSH？**

1. 在手机上，termux中安装 openssh
2. 电脑（客户端）上生成自己的公钥，秘钥
3. 把公钥传到手机端ssh对应文件中
4. 手机端开启ssh
5. pc端连接

其中1-3只需配置一次，步骤4根据用户喜好可以自定义，总之，以后直接连接即可。

## 展开*******************

### 1.安装 openssh

执行命令

```bash
pkg install openssh
```

（如果有问题，可能权限不够或者内核不同，权限不够可以root，关于root可以百度一下~，也可以采用其他的安装方式，比如apt-get install openssh，apt install openssh等等）

### 2.成自己的公钥，秘钥

这里有很多种方式，我使用的是xshell。

2.1 xshell方式：

xshell是一个软件，可以自己搜索下载，或者留言给我，直接开始了;

[![详细 termux 开启ssh_第1张图片](https://img.it610.com/image/info8/a8c78b63514844779b3bd143e2e0bcc5.jpg)](https://img.it610.com/image/info8/a8c78b63514844779b3bd143e2e0bcc5.jpg)

按照图中，选 工具 --- 新建用户秘钥生成向导

[![详细 termux 开启ssh_第2张图片](https://img.it610.com/image/info8/705da72866714fa6964c32952921c3b0.jpg)](https://img.it610.com/image/info8/705da72866714fa6964c32952921c3b0.jpg)

我这里选择的是RSA，因为 SSH有两个版本 ssh1 和 ssh2 ，rsa是两个版本都兼容的，DSA只能在 SSH2 协议中使用。

下一步

生成完毕之后继续下一步

[![详细 termux 开启ssh_第3张图片](https://img.it610.com/image/info8/63a054d792d7434eb996e054aeacd460.jpg)](https://img.it610.com/image/info8/63a054d792d7434eb996e054aeacd460.jpg)

秘钥名称无所谓，输入你的密码，自己随便输就好了，继续下一步

[![详细 termux 开启ssh_第4张图片](https://img.it610.com/image/info8/f4d6c7e0d96b4979aad82386e63ca182.jpg)](https://img.it610.com/image/info8/f4d6c7e0d96b4979aad82386e63ca182.jpg)

这里点保存为文件存在自己的电脑上，比如 C:/xxx.pub

之后完成即可。

\--------------------

其他秘钥生成方式，比如windos上打开 git bash ，然后运行下面命令，类似的，输入好保存的地址回车就行了，

linux系统可以直接运行以下命令（有openssh前提）

```html
ssh-keygen
```

### 3.把公钥传到手机端ssh对应文件中

这一步由于手机上不好操作，比较麻烦，各位可以差键盘或者用qq 发文件，或者用 adb 命令等。这里为了照顾小白，用最直白的方式：发文件

用QQ也好，微信也好，啥都行，总之就是要把刚才生成的 xxx.pub 文件放到手机上，不管放到哪里，然后在termux里执行

```
 cat xxx.pub > data/data/com.termux/files/home/.ssh/authorized_keys 
```

\------------------------

其他：如果不知道传到哪里了，可以通过 find 命令来定位文件：

```
find / -name "xxx.pub"
```

定位到之后可以:

```
 cat (这里输入路径)/xxx.pub > data/data/com.termux/files/home/.ssh/authorized_keys 
```

### 4.手机端开启ssh

sshd命令即可开启

```
sshd
```

\-----------------------

，如果之前开启了，需要重启(重新读取配置文件)

```
service restart sshd
```

### 5.连接

最后一步，在新建连接里可以设置，其中用户名可以在 termux 里使用 whoami 命令来获取，秘钥选择刚才的，密码为刚才输入的

 

 

[![详细 termux 开启ssh_第5张图片](https://img.it610.com/image/info8/6e11c61eee6b4485a66e567685bdfe30.jpg)](https://img.it610.com/image/info8/6e11c61eee6b4485a66e567685bdfe30.jpg)

连接上之后，你就可以为所欲为了！

### 关于乱码解决方案：https://blog.csdn.net/qq_35425070/article/details/84790007