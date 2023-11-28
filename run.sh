#!/bin/bash

# 引数が与えられなかった場合のエラーチェック
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# 引数で指定されたディレクトリに移動する
directory=$1
cd "$directory" || exit 1

# ディレクトリ内のすべての Python ファイルを取得し実行する
for file in *.py; do
    if [ -f "$file" ]; then
        echo "実行中: $file"
        python "$file"
        echo "------------"
    fi
done