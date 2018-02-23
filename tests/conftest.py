import pytest

from app.__main__ import init


@pytest.fixture
def cli(loop, test_client):
    app = init()
    return loop.run_until_complete(test_client(app))
