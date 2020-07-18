echo 查看本地分支，只显示master
git branch

echo 从上游啦，报错error: Unknown subcommand: –v
git remote –v

echo 加关联
git remote add origin git@github.com:ii6uu99/ruanjian.git

echo 检查分支
git fetch origin

echo 再次检查远程仓库，显示对应的clone地址
git remote –v

echo 再查分支
git branch –a