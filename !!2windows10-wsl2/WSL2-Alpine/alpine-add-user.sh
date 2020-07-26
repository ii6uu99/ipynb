#建立一个指定GID的组：
addgroup -g 10001 -S groupA

#建立一个指定UID的用户，指定shell, 让它属于指定的用户组。
adduser ming -u 20001 -D -S -s /bin/bash -G groupA

#让用户可以使用su -到root用户下
chmod 4755 /bin/busybox

#root更改密码。（这条和上条，可以在dockerfile里提前实现）
echo -e "mingming\nmingming" | passwd root

#转到普通用户  
su ming

# 安装sudo软件包
apk add sudo

######后面用sudo执行程序
