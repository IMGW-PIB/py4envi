import os
import sys
import logging
from py4envi import cli


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "debug").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def main() -> int:
    configure_logging()
    cli.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
