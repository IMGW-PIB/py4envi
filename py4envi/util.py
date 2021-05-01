import logging
import os
import requests
import inspect
from pathlib import Path
from typing import Dict, Optional, Union, Any, List
from urllib.parse import urlparse
import pandas
import geopandas
from tqdm import tqdm

logger = logging.getLogger(__name__)


def print_df(
    x: Union[pandas.DataFrame, geopandas.GeoDataFrame],
    width: int = 2000,
    json: bool = True,
):
    if isinstance(x, geopandas.GeoDataFrame):
        x = pandas.DataFrame(x)
    if json:
        print(x.to_json(orient="records", default_handler=str))
        return
    try:
        pandas.set_option("display.max_rows", None)
        pandas.set_option("display.max_columns", None)
        pandas.set_option("display.width", width)
        pandas.set_option("display.float_format", "{:20,.2f}".format)
        pandas.set_option("display.max_colwidth", None)
        print(x)
    except Exception:
        pandas.reset_option("display.max_rows")
        pandas.reset_option("display.max_columns")
        pandas.reset_option("display.width")
        pandas.reset_option("display.float_format")
        pandas.reset_option("display.max_colwidth")
        logger.error("error while printing dataframe", exc_info=True)


def nonempty_dict(d: dict) -> bool:
    return bool(d)


def get_union_positional_type(u: Union[Any], index: int = 0) -> Any:
    return u.__args__[index]


def extract_optional_args_with_types(
    fun: Any,
    exclude: List[str] = [
        "return",
        "footprint",
        "ingestion_from",
        "ingestion_to",
        "sensing_from",
        "sensing_to",
    ],
) -> Dict[str, Any]:
    spec = inspect.getfullargspec(fun)
    res = {}
    for k, v in spec.annotations.items():
        if k not in exclude:
            s = str(v)
            # filter to only optional args that are optional
            if "Union" in s and "NoneType" in s and len(v.__args__) == 2:
                t = get_union_positional_type(v, index=0)
                res[k] = t
    return res


def filename_from_url(url: str) -> str:
    pr = urlparse(url)
    return os.path.basename(pr.path)


def filesize(f: Path) -> Optional[int]:
    if f.exists():
        return f.stat().st_size
    return None


def download(
    url: str, dest_folder: os.PathLike, chunk_size: int = 1024, overwrite: bool = False
) -> os.PathLike:
    """
    Downloads a file from url to the specified directory.
    Directory will be created if does not exist.
    Download will be resumed if file parts are found.
    Overwrite can be specified to start download from scratch if anything was downloaded before.
    """
    dest_folder = Path(dest_folder)

    def resume_headers(start_bytes: int) -> Dict[str, str]:
        return {"Range": f"bytes={start_bytes}-"}

    filename = filename_from_url(url)
    filepath = dest_folder.joinpath(filename)
    dest_folder.mkdir(parents=True, exist_ok=True)
    if overwrite and filepath.exists():
        filepath.unlink()

    # if file exists, continue download
    current_size = filesize(filepath)
    if current_size is not None:
        r = requests.get(url, stream=True, headers=resume_headers(current_size))
        mode = "ab"
    else:
        r = requests.get(url, stream=True)
        mode = "wb"

    # now save chunk by chunk and show progress
    # below dict is case insensitive, no need to check case
    total_size = int(r.headers.get("Content-Length", "1")) + (current_size or 0)
    with tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        desc=str(filepath),
        initial=current_size or 0,
        ascii=True,
    ) as progress:
        with open(filepath, mode) as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))
    return filepath
