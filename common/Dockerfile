ARG BASE_IMAGE="nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04"
FROM ${BASE_IMAGE}


ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN apt-get update || true && apt-get install -y build-essential  openssh-client \
    wget curl git git-lfs vim zip unzip tmux htop software-properties-common \
    libglib2.0-0 libsm6 libxext6 libxrender-dev \
    zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
    libssl-dev libsqlite3-dev libreadline-dev libffi-dev libbz2-dev \
    python3.8 python3-pip python3.8-venv python3.8-dev \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get install python3.8 -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py \
    && rm get-pip.py

RUN mkdir -p /usr/tmp
WORKDIR /usr/tmp
COPY poetry.lock pyproject.toml /usr/tmp/

RUN python -m pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev \
    && rm -rf ~/.cache

RUN mkdir -p /usr/src/dev
WORKDIR /usr/src/dev

CMD [ "bash" ]