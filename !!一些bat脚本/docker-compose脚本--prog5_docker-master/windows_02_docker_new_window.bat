@REM file: windows_02_docker_new_window.bat
@REM brief: プログラミング演習５の開発用コンテナ（クライアント兼APサーバ）に接続する。
@REM author: Takahiro55555(Github)

@echo off

REM 文字コードをUTF-8に設定。
chcp 65001

echo.
echo ====================================================================
echo "この端末は作業用の端末です。"
echo "演習室と同じコマンドが使用できます。"
echo "終了する際は`exit`と入力してください。"
echo ====================================================================
echo.

docker exec -it prog5-ubuntu /bin/bash