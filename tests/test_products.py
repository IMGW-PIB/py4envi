from typing import Callable
from py4envi import products
from py4envi_openapi_client.apis import ProductApi
from py4envi_openapi_client import ApiClient
from py4envi_openapi_client.models import BasicProductResponse, BasicProductCategoryResponse


def _gen_mocked_product_api() -> Callable[[ApiClient], ProductApi]:

    class MockedProductApi(ProductApi):
        def __init__(self):
            # initialize super to later overwrite token
            super().__init__()

            def get_products_f():
                return [
                    BasicProductResponse(
                        name='test',
                        display_name='test',
                        product_category=BasicProductCategoryResponse(
                            label='test'))]

            self.get_products = get_products_f

    return lambda _: MockedProductApi()


def test_get_raw_products():
    # mock our class
    prods = products._get_raw_products('fake token', product_api_fun=_gen_mocked_product_api())
    assert len(prods) > 0
    assert isinstance(prods[0], BasicProductResponse)
    assert prods[0].name == 'test'
    assert prods[0].display_name == 'test'
    assert prods[0].product_category.label == 'test'


def test_get_products():
    # mock our class
    prods = products.get_products('fake token', product_api_fun=_gen_mocked_product_api())
    assert len(prods) > 0
    assert isinstance(prods[0], products.Product)
    assert prods[0].name == 'test'
    assert prods[0].display_name == 'test'
    assert prods[0].label == 'test'
