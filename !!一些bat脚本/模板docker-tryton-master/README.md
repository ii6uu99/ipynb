# 码头工人

Tryton与Jenkins和Docker



https://github.com/conology/docker-tryton





# 安装本地开发环境（Win）

1. 在Windows下打开cmd
2. 摘录'install_dev_env.cmd'
3. 脚本完成后大约20秒钟执行'docker container logs jenkins-blueocean'
4. 复制令牌
5. 打开'localhost：1000'并插入令牌
6. 安装标准插件
7. 通过对话框添加管理员帐户
8. jenkins的网址是' [http：// localhost：1000 /](http://localhost:1000/) '
9. 点击“开始使用詹金斯”

# 为docker-tryton项目创建管道

1. 点击左侧栏上的“打开蓝海”
2. “创建新管道”
3. “ Github”
4. “在这里创建访问令牌。”
5. 登录到github，给令牌命名，点击回车，复制令牌
6. 将令牌插入詹金斯，然后点击“连接”
7. 选择“生态学”
8. 选择“ docker-tryton”
9. 点击“创建管道”
10. tryton网址为“ [http：// localhost：8000 /](http://localhost:8000/) ”

# 有用的链接

https://hub.docker.com/r/tryton/tryton环境设置