from flask_testing import TestCase

from flask_template import create_app


class PingTest(TestCase):
    def create_app(self):
        app = create_app('testing')
        return app

    def test_server_up(self):
        response = self.client.get('/api/v1/ping')
        self.assertEqual(response.json, {'msg': 'pong!'})
