git config --global user.name "ii6uu99"
git config --global user.email "ii6uu99@163.com"

rem 创建ssh钥匙
ssh-keygen -t rsa -C "ii6uu99@163.com"

rem 用笔记本打开钥匙并复制
start notepad C:\Users\Administrator\.ssh\id_rsa.pub

rem 粘贴在ssh的新钥匙那
start chrome https://github.com/settings/ssh/new

rem 链接github
ssh -T git@github.com