import logging
from typing import Dict, Any
from requests import Response


logger = logging.getLogger(__name__)


class ModelResponse:
    def __init__(self, response: Response):
        self._response = response
        try:
            self._json = response.json()
        except Exception:
            logger.error(
                "cannot get json from response content: %s",
                response.content,
                exc_info=True)
            self._json = {}

    @property
    def status_code(self) -> int:
        return self._response.status_code


class ModelRequest:
    def __init__(self):
        pass

    @property
    def json(self) -> Dict[str, Any]:
        return self.__dict__
