@REM file: windows_01_docker_start.bat
@REM brief: プログラミング演習５の開発用コンテナ（クライアント兼APサーバ、DBサーバ）を起動する。
@REM author: Takahiro55555(Github)

@echo off

REM 文字コードをUTF-8に設定。
chcp 65001


echo.
echo ====================================================================
echo "この端末はサーバ（コンテナ）のログ出力用です。"
echo "作業をしたい場合は以下のファイルを実行してください。"
echo "windows_02docker_new_window.bat"
echo "全体の作業が終了した場合は以下のファイルを実行してください。"
echo "windows_03docker_stop.bat"
echo ====================================================================
echo.

cd .\.docker\
docker-compose up --build