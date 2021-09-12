はじめに
====
以下の作業に沿って実行してください。

# ファイル構成
```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── work    # ソース用のディレクトリ
```

# 実行
```
# Dockerfileビルド
docker-compose up -d --build

# コンテナ起動

# コンテナ入場
docker-compose exce {container_name} bash

# コンテナ退場
CTRL + D

# コンテナ削除
docker-compose down

# コンテナ終了
docker stop コンテナネーム

```
# jupyter notebook
## コンテナ作成時
```
cp jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
```

## 起動
```
jupyter notebook --ip=0.0.0.0 --allow-root
```

## docker images list
```
docker images
```

## docker container list
```py
# -a は停止中のコンテナも表示する
docker ps -a 
```

## 