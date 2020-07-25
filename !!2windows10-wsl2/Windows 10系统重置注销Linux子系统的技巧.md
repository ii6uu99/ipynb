# Windows 10系统重置|注销Linux子系统的技巧

作者：[电脑系统](http://www.386w.com/)  时间：2019-03-20   来源： [Win10下载](http://www.win7w.com/)   游览量： 7503次

　　

在Windows 10中，我们可以注销Linux子系统的发行版，也可以将其重置为默认值。重置后，当我们下次启动它时，Windows 10将安装一个干净的、未配置的Linux子系统发行版副本，这样，我们就可以从头配置Linux子系统，例如新建用户、设置密码，并在里面安装我们需要的应用程序等。

 

**今天的这篇文章，我们要讨论的话题是如何重置和注销Linux子系统。**

**一、重置Linux子系统**

重置某一Linux子系统发行版为默认值的方法非常简单，我们甚至可以完全脱离命令行来操作，以下是具体的方法：

打开Windows设置，依次点击“应用”-“应用和功能”，在设置窗口的右半边，我们可以看到当前Windows 10中所安装的所有应用程序。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/3887d3ca1876ecba2354140c28843095.jpg)

 

在所有应用程序列表里，我们可以找到已经安装在Windows 10里的Linux子系统。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/d01f73bea782430c4748e61a700ba810.jpg)

 

以Ubuntu为例，我们点击它，然后再点击“高级选项”链接，Windows设置将跳转到如下页面：

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/399929f1ed01a2758a17b8bb0b1fa129.jpg)

 

在这个页面里，我们可以看到终止（位于标题“终止”下）、“修复”（位于标题“重置”下）、“重置”（位于标题“重置”下）和“卸载”（位于标题“卸载”下）共四个按钮。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/841bda2d6fcbc1d9da89a3b62bd1ffd8.jpg)

 

我们需要点击“重置”标题下的“重置”按钮，Windows设置将会弹出一个用以确认操作的对话框，点击对话框中的“重置”按钮并稍作等待，Linux子系统既可以被重置为默认值。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/624646fc45751d79884ff11b1768d8f0.jpg)

 

当重置操作完成时，我们可以在重置按钮的右侧看到一个对号标志。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/484d65334172296390715cfb63732de3.jpg)

此时，当我们开启刚刚被重置过的Linux子系统，这个干净的子系统就会全新安装，然后要求我们从头开始配置了。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/7ffa44e8e9686b4953629f1436d2c752.jpg)

 

**二、注销Linux子系统**

除了重置Linux子系统之外，我们还可以注销Linux子系统，一旦我们针对某一安装在Windows 10里的Linux发行版执行注销操作，那么与该发行版关联的所有数据、设置和应用程序都将被抹掉，我们可以从微软商店重新安装全新的发行版副本。

在上一篇关于Linux子系统的文章中，Win10天地曾简单地和大家讨论过注销Linux子系统发行版的方法，今天的这期文章，我们将结合用例，为大家做一个更详尽的演示。

现在我们假设，我们在Windows 10安装了很多个相互共存的Linux子系统发行版，而要注销它们中的其中一个，我们需要知道都有哪些Linux子系统发行版此刻存在于Windows 10中。这时，我们可以在命令提示符或者中使用这一命令来列出已经安装在Windows 10中的Linux子系统发行版的列表：

wsl.exe --list --all

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/372310a16317d32e1ffd761f0c60f4e2.jpg)

在本文中，我们以注销列表中的Ubuntu子系统为例，此时，我们需要使用到的命令是：

wsl.exe --unregister Ubuntu

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/bb9d406b2a5cfe7579a9990a25e317ce.jpg)

 

举一反个三，若需要注销Debian子系统，那我们需要在命令行中执行的命令则为：wsl --unregister Debian

其他Linux子系统的发行版同理。

注意，虽然我们注销了某一Linux子系统，使用wsl --list --all命令来列出安装在Windows 10中的Linux发行版的列表时，这一Linux子系统也并未存在于列表中，但这并不意味着上面我们所做的操作等效于“卸载”，当我们从开始菜单中点击图标启动刚刚被注销的Linux子系统的发行版，它会重新安装并要求我们重新配置。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/6c68bc66a6ba1e75767fc4406f07c88a.jpg)

 

**三、重置Linux账户的密码**

有时，我们可能会忘掉Linux子系统发行版中的用户账户的密码，有些同学此时可能会选择重置或者注销Linux子系统，其实这种做法是比较可惜的，正如前文所述，若我们重置或者注销了某一Linux子系统发行版，那么与该发行版关联的所有数据、设置和应用程序都将被抹掉。事实上，当遇到这种情况，比起重置或者注销整个系统来说，重置账户密码是一种几乎不会带来任何损失的做法。

要重置Linux账户的密码，我们只需按教程的指引来执行这些步骤：

打开命令提示符或者PowerShell，执行如下命令：

目标Linux子系统发行版的名称 config --default-user root

例如：

Kali config --default-user root

注：Ubuntu每次都当小白鼠，这次我们换一个发行版下手吧。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/65637277cdb9d22b0c9804b04323a43d.jpg)

 

这行命令的作用是将登录Linux发行版的默认账户设置为root。

启动你忘了用户密码的Linux发行版（例如Kali-Linux），此时我们将以root用户登录。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/e202e4265202ec3e31ab1d97dd5eecf2.jpg)

 

执行以下命令：

passwd 你忘了密码的用户的用户名

例如：

passwd threeseven

此时，Linux子系统将要求我们为忘了密码的用户重新设置密码，按步骤操作即可。

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/854f144febe4db2487b99071c2a62864.jpg)

 

重置过Linux账户的密码之后，不要忘了将登录Linux发行版的默认账户设置为标准账户，使用这一命令：

Kali config --default-user 刚刚重置过密码的用户名

例如：

Kali config --default-user threesevn

![重置|注销Linux子系统](http://xttd.147xz.com/d/file/wenzhang/win10/2019-03-20/d2bcef0d920274711ad1c72d25433d66.jpg)

 

**四、总结**

以上就是今天这期教程的全部内容，在这期教程中，我们讨论了重置Linux子系统发行版、注销Linux子系统发行版和重置Linux账户的密码的方法。正如它们看上去的那样，这篇文章中的各项操作做起来也非常简单。想要了解更多关于Windows的使用技巧，请继续关注Win10天地学院。