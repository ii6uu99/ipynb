# 电脑上使用Xshell通过ssh连接Termux的详细过程

- [Linux](https://www.it610.com/search/Linux/1.htm)

# 下载安装Xshell免费版

## 进入中文官网

进入Xshell的官网,然后点击顶部导航条上的`所有下载`，`家庭/学校免费`.
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第1张图片](https://img.it610.com/image/info8/b299a5eb09d04ef09d53dba05c78e211.jpg)](https://img.it610.com/image/info8/b299a5eb09d04ef09d53dba05c78e211.jpg)

## 填写邮箱获取下载链接

然后填写姓名和邮箱，选择要下载的程序，然后点击下载,下载链接会发送到刚才邮箱上。
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第2张图片](https://img.it610.com/image/info8/b68a2a6848424ef39dcbb8164691d695.jpg)](https://img.it610.com/image/info8/b68a2a6848424ef39dcbb8164691d695.jpg)

## 接收邮件 并下载

打开邮箱,点击下载链接即可下载Xshell
下载好之后安装Xshell,过程省略…

# 使用Xshell创建秘钥

## Xshell创建秘钥详细过程

打开Xshell，点击`工具`，`新建用户密钥生成向导`
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第3张图片](https://img.it610.com/image/info8/016cb950f69248aa85bc6c887e345f3b.png)](https://img.it610.com/image/info8/016cb950f69248aa85bc6c887e345f3b.png)
然后选择`秘钥类型`和`秘钥长度`,默认即可,点击下一步
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第4张图片](https://img.it610.com/image/info8/b344455fd458468a8054f1b59498944b.jpg)](https://img.it610.com/image/info8/b344455fd458468a8054f1b59498944b.jpg)
等待秘钥生成结束后,继续点击`下一步`.
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第5张图片](https://img.it610.com/image/info8/11fa7fe8754442f9a063826ac5c90f48.jpg)](https://img.it610.com/image/info8/11fa7fe8754442f9a063826ac5c90f48.jpg)
输入`秘钥名称`和`秘钥密码`,继续点击`下一步`
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第6张图片](https://img.it610.com/image/info8/d62206c830a44c55a102194e587b8339.jpg)](https://img.it610.com/image/info8/d62206c830a44c55a102194e587b8339.jpg)

## 保存公钥

此时可以看到公钥了,点击`存为文件`
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第7张图片](https://img.it610.com/image/info8/a20f9fb7d0814165b39d6e9cfb80a7a6.jpg)](https://img.it610.com/image/info8/a20f9fb7d0814165b39d6e9cfb80a7a6.jpg)
保存到电脑上的用户目录下的.ssh目录下:
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第8张图片](https://img.it610.com/image/info8/df4dddf5d11d4b569e880e48c997045f.png)](https://img.it610.com/image/info8/df4dddf5d11d4b569e880e48c997045f.png)

## 导出私钥并保存

然后就看看到创建好的用户秘钥了.
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第9张图片](https://img.it610.com/image/info8/480cb51936994841973af2c0db8391e9.png)](https://img.it610.com/image/info8/480cb51936994841973af2c0db8391e9.png)
导出私钥
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第10张图片](https://img.it610.com/image/info8/6c00a30c38574b47a8859f475830f6c7.jpg)](https://img.it610.com/image/info8/6c00a30c38574b47a8859f475830f6c7.jpg)
输入密码
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第11张图片](https://img.it610.com/image/info8/8e88d6c7517944ad9870652e7bb5ada8.png)](https://img.it610.com/image/info8/8e88d6c7517944ad9870652e7bb5ada8.png)

# 将Xshell创建的秘钥设置到Termux中

## Termux访问`手机存储器`

会在用户主目录下生成`storage`目录,`storage`目录下的`shared`目录对应我们手机**内部存储的根目录**(`/storage/emulated/0/`),我们通过文件资源浏览器打开的就是这个`/storage/emulated/0/`目录,只不过在`Termux`中`/storage/emulated/0/`对应的是`storage`目录下的`shared`目录。

## 将公钥发送到手机上

我这里将公钥通过`QQ`发送到手机上.
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第12张图片](https://img.it610.com/image/info8/b447e4f174f948faadfc414c72f9ec76.jpg)](https://img.it610.com/image/info8/b447e4f174f948faadfc414c72f9ec76.jpg)然后打开手机QQ,接收电脑上发送过来的公钥.

## 复制公钥到.ssh目录下

打开Termux,进入用户home目录下:

```shell
cd ~
```

创建手机QQ`接收文件的那个目录`(`tencent/QQfile_recv`)的`软连接`.

```shell
ln -s /data/data/com.termux/files/home/storage/shared/tencent/QQfile_recv qq
```

[![电脑上使用Xshell通过ssh连接Termux的详细过程_第13张图片](https://img.it610.com/image/info8/d9178a4194054df582da8aa40d15cec6.jpg)](https://img.it610.com/image/info8/d9178a4194054df582da8aa40d15cec6.jpg)
然后复制qq软连接下的公钥到home目录下的.ssh目录中

```shell
mv ~/qq/id_rsa_2048.pub ~/.ssh
```

## 将公钥写入authorized_keys中

进入home目录下的.ssh目录.

```shell
cd ~/.ssh
```

将公钥写入`authorized_keys`文件中

```shell
cat id_rsa_2048.pub > authorized_keys
```

查看公钥

```shell
cat authorized_keys
ssh-rsa AAAAB3Nza.............................................................
```

[![电脑上使用Xshell通过ssh连接Termux的详细过程_第14张图片](https://img.it610.com/image/info8/48ad6488a650460a93582d377e0aaf03.jpg)](https://img.it610.com/image/info8/48ad6488a650460a93582d377e0aaf03.jpg)

# 开启sshd

```shell
sshd
```

# 获取链接信息

## 查看当前Termux用户信息

```shell
whoami
```

whoami的输出就是当前用户的信息:

```
u0_a391
```

## 查看Termux的ip地址

```shell
ifcofig
```

ifcofig运行效果如下:

```
dummy0: flags=195  mtu 1500
        inet6 fe80::bc05:1ff:fe55:4556  prefixlen 64  scopeid 0x20
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 66  bytes 4620 (4.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
......这里省略部分信息.
wlan0: flags=4163  mtu 1500
        inet 192.168.43.1  netmask 255.255.255.0  broadcast 192.168.137.255
        inet6 fe80::76d2:1dff:fe00:73fd  prefixlen 64  scopeid 0x20
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 1824  bytes 1096921 (1.0 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2529  bytes 366296 (357.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

这里的`wlan0`中的** inet 192.168.43.1**中的`192.168.43.1`就是**当前手机的ip地址**

```
wlan0: flags=4163  mtu 1500
        inet 192.168.43.1  netmask 255.255.255.0  broadcast 192.168.137.255
```

# 确保手机和电脑在同一个网络下

- 电脑和手机链接到同一个WiFi下

  ,

  - 这种方式可能会失败,
  - 我在电脑上和手机上分别登录到校园网后,使用Xshell链接不成功,估计是校园网有限制吧,这个问题,浪费我好长时间!,最后发现可以通过热点进行连接

- **电脑链接到手机热点上**

- **手机链接到电脑的热点上**

经过我的测试两种热点连接方式都通过`Xshell`连接到手机上的`Termux`,最好**使用热点方式**。

# 使用Xshell链接Termux

[![电脑上使用Xshell通过ssh连接Termux的详细过程_第15张图片](https://img.it610.com/image/info8/0d1885545196499abb060e0d20fcbdfe.png)](https://img.it610.com/image/info8/0d1885545196499abb060e0d20fcbdfe.png)

## 设置链接常规信息

在弹出的窗口左侧点击`连接`填写上面获取到的的`ip`地址:
端口填写`8020`
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第16张图片](https://img.it610.com/image/info8/0d0ffe2beb8b453886a9ab20106cb783.png)](https://img.it610.com/image/info8/0d0ffe2beb8b453886a9ab20106cb783.png)

## 设置用户身份验证信息

- 点击窗口左侧的`用户身份验证`
- 方法选择框中选择使用`Public key`,
- 在用户名填写上面获取到的Termux`用户名`,
- 选择上面创建好的`秘钥`,
- 填写创建秘钥时的指定的`秘钥密码`.
- 最后点击`连接`

[![电脑上使用Xshell通过ssh连接Termux的详细过程_第17张图片](https://img.it610.com/image/info8/95a00cda31c944f8824bb1cdfc126b70.png)](https://img.it610.com/image/info8/95a00cda31c944f8824bb1cdfc126b70.png)

## 链接成功效果

### 链接成功但是无法操作的情况

如果运行效果如下

```
Connecting to 192.168.137.191:8022...
Connection established.
To escape to local shell, press 'Ctrl+Alt+]'.
```

这说明链接是成功的,但是无法操作,这是因为Termux现在不在前台,把Termux显示在前台即可,也就是显示在屏幕上.

### 保证Termux显示在手机屏幕最上方

如果Termux没有显示在前台的话Xshell无法操作.

```shell
Connecting to 192.168.137.191:8022...
Connection established.
To escape to local shell, press 'Ctrl+Alt+]'.
WARNING! The remote SSH server rejected X11 forwarding request.
Welcome to Termux!
Wiki:            https://wiki.termux.com
Community forum: https://termux.com/community
Gitter chat:     https://gitter.im/termux/termux
IRC channel:     #termux on freenode
Working with packages:
 * Search packages:   pkg search <query>
 * Install a package: pkg install <package>
 * Upgrade packages:  pkg upgrade
Subscribing to additional repositories:
 * Root:     pkg install root-repo
 * Unstable: pkg install unstable-repo
 * X11:      pkg install x11-repo
Report issues at https://termux.com/issues
 u0_a391@localhost  ~  
```

`Termux`从前台切换到后台后连接失败,需要重新连接。

```shell
Socket error Event: 32 Error: 10053.
Connection closing...Socket close.

Connection closed by foreign host.

Disconnected from remote host(Termux) at 16:57:47.

Type `help' to learn how to use Xshell prompt.
[F:\~]$ 
```

## 如何重新链接

将`Termux`切换到前台,然后点击`Xshell`菜单栏面的`文件`,然后点击`重新连接`。
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第18张图片](https://img.it610.com/image/info8/9108dc356e384a3a80f6a9afec8a5640.png)](https://img.it610.com/image/info8/9108dc356e384a3a80f6a9afec8a5640.png)
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第19张图片](https://img.it610.com/image/info8/746cb5b91f5846c88b9fc241dabab373.png)](https://img.it610.com/image/info8/746cb5b91f5846c88b9fc241dabab373.png)

## 设置Termux常驻后台

一直将`Termux`显示在前台还是不方便,可以点击手机通知栏上的`ACQUIRE WAKELOCK`,让`Termux`常驻后台.这样`Termux`在后台的时候也可以保持和`Xshell`的连接。
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第20张图片](https://img.it610.com/image/info8/a2ae08676f364420842d3377bac86008.jpg)](https://img.it610.com/image/info8/a2ae08676f364420842d3377bac86008.jpg)
常驻后台时的效果:
[![电脑上使用Xshell通过ssh连接Termux的详细过程_第21张图片](https://img.it610.com/image/info8/21c1fbdc262d485ebe5f3e5bacd1d644.jpg)](https://img.it610.com/image/info8/21c1fbdc262d485ebe5f3e5bacd1d644.jpg)

# 参考资料

https://blog.csdn.net/jacka654321/article/details/81145756