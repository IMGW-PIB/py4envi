import os
import sys
import logging
import atexit


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "info").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def cleanup():
    """Cleans up data after the application
    """
    logging.info("cleaning stuff up")


def run() -> int:
    atexit.register(cleanup)
    #email, pwd = token.read_netrc_for_url("dane.sat4envi.imgw.pl") or ("", "")
    #token.get_new_token(email, pwd)
    return 0


if __name__ == "__main__":
    configure_logging()
    exitcode = run()
    sys.exit(exitcode)
