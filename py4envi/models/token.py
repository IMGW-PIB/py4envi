from requests import Response
from typing import Optional
from py4envi.models import ModelResponse, ModelRequest


class TokenResponse(ModelResponse):
    def __init__(self, response: Response):
        super().__init__(response)
        self._email = self._json.get("email")
        self._token = self._json.get("token")

    @property
    def email(self) -> Optional[str]:
        return self._email

    @property
    def token(self) -> Optional[str]:
        return self._token


class TokenRequest(ModelRequest):
    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password
