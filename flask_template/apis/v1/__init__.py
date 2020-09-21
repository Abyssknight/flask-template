from flask import Blueprint
from flask_restx import Api

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1_resource = Api(app=api_v1, version='1.0', doc='/doc', title='flask-template', description='')

# import resources here
from flask_template.apis.v1.resources import Resources  # NOQA
