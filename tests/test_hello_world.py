async def test_get_root(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    assert await resp.text() == 'Hello, world!'


async def test_get_index(cli):
    resp = await cli.get('/index')
    assert resp.status == 200
    assert await resp.text() == 'Hello, world!'
