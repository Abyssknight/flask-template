# 描述

个人使用的 `Flask` 项目开发模板

## 插件集成

* Flask-SQLAlchemy
* Flask-Migrate
* Flask-Redis
* Flask-Execute
  * Celery 任务
* Flask-Testing
* Flask-Restx
    * REST API
    * Swagger doc
* Schedule
  * 定时任务
  
## 功能

* shell 上下文
* 命令行工具
* 日志集成
* docker部署(测试用)
  
## 命令

* `flask --help` 查看帮助
* `flask celery --help` celery帮助
    * `flask celery worker` 启动celery任务
* `flask cron` 启动 schedule 定时任务
