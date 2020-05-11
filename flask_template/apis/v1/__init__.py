from flask import Blueprint, jsonify
from flask_restx import Api

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(app=api_v1, version='1.0', doc='/doc', title='flask-template', description='flask template api v1 doc')


@api_v1.route('/ping')
def ping():
    return jsonify({'msg': 'pong!'})


from .namespace import ns  # NOQA
