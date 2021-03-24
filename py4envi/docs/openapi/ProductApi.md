# openapi_client.ProductApi

All URIs are relative to *https://dane.sat4envi.imgw.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_products**](ProductApi.md#get_products) | **GET** /api/v1/products | View a list of products


# **get_products**
> [BasicProductResponse] get_products()

View a list of products

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import openapi_client
from openapi_client.api import product_api
from openapi_client.model.basic_product_response import BasicProductResponse
from pprint import pprint
# Defining the host is optional and defaults to https://dane.sat4envi.imgw.pl
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dane.sat4envi.imgw.pl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-token
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_api.ProductApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # View a list of products
        api_response = api_instance.get_products()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->get_products: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[BasicProductResponse]**](BasicProductResponse.md)

### Authorization

[bearer-token](../README.md#bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

