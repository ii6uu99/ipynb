# termux+uiautomator2实现手机自动化测试

- [python](https://www.it610.com/search/python/1.htm)

## 手机自动化测试

针对某应用的代码测试，termux+uiautomator2环境，代码编写-python3

### **一. 环境配置**

**1. 手机安装termux软件**(下载termux,提取码：30f6)
安装且初始化完成：
[![termux+uiautomator2实现手机自动化测试_第1张图片](https://img.it610.com/image/info8/293bb585020049e1b070082b5717eec9.jpg)](https://img.it610.com/image/info8/293bb585020049e1b070082b5717eec9.jpg)
**2. termux更换软件源：**

```bash
cd /data/data/com.termux/files/usr/etc/apt#进入目录
#编辑软件源文件
mv sources.list sources.list.bak #备份
vi sources.list
```

更换为清华源

```bash
# The termux repository mirror from TUNA:
deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main
```

**3. 软件安装和配置(需要耐心)**

```bash
#首先是常规升级
apt update
apt upgrade

#获取手机读写权限
termux-setup-storage

#然后是安装需要的软件
apt install openssh
apt install python
apt install git
pkg install termux-auth
pkg install termux-tools
pkg install clang
pkg install libxml2 libxslt libiconv
```

**4. 导入uiautomator2的model文件**
model下载 提取码：8dcz
将文件移动至手机文件的根目录
[![termux+uiautomator2实现手机自动化测试_第2张图片](https://img.it610.com/image/info8/0ca09457e01c4489af2f108953dcaf3b.jpg)](https://img.it610.com/image/info8/0ca09457e01c4489af2f108953dcaf3b.jpg)

```bash
#复制到python3.8model目录下
cp /data/data/com.termux/files/home/storage/shared/uiautomator2.zip\
 /data/data/com.termux/files/usr/lib/python3.8/site-packages/
cd /data/data/com.termux/files/usr/lib/python3.8/site-packages/
unzip uiauyomator2.zip       #解压
```

**5. pip安装python依赖库**

```bash
pip install --default-timeout=1000 humanize
pip install --default-timeout=1000 retry
pip install --default-timeout=1000 requests
pip install --default-timeout=1000 progress
pip install --default-timeout=1000 humanize
pip install --default-timeout=1000 adbutils
pip install --default-timeout=1000 six
pip install --default-timeout=1000 logzero
pip install --default-timeout=1000 Cython
pip install --default-timeout=1000 lxml
```

或者

```bash
pip install --default-timeout=1000 humanize retry requests progress\
 humanize adbutils six logzero Cython lxml
```

**6.在手机termux中安装adb**
adb_arm获取,移入手机根目录

```bash
mv /data/data/com.termux/files/home/storage/shared/adb \
$PREFIX/bin
chmod +x $PREFIX/bin
```

基础配置完成

### **二. 电脑端uiautomator2安装及终端设备初始化**

**1、安装uiautomator2，执行命令**
python2版本

```bash
pip install --pre -U uiautomator2
```

python3版本

```bash
pip3 install --pre -U uiautomator2
```

**2、设备安装atx-agent和atx-apk**
首先Android设备连接到PC，打开usb调试，usb安装，usb调试，记得完成后及时关闭权限

[![termux+uiautomator2实现手机自动化测试_第3张图片](https://img.it610.com/image/info8/66a5299d0e564a538e0509b25d5e845a.jpg)](https://img.it610.com/image/info8/66a5299d0e564a538e0509b25d5e845a.jpg)

在电脑端安装python，安装adb

```bash
adb devices#查看设备是否连接
python -m uiautomator2 init  #python初始化设备
```

最后提示success，代表atx-agent初始化成功。

### **三. termux端检测：**

依次输入

```bash
python3 #进入python3命令行
import uiautomator2 as ui2
d = ui2.connect('0.0.0.0')
```

[![termux+uiautomator2实现手机自动化测试_第4张图片](https://img.it610.com/image/info8/30f7c3e5878c4b9bae24e8fad41a5426.jpg)](https://img.it610.com/image/info8/30f7c3e5878c4b9bae24e8fad41a5426.jpg)

结束
[![termux+uiautomator2实现手机自动化测试_第5张图片](https://img.it610.com/image/info8/7598a71f6a704eee97c092ecb95fb495.jpg)](https://img.it610.com/image/info8/7598a71f6a704eee97c092ecb95fb495.jpg)
关于某个应用的测试：（服务器太卡~~）
[![termux+uiautomator2实现手机自动化测试_第6张图片](https://img.it610.com/image/info8/493feeef9ce64dffa01f20009dc048af.jpg)](https://img.it610.com/image/info8/493feeef9ce64dffa01f20009dc048af.jpg)
相关代码 `https://gitee.com/weilizhang/autock`