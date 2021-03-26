import requests
from requests.adapters import HTTPAdapter
from requests.auth import AuthBase
from urllib3.util.retry import Retry
import logging
import urllib.parse
from typing import Optional
from py4envi.util import config


REST_CONFIG = config.RestConfig()
SAT4ENVI_CONFIG = config.Sat4enviConfig()

logger = logging.getLogger(__name__)


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = REST_CONFIG.timeout
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class REST:
    def __init__(
            self,
            auth: AuthBase = None,
            path: str = None):
        self._http = requests.Session()
        self._retries = Retry(
            total=REST_CONFIG.max_retries,
            backoff_factor=REST_CONFIG.backoff_factor,
            method_whitelist=False)
        self._adapter = TimeoutHTTPAdapter(max_retries=self._retries)
        self._http.mount("https://", self._adapter)
        self._http.mount("http://", self._adapter)

        self._host = SAT4ENVI_CONFIG.url
        if not self._host.endswith("/"):
            self._host = self._host + "/"
        self._path = path
        self._url = urllib.parse.urljoin(self._host, path)
        self._http.auth = auth

    def post_json(self, json: dict,
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


class BearerAuth(AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r
