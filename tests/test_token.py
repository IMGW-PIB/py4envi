from py4envi import token


def test_cache_token():
    token._cache_token('fake token')

    tkn = token._read_cached_token()
    assert tkn == 'fake token'
