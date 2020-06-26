"""
使用 Namespace 实现 REST API 资源隔离

apis = api.namespace('apis', description='api resource')


@apis.route('/')
class Apis(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}
"""

from flask_restx import Resource

from . import api

# Resource here
