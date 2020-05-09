"""
扩展
"""

from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_execute import Celery

migrate = Migrate()
redis = FlaskRedis(decode_responses=True)
db = SQLAlchemy()
celery = Celery()
