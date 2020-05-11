"""
扩展
"""

from flask_execute import Celery
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
redis = FlaskRedis(decode_responses=True)
db = SQLAlchemy()
celery = Celery()
