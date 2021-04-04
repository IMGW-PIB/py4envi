from __future__ import annotations
import logging
from typing import Callable, List
import pandas
from py4envi import frames
import py4envi_openapi_client
from py4envi_openapi_client.apis import ProductApi
from py4envi_openapi_client.models import BasicProductResponse

logger = logging.getLogger(__name__)


def _get_raw_products(
    token: str,
    product_api_fun: Callable[[py4envi_openapi_client.ApiClient], ProductApi],
) -> List[BasicProductResponse]:
    """
    requests and returns a list of all products accessible through this api
    """
    logger.debug("Requesting all products")
    configuration = py4envi_openapi_client.Configuration(
        access_token=token,
    )
    with py4envi_openapi_client.ApiClient(configuration) as api_client:
        api_instance = product_api_fun(api_client)

        try:
            api_response: List[BasicProductResponse] = api_instance.get_products()
            return api_response
        except py4envi_openapi_client.ApiException:
            logger.error(
                "Exception when calling ProductApi->get_products", exc_info=True
            )
        return []


def get_products(
    token: str,
    product_api_fun: Callable[
        [py4envi_openapi_client.ApiClient], ProductApi
    ] = lambda c: ProductApi(c),
) -> pandas.DataFrame:
    js = [x.to_dict() for x in _get_raw_products(token, product_api_fun)]
    return frames.json_response_to_df(js)
