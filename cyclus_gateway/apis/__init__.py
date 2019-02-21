from flask_restplus import Api

from jwt.exceptions import ExpiredSignatureError
from flask_jwt_extended.exceptions import JWTExtendedException
from cyclus_gateway.security.exceptions import TokenNotFound

from .admin import api as ns_admin
from .batch import api as ns_batch


api = Api(
    title='Cyclus Gateway',
    version = '1',
    description = 'Remote cyclus services api')


api.add_namespace(ns_admin)  # path='/prefix/of/ns'
api.add_namespace(ns_batch)


@api.errorhandler
def default_error_handler(error):
    '''Default error handler'''
    return {'message': str(error)}, getattr(error, 'code', 500)


@api.errorhandler(JWTExtendedException)
@api.errorhandler(TokenNotFound)
def handle_security_exception(error):
    '''Security exceptions handler'''
    return {'message': error.message}, 400

@api.errorhandler(ExpiredSignatureError)
def handle_expire_exception(error):
    return {'message': 'Signature expired'}, 400
