#!/bin/bash
set -e

# ワークスペースのパーミッションを確認・修正
sudo chown -R jupyter:jupyter /workspace
sudo chmod -R 777 /workspace

# コマンドの実行
exec "$@"