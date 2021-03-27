import tempfile
import random
import string
from unittest.mock import patch
from pathlib import Path
from requests.models import Response
from py4envi import token
from py4envi.util import rest


def _random_str() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


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
    resp = Response()
    resp._content = b'{"email": "a@a.a", "token": "fake token"}'

    # mock our entry REST class to return what we want
    with patch.object(rest.REST, 'post_json', return_value=resp):
        tkn = token._get_new_token('', '')
        assert tkn is not None
        assert tkn == 'fake token'


def test_get_or_request_token():
    resp = Response()
    resp._content = b'{"email": "a@a.a", "token": "some token"}'

    # mock our entry REST class to return what we want
    with patch.object(rest.REST, 'post_json', return_value=resp):
        tkn = token.get_or_request_token('', '', force=True)
        assert tkn is not None
        assert tkn == "some token"

    resp._content = None
    # mock our entry REST class to return nothing, we should get error because we are forcing
    with patch.object(rest.REST, 'post_json', return_value=resp):
        try:
            tkn = token.get_or_request_token('', '', force=True)
        except BaseException:
            tkn = None

        assert tkn is None
    # mock our entry REST class to return nothing, now we should get cached token
    with patch.object(rest.REST, 'post_json', return_value=resp):
        tkn = token.get_or_request_token('', '', force=False)
        assert tkn is not None
        assert tkn == "some token"
