import os
import geojson
import dateutil.parser
import logging
import sys
import argparse
from typing import Dict,Any
from pathlib import Path
import py4envi
from py4envi import products, search, token, util


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "error").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def _products_parser(subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    p = subparsers.add_parser("products", help="lists available products")
    return p


def _search_parser(subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    p = subparsers.add_parser("search", help="searches available products")

    p.add_argument(
        "--count", action="store_true", help="returns just a count of found artifacts"
    )

    p.add_argument(
        "--product-type",
        type=str,
        default=None,
        required=True,
        help="product type to query",
    )
    # add specific optionals here
    p.add_argument(
        "--footprint",
        type=str,
        default=None,
        help="local path to geojson file (1 feature) to use as spatial selection",
    )

    p.add_argument(
        "--sensing-from",
        type=str,
        default=None,
        help="start time of sensing ISO-8601",
    )

    p.add_argument(
        "--sensing-to",
        type=str,
        default=None,
        help="end time of sensing ISO-8601",
    )

    p.add_argument(
        "--ingestion-from",
        type=str,
        default=None,
        help="start time of ingestion ISO-8601",
    )

    p.add_argument(
        "--ingestion-to",
        type=str,
        default=None,
        help="end time of ingestion ISO-8601",
    )

    # add generic optionals in a loop
    # function does not make a difference, args are the same
    optionals = util.extract_optional_args_with_types(search.count_artifacts)
    for n, t in optionals.items():
        p.add_argument(
            f"--{n.replace('_','-')}",
            type=t,
            default=None,
            help=f"openapi parameter: {n}",
        )

    return p


def _main_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # misc
    p.add_argument(
        "--version", action="store_true", help="shows current library version"
    )

    p.add_argument(
        "--force-new-token", action="store_true", help="forces query for a new token"
    )

    p.add_argument(
        "-w",
        "--width",
        type=int,
        default=2000,
        help="max width of the printed dataframe (default: %(default)s)",
    )

    p.add_argument(
        "--json", action="store_true", help="prints json instead of dataframes"
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
    subparsers = p.add_subparsers(help="specify a command", dest="command")
    _ = _products_parser(subparsers)
    _ = _search_parser(subparsers)

    return p


def _version() -> str:
    """Gets current version of the library"""
    return py4envi.__version__


def cmd_products(ns: argparse.Namespace, tkn: str):
    df = products.get_products(tkn)
    util.print_df(df, width=ns.width, json=ns.json)


def cmd_search(ns: argparse.Namespace, tkn: str):
    # TODO additional flag to download
    def validate_and_clean_kwargs(args: Dict[str,Any])->Dict[str,Any]:
        ret = {}
        optionals = list(util.extract_optional_args_with_types(search.count_artifacts).keys())
        for k,v in args.items():
            if k == 'footprint' and v is not None:
                gjs_file = Path(v)
                assert gjs_file.exists(), "passed geojson file has to exist"
                with open(gjs_file) as f:
                    ret[k] = geojson.load(f)
            elif k == 'sensing_from' and v is not None:
                ret[k] = dateutil.parser.parse(v)
            elif k == 'sensing_to' and v is not None:
                ret[k] = dateutil.parser.parse(v)
            elif k == 'ingestion_from' and v is not None:
                ret[k] = dateutil.parser.parse(v)
            elif k== 'ingestion_to' and v is not None:
                ret[k] = dateutil.parser.parse(v)
            elif k in optionals:
                ret[k] = v
        return ret

    kwargs = validate_and_clean_kwargs(ns.__dict__)

    if ns.count:
        print(search.count_artifacts(tkn, ns.product_type, **kwargs))
    else:
        df = search.search_artifacts(tkn, ns.product_type, **kwargs)
        util.print_df(df, width=ns.width, json=ns.json)

def cmd_scene(ns:argparse.Namespace, tkn:str):
    # TODO
    # get and return as json
    # additional flag to download
    pass

def run():
    configure_logging()
    if sys.version_info < (3, 6, 0):
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit(1)

    parser = _main_parser()
    namespace = parser.parse_args()
    lazy_token = lambda: token.get_or_request_token(
        namespace.email, namespace.password, force=namespace.force_new_token
    )
    if namespace.version:
        print(_version())
    elif namespace.command == "products":
        cmd_products(namespace, lazy_token())
    elif namespace.command == "search":
        cmd_search(namespace, lazy_token())
    else:
        parser.print_help()
