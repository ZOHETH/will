FROM python:3.8.12

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    WILL_HOME="/app/will_home"

RUN mkdir /app \
        && apt-get update -y \
        && apt-get install -y --no-install-recommends \
            libpq-dev \
            libsasl2-dev \
            libecpg-dev \
            vim \
        && rm -rf /var/lib/apt/lists/* \


# 替换pip国内源
RUN pip install -i https://pypi.douban.com/simple pip -U \
    && pip config set global.index-url https://pypi.douban.com/simple \
    && pip config set global.trusted-host pypi.douban.com \


COPY ./requirements.txt  /app/requirements.txt

RUN cd /app \
    && pip install -r requirements.txt

WORKDIR /app
ADD ./docker /app/docker
ADD ./will /app/will
