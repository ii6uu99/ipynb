@REM file: windows_03_docker_stop.bat
@REM brief: プログラミング演習５の開発用コンテナ（クライアント兼APサーバ、DBサーバ）を終了する。
@REM author: Takahiro55555(Github)

@echo off

REM 文字コードをUTF-8に設定。
chcp 65001

cd .\.docker\
docker-compose down
