from typing import List, Dict, Any, cast
import pandas
import geopandas


def _df_to_gdf(
    df: pandas.DataFrame, geometry_column: str = "footprint"
) -> geopandas.GeoDataFrame:
    assert geometry_column in list(
        df.columns.values
    ), f"{geometry_column} was not in {list(df.columns.values)}"
    gs = geopandas.GeoSeries.from_wkt(df[geometry_column], crs=4326)
    return geopandas.GeoDataFrame(df, geometry=gs)


def json_response_to_df(jss: List[Dict[str, Any]]) -> pandas.DataFrame:
    df = pandas.DataFrame(jss)
    return pandas.json_normalize(cast(dict, df.to_dict(orient="records")))


def json_response_to_gdf(jss: List[Dict[str, Any]]) -> geopandas.GeoDataFrame:
    df = json_response_to_df(jss)
    return _df_to_gdf(df)
