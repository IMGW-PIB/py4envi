import sys
from py4envi import cli


def main() -> int:
    cli.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
