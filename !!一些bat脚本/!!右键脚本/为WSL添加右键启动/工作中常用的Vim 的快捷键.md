# 工作中常用的Vim 的快捷键

[![img](https://upload.jianshu.io/users/upload_avatars/2907896/20efad908363?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp)](https://www.jianshu.com/u/12ac172cedc5)

[晴空一垩](https://www.jianshu.com/u/12ac172cedc5)关注

0.3372019.08.01 23:04:27字数 436阅读 23

在手机上发布的。可能排版有点差。但是没有办法了。



跳转

gg 跳转到文件头

shift + g 跳转到文件尾

xxxgg 跳转到具体行 eg:123gg 跳转到123行

模式切换

v 进入可视模式

ctrl + v 进入块选择，之后可以同时插入相同的自符。 方法：Ctrl + v ；选择自己需要的行； I （插入模式）;输入；esc；就可以了

插入模式

i

a: 在光标后插入

o:在当前后插入一个新行

O: 在当前行前插入一行新行

esc 进入正常模式

： 进入命令模式

正常模式下

删除

dd 删除当前行

dxx 删除 几行 从0 开始 eg：d1 表示删除2行

d$ 删除光标到行尾。

d^ 删除光标到行首

复制

yy 复制当前行

yxx 复制几行从0开始 eg: y1 表示复制2行

0y$,移动到行首，进行复制，拷贝本行到最后一个字符

撤销

u

重复上次的指令

ctrl + r

替换

r 更换当前字符

:{作用范围}s/{目标}/{替换}/{替换标志} eg:%s/foo/bar/g会在全局范围(%)查找foo并替换为bar，所有出现都会被替换（g）。

参考字符串替换

可组合项

0:数字0，当行头

^: 到本行第一个不是blank字符的位置(blank:空格，换行)

$:到行尾

/string: 搜索string字符串(搜索有多行，n会到下一个，N回到上一个)

W/B w/b 往后跳或往前跳一个单词。

常见Linux命令

其他

set nu 显示行号