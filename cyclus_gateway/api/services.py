import requests
from flask import Blueprint
from flask import request, Response, stream_with_context


from flask_restplus import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_claims

api = Namespace('services', description='services')

batch_server = 'http://batch:5010'


def forward(url, stream=False):

    resp = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=stream)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    if stream:
        return Response(stream_with_context(resp.iter_content()), content_type=resp.headers['content-type'])
    else:
        return Response(resp.content, resp.status_code, headers)
    
    
@api.route('/batch/<path:path>')
class Batch(Resource):
    @jwt_required
    def post(self, path):
        claims = get_jwt_claims()
        print('claims:', claims)
        resp = forward(f'{batch_server}/{path}')
        return resp
