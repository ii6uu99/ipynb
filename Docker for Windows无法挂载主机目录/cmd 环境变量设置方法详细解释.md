# [cmd 环境变量设置方法详细解释](http://www.cppcns.com/jiaoben/dosbat/219111.html)

发布时间: 2019-04-09 12:31:18 来源: 互联网 作者: mdxy-dxy 栏目: [DOS/BAT](http://www.cppcns.com/jiaoben/dosbat/) 点击: 595

cmd设置环境变量可以方便我们bat脚本的运行，但是要注意的是变量只在当前的cmd窗口有作用,需要的朋友可以参考下

cmd设置环境变量可以方便我们bat脚本的运行，但是要注意的是变量只在当前的cmd窗口有作用(局部生效)，如果想要设置持久的环境变量需要我们通过两种手段进行设置：一种是直接修改注册表，另一种是通过我的电脑-〉属性-〉高级，来设置系统的环境变量。

1、**查看当前所有可用的环境变量**：输入 set 即可查看。

![img](http://img.cppcns.com/pic.php?url=/file_images/article/201801/201801302026571.jpg)

2、**查看某个环境变量：输入** “set 变量名”即可，比如想查看temp变量的值，即输入 set temp

![img](http://img.cppcns.com/pic.php?url=/file_images/article/201801/201801302026582.jpg)

当然也可以使用echo %temp%

![img](http://img.cppcns.com/pic.php?url=/file_images/article/201801/201801302026583.jpg)

3、**修改环境变量** ：输入 “set 变量名=变量内容”即可，比如将temp设置为“d:\tempfile”，只要输入set temp="d:\tempfile"。注意，此修改环境变量是指用现在的内容去覆盖以前的内容，并不是追加。比如当我设置了上面的path路径之后，如果我再重新输入set temp="c"，再次查看temp路径的时候，其值为“c”，而不是“d:\tempfile”；“c”。

4、**设置为空**：如果想将某一变量设置为空，输入“set 变量名=”即可。如“set path=” 那么查看path的时候就为空。注意，上面已经说了，只在当前命令行窗口起作用。因此查看path的时候不要去右击“我的电脑”——“属性”........

5、**给变量追加内容**（不同于3，那个是覆盖）：输入“set 变量名=%变量名%;变量内容”。如，为temp添加一个新的路径，输入“ set path=%path%;d:\tempfile”即可将d:\tempfile添加到path中，再次执行"set path=%path%;c:"，那么，使用set path语句来查看的时候，将会有：d:\tempfile;c:，而不是像第3步中的只有c:。

**环境变量详细解释**

**1、查看当前可用的所有环境变量（＝系统变量＋用户变量）**

```
set
```

查看某个环境变量，如PATH

```
set PATH
```

添加环境变量，如xxx=aa

```
set xxx=aa
```

将环境变量（如xxx）的值置为空

```
set xxx=
```

在某个环境变量（如PATH）后添加新的值（如d:\xxx）

```
set PATH=%PATH%;d:\xxx
```

[注]：以命令行方式对环境变量的操作只对当前窗口的应用有效！

**2、Windows下JAVA用到的环境变量主要有3个：JAVA_HOME、CLASSPATH、PATH。**

1）JAVA_HOME指向的是JDK的安装路径，如x:\ j2sdk1.4.2，在这路径下你应该能够找到bin、lib等目录。设置方法：JAVA_HOME=c:\ j2sdk1.4.2

2）PATH变量的作用
java程序在运行时首先在path变量所定义的路径去找java.exe，并以最先找到的为准，如果安装完j2sdk后不加设置，一般是C:\WINDOWS\system32目录。
j2sdk1.4（还有其它java开发工具如jbuilder8）在安装后会将java.exe拷贝到C:\WINDOWS\system32目录下，当执行java.exe时，需要装载这个SDK下的一些文件。
如j2sdk1.4在安装完成后，C:\WINDOWS\system32下的java.exe在运行时会在C:\Program File\java\目录下装载必需的一些文件。但安装j2sdk后一般会在PATH变量的最前面设置C:\ j2sdk1.4.2 \bin。
当先安装j2sdk1.4.2，后安装jbuilder8等开发工具时，由于jbuilder8的java.exe在拷贝到C:\WINDOWS\system32时可能覆盖了j2sdk1.4.2的java.exe，那么这时在运行的java.exe会到jbuilder8所在的目录去装载必需的一些文件。

3）CLASSPATH环境变量的作用
告诉类装载器到哪里去寻找第三方提供的类和用户定义的类。也可用使用JVM命令行参数-classpath分别为应用程序指定类路径，在－classpath中指定的类路径覆盖CLASSPATH环境变量中指定的值。

**3、当机器内装有多个SDK版本时，如何查看所用的是哪个SDK？**

```
java -verbose
```

在出现的屏幕信息中可以看出系统装载的是哪个目录下的文件。

**4、Windows OS下设置PATH的方法**

〔系统〕->〔环境〕-> 〔高级〕，在PATH变量的文本框中的最前面输入C:\ j2sdk1.4.2\bin
或在命令行窗口中执行 set path=c:\j2sdk1.4.2\bin;%path%; 这样在命令行窗口的任一路径下都可以执行java.exe程序了。或设置PATH=%JAVA_HOME%\bin;%PATH%

**5、对于CLASSPATH环境变量的设置方法要加倍小心，是因为以后你出现的莫名其妙80%以上的怪问题都可能是由于CLASSPATH设置不对引起的。**

CLASSPATH=.\;%JAVA_HOME%\lib\tools.jar

首先要注意的是最前面的".\;"，——句点反斜杠分号。这个是告诉JDK，搜索CLASS时先查找当前目录的CLASS文件。
【Troubleshooting】

编译会出现以下情况，看你是否真得都理解环境变量的设置，并能解决它。
[T1]error：java不是一个可运行的程序？ 由于没有设置环境变量path
[T2] error：不能打开某个目录？ 可能是忽视了path环境变量中的目录的设置顺序。
[T3]Exception on thread “main” java.lang.DoClassDefFoundError:Test？ 没有设置classpath的路径。

**cmd查看环境变量**

1、查看当前所有可用的环境变量：输入 set 即可查看。
2、查看某个环境变量：输入 “set 变量名”即可，比如想查看path变量的值，即输入 set path
3、修改环境变量 ：输入 “set 变量名=变量内容”即可，比如将path设置为“d:\hacker.exe”，只要输入set path="d:\nmake.exe"。注意，此修改环境变量是指用现在的内容去覆盖以前的内容，并不是追加。比如当我设置了上面的path路径之后，如果我再重新输入set path="c"，再次查看path路径的时候，其值为“c:”，而不是“d:\nmake.exe”;“c”。
4、设置为空：如果想将某一变量设置为空，输入“set 变量名=”即可。如“set path=” 那么查看path的时候就为空。注意，上面已经说了，只在当前命令行窗口起作用。因此查看path的时候不要去右击“我的电脑”——“属性”........
5、给变量追加内容（不同于3，那个是覆盖）：输入“set 变量名=%变量名%;变量内容”。如，为path添加一个新的路径，输入“ set path=%path%;d:\hacker.exe”即可将d:\hacker.exe添加到path中，再次执行"set path=%path%;c:"，那么，使用set path语句来查看的时候，将会有：d:\hacker.exe;c:，而不是像第3步中的只有c:。

%ALLUSERSPROFILE% 局部 返回所有“用户配置文件”的位置。
%APPDATA% 局部 返回默认情况下应用程序存储数据的位置。
%CD% 局部 返回当前目录字符串。
%CMDCMDLINE% 局部 返回用来启动当前的 Cmd.exe 的准确命令行。
%CMDEXTVERSION% 系统 返回当前的“命令处理程序扩展”的版本号。
%COMPUTERNAME% 系统 返回计算机的名称。
%COMSPEC% 系统 返回命令行解释器可执行程序的准确路径。
%DATE% 系统 返回当前日期。使用与 date /t 命令相同的格式。由 Cmd.exe 生成。有关 date 命令的详细信息，请参阅 Date。
%ERRORLEVEL% 系统 返回最近使用过的命令的错误代码。通常用非零值表示错误。
%HOMEDRIVE% 系统 返回连接到用户主目录的本地工作站驱动器号。基于主目录值的设置。用户主目录是在“本地用户和组”中指定的。
%HOMEPATH% 系统 返回用户主目录的完整路径。基于主目录值的设置。用户主目录是在“本地用户和组”中指定的。
%HOMESHARE% 系统 返回用户的共享主目录的网络路径。基于主目录值的设置。用户主目录是在“本地用户和组”中指定的。
%LOGONSEVER% 局部 返回验证当前登录会话的域控制器的名称。
%NUMBER_OF_PROCESSORS% 系统 指定安装在计算机上的处理器的数目。
%OS% 系统 返回操作系统的名称。Windows 2000 将操作系统显示为 Windows_NT。
%PATH% 系统 指定可执行文件的搜索路径。
%PATHEXT% 系统 返回操作系统认为可执行的文件扩展名的列表。
%PROCESSOR_ARCHITECTURE% 系统 返回处理器的芯片体系结构。值: x86，IA64。
%PROCESSOR_IDENTFIER% 系统 返回处理器说明。
%PROCESSOR_LEVEL% 系统 返回计算机上安装的处理器的型号。
%PROCESSOR_REVISION% 系统 返回处理器修订号的系统变量。
%PROMPT% 局部 返回当前解释程序的命令提示符设置。由 Cmd.exe 生成。
%RANDOM% 系统 返回 0 到 32767 之间的任意十进制数字。由 Cmd.exe 生成。
%SYSTEMDRIVE% 系统 返回包含 Windows XP 根目录（即系统根目录）的驱动器。
%SYSTEMROOT% 系统 返回 Windows XP 根目录的位置。
%TEMP% and %TMP% 系统和用户 返回对当前登录用户可用的应用程序所使用的默认临时目录。有些应用程序需要 TEMP，而其它应用程序则需要 TMP。
%TIME% 系统 返回当前时间。使用与 time /t 命令相同的格式。由 Cmd.exe 生成。有关 time 命令的详细信息，请参阅 Time。
%USERDOMAIN% 局部 返回包含用户帐户的域的名称。
%USERNAME% 局部 返回当前登录的用户的名称。
%UserProfile% 局部 返回当前用户的配置文件的位置。
%WINDIR% 系统 返回操作系统目录的位置。

本文标题: cmd 环境变量设置方法详细解释

本文地址: http://www.cppcns.com/jiaoben/dosbat/219111.html