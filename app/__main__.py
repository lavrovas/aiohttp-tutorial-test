import argparse
import sys

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web_app import Application

from app.routes import setup_routes


def init() -> Application:
    app = web.Application()
    setup_routes(app)

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('app', 'templates'))

    return app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aiohttp tutorial app')
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Network interface to use')
    parser.add_argument('-P', '--port', type=int, default=8080, help='Network port to use')
    args = parser.parse_args(sys.argv[1:])

    app = init()
    web.run_app(app, host=args.host, port=args.port)
