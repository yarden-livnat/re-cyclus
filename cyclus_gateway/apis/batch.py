
from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims

api = Namespace('batch', description='run remote cyclus')

@api.route('/run')
class Batch(Resource):
    @jwt_required
    def post(self):
        print('post batch')
        resp = {
            'dentity': get_jwt_identity(),  # test
            'roles': get_jwt_claims()  # ['foo', 'bar']
        }
        return resp
