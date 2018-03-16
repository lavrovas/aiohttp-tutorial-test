async def test_get_root(cli):
    resp = await cli.get('/')
    assert resp.status == 200

    text = await resp.text()
    assert 'Home Page - Microblog' in text
    assert 'Hello, Miguel!' in text


async def test_get_index(cli):
    resp = await cli.get('/index')
    assert resp.status == 200

    text = await resp.text()
    assert 'Home Page - Microblog' in text
    assert 'Hello, Miguel!' in text
