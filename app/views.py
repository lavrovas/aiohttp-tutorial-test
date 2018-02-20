from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def index(request: Request) -> Response:
    return web.Response(text='Hello, world!')
