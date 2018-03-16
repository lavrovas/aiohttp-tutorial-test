from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def index(request: Request) -> Response:
    user = {'username': 'Miguel'}
    return web.Response(content_type='text/html', body=(
        '<html>\n'
        '    <head>\n'
        '        <title>Home Page - Microblog</title>\n'
        '    </head>\n'
        '    <body>\n'
        '        <h1>Hello, ' + user['username'] + '!</h1>\n'
        '    </body>\n'
        '</html>')
    )
