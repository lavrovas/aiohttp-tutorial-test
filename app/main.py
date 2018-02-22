import argparse
from typing import List, Tuple

from aiohttp import web
from aiohttp.web_app import Application

from app.routes import setup_routes


def init() -> Application:
    app = web.Application()
    setup_routes(app)
    return app


def parse_args(argv: List[str]) -> Tuple[str, int]:
    parser = argparse.ArgumentParser(description='Aiohttp tutorial app')
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Network interface to use')
    parser.add_argument('-P', '--port', type=int, default=8080, help='Network port to use')
    args = parser.parse_args(argv)

    return args.host, args.port


def main(argv: List[str]) -> None:
    host, port = parse_args(argv)

    app = init()
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
