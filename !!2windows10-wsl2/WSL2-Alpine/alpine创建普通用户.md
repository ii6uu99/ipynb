# Alpine里的用户管理命令

![img](https://csdnimg.cn/release/phoenix/template/new_img/reprint.png)

[weixin_30901729](https://me.csdn.net/weixin_30901729) 2018-09-07 15:27:00 ![img](https://csdnimg.cn/release/phoenix/template/new_img/articleReadEyes.png) 1642 ![img](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollect.png) 收藏

版权

注意噢，和普通的linux不一样的。

1, 建立一个指定GID的组：

```
addgroup -g 10001 -S groupA
```

2, 建立一个指定UID的用户，指定shell, 让它属于指定的用户组。

```
adduser ming -u 20001 -D -S -s /bin/bash -G groupA
```

3, 让用户可以使用su -到root用户下，

```
chmod 4755 /bin/busybox
```

4，root更改密码。（这条和上条，可以在dockerfile里提前实现）

```
echo -e "mingming\nmingming" | passwd root
```

转到普通用户  su ming



5，dockerfile里，可以同时改变用户同时COPY文件到镜像里。（为什么一定要同时作？？如果不同时作，docker的layer增加一层，改权限和属主，镜像大小会翻倍。）

   你试过仅仅修改一个JDK的权限和属主，镜像增加近180M的事儿么？但这个高版本的DOCKER才支持这样的语法。（BUILDA希望能普及~~人家只作镜像）

```
COPY --chown=userA:groupA bs.sh ${BS_DIR}
```

 

转载于:https://www.cnblogs.com/aguncn/p/9604936.html