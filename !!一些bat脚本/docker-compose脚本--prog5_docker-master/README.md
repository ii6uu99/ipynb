# prog5_docker

## About
プログラミング演習５の開発環境です。個人PCで利用する前提で作成しました。\
演習室と同じDBの設定のままでDBに接続、使用することができます。

なお、実際に使用するには[Docker](https://www.docker.com/products/docker-desktop)が必要です。\
Windowsの場合、OSのエディションによってインストールの方法が異なるみたいです。\
[Windows10 Home](https://qiita.com/idani/items/fb7681d79eeb48c05144)の場合\
[Windows10 Pro](https://qiita.com/ksh-fthr/items/6b1242c010fac7395a45)の場合\
なお、参考サイトは適当なので分からない箇所があったら適宜ググってください。

### 使い方
[Windows (Pro) 版](https://github.com/Takahiro55555/prog5_docker/wiki/windows_usage)\
Mac OS (Coming soon...)

※）アニメーションGIFを複数利用しているため、モバイル回線から閲覧する場合はお気を付けください。（約37MB）

### DBサーバ
- DB: PostgreSQL 9.2
- ホスト名: 演習室と同じ
- データベース名: 演習室と同じ
- ユーザ名: 演習室と同じ
- パスワード： 演習室と同じ

### APサーバ・クライアント
- OS: Ubuntu16.04
- ユーザ名: penshu

### ファイル構成
```
prog5_docker/
├── .docker #基本的に触ったらダメ
│   ├── docker-compose.yml
│   ├── postgres
│   │   └── Dockerfile
│   └── ubuntu
│       └── Dockerfile
├── README.md
├── mac_01_docker_start.sh            # Macで仮想マシン（コンテナ）を起動する
├── mac_02_docker_new_window.sh       # Macで仮想マシンにログインする（bash）
├── mac_03_docker_stop.sh             # Macで仮想マシンを停止する
├── windows_01_docker_start.bat       # Windowsで仮想マシンを起動する
├── windows_02_docker_new_window.bat  # Windowsで仮想マシンにログインする（bash）
└── windows_03_docker_stop.bat        # Windowsで仮想マシンを停止する
```

### Images
- [DockerHub(prog5-ubuntu)](https://hub.docker.com/r/takahiro55555/prog5-ubuntu)
- [DockerHub(prog5-postgres)](https://hub.docker.com/r/takahiro55555/prog5-postgres)
