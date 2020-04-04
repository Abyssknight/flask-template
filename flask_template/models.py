"""
数据库模型
"""

from flask_template.extensions import db
import arrow


class Mixin:
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=arrow.now().datetime, nullable=False, comment='创建时间')
    update_at = db.Column(db.DateTime, default=arrow.now().datetime, nullable=False, comment='更新时间')


class MyDB(Mixin, db.Model):
    pass
