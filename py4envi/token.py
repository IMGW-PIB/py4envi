import tempfile
import logging
import netrc
import os
from pathlib import Path
from typing import Optional, Tuple
from . import openapi_client
from .openapi_client.api import auth_api
from .openapi_client.model.token_response import TokenResponse
from .openapi_client.model.login_request import LoginRequest

logger = logging.getLogger(__name__)
TOKEN_FILENAME = 'sat4envi-tkn.txt'


def _read_netrc_for_url(url: str) -> Optional[Tuple[str, str]]:
    """
    reads username and password from netrc file in the user's home dir
    """
    logger.debug("getting auth data for host: %s from netrc file", url)
    # explicitly specify file to avoid permission checks
    nrc = netrc.netrc(os.path.expanduser("~/.netrc"))
    for h, lap in nrc.hosts.items():
        if h in url:
            return lap[0], lap[2] or ""
    # fallback here
    lap2 = nrc.authenticators(url)
    if lap2 is not None and lap2[2] is not None:
        return lap2[0], lap2[2] or ""
    logger.warn("auth data for host: %s not found in netrc file", url)
    return None


def _get_new_token(email: str, password: str) -> Optional[str]:
    """
    requests and returns a current api token
    """
    logger.info("Requesting new api token")
    configuration = openapi_client.Configuration()
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
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
        except openapi_client.ApiException:
            logger.error("Exception when calling AuthApi->token", exc_info=True)
        return None


def _cache_token(token: str) -> bool:
    """
    saves the provided token in a temporary file
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir).joinpath(TOKEN_FILENAME)
        with open(out, "w") as f:
            bytes_written = f.write(token)
        return bytes_written > 0


def _read_cached_token() -> Optional[str]:
    """
    reads the cached token
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir).joinpath(TOKEN_FILENAME)
        if out.exists():
            with open(out, "r") as f:
                token = f.read()
            token = token.strip()
            if token != "":
                return token
    return None


def get_or_request_token(force: bool = False) -> str:
    # TODO
    return "fake token"
