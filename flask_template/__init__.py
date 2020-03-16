import os

from flask import Flask

from flask_template.extensions import db, migrate, redis
from flask_template.settings import config


def create_app(config_name=None):
    """工厂函数"""

    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    """注册蓝图"""

    from flask_template.apis.v1 import api_v1
    app.register_blueprint(api_v1)


def register_extensions(app):
    """注册扩展"""

    db.init_app(app)
    migrate.init_app(app, db=db)
    redis.init_app(app)
