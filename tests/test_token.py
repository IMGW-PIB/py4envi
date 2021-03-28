import tempfile
import random
import string
from pathlib import Path
from typing import Callable, Optional
from py4envi import token
from py4envi_openapi_client.apis import AuthApi
from py4envi_openapi_client import ApiClient
from py4envi_openapi_client.models import TokenResponse, LoginRequest


def _random_str() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


def _gen_mocked_auth_api(
        ret_token: Optional[str] = "fake token",
) -> Callable[[ApiClient], AuthApi]:

    class MockedAuthApi(AuthApi):
        def __init__(self):
            # initialize super to later overwrite token
            super().__init__()

            def token_f(_: LoginRequest):
                tr = TokenResponse()
                tr.email = "fake@fake.com"
                tr.token = ret_token
                return tr

            self.token = token_f

    return lambda _: MockedAuthApi()


def test_cache_token():
    rnd = _random_str()
    token._cache_token(rnd)

    tkn = token._read_cached_token()
    assert tkn == rnd


def test_netrc():
    with tempfile.NamedTemporaryFile(mode='w+t') as f:
        # write netrc contents
        lines = [
            'machine random.host.com\n',
            'login admin\n',
            'password admin1234\n',
        ]
        f.writelines(lines)
        f.flush()

        netrc = token.read_netrc_for_url('random.host.com', file_location=Path(f.name))
        assert netrc
        assert netrc[0] == 'admin'
        assert netrc[1] == 'admin1234'


def test_get_new_token():
    test_token = "fake token"

    # mock our class to return what we want
    tkn = token._get_new_token('', '', auth_api_fun=_gen_mocked_auth_api(test_token))
    assert tkn is not None
    assert tkn == test_token


def test_get_or_request_token():
    test_token = "fake token"

    tkn = token.get_or_request_token(
        '', '', auth_api_fun=_gen_mocked_auth_api(test_token), force=True)
    assert tkn is not None
    assert tkn == test_token

    # we should get error because we are forcing
    try:
        tkn = token.get_or_request_token(
            '', '', auth_api_fun=_gen_mocked_auth_api(None), force=True)
    except BaseException:
        tkn = None
    assert tkn is None

    # now just read that cached one
    tkn = token.get_or_request_token('', '', auth_api_fun=_gen_mocked_auth_api(None), force=False)
    assert tkn is not None
    assert tkn == test_token
