# openapi_client.SceneApi

All URIs are relative to *https://dane.sat4envi.imgw.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_download_link**](SceneApi.md#generate_download_link) | **GET** /api/v1/scenes/{id}/download/{artifactName} | Redirect to a presigned download url for a scene&#39;s artifact


# **generate_download_link**
> generate_download_link(id, artifact_name)

Redirect to a presigned download url for a scene's artifact

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import openapi_client
from openapi_client.api import scene_api
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
    api_instance = scene_api.SceneApi(api_client)
    id = 1 # int | 
    artifact_name = "artifactName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Redirect to a presigned download url for a scene's artifact
        api_instance.generate_download_link(id, artifact_name)
    except openapi_client.ApiException as e:
        print("Exception when calling SceneApi->generate_download_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **artifact_name** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearer-token](../README.md#bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**404** | Scene or artifact not found |  -  |
**303** | Redirect to the presigned download url |  * Location - The presigned download url <br>  |
**401** | Unauthenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

