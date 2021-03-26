from dataclasses import dataclass
from typing import Optional
from requests import Response
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


@dataclass
class TokenRequest(ModelRequest):
    email: str
    password: str
