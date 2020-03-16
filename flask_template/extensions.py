"""
扩展
"""

from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
redis = FlaskRedis(decode_responses=True)
db = SQLAlchemy()
