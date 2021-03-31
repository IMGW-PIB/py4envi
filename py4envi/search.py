import logging
from typing import Callable, List, Optional, Dict, Union, Any, cast
import py4envi_openapi_client
from py4envi_openapi_client.apis import SearchApi
from py4envi_openapi_client.models import SearchResponse

logger = logging.getLogger(__name__)


def _clean_api_arguments(args: Dict[str, Any]) -> Dict[str, str]:
    """
    remove none values and non-api keywords, we cannot pass them, just omit
    also convert to str
    """
    not_passed = ['token', 'search_api_fun', 'method']
    kwargs = {}
    for k, v in args.items():
        if v is not None and k not in not_passed:
            kwargs[k] = str(v)
    return kwargs

# TODO fix types, custom classes etc


def _raw_api(
    method: str,
        token: str,
        product_type: str,
        search_api_fun: Callable[[py4envi_openapi_client.ApiClient], SearchApi],
        sensing_from: Optional[str] = None,
        sensing_to: Optional[str] = None,
        ingestion_from: Optional[str] = None,
        ingestion_to: Optional[str] = None,
        satellite_platform: Optional[str] = None,
        processing_level: Optional[str] = None,
        polarisation: Optional[str] = None,
        sensor_mode: Optional[str] = None,
        relative_orbit_number: Optional[str] = None,
        absolute_orbit_number: Optional[str] = None,
        collection: Optional[str] = None,
        timeliness: Optional[str] = None,
        instrument: Optional[str] = None,
        footprint: Optional[str] = None,
        product_level: Optional[str] = None,
        cloud_cover: Optional[int] = None,
        sort_by: Optional[str] = None,
        order: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
) -> Union[Optional[int], List[SearchResponse]]:
    """
    requests a count/list of all artifacts that conform to the specified keywords
    method must be in ['get_count', 'get_scenes']
    """
    kwargs = _clean_api_arguments(locals())

    logger.debug("%s on artifacts", method)
    configuration = py4envi_openapi_client.Configuration(
        access_token=token,
    )
    with py4envi_openapi_client.ApiClient(configuration) as api_client:
        api_instance = search_api_fun(api_client)

        try:
            func = getattr(api_instance, method)
            api_response = func(**kwargs)
            return api_response
        except py4envi_openapi_client.ApiException:
            logger.error("Exception when calling SearchApi->%s", method, exc_info=True)
        return None


def count_artifacts(
    token: str,
    product_type: str,
    sensing_from: Optional[str] = None,
    sensing_to: Optional[str] = None,
    ingestion_from: Optional[str] = None,
    ingestion_to: Optional[str] = None,
    satellite_platform: Optional[str] = None,
    processing_level: Optional[str] = None,
    polarisation: Optional[str] = None,
    sensor_mode: Optional[str] = None,
    relative_orbit_number: Optional[str] = None,
    absolute_orbit_number: Optional[str] = None,
    collection: Optional[str] = None,
    timeliness: Optional[str] = None,
    instrument: Optional[str] = None,
    footprint: Optional[str] = None,
    product_level: Optional[str] = None,
    cloud_cover: Optional[int] = None,
    sort_by: Optional[str] = None,
    order: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    search_api_fun: Callable[[py4envi_openapi_client.ApiClient], SearchApi] = lambda c: SearchApi(c),
) -> Optional[int]:
    """
    requests a count of all artifacts that conform to the specified keywords
    """
    ret = _raw_api(
        'get_count',
        token,
        product_type,
        search_api_fun=search_api_fun,
        sensing_from=sensing_from,
        sensing_to=sensing_to,
        ingestion_from=ingestion_from,
        ingestion_to=ingestion_to,
        satellite_platform=satellite_platform,
        processing_level=processing_level,
        polarisation=polarisation,
        sensor_mode=sensor_mode,
        relative_orbit_number=relative_orbit_number,
        absolute_orbit_number=absolute_orbit_number,
        collection=collection,
        timeliness=timeliness,
        instrument=instrument,
        footprint=footprint,
        product_level=product_level,
        cloud_cover=cloud_cover,
        sort_by=sort_by,
        order=order,
        limit=limit,
        offset=offset,
    )
    return cast(Optional[int], ret)


def search_artifacts(
    token: str,
    product_type: str,
    sensing_from: Optional[str] = None,
    sensing_to: Optional[str] = None,
    ingestion_from: Optional[str] = None,
    ingestion_to: Optional[str] = None,
    satellite_platform: Optional[str] = None,
    processing_level: Optional[str] = None,
    polarisation: Optional[str] = None,
    sensor_mode: Optional[str] = None,
    relative_orbit_number: Optional[str] = None,
    absolute_orbit_number: Optional[str] = None,
    collection: Optional[str] = None,
    timeliness: Optional[str] = None,
    instrument: Optional[str] = None,
    footprint: Optional[str] = None,
    product_level: Optional[str] = None,
    cloud_cover: Optional[int] = None,
    sort_by: Optional[str] = None,
    order: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    search_api_fun: Callable[[py4envi_openapi_client.ApiClient], SearchApi] = lambda c: SearchApi(c),
) -> List[SearchResponse]:
    """
    requests and returns a list of all artifacts that conform to the specified keywords
    """
    ret = _raw_api(
        'get_scenes',
        token,
        product_type,
        search_api_fun=search_api_fun,
        sensing_from=sensing_from,
        sensing_to=sensing_to,
        ingestion_from=ingestion_from,
        ingestion_to=ingestion_to,
        satellite_platform=satellite_platform,
        processing_level=processing_level,
        polarisation=polarisation,
        sensor_mode=sensor_mode,
        relative_orbit_number=relative_orbit_number,
        absolute_orbit_number=absolute_orbit_number,
        collection=collection,
        timeliness=timeliness,
        instrument=instrument,
        footprint=footprint,
        product_level=product_level,
        cloud_cover=cloud_cover,
        sort_by=sort_by,
        order=order,
        limit=limit,
        offset=offset,
    )
    return cast(List[SearchResponse], ret)
