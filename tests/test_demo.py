from flask_testing import TestCase

from flask_template import create_app
from flask_template.extensions import db


class BaseTest(TestCase):
    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
