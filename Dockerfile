FROM ubuntu:22.04
ARG user
ARG gid
ARG uid

ARG hugging_face_token
ARG openai_api_key

ENV HUGGING_FACE_HUB_TOKEN=${hugging_face_token}
ENV OPENAI_API_KEY=${openai_api_key}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install sudo -y
RUN apt-get install htop -y
RUN apt-get install git -y
RUN apt-get install cmake make -y
RUN apt install software-properties-common -y
RUN apt-get install build-essential -y

RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get install python3.10 python3.10-dev python3.10-venv python3-pip -y
RUN ln -s /usr/bin/python3.10 /usr/bin/python

RUN groupadd -g ${gid} ${user} || true
RUN useradd -m ${user} -u ${uid} -g ${gid} -s /usr/bin/bash
RUN adduser ${user} sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers


USER ${user}


WORKDIR /home/${user}/app

COPY ./requirements.txt /home/${user}/app/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . /home/${user}/app
