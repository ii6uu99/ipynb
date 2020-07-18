fatal:'origin' does not appear to be a git repository fatal:Could not read from remote repository

huanhuaqian 2018-08-23 22:35:28  34019  收藏 18
分类专栏： ubuntu
版权
今天gitlab中遇到的问题：

当 git push origin branch_name时遇到报错如下：

fatal:'origin' does not appear to be a git repository

fatal:Could not read from remote repository

原因：

本地分支和远程分支断开连接

解决方法：

cd 本地分支里
1、git branch 
               ——*master   只显示master

然后查看是否从上游拉了
2、git remote –v
             ——若什么都没有，则和上游已断联系，拉不了代码也推不了代码 


加关联
3、git remote add origin ssh://git@gitlab*********************************.git(地址)


然后
4、git fetch origin

              ——会显示下拉的branch情况
    
                    格式为From ssh://gitlab.********************************
    
                  *  [new branch]         XXXXX        ->origin/XXXXX

再次检查远程仓库，显示对应的clone地址
git remote –v
——origin  git://github.com/schacon/ticgit.git (fetch)
origin  git://github.com/schacon/ticgit.git (push)

然后再查分支
git branch –a

            ——* mater
    
                   remotes/origin/XXXXXX         **********

具体的切换分支可参考https://blog.csdn.net/tanningzhong/article/details/79724488

git 重命名仓库、修改远程仓库地址、修改仓库配置可参考：https://blog.csdn.net/u011884440/article/details/71246572
————————————————
版权声明：本文为CSDN博主「huanhuaqian」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/huanhuaqian/article/details/81986064