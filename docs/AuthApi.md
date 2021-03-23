# py4envi.AuthApi

All URIs are relative to *https://dane.sat4envi.imgw.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token**](AuthApi.md#token) | **POST** /api/v1/token | Get authorization token


# **token**
> TokenResponse token(login_request)

Get authorization token

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import py4envi
from py4envi.api import auth_api
from py4envi.model.token_response import TokenResponse
from py4envi.model.login_request import LoginRequest
from pprint import pprint
# Defining the host is optional and defaults to https://dane.sat4envi.imgw.pl
# See configuration.py for a list of all supported configuration parameters.
configuration = py4envi.Configuration(
    host = "https://dane.sat4envi.imgw.pl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-token
configuration = py4envi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with py4envi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    login_request = LoginRequest(
        email="email_example",
        password="password_example",
    ) # LoginRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get authorization token
        api_response = api_instance.token(login_request)
        pprint(api_response)
    except py4envi.ApiException as e:
        print("Exception when calling AuthApi->token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[bearer-token](../README.md#bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden: Account disabled (not activated) |  -  |
**401** | Unauthenticated: Incorrect credentials or account doesn&#39;t exist |  -  |
**200** | OK |  -  |
**400** | Incorrect request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

