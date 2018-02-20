from aiohttp import web

from app.routes import setup_routes


def init():
    app = web.Application()
    setup_routes(app)
    return app


def main():
    app = init()
    web.run_app(app, host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
