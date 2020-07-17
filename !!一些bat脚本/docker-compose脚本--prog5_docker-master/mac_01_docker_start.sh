#!/bin/bash
# @file: mac_01_docker_start.sh
# @brief: プログラミング演習５の開発用コンテナ（クライアント兼APサーバ、DBサーバ）を起動する。
# @author: Takahiro55555(Github)

echo ""
echo "===================================================================="
echo "この端末はサーバ（コンテナ）のログ出力用です。"
echo "作業をしたい場合は以下のファイルを実行してください。"
echo "mac_02_docker_new_window.sh"
echo "全体の作業が終了した場合は以下のファイルを実行してください。"
echo "mac_03_docker_stop.sh"
echo "===================================================================="
echo ""

cd ./.docker/
docker-compose up --build
