import tempfile
import logging
import netrc
from pathlib import Path
from typing import Optional, Tuple, Callable
from urllib.parse import urlparse
import py4envi_openapi_client
from py4envi_openapi_client.apis import AuthApi
from py4envi_openapi_client.models import TokenResponse, LoginRequest


logger = logging.getLogger(__name__)
TOKEN_CACHE_FILENAME = "sat4envi_token.txt"


def _read_netrc_for_url(
    file_location: Path = Path("~/.netrc"),
) -> Optional[Tuple[str, str]]:
    """
    reads username and password from netrc file in the user's home dir
    """
    configuration = py4envi_openapi_client.Configuration()
    url = urlparse(configuration._base_path).hostname
    assert url, "url read from openapi config was None"

    logger.debug("getting auth data for host: %s from netrc file", url)
    # explicitly specify file to avoid permission checks
    nrc = netrc.netrc(str(file_location.expanduser().resolve().absolute()))
    for h, lap in nrc.hosts.items():
        if h in url:
            return lap[0], lap[2] or ""
    # fallback here
    lap2 = nrc.authenticators(url)
    if lap2 is not None and lap2[2] is not None:
        return lap2[0], lap2[2] or ""
    logger.warning("auth data for host: %s not found in netrc file", url)
    return None


def _get_new_token(
    email: str,
    password: str,
    auth_api_fun: Callable[[py4envi_openapi_client.ApiClient], AuthApi],
) -> Optional[str]:
    """
    requests and returns a current api token
    """
    logger.info("Requesting new api token")
    configuration = py4envi_openapi_client.Configuration()
    # Enter a context with an instance of the API client
    with py4envi_openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = auth_api_fun(api_client)
        login_request = LoginRequest(
            email=email,
            password=password,
        )

        try:
            # Get authorization token
            api_response: TokenResponse = api_instance.token(login_request)
            if api_response:
                return api_response.token
            logger.error("bad response from api token request")
        except py4envi_openapi_client.ApiException:
            logger.error("Exception when calling AuthApi->token", exc_info=True)
        return None


def _cache_token(token: str) -> bool:
    """
    saves the provided token in a temporary file
    """
    dir = tempfile.gettempdir()
    out = Path(dir).joinpath(TOKEN_CACHE_FILENAME)
    with open(out, "w") as f:
        bytes_written = f.write(token)
        return bytes_written > 0


def _read_cached_token() -> Optional[str]:
    """
    reads the cached token
    """
    dir = tempfile.gettempdir()
    out = Path(dir).joinpath(TOKEN_CACHE_FILENAME)
    if out.exists():
        with open(out, "r") as f:
            token = f.read()
        token = token.strip()
        if token != "":
            return token
    return None


def get_or_request_token(
    email: str = None,
    password: str = None,
    force: bool = False,
    auth_api_fun: Callable[
        [py4envi_openapi_client.ApiClient], AuthApi
    ] = lambda c: AuthApi(c),
) -> str:
    """
    gets the cached token if it exists and force is not specified,
    else it gets a new token and caches it.
    If email or password are not provided, tries to read them from netrc.
    """
    if email is None or password is None:
        logger.info("email or password was None, reading credentials from netrc...")
        nrc = _read_netrc_for_url()
        assert nrc, "email or password was not provided, but it was not found in netrc"
        email, password = nrc
    tkn = _read_cached_token()
    if force or not tkn:
        tkn = _get_new_token(email, password, auth_api_fun)
        if not tkn:
            logger.error("did not receive token for the specified credentials")
            raise Exception("empty token response")
        _cache_token(tkn)
    return tkn
