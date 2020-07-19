# 安卓手机安卓Mysql，Termux安装MariaDB/MySQL数据库

- [Termux](https://www.it610.com/search/Termux/1.htm)

MySQL数据库衍生版，也被视为开源数据库MySQL的替代品。 MariaDB虽然被视为MySQL数据库的替代品，但它在扩展功能、存储引擎以及一些新的功能改进方面都强过MySQL。而且从MySQL迁移到MariaDB也是非常简单的。

虽然他们确实存在很多差异，但是在这里，我们将使用 MariaDB 和 MySQL 作为同义词。也就是说，如果您看到我说 MariaDB 不用感到困惑，那就是 MySQL。反之亦然。

### 如何在Termux中安装

安装好 Termux 后更新终端软件包

```powershell
apt update
apt upgrade
```

在这两种情况下，如果应用程序都询问，请选择“是”，即输入字母y。此步骤非常重要，因为它将更新在我们的移动设备上安装 MySQL 所需的库。

### 安装 MariaDB

好的，一旦您更新了系统，我们将安装 MariaDB 软件包。为此，执行：

```powershell
pkg install mariadb
```

这里有一点需要注意：如果安装失败可能是因为没有名为 my.cnf.d 的目录。然后，必须创建该目录，导航到如下的位置查看该目录是否存在：

```powershell
cd /data/data/com.termux/files/usr/etc
```

使用命令 ls 查看 etc 目录下的内容，如果目录下没有出现名为 my.cnf.d 的文件夹，则使用如下命令创建一个：

```powershell
mkdir my.cnf.d
```

如果 my.cnf.d 目录已存在，则不执行任何操作，然后返回主页：

```powershell
cd $home
```

### 配置 MariaDB

一旦创建目录（如果目录不存在），我们将执行以下命令：

```powershell
mysql_install_db
```

mysql_install_db 初始化 MariaDB 数据目录，并在数据库中创建 系统表mysql（如果不存在）。MariaDB使用这些表来管理特权，角色和插件。

### 启动 MariaDB 服务器

之后，我们要做的就是启动 MySQL 守护进程（如果我们重启手机或Termux，也应该这样做）。

```powershell
mysqld
```

或

```powershell
mysqld_safe -u root &
```

mysqld_safe 与 root 用户一起运行的；“＆”号将在后台运行。
启动完成后,这个会话就一直存活,类似与debug调试一样,只有新建会话才可以操作.
[![安卓手机安卓Mysql，Termux安装MariaDB/MySQL数据库_第1张图片](https://img.it610.com/image/info8/8c34b5611f8446abbf6f0200ce966111.jpg)](https://img.it610.com/image/info8/8c34b5611f8446abbf6f0200ce966111.jpg)
关于隐藏会话可以使用nohup命令和tmux命令,这里我建议使用tmux命令
当然你也可以在termux界面上从左往右滑动，新建终端窗口执行mysql

mysql与mysqld的区别：mysqld 是服务端程序（即MySQL的服务器）要想使用客户端程序，该程序必须运行，因为客户端通过连接服务器来访问数据库；mysql 是命令行客户端程序。

mysqld_safe 与 mysqld 区别：直接运行 mysqld 程序来启动 MySQL 服务的方法很少见。mysqld_safe 脚本会在启动 MySQL 服务器后继续监控其运行情况，并在其死机时重新启动它。mysql.server 脚本其实也是调用 mysqld_safe 脚本去启动 MySQL 服务器的。

mysqld_safe 相当于多了一个守护进程，当 mysqld 挂了会自动把 mysqld 进程拉起来。

### 访问数据库

要访问 MariaDB 数据库服务器，请输入：

```powershell
mysql -u root -p
```

但是 MariaDB 数据库服务器，默认情况下，是没有密码的，只需要输入以下命令即可登录：

```powershell
mysql
```

默认登录后即可为 root 帐号设置一个密码。

### 配置 MariaDB 远程登录

有时候，为了开发或操作方便，可以使用电脑远程访问和管理手机里的数据库。默认情况下，为了安全 MariaDB 只允许本地登录，如果要开启远程连接可进行以下配置。

创建一个可远程登录的用户：

```powershell
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
```

% 通配符表示创建外网可访问的用户。

用户授权：

```powershell
GRANT ALL privileges ON databasename.tablename TO 'username'@'%';
```

如果要授予该用户对所有数据库和表的相应操作权限则可用 * 表示，如 *.*

刷新授权：

```powershell
flush privileges;
```

通过以上配置即可通过局域网内其它设备登录手机里的数据库进行操作。

注：由于 my.cnf.d 目录下并未找到 mysqld.cnf 配置文件，所以并未修改注释 bind-address 这个选项也可进行远程登录。

### 停止 MariaDB 服务器

要停止 MariaDB 服务器，请输入：

```powershell
pkill mysql
```

或者，使用单词“MySQL”取其进程 ID ，使用命令 grep，然后杀死他们kill -9 [ID]，-9 是发送终止信号。

### 要查找执行的进程ID：

```powershell
ps aux | grep mysql
```

拥有ID后，请杀死它们：

```powershell
kill -9 15423
```

可选，但建议：安全的 MariaDB
MariaDB 的安装已经可以正常工作，并且如果我们只打算使用它，那么我们就不必在意安全性。但是，相反，如果您想通过良好的习惯来确保它，可以这样做。为此，执行：

```powershell
mysql_secure_installation
```

这将为您提供一个向导，该向导将帮助您确保安装MySQL：输入密码，删除测试特权等。