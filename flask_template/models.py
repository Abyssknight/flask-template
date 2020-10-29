"""
数据库模型
"""

from flask_template.extensions import db
from flask_template.utils import now


class BaseMixin:
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=now, nullable=False, comment='创建时间')
    update_at = db.Column(db.DateTime, default=now, onupdate=now, nullable=False, comment='更新时间')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class MyDB(BaseMixin, db.Model):
    pass
