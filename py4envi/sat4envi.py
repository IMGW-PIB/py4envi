import requests
from requests.adapters import HTTPAdapter
from requests.auth import AuthBase, HTTPBasicAuth
from urllib3.util.retry import Retry
import logging
import urllib.parse
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 30  # seconds
MAX_RETRIES = 15
TOKEN_PATH = 'token'


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class Sat4envi:
    _http = requests.Session()
    _retries = Retry(
        total=MAX_RETRIES,
        backoff_factor=1,
        method_whitelist=False)
    _adapter = TimeoutHTTPAdapter(max_retries=_retries)
    _http.mount("https://", _adapter)
    _http.mount("http://", _adapter)

    def __init__(
            self,
            host: str,
            auth: HTTPBasicAuth,
            path: str = None):
        self._host = host
        if not self._host.endswith("/"):
            self._host = self._host + "/"
        self._path = path
        self._url = urllib.parse.urljoin(self._host, path)
        self._auth = auth
        self._http.auth = auth

    def _post_json(self, json: dict,
                   path: str = None) -> Optional[requests.Response]:
        if path is not None:
            url = urllib.parse.urljoin(self._url, path)
        else:
            url = self._url
        r = self._http.post(url=url, json=json)
        logger.debug(
            "Sent POST to: {}, payload: {} with response: {}".format(
                url, json, r))
        if r.status_code == 404:
            logger.error("error from api: %s", r.content)
            return None
        elif r.status_code == 401:
            logger.error("forbidden: %s", r.content)
            return None
        elif r.status_code != 200:
            logger.error(
                "unknown error code: %s from api: %s",
                r.status_code,
                r.content)
            return None
        return r

    def request_bearer_token(self) -> Optional[Tuple[str, str]]:
        username = self._auth.username
        password = self._auth.password
        payload = {
            "email": username,
            "password": password,
        }
        response = self._post_json(payload, path=TOKEN_PATH)
        if response is not None:
            logger.debug(
                "got bearer token response from sat4envi with status: %s",
                response.status_code)
            js = response.json()
            return js['email'], js['token']
        return response


class BearerAuth(AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


def retrieve_credentials(host: str, email: str,
                         password: str) -> Optional[Tuple[str, str]]:
    api = Sat4envi(host, auth=HTTPBasicAuth(email, password))
    return api.request_bearer_token()
