"""
数据库模型
"""

from flask_template.extensions import db
from flask_template.utils import now


class Mixin:
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=now, nullable=False, comment='创建时间')
    update_at = db.Column(db.DateTime, default=now, onupdate=now, nullable=False, comment='更新时间')


class MyDB(Mixin, db.Model):
    pass
