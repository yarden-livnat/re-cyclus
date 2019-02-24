from flask import Blueprint
from flask_restplus import Resource, Namespace
from flask_jwt_extended import (fresh_jwt_required)
from webargs.flaskparser import use_args, use_kwargs

from cyclus_gateway.security import User, UserSchema, auth

from flask_jwt_extended import get_jwt_identity

api = Namespace('admin', description='authentication')


@api.route('/register')
# @api.doc('registration')
class Register(Resource):

    # @api.response(401, 'Unauthorized')
    # @api.doc(responses={401: 'Unauthorized'})
    @api.doc('register a new user', body={'username': '', 'password': '', 'email': ''})
    @use_kwargs(UserSchema())
    def post(self, username, password, email, **kwargs):
        if User.query.filter_by(email=email).first():
            return {'message': f'User {email} already exists'}, 401

        user = User(username, email, password, **kwargs).save()
        access_token = auth.get_access_token(user)
        refresh_token = auth.get_refresh_token(user)
        return {
            'Authorization': {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        }, 201


@api.route('/unregister')
class Unregister(Resource):
    @fresh_jwt_required
    def delete(self):
        identity = get_jwt_identity()
        user = User.query.filter_by(email=identity).first()
        if user:
            auth.revoke_all(identity)
            user.delete()
            return {'status': 'success'}
        else:
            return {'status': 'failed'}, 401
