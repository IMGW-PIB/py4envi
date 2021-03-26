import random
import string
from py4envi import token


def test_cache_token():
    rnd = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

    token._cache_token(rnd)

    tkn = token._read_cached_token()
    assert tkn == rnd
