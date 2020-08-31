"""
自定义库
"""

from sqlalchemy.ext.automap import automap_base


class AutoMap:
    """
    自动映射表结构到模型
    """

    def __init__(self, app=None, db=None):
        self.app = app
        self.db = db
        self.Base = None
        self.metadata = None

        self.reflected = False

        if self.app and self.db:
            self.init_app()

    def init_app(self, app=None, db=None):
        self.app = app or self.app
        self.db = db or self.db
        self.metadata = db.metadata
        self.Base = automap_base(metadata=self.metadata)

    def _reflect(self):
        engine = self.db.engine

        automap_tables = self.app.config.get('AUTOMAP_TABLES', [])
        self.metadata.reflect(
            engine,
            only=lambda t, i: any([t.startswith(table) for table in automap_tables]) if automap_tables else None
        )

        self.Base.prepare()
        self.reflected = True

    def get_model(self, table_name):
        if self.reflected is False:
            self._reflect()

        return getattr(self.Base.classes, table_name)
