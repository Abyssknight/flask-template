"""
应用配置
"""

import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    """基础配置"""

    SECRET_KEY = '5dbefe8430d17d34cd36121517eab54728b01ebddff60807ae30d2194b743cad'

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.db'))

    # Redis
    REDIS_URL = "redis://localhost:6379/0"

    # Celery
    CELERY_LOG_DIR = 'logs'
    CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'


class TestingConfig(BaseConfig):
    """测试环境"""

    TESTING = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data-test.db'))


class DevelopmentConfig(BaseConfig):
    """开发环境"""

    DEBUG = True


class ProductionConfig(BaseConfig):
    """生产环境"""

    DEBUG = False


config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
