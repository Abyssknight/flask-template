import logging
import os
import time
from logging.handlers import RotatingFileHandler

import click
import schedule
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from flask_template import tasks
from flask_template.configs import basedir, config
from flask_template.extensions import celery, db, migrate, redis
from flask_template.utils import get_host_ip, get_host_name


def create_app(config_name=None):
    """工厂函数"""

    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_logger(app)
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    register_shell_context(app)
    register_middlewares(app)
    register_ping(app)

    return app


def register_logger(app):
    """注册日志"""
    app.logger.setLevel(logging.DEBUG)

    class RequestFormatter(logging.Formatter):
        def format(self, record):
            record.hostname = get_host_name()
            return super().format(record)

    log_dir = app.config.get('LOG_DIR', os.path.join(basedir, 'logs'))
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, f'{app.name}.log'),
        maxBytes=10 * 1024 * 1024,
        backupCount=10
    )
    formatter = RequestFormatter(
        '(%(hostname)s)[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s'
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)


def register_blueprints(app):
    """注册蓝图"""

    from flask_template.apis import api_v1
    app.register_blueprint(api_v1)


def register_extensions(app):
    """注册扩展"""

    db.init_app(app)
    migrate.init_app(app, db=db)
    redis.init_app(app)
    celery.init_app(app)


def register_commands(app):
    """注册命令"""

    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """初始化数据库"""
        from flask_template.models import MyDB

        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')

        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def cron():
        """启动定时任务"""
        from flask_template import schedules
        while True:
            schedule.run_pending()
            time.sleep(1)


def register_shell_context(app):
    """注册 shell 上下文"""

    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, celery=celery, tasks=tasks)


def register_middlewares(app):
    """注册中间件"""
    app.wsgi_app = ProxyFix(app.wsgi_app)


def register_ping(app):
    """ping"""

    @app.route('/')
    def ping():
        app.logger.info('ping')
        return 'pong!'
