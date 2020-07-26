# 从零开始使用git进行版本管理

[![img](https://upload.jianshu.io/users/upload_avatars/2907896/20efad908363?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp)](https://www.jianshu.com/u/12ac172cedc5)

[晴空一垩](https://www.jianshu.com/u/12ac172cedc5)关注

0.1792019.08.13 21:24:06字数 908阅读 129

git 是个版本管理的工具，相较于SVN有着更加强大的优势

[] 为可填选项 <> 为必填项

## 拉取资源

如果你要自己测试的话，可以在github上面自己手动点击进行创建一个空的项目进行玩耍。

#### 拉取资源到本地



```php
# 这样就可以拉取一个网上的资源到本地，名称为工程名称或者名称为[dir]的文件夹
git clone http://xxxxx.git [dir]
```

#### 拉取资源到指定非空文件夹

有两种方式可以做到

第一种方式



```csharp
# mkdir proj1
# 进入你的项目 proj1
# cd proj1 
$ git init #初始化仓库
$ git remote add origin https://github.com/telenewbie/Demo4Linux.git # 添加远程仓库
$ git pull origin master # 需要先更新代码
$ git push origin master # 需要指定提交的目标 
```

第二种方式



```bash
# 进入你的项目 proj1
$ git clone --no-checkout https://git.oschina.net/user/proj.git tmp # clone 到一个新的目录下面
$ mv tmp/.git .   #将 tmp 目录下的 .git 目录移到当前目录
$ rmdir tmp   #清除掉之前的临时目录
$ git reset --hard HEAD 
```

到这里你会发现都不需要用户名和密码，用起来非常的简单，因为你就是clone一个资源下来而已

## 提交

#### 初始化

提交代码，你会被需要告知要有密码和账号。所以这里需要你使用如下命令，来设置全局的账号名和密码，方便之后提交【当然你也可以不设置，每次提交的时候都写用户名密码就好】



```ruby
$ git config --global user.name "Your Name Comes Here"
$ git config --global user.email you@yourdomain.example.com
```

#### 查看修改

在你每次提交的时候，都可以看下哪些文件做了修改，来确认自己需要将哪些文件进行提交。



```bash
# 会显示哪些文件需要提交，哪些文件已add到临时存储区了
git status 
```

#### 提交

提交之前需要add 到 称为“index” 的临时存储区

之后再commit 到 称为 “暂存区” 的本地仓库

之后就是push 到 远程仓库了 【依赖于网络】



```bash
# 添加到 index
git add [<filename>|正则表达]

# 提交到本地仓库
git commit [filename]
git commit -m "提交记录" [filename]
# “-a” 表示帮你add了，可以不执行add 也可以commit
git commit -a -m "提交记录" [filename]

# 提交到远程仓库
git push [远程名] [本地分支]:[远程分支]  eg:git push origin tele_3.1.0:3.1.0
git push origin origin/master 
```

#### 比较【x】

在提交之前也许你想知道你相对于远程仓库的改动有哪些



```undefined
git diff origin/master  master 
```

## 分支

这里强制规定：如果你是多人协作的项目，一定要创建分支进行开发的工作。

master 为主干分支

release 为发布版分支

hotfix 为修复bug版本分支

dev 为开发分支【这个应该是我们经常在的分支】

fetures 为开发新需求分支 【这个应该是我们经常在的分支】

###### Q： 分支有什么用?

> 分支就像一个环境一样，分支与分支之间是互不干涉的，可以将一个分支的提交合并到另一个分支上面，所以你在dev上面的提交，可以通过merge合并到master上面。

#### 本地分支的创建与删除



```xml
git branch <分支名称>

# 创建分支并创建
git checkout -b <分支名称> [远程分支]

# 删除
git branch -d <分支名称>
# 强制删除
git branch -D <分支名称>
```

#### 远程分支的创建与删除



```css
git branch <分支名称>

git push origin [本地分支名称]:[需要新建的远程分支名称]

# 删除
git push origin :[需要删除的远程分支名称]
```

#### 分支的查看



```bash
# 查看本地分支
git branch 

# 查看远程分支
git branch -r

# 查看所有分支，不管本地还是远程
git branch -a
```

#### 分支未提交代码的暂存

note ： 也许切换的时候，你在当前的分支还有修改未提交，你可以先提交。

什么？你不想提交，因为你还没做完，你可以使用



```php
# 将修改暂存
git stash
# 查看 暂存的修改
git stash list

# 这个时候你就可以切换到你需要的分支了

# 在你切换之前的分支进行恢复的操作
git stash pop
```

#### 切换



```bash
# 切换到另一个分支
git checkout <分支名称>
```

#### 全部的信息



```dart
$ git remote show origin 
* 远程 origin
  获取地址：https://github.com/telenewbie/read_me_first.git
  推送地址：https://github.com/telenewbie/read_me_first.git
  HEAD 分支：master
  远程分支：
    branch_another 已跟踪
    master         已跟踪
    mine           已跟踪
    my-dev         已跟踪
  为 'git pull' 配置的本地分支：
    master 与远程 master 合并
  为 'git push' 配置的本地引用：
    master 推送至 master (可快进)
    mine   推送至 mine   (最新)
    my-dev 推送至 my-dev (可快进)
```

## 日志

每次提交都会产生一个commit_id 的hash值

#### 查看



```bash
# 查看所有的本地仓库的提交日志
git log 

# 查看某个区间的提交日志
git log HEAD^1..HEAD

# 查看近几次的提交
git log -1

# 查看详细信息
git show commit_id
git show commit_id:文件名称
```

#### 特殊



```bash
# 能够查看所有的commit 包括回滚的提交，git log看不到回滚的提交
git reflog
```

顺便说下：

`git show -s` 和 `git log -1` 一致哦

## 回滚

#### 丢弃修改，恢复提交的样子



```jsx
git checkout -- <文件>...
```

#### 取消add



```css
git reset HEAD [文件名称]
```

#### 取消commit



```undefined
git reset commit_id
```

#### 取消push 【x】



```bash
# 恢复到 commit_id 的那次提交
git reset commit_id 

# 重新push 到服务器
git push origin HEAD --force
```

## 更新

#### 更新仓库



```undefined
git fetch 
git pull
```

两者的不同之处在于：`git fetch` 不会执行合并的操作，`git pull = git fetch + git merge`

## 合并

#### 合并分支代码

合并在多人协作的项目里面经常发生，

> note : `git rebase <另一个分支>` 表示把另一个分支的提交按照当前分支的提交方式进行提交，他和 `git merge <另一个分支>` 的 区别是，后者会显示在自己的分支上进行提交而非master



```xml
git merge <另一个分支名称>
```

#### 合并另一个分支的一个特定的commit到本分支



```undefined
git cherry-pick commit_id
```

##### 实例



```csharp
$ git merge mine 
自动合并 README.md
冲突（内容）：合并冲突于 README.md
自动合并失败，修正冲突然后提交修正的结果。

$ git diff README.md
diff --cc README.md
index e1d0a3b,0fce3e5..0000000
--- a/README.md
+++ b/README.md
@@@ -3,6 -3,4 +3,10 @@@ just do test  for  newbie with githu
++<<<<<<< HEAD
 +hell
 +
 +from my-dev
++=======
+ add by mine
++>>>>>>> mine
```

其中 `=======` 之上表示自己的修改 ，之下表示另一个分支的修改，所以自己 vim 进入进行修改即可