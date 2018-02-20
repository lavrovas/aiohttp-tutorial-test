from aiohttp import web
from aiohttp.web_app import Application

from app.routes import setup_routes


def init() -> Application:
    app = web.Application()
    setup_routes(app)
    return app


def main() -> None:
    app = init()
    web.run_app(app, host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
