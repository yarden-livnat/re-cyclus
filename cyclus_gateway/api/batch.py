from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from cyclus_gateway.utils import forward

api = Namespace('batch', description='run remote cyclus')

batch_server = 'http://localhost:5010/'


@api.route('/run')
class Batch(Resource):
    @jwt_required
    def post(self):
        claims = get_jwt_claims()
        print('claims:', claims)
        resp = forward(service=api.name, url=batch_server)
        return resp
