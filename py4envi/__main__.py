import os
import sys
import logging
import atexit
from . import token, products, scenes


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "debug").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def cleanup():
    """Cleans up data after the application
    """
    logging.info("cleaning stuff up")


def run() -> int:
    atexit.register(cleanup)
    email, pwd = token.read_netrc_for_url("dane.sat4envi.imgw.pl") or ("", "")
    tkn = token.get_or_request_token(email, pwd)
    print(f'token is: {tkn}')
    prds = products.get_products(tkn)
    print('proucts:')
    print(prds)
    scene = scenes.get_scene_artifact(tkn, 6675430, "product_archive")
    print("scene")
    print(scene)
    return 0


if __name__ == "__main__":
    configure_logging()
    exitcode = run()
    sys.exit(exitcode)
