# 描述

个人使用的 `Flask` 项目开发模板

## 插件集成

* `flask_sqlalchemy` ORM 框架
* `flask_migrate` ORM 数据迁移
* `flask_redis` 连接 Redis
* `flask_restx` 方便实现 `RESTFul API`
* `flask_execute` 分发 `Celery` 任务, 相关功能使用需要看下 [文档](https://pypi.org/project/Flask-Execute/)
* `flask_testing` 更方便的编写单元测试

其他包:

* `schedule` 使用定时任务
 
## 包管理

包管理使用了 [pipenv](https://pipenv.pypa.io/en/latest/) , 配合 `scripts` 非常好用

## 使用方式

* `git clone https://github.com/Abyssknight/flask-template YOUR_PROJECT_NAME`
* 使用 `Pycharm` 或其他工具，全局将 `flask_template` 替换为 `YOUR_PROJECT_NAME`
* `pipenv install --dev` 安装项目依赖
* `cp .env.example .env` 项目配置项从环境变量读取, 遵守 [12factor](https://12factor.net/zh_cn/config)
* 如有必要, 可修改 `.env` 配置
* `pipenv run dev` 启动开发环境

使用以上步骤就可以将项目启动, 十分方便

## 相关功能

由于采用了 `pipenv` 进行包管理，所以项目的启动都是基于它的:

* `pipenv run dev` 开发环境启动
* `pipenv run prd` 生产环境启动
* `pipenv run test` 启动单元测试
* `pipenv run cron` 启动定时任务
* `pipenv run celery` 启动 `celery` 进程

以上命令相当于 `Alias`, 本质上还是使用 `Flask` 基于 `Click` 实现的命令行功能

## 其他命令

* `flask --help` 查看命令帮助
* `flask shell` 进入 `shell` 上下文
* `flask routes` 查看所有路由
* `flask initdb` 初始化数据库表，如果没有则创建