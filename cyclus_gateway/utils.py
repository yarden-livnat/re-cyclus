from flask import request, Response, stream_with_context
import requests


def forward(service, url, stream=False):

    resp = requests.request(
        method=request.method,
        url=request.url.replace(f'{request.host_url}{service}/', url),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=stream)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    if stream:
        return Response(stream_with_context(resp.iter_content()), content_type = resp.headers['content-type'])
    else:
        return Response(resp.content, resp.status_code, headers)
