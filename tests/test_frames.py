import datetime
from dateutil.tz import tzutc
from py4envi import frames

JS = [{'artifacts': ['metadata',
                     'thumbnail',
                     'manifest',
                     'checksum',
                     'RGBs_8b',
                     'RGB_16b',
                     'quicklook',
                     'product_archive'],
       'footprint': 'POLYGON((16.77772 56.37068,16.71851 56.27917,16.62692 '
       '56.13675,16.53603 55.99426,16.446 55.85179,16.44303 '
       '55.84704,14.99968 55.85732,14.99967 56.84381,16.79911 '
       '56.83085,16.77772 56.37068))',
       'has_zip_artifact': True,
       'id': 6688998,
       'metadata_content': {'cloud_cover': 35.414091,
                            'format': 'COG',
                            'ingestion_time': datetime.datetime(2021, 4, 1, 14, 19, 13, tzinfo=tzutc()),
                            'polygon': '56.37068419214287,16.777722126970083 '
                            '56.279167284412935,16.71850672209719 '
                            '56.13674903301303,16.626918104956353 '
                            '55.99426050153304,16.536029448240836 '
                            '55.85178747844496,16.446004914773514 '
                            '55.847040421390425,16.443029870128687 '
                            '55.85732112564965,14.999680497860194 '
                            '56.84381181769674,14.999672142640447 '
                            '56.8308490729103,16.79910585152769 '
                            '56.37068419214287,16.777722126970083',
                            'processing_level': 'Level-2A',
                            'relative_orbit_number': '065',
                            'schema': 'Sentinel-2.metadata.v1.json',
                            'sensing_time': datetime.datetime(2021, 4, 1, 10, 15, 59, 24000, tzinfo=tzutc()),
                            'spacecraft': 'Sentinel-2B',
                            'tile': 'T33VWC'},
       'product_id': 5,
       'scene_key': 'Sentinel-2/2021-04-01/S2B_MSIL2A_20210401T101559_N0300_R065_T33VWC_20210401T141913.scene',
       'timestamp': datetime.datetime(2021, 4, 1, 10, 15, 59, 24000, tzinfo=tzutc())}]


def test_json_response_to_df():
    df = frames.json_response_to_df(JS)
    assert list(
        df.columns.values) == [
        'artifacts',
        'footprint',
        'has_zip_artifact',
        'id',
        'product_id',
        'scene_key',
        'timestamp',
        'metadata_content.cloud_cover',
        'metadata_content.format',
        'metadata_content.ingestion_time',
        'metadata_content.polygon',
        'metadata_content.processing_level',
        'metadata_content.relative_orbit_number',
        'metadata_content.schema',
        'metadata_content.sensing_time',
        'metadata_content.spacecraft',
        'metadata_content.tile']
    assert df.shape == (1, 17)


def test_json_response_to_gdf():
    gdf = frames.json_response_to_gdf(JS)
    print(gdf.columns.values)
    assert list(
        gdf.columns.values) == [
        'artifacts',
        'footprint',
        'has_zip_artifact',
        'id',
        'product_id',
        'scene_key',
        'timestamp',
        'metadata_content.cloud_cover',
        'metadata_content.format',
        'metadata_content.ingestion_time',
        'metadata_content.polygon',
        'metadata_content.processing_level',
        'metadata_content.relative_orbit_number',
        'metadata_content.schema',
        'metadata_content.sensing_time',
        'metadata_content.spacecraft',
        'metadata_content.tile',
        'geometry']
    assert gdf.shape == (1, 18)
