##### 第一阶段构建 安装依赖包 #####
FROM python:3.8-alpine as build

# 更换镜像源 安装依赖
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && apk update && apk add git gcc musl-dev libffi-dev openssl-dev make

# 安装依赖
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

##### 第二阶段构建 拷贝依赖包 #####
FROM python:3.8-alpine

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# 切换工作路径
WORKDIR /app
COPY . /app

EXPOSE 5000
CMD gunicorn -c gunicorn.py wsgi:app
