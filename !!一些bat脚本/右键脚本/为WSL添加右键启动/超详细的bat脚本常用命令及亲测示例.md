超详细的bat脚本常用命令及亲测示例

WZH577 2019-09-04 19:04:38  8131  收藏 47
分类专栏： 计算机基础
版权
注意：编辑bat文件请使用ANSI编码（不然会出现中文乱码）

1、语句注释

rem命令行注释，可以回显（语句会在命令行中显示）；

::两个冒号，效果同上，但不会回显。（冒号后加任意非字母数字字符都可起到注释作用）

2、暂停

pause暂停，命令行中出现"请按任意键继续..."

自定义暂停时的文本，如下：

::pause>nul,隐藏原暂停文本
echo 这里是自定义文本！ & pause > nul
3、输出和换行

echo后加内容即输出该内容，如：echo "welcome!"；

echo.换行命令，即echo后加一个点

4、开启关闭回显

@置于语句前则该条语句不会回显（无视echo on）

echo off关闭回显功能，直到出现echo on，但其本身会回显，故其之前往往和@一起使用，即@echo off（关闭所有回显功能）

5、新建文件、增加文件内容

@echo off
rem 格式：echo 文件内容>文件路径
echo @echo off>test1.bat
::其中>>在文末添加，>覆盖原内容
echo echo this is test>>test1.bat
echo pause>>test1.bat
rem 显示该文件内容
type test1.bat
pause


6、设置标题title、查看返回码errorlevel

@echo off
::title设置标题
title 我测试一下！
::用以判断上一条命令是否执行成功，默认为0，出错为1
echo %errorlevel%
if %errorlevel% 0 echo 没问题
pause


7、设置颜色

例：color 0A



8、if语句

注意：if语句块在执行时是当做一条语句加载的，故需要通过11中的延迟赋值来解决其内部变量引用的问题

::if常规用法，注意空格
@echo off
:start
set /p a=
if not %a%==1 (
	echo 请输入1
	goto start
) else (
	echo 输入正确
)
pause>nul
@echo off
if not exist d:\test.bat (
	echo @echo off>d:\test.bat
) else (
	del d:\test.bat
)
pause>nul
@echo off
set a=1
if defined a (
	echo 已定义a
) else (
	echo 未定义a
)
pause>nul
@echo off
set a=123
set b=abc
set c=12
::/i字符串大小写忽略
if /i %b% equ ABC (
  if %a% geq %c% (
    echo %a%^>=%c%
  ) else (
    echo %a%^<%c%
  )
) else (
  echo %b%不等于ABC
)
pause>nul
如上的操作数可以是字符串、数值、变量；当参与比较的字符串是字符串时，将被转换为对于的ASCII码进行比较；比较运算符有如下：



9、goto语句

@echo off
::使用冒号加标记名作为goto语句的标记
:start
set /p param=
echo %param%
if %param%==4 echo 请不要输入4！ & goto start
pause
10、set用法之接收用户输入数据

@echo off
set /p param=请输入密码：
echo %param%
pause


11、set用法之定义变量和延迟赋值

::输出为1
@echo off
set a=1
set a=2&echo %a%
pause
注意：批处理在运行“set a=2&echo %a%”之前，会先把这一句整句读取并做了预处理，即对变量a赋了值，那么%a%值为4，为解决该问题，批处理设计了变量延迟。也就是说，在读取了一条完整的语句之后，不立即对该行的变量赋值，而会在某个单条语句执行之前再进行赋值，具体实现如下：

::输出为2
@echo off&setlocal enabledelayedexpansion
set a=1
set a=2&echo !a!
pause
12、set用法之系统变量

@echo off
::查看所有环境变量
set
::查看环境变量JAVA_HOME的值
if defined JAVA_HOME echo %JAVA_HOME%
13、set用法之定义数字表达式

@echo off
set a=1&set b=6
set c=%a%+%b%
::输出1+6
echo %c%
set d=a+b
::输出a+b
echo %d%
set /a e=a+b
::输出7
echo %e%
pause
14、for语句

@echo off
::关键字for、in、do必有，括号必有
::分隔符可以是逗号、分号、等号、空格
::输出为A换行1换行B。。。
for %%i in (A,B,C) do echo %%i & echo 1
pause>nul
@echo off
::找出D盘下所有文件
for %%i in (d:\*.*) do echo "%%i"
pause
@echo off
set str=c d e f g h i j k l m n o p q r s t u v w x y z
echo 当前硬盘的分区有：
for %%i in (%str%) do if exist %%i: echo %%i:
pause
@echo off
::找出当前目录下文件名为四个字符的txt文件
for %%i in (????.txt) do echo "%%i"
pause
15、变量%0--%9

%0指该文件本身，%1--%9为接收到的参数，如下例子中子程序的%1即为主程序传输的param1，%2即为param2

::该文件名为test.bat
@echo off
echo 这是主程序第一个输出
timeout 2
start test1.bat param1 param2
timeout 2
echo 这是主程序第二个输出
pause
::该文件名为test1.bat
@echo off
timeout 2
echo 这是子程序第一个输出
echo 这是接收到的第一个参数%1 和第二个参数%2
pause
16、切换目录

::@echo off
::显示当前目录
cd
::切换到根目录
cd\
::盘符加冒号，切换到该盘
d:
::切换到e:hi目录下(目录名不区分大小写)
cd /d e:\hi
::保存当前目录，并切换当前目录为d:\test
pushd d:\test
::恢复当前目录为刚才保存的e:\hi
popd
pause


17、md命令创建文件夹

::创建文件夹
md e:\test\test1
::文件夹名有空格需要加引号
md "e:\test op"
::空格隔开，创建多个
md e:\test1 e:\test9\test2 "e:\test5 lmn"
 18、rd命令删除文件夹

@echo off
::删除e:\test9空文件夹,不为空不能删除
rd "e:\test op"
::删除e:\test9下所有文件夹,不管是否为空,但会询问是否确认删除[Y/N]
rd /s e:\test9
::自定义删除提示信息
echo 是否删除[Y/N]: & rd /s e:\test9>nul
::/s/q联合使用，不会询问直接删除
rd /s/q e:\test9
 19、move命令移动文件(夹)

@echo off
::文件夹移动,如果test文件夹存在,则将test5文件夹移动到test文件夹下
::如果test文件夹不存在，则将test5文件夹移动到test1文件夹下并重命名为test
::注意：文件夹移动不能跨分区
move e:\test5 e:\test1\test
::将d:\test\1.txt文件移动到e:\下并重命名为23.txt
::如果该目录已存在23.txt,则会覆盖
move d:\test\1.txt e:\23.txt>nul&&echo 移动成功并重命名
::将e:\23.txt文件移动到e:\test文件夹下
move e:\23.txt e:\test>nul&&echo 移动到文件夹下
20、del命令删除文件 

@echo off
::删除该层目录下的所有文件,需要确认[Y/N]
del d:\test
pause
::不需要确认
del /q d:\test
::删除该目录下所有层级的文件,不删除文件夹,需要逐个文件夹确认
del /s d:\test
::删除文件111.png,不需要确认
del d:\test\111.png
21、cope命令复制文件

@echo off
::将d:\test\test.txt复制到e:\test1\目录下并重命名为test2.txt
::如果test2.txt文件已存在，将自动覆盖
copy d:\test\test.txt e:\test1\test2.txt
::将e:\test该层目录下所有文件复制到d:\test1\test3文件夹下
::前提d:\test1\test3文件夹必须已存在
::相同文件名的文件会被覆盖
copy e:\test d:\test1\test3
22、xcope命令复制文件

@echo off
::将e:\test目录下所有文件(夹)复制到d:\test1
::/e目录下所有文件(夹),/y已存在时直接覆盖
xcopy e:\test d:\test1 /e/y
23、cope命令合并文件

@echo off
cd /d d:\test
::将129.txt和156.txt两个文件内容合并存入新建的new.txt中
copy 129.txt+156.txt new.txt
::打印出new.txt中的内容
type new.txt
::将d:\mp3\111.mp3和e:\2.mp3以二进制数据合并复制到d:\new.mp3
::其中/b二进制,/a文本形式
copy /b d:\mp3\111.mp3+e:\2.mp3 d:\new.mp3
24、ren命令重命名文件(夹)

@echo off
::将1.txt重命名为58.bat
ren d:\test\1.txt 58.bat
::将d:\test\目录下所有文件名为1开头的txt文件改为bat文件
ren d:\test\1*.txt *.bat
::将d:\test\目录下所有文件名为1开头三个字符的bat改为txt文件
ren d:\test\1??.bat ???.txt
25、call使用

在程序中调用子脚本，在当前程序中运行子脚本代码，子脚本执行完后继续执行本程序之后的代码

::该文件名为test.bat
@echo off
echo 这是主程序第一个输出
timeout 2
call test1.bat param1 param2
timeout 2
echo 这是主程序第二个输出
pause
::该文件名为test1.bat
@echo off
timeout 1
echo 这是子程序第一个输出
echo 这是接收到的第一个参数%1 和第二个参数%2
pause


26、timeout延迟

@echo off
set a=1
:start
echo %a%&set /a a=a+1
timeout 1 > nul
goto start
pause
@echo off
::每隔一秒输出斐波拉契数列
set a=1
set b=1
echo %a%&timeout 1 >nul
echo %b%&timeout 1 >nul
:start
set /a c=a+b
echo %c%&set a=%b%&set b=%c%
timeout 1 > nul
goto start
pause
27、start命令

注意：执行start时将开启一个新线程来执行该程序，原程序不受影响继续执行

@echo off
::打开test.txt文件
start e:\test.txt
::启动jar包
start java -jar e:\demo.jar
pause
28、调用弹框

::一、MSG命令方式
@echo off
::/time:5设置时间弹框的显示时间为5S,5S后自动关闭
msg * /time:5 这里是弹窗显示的文本
pause
::设置弹窗的多行文本
(echo 这是弹窗的第一行文本
echo 这是第二行文本)|msg * /time:5
pause
::一、调用VBScript的MsgBox实现弹窗
@echo off
::第二个参数65的解释在代码之后的列表中
mshta vbscript:msgbox("弹窗单行显示内容",65,"弹窗的标题")(window.close)
::多行显示文本可在文本中使用vbCrLf或vbNewLine
set msg="多行显示vbCrLf这是第二行vbNewLine这是第三行"
mshta vbscript:msgbox(Replace(Replace(%msg%,"vbCrLf",vbCrLf),"vbNewLine",vbNewLine),6,"自定义标题")(window.close)
 MsgBox的button参数取值如下：

0 = vbOKOnly - 只显示确定按钮。
1 = vbOKCancel - 显示确定和取消按钮。
2 = vbAbortRetryIgnore - 显示放弃、重试和忽略按钮。
3 = vbYesNoCancel - 显示是、否和取消按钮。
4 = vbYesNo - 显示是和否按钮。
5 = vbRetryCancel - 显示重试和取消按钮。
16 = vbCritical - 显示临界信息图标。
32 = vbQuestion - 显示警告查询图标。
48 = vbExclamation - 显示警告消息图标。
64 = vbInformation - 显示信息消息图标。
0 = vbDefaultButton1 - 第一个按钮为默认按钮。
256 = vbDefaultButton2 - 第二个按钮为默认按钮。
512 = vbDefaultButton3 - 第三个按钮为默认按钮。
768 = vbDefaultButton4 - 第四个按钮为默认按钮。
0 = vbApplicationModal - 应用程序模式：用户必须响应消息框才能继续在当前应用程序中工作。
4096 = vbSystemModal - 系统模式：在用户响应消息框前，所有应用程序都被挂起。
注意：第一组值 (0 - 5) 用于描述对话框中显示的按钮类型与数目；第二组值 (16, 32, 48, 64) 用于描述图标的样式；第三组值 (0, 256, 512) 用于确定默认按钮；而第四组值 (0, 4096) 则决定消息框的样式。在将这些数字相加以生成 buttons 参数值时，只能从每组值中取用一个数字。

29、获得管理员权限

可尝试以下两种方式

@ echo off
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin
::上面这段代码之后执行的所有东西都是管理员权限方式
@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
>if '%errorlevel%' NEQ '0' (
>echo 请求管理员权限...
>goto UACPrompt
>) else ( goto gotAdmin )
>:UACPrompt
>echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
>echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
>"%temp%\getadmin.vbs"
>exit /B
>:gotAdmin
>echo 获得管理员权限
>pause
> 30、for语句读取文件内容

@echo off
::按行读取d:\test.txt文件中的内容,输出每行的第一个数据,默认每行内以空格和tab为分隔符
for /f %%i in (d:\test.txt) do echo %%i
::delims参数指定分隔符为/
for /f "delims=/" %%i in (d:\test.txt) do echo %%i
::tokens参数指定读取第二列,tokens=*读取所有
for /f "tokens=2 delims=/" %%i in (d:\test.txt) do echo %%i
::skip参数直接跳过前两行,从第三行开始
::tokens=2,*读取第二个和之后剩余所有,%%i为第一列值,%%j为之后剩余所有
::tokens=1,4读取第一个和第四个,%%i为第一列值,%%j为第四列值
::('net start')表示将单引号内语句的执行结果作为集合
for /f "skip=2 tokens=1,* delims=/" %%i in ('net start') do echo %%i %%j
::("asc/2ap/as5")表示对字符串进行处理
for /f "tokens=2,* delims=/" %%i in ("asc/2ap/as5") do echo %%i--%%j
::eol参数直接忽略以#开头的行
for /f "eol=# tokens=*" %%i in (d:\test.txt) do echo %%i
31、sc和net命令

@echo off
::关闭/启动MySQL服务,执行该条语句后会立即执行之后的代码,不会等待停止/启动的过程
sc stop MySQL
sc start MySQL
::设置MySQL服务为自启动,demand手动,disabled禁用
sc config MySQL start= auto
::安装服务
sc create MySQL binPath= "F:\installFiles\mysql-5.7.1.exe"
::卸载服务(卸载前先关闭服务)
sc delete MySQL
::关闭/启动MySQL服务,等待停止/启动的过程,完成后执行之后的代码
net start MySQL
net stop MySQL
::查看所有运行的服务
net start
32、ping命令

@echo off
ping 192.168.0.225
::无休止ping某地址
ping www.baidu.com -t
33、mshta命令

::可以调用vb脚本和js脚本
mshta vbscript:window.execScript("alert('hello world!');","javascript")(window.close)
mshta javascript:window.execScript("msgBox('hello world!')(window.close)","vbs")
mshta vbscript:msgbox("弹窗单行显示内容",65,"弹窗的标题")(window.close)
mshta vbscript:CreateObject("Wscript.Shell").popup("弹窗内容",7,"标题",64)(window.close)
::连续弹二个信息框
mshta vbscript:execute("msgbox ""one BOX"":msgbox ""two BOX"":window.close")
————————————————
版权声明：本文为CSDN博主「WZH577」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/WZH577/article/details/100512784