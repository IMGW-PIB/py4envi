from typing import Callable
import datetime
from py4envi import search
from py4envi_openapi_client.apis import SearchApi
from py4envi_openapi_client.models import SearchResponse
from py4envi_openapi_client import ApiClient


def _gen_mocked_search_api() -> Callable[[ApiClient], SearchApi]:
    class MockedSearchApi(SearchApi):
        def __init__(self):
            # initialize super to later overwrite
            super().__init__()

            def f1(**kwargs):
                sr = SearchResponse(
                    footprint="POLYGON ((17.92599678039551 51.42511600068021, 17.94530868530273 51.42153011340418, 17.9322624206543 51.43180533674875, 17.92170524597168 51.4291832337135, 17.92599678039551 51.42511600068021))",
                )
                return [sr]

            def f2(**kwargs):
                return 1

            self.get_scenes = f1
            self.get_count = f2

    return lambda _: MockedSearchApi()


def test_geojson_to_wkt():
    gjs = {
        "type": "Polygon",
        "coordinates": [
            [
                [17.925996780395508, 51.42511600068021],
                [17.945308685302734, 51.42153011340418],
                [17.932262420654297, 51.43180533674875],
                [17.92170524597168, 51.4291832337135],
                [17.925996780395508, 51.42511600068021],
            ]
        ],
    }
    assert search._geojson_to_wkt(gjs).startswith("POLYGON")


def test_clean_api_arguments():
    test_args1 = {
        "method": "get_count",
        "token": "fake token",
        "product_type": "Sentinel-2-L2A",
        "search_api_fun": lambda x: x,
        "sensing_from": None,
        "sensing_to": None,
        "ingestion_from": None,
        "ingestion_to": None,
        "satellite_platform": None,
        "processing_level": None,
        "polarisation": None,
        "sensor_mode": None,
        "relative_orbit_number": None,
        "absolute_orbit_number": None,
        "collection": None,
        "timeliness": None,
        "instrument": None,
        "footprint": {
            "type": "Polygon",
            "coordinates": [
                [
                    [17.925996780395508, 51.42511600068021],
                    [17.945308685302734, 51.42153011340418],
                    [17.932262420654297, 51.43180533674875],
                    [17.92170524597168, 51.4291832337135],
                    [17.925996780395508, 51.42511600068021],
                ]
            ],
        },
        "product_level": None,
        "cloud_cover": 30.1,
        "sort_by": None,
        "order": None,
        "limit": None,
        "offset": None,
    }
    test_cleaned1 = {
        "product_type": "Sentinel-2-L2A",
        "footprint": "POLYGON ((17.92599678039551 51.42511600068021, 17.94530868530273 51.42153011340418, 17.9322624206543 51.43180533674875, 17.92170524597168 51.4291832337135, 17.92599678039551 51.42511600068021))",
        "cloud_cover": "30.1",
    }
    test_args2 = {
        "method": "get_scenes",
        "token": "fake token",
        "product_type": "Sentinel-2-L2A",
        "search_api_fun": lambda x: x,
        "sensing_from": None,
        "sensing_to": None,
        "ingestion_from": datetime.datetime(2021, 1, 30, 19, 28, 47, 290676),
        "ingestion_to": None,
        "satellite_platform": None,
        "processing_level": None,
        "polarisation": None,
        "sensor_mode": None,
        "relative_orbit_number": None,
        "absolute_orbit_number": None,
        "collection": None,
        "timeliness": None,
        "instrument": None,
        "footprint": None,
        "product_level": None,
        "cloud_cover": None,
        "sort_by": None,
        "order": None,
        "limit": 5,
        "offset": None,
    }
    test_cleaned2 = {
        "product_type": "Sentinel-2-L2A",
        "ingestion_from": "2021-01-30T19:28:47.290676Z",
        "limit": "5",
    }

    assert search._clean_api_arguments(test_args1) == test_cleaned1
    assert search._clean_api_arguments(test_args2) == test_cleaned2


def test_count_artifacts():
    count = search.count_artifacts(
        "fake token", "fake product", search_api_fun=_gen_mocked_search_api()
    )
    assert count == 1


def test_search_artifacts():
    arts = search.search_artifacts(
        "fake token", "fake product", search_api_fun=_gen_mocked_search_api()
    )
    assert list(arts.columns.values) == ["footprint", "geometry"]
    assert arts.shape == (1, 2)
