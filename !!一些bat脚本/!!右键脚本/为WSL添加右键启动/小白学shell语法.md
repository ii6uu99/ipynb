# 小白学shell语法

[![img](https://upload.jianshu.io/users/upload_avatars/2907896/20efad908363?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp)](https://www.jianshu.com/u/12ac172cedc5)

[晴空一垩](https://www.jianshu.com/u/12ac172cedc5)关注

0.1682019.07.31 10:16:04字数 856阅读 68

注意事项

1. 赋值 “=” 左右两边不能有空格
2. 判断区间"[]" 方括号的左右两边都必须有空格！

### 第一行

写shell第一行叫做伴释行，就是制定使用什么解释器来执行下面的语句

如果我们不写这一行，在某些平台上默认使用`/bin/sh`，在某些平台上会有问题。

而一般我们指定`/bin/bash` 因为这两个解释器的语法规则不大一样，建议使用bash，具体的区别看 [这里](https://links.jianshu.com/go?to=https%3A%2F%2Faskubuntu.com%2Fquestions%2F141928%2Fwhat-is-the-difference-between-bin-sh-and-bin-bash)

意思是bash基本上就是sh，但是比sh有更多的特性和更好的语法 。

sh在很多平台上是一个连接，在某些平台上指向bash或者dash。所以我们指定了sh，在别的平台上可能使用dash来进行解释了，导致出现问题。

在我的电脑上运行



```shell
file /bin/sh

# 输出
/bin/sh: symbolic link to dash
```

### 控制流



```bash
# for语句
for name in w1 w2 ...
do command-list
done

# case 语句
case word in
pattern ) command-list ;;
*) ...;;
esac

# if语句
if command-list
then command-list
else command-list
fi

# while语句
while command-list1
do command-list2
done
```

### $ 的意思



```ruby
1，$# ：代表命令行参数个数，即 2 
2，$* ：代表所有的参数，即 abcd 1234
3，$@ ：同上
4，$n ：第 n 个参数，比如$1 即 abcd，而$2 就是 1234
5，$? ：代表最后一个命令执行之后的返回值
6，$$ ：代表当前 shell ds
7, $! : 上一个后台进程号
```

### trap 跟踪脚本的信号，

eg：SIGEXIT

```
trap on_exit EXIT
```

表示将订阅SIGEXIT这个信号。使用on_exit进行处理

```
trap -l` 可以查看可以订阅多少个类型的信号。注意去掉前面的`SIG
```

### shell 里的符号



```shell
$ parameter substitution
$() command substitution
` command substitution
" ends the quoted string 其中可以包含变量，
' 单引号 ：表示都是字符串来解释
\ quotes the special characters $`"\
```

### shell 里面的比较

语法：`[ xxx ]` 或者 `test xxx` ,两种都是等效的。



```shell
if test -z "$func_normal_abspath_result" ; then
    func_normal_abspath_result=/
fi

# 或者
if [ -z "$func_normal_abspath_result" ] ; then
    func_normal_abspath_result=/
fi
```

![img](https://upload-images.jianshu.io/upload_images/2907896-434cdb556b789aa1.png?imageMogr2/auto-orient/strip|imageView2/2/w/553/format/webp)

shell_compile.png

### {} vs ()

> () 会起一个新进程来执行命令，不会影响当前会话
> {} 和() 相反，会影响。

### 参数拓展

##### ${parameter:-word}

parameter没有设置则使用word进行替换，如果有则不改变原有的值

If parameter is unset or null, the expansion of word is substituted. Otherwise, the value of parameter is substituted.

##### ${parameter:=word}

无则设值

If parameter is unset or null, the expansion of word is assigned to parameter. The value of parameter is then substituted. Positional parameters and special parameters may not be assigned to in this way.

##### ${parameter:?word}

如果parameter没有设值，则抛出异常信息word

If parameter is null or unset, the expansion of word (or a message to that effect if word is not present) is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of parameter is substituted.

##### ${parameter:+word}

有则添加，没有则不添加

If parameter is null or unset, nothing is substituted, otherwise the expansion of word is substituted.

##### ![{parameter:offset} VS](https://math.jianshu.com/math?formula=%7Bparameter%3Aoffset%7D%20VS){parameter:offset:length}

类似substring ，字段截取

### 几个问题

> ![{var%} 和](https://math.jianshu.com/math?formula=%7Bvar%25%7D%20%E5%92%8C){var%%} 是什么意思



```bsh
${var%Pattern} Remove from $var the shortest part of $Pattern that matches the back end of $var.
${var%%Pattern} Remove from $var the longest part of $Pattern that matches the back end of $var.

# So if var="abc def ghi jkl"

echo "${var% *}" # will echo "abc def ghi"
echo "${var%% *}" # will echo "abc"
```

> shell 作用域 global vs local

local一般用于局部变量声明，多在在函数内部使用。

shell函数定义的变量默认是global的，

> shell中eval 的意义？

construct command by concatenating arguments

链接参数成为一个命令



```shell
 option_set_attr ()
 {
   eval OPTIONS_$1_$2=\"$3\"
 }
 option_set()
 {
     OPTIONS_$1_$2=\"$3\"
 }
 
 option_set_attr 1 2 3
 option_set 2 3 4
 
 echo ${OPTIONS_1_2:?"x"}
 echo ${OPTIONS_2_3:?"xxx"}

# 输出：
./testbashdefault.sh:行28: OPTIONS_2_3="4": 未找到命令
3
./testbashdefault.sh:行35: OPTIONS_2_3: xxx
```

> 通过Shell写入多行内容到一个文件

[<< EOF](https://links.jianshu.com/go?to=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F2500436%2Fhow-does-cat-eof-work-in-bash)



```shell
 cat > filename<<EOF
 echo $TEST
 ...
 EOF
```

> 为什么我学会shell了，但是还是看不懂别人写的shell

这里要说一下，shell是基于linux的，所以，你学会了shell，但是还要学习linux的相关指令才能配合着更好的使用。

这是我以前写过的一个shell，功能：将一个没有目录层级的文件放置到替换之前有目录层级的文件。

为什么会有会这样，因为我不小心在百度了一个linux指令，以为能解决我的问题，殊不知是去掉我的目录层级，然后我一紧张在我原来的项目`rm -rf *`，所以只能把文件覆盖过去了，毕竟我写了好多代码还没有提交。



```bash
#!/bin/bash
FileListArrays=()
DirListArrays=()


function read_dir()
{
    for file in `ls  $1`
    do
        if [ -d $1"/"$file ]
        then
            if [ -L $1"/"$file"." ]
            then
                SoftLinkList+=$1"/"$file
            elif [ $file == "android" ]
            then
                echo "hahahahahahahha"
            else
                read_dir $1"/"$file
            fi
        else
            FileListArrays+=($file)
            DirListArrays+=($1)
            FileList+=$file" " #空格分割
            FileDirList+=$1" "
        fi
    done
}

MyFileListArrays=()
MyDirListArrays=()
function read_myself()
{
    for file in `ls  $1`
    do
        if [ -d $1"/"$file ]
        then
            if [ -L $1"/"$file"." ]
            then
                SoftLinkList+=$1"/"$file
            else
                read_myself $1"/"$file
            fi
        else
            MyFileListArrays+=($file)
            MyDirListArrays+=($1)
        fi
    done
}


echo $1
echo $2
read_dir $1
read_myself $2

count=0
compare=0 #对比的次数
testMax=3000 #最大对比次数
for file in ${FileListArrays[@]}
do
#    echo $file
    # 如果存在在这里面
    compare=0
    for item in ${MyFileListArrays[@]}
    do
        if [ $item == $file ]
        then
            #echo "this is same "$file":::"$item
            echo cp ${MyDirListArrays[$compare]}/${MyFileListArrays[$compare]}  ${DirListArrays[$count]}/${FileListArrays[$count]}
#            echo ${DirListArrays[$count]}/${FileListArrays[$count]}
            #cp ${MyDirListArrays[$compare]}/${MyFileListArrays[$compare]}  ${DirListArrays[$count]}/${FileListArrays[$count]}
        fi
        compare=`expr $compare + 1`
    done

    count=`expr $count + 1`
    if [ $count -ge $testMax ]
    then
        break
    fi
done
echo $count
```



1人点赞



[日记本](https://www.jianshu.com/nb/6013943)