"""
使用 Namespace 实现 REST API 资源隔离
"""

from flask_restx import Resource

from . import api_v1_resource

# Resource here
resources = api_v1_resource.namespace('resources', description='')


@resources.route('')
class Resources(Resource):
    name = 'resources'

    def get(self):
        return f'get {self.name}'

    def post(self):
        return f'post {self.name}'

    def put(self):
        return f'put {self.name}'

    def patch(self):
        return f'patch {self.name}'

    def delete(self):
        return f'delete {self.name}'
