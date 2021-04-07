import os
import sys
import logging
import atexit
from datetime import datetime, timedelta
from . import token, products, scenes, search, util


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "debug").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def cleanup():
    """Cleans up data after the application"""
    logging.info("cleaning stuff up")


def run() -> int:
    atexit.register(cleanup)
    email, pwd = token.read_netrc_for_url("dane.sat4envi.imgw.pl") or ("", "")
    tkn = token.get_or_request_token(email, pwd, force=True)

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

    print(f"token is: {tkn}")
    prds = products.get_products(tkn)
    print("proucts:")
    print(prds)
    scene = scenes.get_scene_artifact(tkn, 6675430, "product_archive")
    print("scene")
    print(scene)
    
    from pathlib import Path
    print(util.download(scene.download_link, Path('.')))

    count = search.count_artifacts(
        tkn, "Sentinel-2-L2A", cloud_cover=30.1, footprint=gjs
    )
    print("count")
    print(count)
    srch = search.search_artifacts(
        tkn,
        "Sentinel-2-L2A",
        limit=5,
        ingestion_from=datetime.now() - timedelta(days=60),
    )
    print("srch")
    print(srch)
    print(list(srch.columns.values))

    return 0


if __name__ == "__main__":
    configure_logging()
    exitcode = run()
    sys.exit(exitcode)
