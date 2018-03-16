from typing import Dict

import aiohttp_jinja2
from aiohttp.web_request import Request


@aiohttp_jinja2.template('index.html')
async def index(request: Request) -> Dict:
    return {
        'title': 'Home Page',
        'user': {
            'username': 'Miguel',
        },
    }
