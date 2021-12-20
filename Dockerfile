FROM python:3.9
ENV PYTHONUNBUFFERED 1

# pygraphvizはGraphvizのpythonラッパーのため以下が追加で必要
RUN apt-get update -y
RUN apt-get dist-upgrade -y
RUN apt-get install -y build-essential graphviz-dev graphviz pkg-config

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/