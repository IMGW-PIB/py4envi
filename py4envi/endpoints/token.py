from requests.auth import HTTPBasicAuth
import logging
from typing import Optional
from py4envi.util.rest import REST
from py4envi.util import config
from py4envi.models.token import TokenResponse, TokenRequest

logger = logging.getLogger(__name__)
URL = config.get_section("sat4envi")['url']


class TokenEndpoint(REST):
    def __init__(
            self,
            email: str,
            password: str):
        self._auth = HTTPBasicAuth(email, password)
        super().__init__(auth=None, path="token")

    def request_bearer_token(self) -> Optional[TokenResponse]:
        request = TokenRequest(self._auth.username, self._auth.password)
        response = self.post_json(request.json)
        if response is not None:
            logger.debug(
                "got bearer token response from sat4envi with status: %s",
                response.status_code)
            token_response = TokenResponse(response)
            return token_response
        return None
