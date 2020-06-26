FROM python:3.8-alpine as build

WORKDIR /app
ENV PIPENV_VENV_IN_PROJECT 1
COPY Pipfile* /app/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && apk update && apk add git gcc musl-dev libffi-dev openssl-dev make && pip install --no-cache-dir pipenv -i https://mirrors.aliyun.com/pypi/simple/ && pipenv install
RUN pip install --no-cache-dir pipenv -i https://mirrors.aliyun.com/pypi/simple/ && pipenv install

FROM python:3.8-alpine

WORKDIR /app
ENV PIPENV_VENV_IN_PROJECT 1

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin/pipenv /usr/local/bin/pipenv
COPY --from=build /app/.venv /app/.venv
COPY . /app
