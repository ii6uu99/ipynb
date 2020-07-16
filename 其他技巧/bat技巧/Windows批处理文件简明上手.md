# Windows批处理文件简明上手

批处理文件主要的功能是依次执行多个命令行语句，可以减少一些繁复的工作。但是它也有一些语言特性，比如变量、控制等。

> 可以专门为bat文件建一个文件夹添加到环境变量里，将一些脚本放进去，就可以在任何位置使用了。

## 简单例子

比如部分朋友可能对下面的Git使用方式很眼熟：



```bash
git add .
git commit -m "some message"
git push
```

里面除了`some message`是变化的，可以写一个下面的脚本（*比如起名**gpush.bat***）：



```bat
git add .
git commit -m "%1"
git push
@pause
```

之后就可以使用一句命令，自动执行上面的操作了。（*此处接受了一个参数作为提交信息*）。



```bash
gpush $message`
```

## 内容提要

1. 语法层面
   1. 控制命令语句显示（*命令语句是否显示在终端界面*）
   2. 变量、控制语句（*if、goto、pause、*）
2. 例子
   1. 计算器实现

## 语法层面

### 基本命令

1. `rem`，什么都不做，可用作注释。
2. `pause`，暂停执行，以双击形式打开`.bat`文件，可以在最后加上`pause`避免执行结束直接关闭终端。

### 命令语句显示

> 区分**命令语句和输出**，命令语句就是你批处理文件里写的每一行代码，输出一般是`echo`命令的执行效果。比如下图关闭和打开命令语句的输出对比：
>
> ![img](https:////upload-images.jianshu.io/upload_images/2668873-c65622c817ffb346.png?imageMogr2/auto-orient/strip|imageView2/2/w/811/format/webp)
>
> 不显示命令与显示命令的对比

首先理解一点，默认情况下，所有命令语句都会显示的，**包括if判断、变量赋值**等。

1. `@`，@开头表示这条语句不显示在终端界面。
2. `echo`，后跟`on/off`时，表示打开/关闭全局命令语句的输出。其他时候，表示输出一些东西到控制台（*也可以输出到指定文件里*）。`echo`命令一般都跟`@`连用，以保证自己不会显示在终端。

### 变量

1. 脚本名后跟一些参数，在脚本里可以使用`%+数字`的形式访问，`%0`指脚本名。比如之前使用的`gpush message`，`%0`就是`gpush`，`%1`就是`message`。

2. 脚本运行中的参数，使用

   ```
   set
   ```

   设置，

   ```
   %{name}%
   ```

   访问:

   

   ```bat
   set a=12
   echo %a%
   ```

   有一些特殊用法：

   1. 将用户输入设置为变量 

      ```
      set /p {name}=提示信息:
      ```

      （

      注意:

      ）

      

      ```bat
      set /p a=请输入参数1:
      ```

   2. 算术运算，比如将a+b的值赋给result变量

      

      ```bat
      set /a result = %a% + %b%
      ```

### 条件和控制

1. `if`，`if "{变量}"=="值"`

2. ```
   goto
   ```

   ，可以直接跳转到指定

   位置

   ，

   位置

   需要以

   ```
   :
   ```

   开头；比如下面要求用户必须输入

   ```
   y/n
   ```

   才可以结束（

   end位置

   ），否则就回到初始位置（

   start位置

   ）：

   

   ```bat
   :start
   set /p agree=是否同意（y/n）:
   
   if "%agree%"=="y" goto end
   if "%agree%"=="n" goto end
   goto start
   
   :end
   pause
   ```

## 例子

1. 加减法计算器

   > 可以输入（`+/-`）选择执行加法还是减法，输入错误会报错。然后获取两个用户输入，输出计算结果。最后让用户可选回到开始位置继续计算。

   

   ```bat
   @echo off
   :start
   set /p action=请选择计算（+/-）:
   
   if "%action%"=="+" goto add
   if "%action%"=="-" goto sub
   goto action_error
   
   :action_error
   @echo 操作错误，只支持（+/-）两种操作
   @goto end
   
   :add
   set /p a=请输入参数1:
   set /p b=请输入参数2:
   set /a result=%a%+%b%
   goto result
   
   :sub 
   set /p a=请输入参数1:
   set /p b=请输入参数2:
   set /a result=%a%-%b%
   goto result
   
   :result
   @echo 计算结果：%a%%action%%b%=%result%
   
   :end
   set /p toStart=继续请输入1:
   if "%toStart%"=="1" goto start
   @pause
   ```



作者：KwokKwok
链接：https://www.jianshu.com/p/876973e26d41
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。