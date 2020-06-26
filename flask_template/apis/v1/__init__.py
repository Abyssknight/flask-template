from flask import Blueprint
from flask_restx import Api

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(app=api_v1, version='1.0', doc='/doc', title='flask-template', description='flask template api v1 doc')

# Import rresource here
# from .apis import apis  # NOQA
