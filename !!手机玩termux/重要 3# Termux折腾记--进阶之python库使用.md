# Termux折腾记--进阶之python库使用



欢迎访问个人博客：blog.spursgo.com

[![Termux折腾记--进阶之python库使用_第1张图片](https://img.it610.com/image/info10/d238274f776d4617b6af36a7c61ffdf6.jpg)](https://img.it610.com/image/info10/d238274f776d4617b6af36a7c61ffdf6.jpg)

sshd



# Termux超级终端折腾记

Termux超级终端的牛x之处我就不在这里描述了。
这次讲的是如何在android手机上安装python的各种科学库和图形库。
Jupyter是这次介绍的重点对象，先卖个关子，不忙介绍它。

## 1. Termux超级终端下载

Termux的下载链接极其介绍见我的其他博文

## 2. 安装python

这一步只是作为一个提示，因为现在你不管是装Linux终端还是linux完整发行版，python几乎是成了标配。所以，不需要我们手动安装。
你可以在命令行下输入python测试一下：

```
python
```

如果你显示的是如下效果，那么恭喜你，python已经作为默认软件



[![Termux折腾记--进阶之python库使用_第2张图片](https://img.it610.com/image/info10/41dc1b5580cd4fdf9e50c1a38a127447.jpg)](https://img.it610.com/image/info10/41dc1b5580cd4fdf9e50c1a38a127447.jpg)

python

## 3. 安装python包管理器pip

两种方法：

### 3.1 直接简单命令安装

```
apt install python-pip
```

可能会提示你找不到python
执行更新命令：

```
apt update
```

如果仍旧无法找到，那么尝试下面的方法

### 3.2 下载源码编译安装

#### 3.2.1 下载脚本

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

#### 3.2.2 执行脚本

```
python get-pip.py
```

自动化安装脚本会帮你把pip安装好
如果你还是失败了，那么你可以联系我，我帮你解决。

## 4. 安装依赖包

```
apt install python-dev clang fftw
```

## 5. 使用pip安装numpy

对python科学计算熟悉的同学一定知道numpy的强大

```
LDFLAGS=" -lm -lcompiler_rt" pip install numpy
```

## 6. 安装matplotlib的相关依赖

```
apt install freetype freetype-dev libpng libpng-dev pkg-config libpng
```

## 7. 图形大神matplotlib安装

```
LDFLAGS=" -lm -lcompiler_rt" pip install matplotlib
```

这里我就不吹捧matplotlib了，要知道python靠它和其他的一些图形库来抗衡matlab

还提供一下pandas的安装方法，我没用过这个库，网上有人说装不上，反正我是成功了。

```
LDFLAGS=" -lm -lcompiler_rt" pip install pandas
```

> 其实到这里就可以结束介绍了，因为python中一些重要的库我们已经安装了，也能正常运行。
> 但是，不要忘了，我们会用到amtplotlib来画图，在termux终端里面虽然可以运行相关代码，但是最后要画图的时候，会出现报错信息。

**咦，怎么办呢？**
别忘了，我们前面提到了一个叫做jupyter的神器。

## 8. 在python下运行使用图形库

### 8.1 jupyter安装

```
LDFLAGS=" -lm -lcompiler_rt" pip install jupyter
```

### 8.2 运行 jupyter

```
jupyter notebook
```

注意前方高冷，见证奇迹的时刻要到来了。
`jupyter notebook`运行之后，命令行下会出现这样的提示：

[![Termux折腾记--进阶之python库使用_第3张图片](https://img.it610.com/image/info10/9f2198806dce4893a5370ef97ad206fd.jpg)](https://img.it610.com/image/info10/9f2198806dce4893a5370ef97ad206fd.jpg)

jypyther


最下面一行是关键所在： http://localhost:8888/?token=longstringofcharacters 类似这样的，你们的肯定和我的不一样。



### 8.3 打开浏览器

把刚刚那个链接复制到浏览器里面
你会看到这样的效果：



[![Termux折腾记--进阶之python库使用_第4张图片](https://img.it610.com/image/info10/b30dc7d857684006a2382d410ba0f787.jpg)](https://img.it610.com/image/info10/b30dc7d857684006a2382d410ba0f787.jpg)

new

### 8.4 新建一个python文件

点击右上方的new，新建一个文件，点击python3，他会自己重新打开一个窗口：



[![Termux折腾记--进阶之python库使用_第5张图片](https://img.it610.com/image/info10/840efd55799d4fc6a0fe9b333bd2192f.jpg)](https://img.it610.com/image/info10/840efd55799d4fc6a0fe9b333bd2192f.jpg)

python3

### 8.5 敲代码

把我给的示例代码复制进去
示例代码：

```
%matplotlib inline
==========================
Dark background style sheet
===========================

This example demonstrates the "dark_background" style, which uses white for
elements that are typically black (text, borders, etc). Note that not all plot
elements default to colors defined by an rc parameter.

"""
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')

fig, ax = plt.subplots()

L = 6
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)
for s in shift:
    ax.plot(x, np.sin(x + s), 'o-')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("'dark_background' style sheet")

plt.show()
```

### 8.6 点击run

然后就可以看到效果了：



[![Termux折腾记--进阶之python库使用_第6张图片](https://img.it610.com/image/info10/9e5637cadba745678bd485fd677d4f00.jpg)](https://img.it610.com/image/info10/9e5637cadba745678bd485fd677d4f00.jpg)

ok



是不是被震撼了。
反正我当时无比激动。
代码中不同于我们平时写的代码的地方：多了一句 %matplotlib inline ，用来指示是子啊jupytrt下运行。

注：该博文重点感谢 leouieda 的文章 Running Jupyter and the Scipy stack on Android
有问题加qq：894237294