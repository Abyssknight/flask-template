import time

from flask_testing import TestCase

from flask_template import create_app
from flask_template.extensions import db
from flask_template.models import MyDB
from flask_template.utils import RedisLock


class BaseTest(TestCase):
    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class InitStateTest(BaseTest):
    def test_server_up(self):
        response = self.client.get('/api/v1/ping')
        self.assertEqual(response.json, {'msg': 'pong!'})

    def test_db(self):
        db.session.add(MyDB())
        db.session.commit()

        db_obj = MyDB.query.get(1)
        self.assertTrue(getattr(db_obj, 'create_at'))
        self.assertTrue(getattr(db_obj, 'update_at'))


class RedisLockTest(BaseTest):
    lock1 = RedisLock(lock_name='lock:name', timeout=3)
    lock2 = RedisLock(lock_name='lock:name', timeout=3)

    def test_redis_lock_acquire(self):
        self.assertTrue(self.lock1.acquire())
        self.assertFalse(self.lock2.acquire())

        self.assertTrue(self.lock1.release())
        self.assertTrue(self.lock2.acquire())
        self.assertTrue(self.lock2.release())

    def test_redis_lock_release(self):
        self.assertTrue(self.lock1.acquire())
        time.sleep(15)
        self.assertTrue(self.lock2.acquire())
        self.assertFalse(self.lock1.release())
        self.assertTrue(self.lock2.release())
