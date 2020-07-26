# [为WSL添加右键启动](https://www.cnblogs.com/heyingquan0210/articles/11874941.html)

最近尝试了一下微软的WSL，感觉做的很不错，windows有望成为最佳linux发行版呀！（笑）

在windows下不免要有不少鼠标操作，如果可以像Git Bash在一个文件夹下快速启动，顺便可以自动切换到当前目录会方便很多。

经过一顿操作过后发现是可行的，需要的朋友可以看看：

环境：windows10 17763.805 / WSL:ubuntu

1，找到WSL的安装路径

WSL是在Microsoft Store上安装的，所以我们去C:\Windows\SystemApps，这个文件夹有权限我们想办法打开

然后在.\CanonicalGroupLimited.UbuntuonWindows_1804.2019.521.0_x64__79rhkp1fndgsc文件夹下找到ubuntu.exe ，复制路径

C:\Program Files\WindowsApps\CanonicalGroupLimited.UbuntuonWindows_1804.2019.521.0_x64__79rhkp1fndgsc\ubuntu.exe

（不同版本电脑可能不同，还是找到ubuntu.exe的路径比较保险）

2，修改注册表

1. 找到注册表的路径：计算机\HKEY_CLASSES_ROOT\Directory\Background\shell，单击选中shell右键新建项取名叫bash

2. 单击选中bash右键新建一个项取名为command，还是单击选中bash再右键新建一个字符串取名叫Icon

    目录结构如图：![img](https://img2018.cnblogs.com/common/1822762/201911/1822762-20191117005728358-654108242.png)

3. 修改注册表的值

​       ![img](https://img2018.cnblogs.com/common/1822762/201911/1822762-20191117005901441-1492748320.png)

这里填右键菜单显示的文字，我写的是“Open with WSL Bash”

![img](https://img2018.cnblogs.com/common/1822762/201911/1822762-20191117005908951-452653376.png)

这里填上要显示的图标，我们把ubuntu.exe的路径贴上去：

C:\Program Files\WindowsApps\CanonicalGroupLimited.UbuntuonWindows_1804.2019.521.0_x64__79rhkp1fndgsc\ubuntu.exe

![img](https://img2018.cnblogs.com/common/1822762/201911/1822762-20191117005914926-1837592498.png)

这里是要启动的exe，**注意后面添上 -c bash""**，为了给程序启动时传递参数，要不然是不能找到当前目录的

C:\Program Files\WindowsApps\CanonicalGroupLimited.UbuntuonWindows_1804.2019.521.0_x64__79rhkp1fndgsc\ubuntu.exe -c bash""

 

好了我们来试一试：

![img](https://img2018.cnblogs.com/common/1822762/201911/1822762-20191117010619410-1493875577.png)

 

![img](https://img2018.cnblogs.com/common/1822762/201911/1822762-20191117010636477-2056625564.png)

 

WSL启动了，而且自动找到了当前目录

大功告成！