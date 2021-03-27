# py4envi_openapi_client.SearchApi

All URIs are relative to *https://dane.sat4envi.imgw.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_count**](SearchApi.md#get_count) | **GET** /api/v1/search/count | Get count of total scene results
[**get_scenes**](SearchApi.md#get_scenes) | **GET** /api/v1/search | Search for scenes


# **get_count**
> int get_count(UNKNOWN_PARAMETER_NAME6)

Get count of total scene results

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import py4envi_openapi_client
from py4envi_openapi_client.api import search_api
from pprint import pprint
# Defining the host is optional and defaults to https://dane.sat4envi.imgw.pl
# See configuration.py for a list of all supported configuration parameters.
configuration = py4envi_openapi_client.Configuration(
    host = "https://dane.sat4envi.imgw.pl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-token
configuration = py4envi_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with py4envi_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    UNKNOWN_PARAMETER_NAME6 =  #  | 
    UNKNOWN_PARAMETER_NAME =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME2 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME3 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME4 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME5 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME7 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME8 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME9 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME10 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME11 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME12 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME13 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME14 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME15 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME16 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME17 =  #  |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get count of total scene results
        api_response = api_instance.get_count(UNKNOWN_PARAMETER_NAME6)
        pprint(api_response)
    except py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_count: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get count of total scene results
        api_response = api_instance.get_count(UNKNOWN_PARAMETER_NAME6, UNKNOWN_PARAMETER_NAME=UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2=UNKNOWN_PARAMETER_NAME2, UNKNOWN_PARAMETER_NAME3=UNKNOWN_PARAMETER_NAME3, UNKNOWN_PARAMETER_NAME4=UNKNOWN_PARAMETER_NAME4, UNKNOWN_PARAMETER_NAME5=UNKNOWN_PARAMETER_NAME5, UNKNOWN_PARAMETER_NAME7=UNKNOWN_PARAMETER_NAME7, UNKNOWN_PARAMETER_NAME8=UNKNOWN_PARAMETER_NAME8, UNKNOWN_PARAMETER_NAME9=UNKNOWN_PARAMETER_NAME9, UNKNOWN_PARAMETER_NAME10=UNKNOWN_PARAMETER_NAME10, UNKNOWN_PARAMETER_NAME11=UNKNOWN_PARAMETER_NAME11, UNKNOWN_PARAMETER_NAME12=UNKNOWN_PARAMETER_NAME12, UNKNOWN_PARAMETER_NAME13=UNKNOWN_PARAMETER_NAME13, UNKNOWN_PARAMETER_NAME14=UNKNOWN_PARAMETER_NAME14, UNKNOWN_PARAMETER_NAME15=UNKNOWN_PARAMETER_NAME15, UNKNOWN_PARAMETER_NAME16=UNKNOWN_PARAMETER_NAME16, UNKNOWN_PARAMETER_NAME17=UNKNOWN_PARAMETER_NAME17)
        pprint(api_response)
    except py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **UNKNOWN_PARAMETER_NAME6** | ****|  |
 **UNKNOWN_PARAMETER_NAME** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME2** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME3** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME4** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME5** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME7** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME8** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME9** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME10** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME11** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME12** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME13** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME14** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME15** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME16** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME17** | ****|  | [optional]

### Return type

**int**

### Authorization

[bearer-token](../README.md#bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**200** | Successfully retrieved count |  -  |
**400** | Incorrect request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenes**
> [SearchResponse] get_scenes(UNKNOWN_PARAMETER_NAME6)

Search for scenes

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import py4envi_openapi_client
from py4envi_openapi_client.api import search_api
from py4envi_openapi_client.model.search_response import SearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://dane.sat4envi.imgw.pl
# See configuration.py for a list of all supported configuration parameters.
configuration = py4envi_openapi_client.Configuration(
    host = "https://dane.sat4envi.imgw.pl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-token
configuration = py4envi_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with py4envi_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    UNKNOWN_PARAMETER_NAME6 =  #  | 
    UNKNOWN_PARAMETER_NAME =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME2 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME3 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME4 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME5 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME7 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME8 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME9 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME10 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME11 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME12 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME13 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME14 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME15 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME16 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME17 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME18 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME19 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME20 =  #  |  (optional)
    UNKNOWN_PARAMETER_NAME21 =  #  |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for scenes
        api_response = api_instance.get_scenes(UNKNOWN_PARAMETER_NAME6)
        pprint(api_response)
    except py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_scenes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for scenes
        api_response = api_instance.get_scenes(UNKNOWN_PARAMETER_NAME6, UNKNOWN_PARAMETER_NAME=UNKNOWN_PARAMETER_NAME, UNKNOWN_PARAMETER_NAME2=UNKNOWN_PARAMETER_NAME2, UNKNOWN_PARAMETER_NAME3=UNKNOWN_PARAMETER_NAME3, UNKNOWN_PARAMETER_NAME4=UNKNOWN_PARAMETER_NAME4, UNKNOWN_PARAMETER_NAME5=UNKNOWN_PARAMETER_NAME5, UNKNOWN_PARAMETER_NAME7=UNKNOWN_PARAMETER_NAME7, UNKNOWN_PARAMETER_NAME8=UNKNOWN_PARAMETER_NAME8, UNKNOWN_PARAMETER_NAME9=UNKNOWN_PARAMETER_NAME9, UNKNOWN_PARAMETER_NAME10=UNKNOWN_PARAMETER_NAME10, UNKNOWN_PARAMETER_NAME11=UNKNOWN_PARAMETER_NAME11, UNKNOWN_PARAMETER_NAME12=UNKNOWN_PARAMETER_NAME12, UNKNOWN_PARAMETER_NAME13=UNKNOWN_PARAMETER_NAME13, UNKNOWN_PARAMETER_NAME14=UNKNOWN_PARAMETER_NAME14, UNKNOWN_PARAMETER_NAME15=UNKNOWN_PARAMETER_NAME15, UNKNOWN_PARAMETER_NAME16=UNKNOWN_PARAMETER_NAME16, UNKNOWN_PARAMETER_NAME17=UNKNOWN_PARAMETER_NAME17, UNKNOWN_PARAMETER_NAME18=UNKNOWN_PARAMETER_NAME18, UNKNOWN_PARAMETER_NAME19=UNKNOWN_PARAMETER_NAME19, UNKNOWN_PARAMETER_NAME20=UNKNOWN_PARAMETER_NAME20, UNKNOWN_PARAMETER_NAME21=UNKNOWN_PARAMETER_NAME21)
        pprint(api_response)
    except py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_scenes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **UNKNOWN_PARAMETER_NAME6** | ****|  |
 **UNKNOWN_PARAMETER_NAME** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME2** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME3** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME4** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME5** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME7** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME8** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME9** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME10** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME11** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME12** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME13** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME14** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME15** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME16** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME17** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME18** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME19** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME20** | ****|  | [optional]
 **UNKNOWN_PARAMETER_NAME21** | ****|  | [optional]

### Return type

[**[SearchResponse]**](SearchResponse.md)

### Authorization

[bearer-token](../README.md#bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**403** | Forbidden |  -  |
**200** | Successfully retrieved list |  -  |
**400** | Incorrect request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

