"""
扩展
"""

from flask_execute import Celery
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from flask_template.libs import AutoMap

migrate = Migrate()
redis = FlaskRedis(decode_responses=True)
db = SQLAlchemy()
automap = AutoMap()
celery = Celery()
