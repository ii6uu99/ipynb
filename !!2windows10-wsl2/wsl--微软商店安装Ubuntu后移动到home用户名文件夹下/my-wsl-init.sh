#!/bin/bash

# dir this script is in
file_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

sudo update-alternatives --set editor /usr/bin/vim.basic

# no password for sudo
sudo_config_str="${USER} ALL=(ALL) NOPASSWD: ALL"
if ! sudo grep -qxF "${sudo_config_str}" /etc/sudoers; then
  sudo cp /etc/sudoers /etc/sudoers.backup
  echo "sudoer file is backed up at: /etc/sudoers.backup"
  echo ${sudo_config_str} | sudo tee --append /etc/sudoers
fi

sudo chmod 777 /etc/apt/sources.list


cat <<EOF | sudo tee /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

EOF

sudo apt-get update -y && apt-get upgrade -y

# ##########安装Anaconda所需的软件包 #############################
#pip-python3是安装pip3的一种方法
sudo apt-get install -y wget curl bzip2 libpython3-dev libboost-python-dev bash pip-python3

cd ~
#下载anaconda安装 
sudo curl -O https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh


# 打开可执行文件属性 
sudo chmod +x Anaconda3-5.3.1-Linux-x86_64.sh 

# 安装Anaconda，不要使用sudo，安装在普通用户
bash Anaconda3-5.3.1-Linux-x86_64.sh -b

# 删除
sudo rm Anaconda3-5.3.1-Linux-x86_64.sh

# 将Anaconda添加到路径 
# echo 'export PATH ="~/anaconda3/bin:$PATH"' >> ~/.bashrc

####################安装anaconda完成##############################
#########################安装python库#########################

#安装pip第二种方法
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py  

#修改pip的默认源
sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
sudo pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
sudo pip3 config set install.trusted-host mirrors.aliyun.com


# pip3安装一下python库
sudo pip3 install wheel
sudo pip3 install flake8
sudo pip3 install helping

#移动.bashrc文件
cp ${file_dir}/.bashrc ~/.bashrc
source ~/.bashrc

# 修改conda更新源
#  sudo su 取得root权限
echo 'export PATH ="~/anaconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes

#解决挂载权限问题
#增加wsl权限
#https://www.jianshu.com/p/4443a24139d0

cat >>~/.bashrc <<EOF
if [[ "$(umask)"=='000' ]]; then
    umask 022
fi
EOF

cat <<EOF | sudo tee /etc/wsl.conf
[automount]
enabled = true
root = /mnt/
options = "metadata,dmask=022,fmask=133"
mountFsTab = false
EOF


# Win10子系统WSL 使用 docker
# https://blog.csdn.net/qq_42751918/article/details/88544895

#WSL安装tmux  bashrc  vimrc Docker的脚本
bash docker.sh


#安装桌面vnc等，功能强大
#https://gitee.com/mo2/linux
sudo apt install -y curl
bash -c "$(curl -L gitee.com/mo2/linux/raw/2/2)"


