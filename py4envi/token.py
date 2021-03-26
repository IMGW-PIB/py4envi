import tempfile
import logging
import netrc
import os
from pathlib import Path
from typing import Optional, Tuple
from py4envi.util.config import Sat4enviConfig
from py4envi.endpoints import token

logger = logging.getLogger(__name__)
SAT4ENVI_CONFIG = Sat4enviConfig()


def read_netrc_for_url(url: str) -> Optional[Tuple[str, str]]:
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
    endpoint = token.TokenEndpoint(email, password)

    token_response = endpoint.request_bearer_token()

    if token_response:
        return token_response.token
    logger.error("could not get a new token")
    return None


def _cache_token(token: str) -> bool:
    """
    saves the provided token in a temporary file
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir).joinpath(SAT4ENVI_CONFIG.token_cache_filename)
        with open(out, "w") as f:
            bytes_written = f.write(token)
        return bytes_written > 0


def _read_cached_token() -> Optional[str]:
    """
    reads the cached token
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir).joinpath(SAT4ENVI_CONFIG.token_cache_filename)
        if out.exists():
            with open(out, "r") as f:
                token = f.read()
            token = token.strip()
            if token != "":
                return token
    return None


def get_or_request_token(email: str, password: str, force: bool = False) -> str:
    """
    gets the cached token if it exists and force is not specified,
    else it gets a new token and caches it.
    """
    tkn = _read_cached_token()
    if force or not tkn:
        tkn = _get_new_token(email, password)
        if not tkn:
            logger.error("did not receive token for the specified credentials")
            raise Exception("empty token response")
        _cache_token(tkn)
    return tkn
