FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i.bak -e "s%http://us.archive.ubuntu.com/ubuntu/%http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%g" /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y subversion vim curl language-pack-ja-base language-pack-ja locales fonts-takao python3.9 python3-pip \
    libcgal-dev libpython3-dev python3-pyqt5 python3-msgpack python3-pulp \
    openmpi-bin libopenmpi-dev \
    cmake python3-paraview paraview jupyter
COPY .vimrc ./

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt \
    && rm /tmp/* -rf

WORKDIR /home
USER root

