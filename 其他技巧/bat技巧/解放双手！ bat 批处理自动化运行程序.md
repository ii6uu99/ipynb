# 解放双手！ bat 批处理自动化运行程序



bat 批处理脚本是 Windows 系统上用于批量执行任务的脚本，其后缀名为 `.bat`。利用批处理文件与“胶水语言” Python 相结合，能解决很多情况下程序的自动化运行问题，为学习、科研、工作上带来很大的便利。

近来做科研项目，需要运行某一个模型软件数十次乃至上百次。此前对 bat 批处理的了解比较有限，借此机会完成项目的机会，对常用的 bat 脚本做了一个简单的入门学习。特此对过程中学习到的知识点作简要总结，也希望对未“入坑”者有所帮助。

### **命令总结**

### **echo**

“echo”一词英文本意为“发出回声”、“产生回响”，大致相当于 Python 中的 print 函数，可以在 cmd 窗口中显示消息，也有打开和关闭回显的功能。常用的代码有以下两种：

1. 在屏幕上打印“hello world”

```text
echo hello world
```

1. 关闭运行命令本身的显示

```text
@echo off
```

### **@**

加在其他命令行最前面，表示运行时不显示该命令行本身。

```text
@echo Now starting the model...
```

### **call**

从一个批处理程序调用其他批处理程序，而不终止原来的程序。举个例子，下面的命令调用 Anaconda 的 activate.bat 脚本，使用该操作可以在 cmd 窗口中激活某一环境。

```text
call D:\Commonsoftware\Anaconda\Scripts\activate.bat
call activate myenv
```

其中，`myenv` 是需要激活的环境名称。

### **pause**

在执行完命令后显示“请按任意键继续···”字样。该命令一般用来调试程序，确保批处理代码在执行中没有出现任何问题。常放在 bat 文件末尾和其他想终止程序的地方。

### **REM**

bat 文件注释。对应的 Notepad++ 的快捷键为 `Ctrl+k` （单行、多行注释）& `Ctrl+q` （区块注释）。

### **if**

批处理中执行条件处理的语句。首先，需要了解 bat 文件中比较运算符的有效值。

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%5Bb%5D%7B%7Cc%7Cc%7Cc%7Cc%7C%7D++%5Chline+%5Ctextbf%7B%E8%BF%90%E7%AE%97%E7%AC%A6%7D%26%5Ctextbf%7B%E6%8F%8F%E8%BF%B0%7D%26%5Ctextbf%7B%E8%BF%90%E7%AE%97%E7%AC%A6%7D%26%5Ctextbf%7B%E6%8F%8F%E8%BF%B0%7D%5C%5C%5Chline+%5Cmathrm%7BEQU%7D%26%E7%AD%89%E4%BA%8E%26%5Cmathrm%7BLEQ%7D%26%E5%B0%8F%E4%BA%8E%E6%88%96%E7%AD%89%E4%BA%8E%5C%5C%5Chline+%5Cmathrm%7BNEQ%7D%26%E4%B8%8D%E7%AD%89%E4%BA%8E%26%5Cmathrm%7BGTR%7D%26%E5%A4%A7%E4%BA%8E%5C%5C%5Chline+%5Cmathrm%7BLSS%7D%26%E5%B0%8F%E4%BA%8E%26%5Cmathrm%7BGEQ%7D%26%E5%A4%A7%E4%BA%8E%E6%88%96%E7%AD%89%E4%BA%8E%5C%5C%5Chline+%5Cend%7Barray%7D)

下面来看一个例子。

```text
@echo off
set /a a=123
set /a b=456
if %a% geq %b% (
  echo %a%^>=%b%
) else (
  echo %a%^<%b% 
)
pause
```

需要注意的是，if 语句后的括号必须要写在与其同一行的末尾。

此外，在进行字符串比较时，if 后加 `/i` 命令可强制字符串比较时忽略大小写。

### **choice**

此命令本意是显示信息并暂停批处理程序，让用户在做一些交互的选择。比如 Anaconda 中安装 Python 包时的提示是否安装的 [y/n] 就是利用的这个命令。

有时，利用此命令占用内存较小、计时较为精确的特点，可以用此命令进行计时，程序会等待特定的时间，再执行下面的命令。以下语句表示等待 10 秒再执行批处理程序。

```text
choice /t 10 /d y /n >nul
```

值得注意的是，用该命令计时有个缺陷：只能计时 0~9999 秒之内的时间（约 2.7 小时，但一般情况还是够用的）。

### **for**

循环命令。直接看代码：

```text
REM 1
@echo off
for %%a in (1, 1, 5) do (
  echo %%a
)
pause
```

执行结果：

```text
1
1
5
```

以上代码表示，变量 `a` 在集合 `(1, 1, 5)` 中进行遍历，然后回显出值。

```text
@echo off
for /l %%a in (1, 1, 5) do (
  echo %%a
)
pause
```

执行结果：

```text
1
2
3
4
5
```

以上代码表示，变量 `a` 从 1 开始，步长为 1，终值为 5，进行循环。

两段代码的区别在于，第二段代码在 for 循环开始时，多了 `/l` 参数。

### **setlocal**

启动批处理文件中环境变量的本地化。通俗地讲，该命令执行后会使得批处理程序对局部变量进行修改，而不是始终保持全局变量的值。如果这里没有看懂的话，请比较以下两段代码就清楚了：

```text
REM 1
@echo off
set /a a=123

if %a% equ 123 (
  set /a a=%a%*2
  echo %a%
) else (
  echo %a% not equal to 123 
)
pause
```

执行结果为：123。

```text
REM 2
@echo off
set /a a=123

setlocal enableDelayedExpansion
if !a! equ 123 (
  set /a a=!a!*2
  echo !a!
) else (
  echo !a! not equal to 123 
)
pause
```

执行结果为：246。

执行结果差异的原因在于第 1 段代码没有开启环境变量的本地化，因此在设置变量值后，引用变量时仍然是全局变量的值；使用 `setlocal` 指令后，解决了这一问题。显然，第 2 段代码是我们预期的结果。

比较这两段代码可以发现，使用 `setlocal` 主要需要注意以下两点：

1. 需要声明 `setlocal enableDelayedExpansion` ；
2. 变量引用形式均为 `!a!` 。

### **taskkill**

结束某一进程。常用的有以下两种用法：

1. 结束已知应用名称的某一进程；
2. 结束已知进程码的某一进程。

以关闭 Notepad++.exe 程序为例举些例子：

```text
REM 1
taskkill /im notepad++.exe

REM 2
taskkill /pid 1376 -t -f
```

进程码可以通过任务管理器查询，或者通过 `cmd` 运行 `tasklist` 获取。

参数 `-t` 表示结束该进程，`-f` 表示强制结束该进程及所有子进程。

### **代码总结**

### **自动化运行 IPython**

有时想启动 Ipython 做个简单的计算或者验证，与打开 Spyder 或者 PyCharm 等 IDE 相比，此时调出 Ipython 最为方便省时间。但打开 Anaconda Prompt 又需要输入激活环境等命令，比较麻烦。使用下面的命令可以大大简化这样的问题。

```text
REM ip.bat
call D:\Commonsoftware\Anaconda\Scripts\activate.bat
call activate myenv
call jupyter qtconsole
```

如果不想把脚本防在桌面，可以配置环境变量，使用 `Win+R` 快捷键输入批处理文件名 `ip.bat` 就能方便地打开 IPython。

### **自动化运行 Jupyter Notebook**

与以上情景类似，使用以下代码，轻松打开 Jupyter Notebook：

```text
E:
cd E:
call D:\Commonsoftware\Anaconda\Scripts\activate.bat 
call activate myenv
start chrome http://localhost:8888/tree
call jupyter notebook
pause
```

默认的打开文件路径在 E 盘，当然可以根据个人情况进行修改~

### **在 cmd 窗口中写 Python语句**

有时在命令行窗口中想做些简单的计算或文本处理，无需再打开 Python IDE，直接在 cmd 窗口中就可以写简单的 Python 程序：

```text
python -c "import numpy as np; print(np.arange(6))"
```

### **自动化运行模型**

回到最初的目的应用场景，下面是自动化运行某一模型或者应用程序的示例代码。`cyc` 是运行次数，`ti` 是模型运行一次的持续时间，`start` 语句是新建一个 cmd 窗口运行程序，`&&` 表示程序先后进行，即先打开程序路径再运行程序，程序中应用 Python 脚本可以进行模型的前处理和后处理。

```bat
@echo off
setlocal enabledelayedexpansion
set cyc=100
set ti=3000
call D:\anaconda3\Scripts\activate.bat
call activate myenv
python model_preprocess.py
for /l %% i in (1,1,!cyc!) do (
   start cmd /c "cd ./AppPath && model.exe"
   choice /t !ti! /d y /n >nul
   taskkill /f /im model.exe
)
python model_postprocess.py
endlocal
taskkill /f /im cmd.exe
```

### **小结**

1. 通过本文，基本上对批处理有了个简单的入门，对某些参数功能不清楚时，在 cmd 窗口中输入 `/?` 是最简单快捷的查看文档的方式；
2. 有些时候在网上复制的代码不能直接在命令行及批处理文件中应用，应将其转化为 ANSI 编码后查看没有乱码后运行才不会出错；
3. 批处理文件作为 Windows 系统的自动化处理的利器，可以做到一些 Python 脚本不能做到或者不方便做到的事情，此时简单学些批处理可以大大提高工作效率和自动化水平，但是如果 Python 脚本可以做到的事采用 Python 更方便快捷，易于调试和维护。

### **参考文献**

1. 张亮清编著《DOS/BIOS高手真经》第2版
2. **[bat中if语句的用法](https://link.zhihu.com/?target=https%3A//blog.csdn.net/sanqima/article/details/37818115)**
3. **[cmd-bat批处理命令延时方法](https://link.zhihu.com/?target=https%3A//blog.csdn.net/jk110333/article/details/41869053)**