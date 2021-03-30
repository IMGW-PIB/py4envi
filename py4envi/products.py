from __future__ import annotations
import logging
from dataclasses import dataclass
from typing import Callable, List
import py4envi_openapi_client
from py4envi_openapi_client.apis import ProductApi
from py4envi_openapi_client.models import BasicProductResponse

logger = logging.getLogger(__name__)


@dataclass
class Product:
    name: str
    display_name: str
    label: str

    @classmethod
    def from_basic_product_response(cls, bpr: BasicProductResponse) -> Product:
        return cls(bpr.name, bpr.display_name, bpr.product_category.label)


def _get_raw_products(token: str,
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
            logger.error("Exception when calling ProductApi->get_products", exc_info=True)
        return []


def get_products(token: str,
                 product_api_fun: Callable[[py4envi_openapi_client.ApiClient],
                                           ProductApi] = lambda c: ProductApi(c),
                 ) -> List[Product]:
    return [Product.from_basic_product_response(p)
            for p in _get_raw_products(token, product_api_fun)]
