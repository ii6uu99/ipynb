#!/bin/bash

 apk add -y tmux vim 
#WSL安装tmux  bashrc  vimrc Docker的脚本
echo -e "Setting up WSL dotfiles"

echo -e "Setting up Docker."
 apk update -y
# 安装Docker的软件包依赖关系。 
 apk add -y \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common

# 下载并添加Docker的官方PGP公钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  apt-key add -
# 验证指纹
 apt-key fingerprint 0EBFCD88
# stable是稳定版
 add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
# 更新apt软件包列表（用于新的apt仓库）
 apk update -y
# 安装最新Docker CE.
 apk add -y docker-ce
# 允许您的用户无需root访问权限即可访问Docker CLI
 usermod -aG docker $USER
# 将Docker Compose安装到用户的主目录中
 apt install docker-compose
#添加host，连接到桌面docker
echo "export DOCKER_HOST=tcp://localhost:2375" >> ~/.bashrc
source ~/.bashrc

 cat > /etc/wsl.conf <<EOF
[automount]
root = /
options = "metadata"
EOF
echo " mount --bind /mnt/c /c" >> ~/.bashrc
source ~/.bashrc
echo -e "Created wsl.conf."
echo -e "FINISHED"
echo -e "Don't forget to run:  vi"
echo -e "Add this line: dan ALL=(root) NOPASSWD: /bin/mount"
docker info
docker-compose --version
echo -e "FINISHED"
