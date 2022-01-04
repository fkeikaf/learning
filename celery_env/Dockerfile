# どのイメージをもとにするか
FROM python:3.8
USER root
# 必ず2つ実行する。upgradeは実行しないこと
# https://docs.docker.jp/engine/userguide/eng-image/dockerfile_best-practice.html#run
RUN apt-get update
# タイムゾーンの設定は一旦保留

# 必要なパッケージを入れる
RUN apt-get install -y vim less

# 作業ディレクトリ
RUN mkdir /var/work
WORKDIR /var/work
COPY requirements.txt /var/work

# python モジュールのアップデート
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
# requirements.txtからパッケージのインストール
RUN python -m pip install -r requirements.txt

# RUN python -m pip install jupyter

# EXPOSE 8888
# RUN jupyter notebook --generate-config