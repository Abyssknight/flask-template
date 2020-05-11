"""
rest api namespace
"""

from flask_restx import Resource

from . import api

ns = api.namespace('apis', description='api resource')


@ns.route('/')
class Apis(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}
