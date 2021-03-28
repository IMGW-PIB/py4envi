# py4envi_py4envi_openapi_client.SearchApi

All URIs are relative to *https://dane.sat4envi.imgw.pl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_count**](SearchApi.md#get_count) | **GET** /api/v1/search/count | Get count of total scene results
[**get_scenes**](SearchApi.md#get_scenes) | **GET** /api/v1/search | Search for scenes


# **get_count**
> int get_count(product_type)

Get count of total scene results

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import py4envi_py4envi_openapi_client
from py4envi_py4envi_openapi_client.api import search_api
from pprint import pprint
# Defining the host is optional and defaults to https://dane.sat4envi.imgw.pl
# See configuration.py for a list of all supported configuration parameters.
configuration = py4envi_py4envi_openapi_client.Configuration(
    host = "https://dane.sat4envi.imgw.pl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-token
configuration = py4envi_py4envi_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with py4envi_py4envi_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    product_type = "productType_example" # str | 
    sensing_from = "sensingFrom_example" # str |  (optional)
    sensing_to = "sensingTo_example" # str |  (optional)
    ingestion_from = "ingestionFrom_example" # str |  (optional)
    ingestion_to = "ingestionTo_example" # str |  (optional)
    satellite_platform = "satellitePlatform_example" # str |  (optional)
    processing_level = "processingLevel_example" # str |  (optional)
    polarisation = "polarisation_example" # str |  (optional)
    sensor_mode = "sensorMode_example" # str |  (optional)
    relative_orbit_number = "relativeOrbitNumber_example" # str |  (optional)
    absolute_orbit_number = "absoluteOrbitNumber_example" # str |  (optional)
    collection = "collection_example" # str |  (optional)
    timeliness = "timeliness_example" # str |  (optional)
    instrument = "instrument_example" # str |  (optional)
    footprint = "footprint_example" # str |  (optional)
    product_level = "productLevel_example" # str |  (optional)
    cloud_cover = "cloudCover_example" # str |  (optional)
    sort_by = "sortBy_example" # str |  (optional)
    order = "order_example" # str |  (optional)
    limit = "limit_example" # str |  (optional)
    offset = "offset_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get count of total scene results
        api_response = api_instance.get_count(product_type)
        pprint(api_response)
    except py4envi_py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_count: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get count of total scene results
        api_response = api_instance.get_count(product_type, sensing_from=sensing_from, sensing_to=sensing_to, ingestion_from=ingestion_from, ingestion_to=ingestion_to, satellite_platform=satellite_platform, processing_level=processing_level, polarisation=polarisation, sensor_mode=sensor_mode, relative_orbit_number=relative_orbit_number, absolute_orbit_number=absolute_orbit_number, collection=collection, timeliness=timeliness, instrument=instrument, footprint=footprint, product_level=product_level, cloud_cover=cloud_cover, sort_by=sort_by, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except py4envi_py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | **str**|  |
 **sensing_from** | **str**|  | [optional]
 **sensing_to** | **str**|  | [optional]
 **ingestion_from** | **str**|  | [optional]
 **ingestion_to** | **str**|  | [optional]
 **satellite_platform** | **str**|  | [optional]
 **processing_level** | **str**|  | [optional]
 **polarisation** | **str**|  | [optional]
 **sensor_mode** | **str**|  | [optional]
 **relative_orbit_number** | **str**|  | [optional]
 **absolute_orbit_number** | **str**|  | [optional]
 **collection** | **str**|  | [optional]
 **timeliness** | **str**|  | [optional]
 **instrument** | **str**|  | [optional]
 **footprint** | **str**|  | [optional]
 **product_level** | **str**|  | [optional]
 **cloud_cover** | **str**|  | [optional]
 **sort_by** | **str**|  | [optional]
 **order** | **str**|  | [optional]
 **limit** | **str**|  | [optional]
 **offset** | **str**|  | [optional]

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
> [SearchResponse] get_scenes(product_type)

Search for scenes

### Example

* Bearer (JWT) Authentication (bearer-token):
```python
import time
import py4envi_py4envi_openapi_client
from py4envi_py4envi_openapi_client.api import search_api
from py4envi_py4envi_openapi_client.model.search_response import SearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://dane.sat4envi.imgw.pl
# See configuration.py for a list of all supported configuration parameters.
configuration = py4envi_py4envi_openapi_client.Configuration(
    host = "https://dane.sat4envi.imgw.pl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-token
configuration = py4envi_py4envi_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with py4envi_py4envi_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    product_type = "productType_example" # str | 
    sensing_from = "sensingFrom_example" # str |  (optional)
    sensing_to = "sensingTo_example" # str |  (optional)
    ingestion_from = "ingestionFrom_example" # str |  (optional)
    ingestion_to = "ingestionTo_example" # str |  (optional)
    satellite_platform = "satellitePlatform_example" # str |  (optional)
    processing_level = "processingLevel_example" # str |  (optional)
    polarisation = "polarisation_example" # str |  (optional)
    sensor_mode = "sensorMode_example" # str |  (optional)
    relative_orbit_number = "relativeOrbitNumber_example" # str |  (optional)
    absolute_orbit_number = "absoluteOrbitNumber_example" # str |  (optional)
    collection = "collection_example" # str |  (optional)
    timeliness = "timeliness_example" # str |  (optional)
    instrument = "instrument_example" # str |  (optional)
    footprint = "footprint_example" # str |  (optional)
    product_level = "productLevel_example" # str |  (optional)
    cloud_cover = "cloudCover_example" # str |  (optional)
    sort_by = "sortBy_example" # str |  (optional)
    order = "order_example" # str |  (optional)
    limit = "limit_example" # str |  (optional)
    offset = "offset_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for scenes
        api_response = api_instance.get_scenes(product_type)
        pprint(api_response)
    except py4envi_py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_scenes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for scenes
        api_response = api_instance.get_scenes(product_type, sensing_from=sensing_from, sensing_to=sensing_to, ingestion_from=ingestion_from, ingestion_to=ingestion_to, satellite_platform=satellite_platform, processing_level=processing_level, polarisation=polarisation, sensor_mode=sensor_mode, relative_orbit_number=relative_orbit_number, absolute_orbit_number=absolute_orbit_number, collection=collection, timeliness=timeliness, instrument=instrument, footprint=footprint, product_level=product_level, cloud_cover=cloud_cover, sort_by=sort_by, order=order, limit=limit, offset=offset)
        pprint(api_response)
    except py4envi_py4envi_openapi_client.ApiException as e:
        print("Exception when calling SearchApi->get_scenes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_type** | **str**|  |
 **sensing_from** | **str**|  | [optional]
 **sensing_to** | **str**|  | [optional]
 **ingestion_from** | **str**|  | [optional]
 **ingestion_to** | **str**|  | [optional]
 **satellite_platform** | **str**|  | [optional]
 **processing_level** | **str**|  | [optional]
 **polarisation** | **str**|  | [optional]
 **sensor_mode** | **str**|  | [optional]
 **relative_orbit_number** | **str**|  | [optional]
 **absolute_orbit_number** | **str**|  | [optional]
 **collection** | **str**|  | [optional]
 **timeliness** | **str**|  | [optional]
 **instrument** | **str**|  | [optional]
 **footprint** | **str**|  | [optional]
 **product_level** | **str**|  | [optional]
 **cloud_cover** | **str**|  | [optional]
 **sort_by** | **str**|  | [optional]
 **order** | **str**|  | [optional]
 **limit** | **str**|  | [optional]
 **offset** | **str**|  | [optional]

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

