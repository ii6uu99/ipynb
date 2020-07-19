# termux安装mariadb_记录自己走过的坑



```
pkg i mariadb
mysql_install_db
```

> 报错：019-09-20 10:22:13 0 [ERROR] InnoDB: Corrupted page [page id: space=0, page number=0] of datafile './ibdata1' could not be found in the doublewrite buffer.
> 2019-09-20 10:22:13 0 [ERROR] InnoDB: Plugin initialization aborted with error Data structure corruption
> 2019-09-20 10:22:13 0 [ERROR] Plugin 'InnoDB' init function returned error.
> 2019-09-20 10:22:13 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
> 2019-09-20 10:22:13 0 [ERROR] Unknown/unsupported storage engine: InnoDB
> 2019-09-20 10:22:13 0 [ERROR] Aborting

查找原因：/data/data/com.termux/files/usr/var/lib/mysql/下面的
ib_logfile1
ibdata1
ib_logfile101
损坏

```
cd  /data/data/com.termux/files/usr/var/lib/mysql
rm ib*
mysql_install_db
mysqld
```

启动成功！
登陆的时候不要使用用户名和密码 直接mysql登陆

```
mysql
```

> $ mysql
> Welcome to the MariaDB monitor. Commands end with ; or \g.
> Your MariaDB connection id is 8
> Server version: 10.4.6-MariaDB MariaDB Server
> Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
> Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
> MariaDB [(none)]>

- 关于中文乱码的问题

  [![termux安装mariadb_记录自己走过的坑_第1张图片](https://img.it610.com/image/info10/9a62d5bc864d4d4db4531949b704d32f.png)](https://img.it610.com/image/info10/9a62d5bc864d4d4db4531949b704d32f.png)

  中文乱码

  修改mysql配置文件

```
vim $PREFIX/etc/my.cnf
```

[![termux安装mariadb_记录自己走过的坑_第2张图片](https://img.it610.com/image/info10/6e80e5e6afd943e086955ef510cae411.png)](https://img.it610.com/image/info10/6e80e5e6afd943e086955ef510cae411.png)

配置文件

```
# use it for options that affect everything
[client]
default_character_set = utf8
[client-server]
#[mysqld]
#innodb_force_recovery = 6
#innodb_purge_threads = 1
#innodb_use_sys_malloc = 1
#feedback = ON
# include all files from the config directory
!includedir /data/data/com.termux/files/usr/etc/my.cnf.d
[mysqld]
default_storage_engine = INNODB
character_set_server = utf8
collation_server=utf8_general_ci
```

- 设置完后，重启mysql 创建的数据库与表都用utf8

  [![termux安装mariadb_记录自己走过的坑_第3张图片](https://img.it610.com/image/info10/203e9261a69c465493bd1592a41a0685.png)](https://img.it610.com/image/info10/203e9261a69c465493bd1592a41a0685.png)

  设置后

- 查询语句带中文也可以正常显示了

  [![termux安装mariadb_记录自己走过的坑_第4张图片](https://img.it610.com/image/info10/05baec722bcf4a04be5067216c46b796.png)](https://img.it610.com/image/info10/05baec722bcf4a04be5067216c46b796.png)

  查询语句带中文