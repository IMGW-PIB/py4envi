import sys
import argparse
import py4envi


def cli_args(p: argparse.ArgumentParser) -> argparse.Namespace:

    p.add_argument(
        "--version", action="store_true", help="shows current library version"
    )

    p.add_argument(
        "-v",
        "--verbosity",
        type=int,
        choices=[0, 1, 2],
        default=0,
        help="increase output verbosity (default: %(default)s)",
    )

    # creds
    p.add_argument(
        "-e",
        "--email",
        type=str,
        default=None,
        help="email to use to get access token (default: %(default)s)",
    )
    p.add_argument(
        "-p",
        "--password",
        type=str,
        default=None,
        help="password to use to get access token (default: %(default)s)",
    )

    # actions
    p.add_argument(
        "-a",
        "--action",
        type=str,
        default="list-products",
        choices=["list-products"],
        help="which action to perform (default: %(default)s)",
    )

    return p.parse_args()


def help():
    h = 'Try $python <script_name> "Hello" 123 --enable'
    print(h)


def version() -> str:
    """Gets current version of the library"""
    return py4envi.__version__


def run():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    if sys.version_info < (3, 6, 0):
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit(1)

    namespace = cli_args(parser)
    if namespace.version:
        print(version())
    else:
        parser.print_help()
