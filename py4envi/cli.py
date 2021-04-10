import os
import json
import dateutil.parser
import logging
import sys
import argparse
from typing import Dict, Any, cast
from pathlib import Path
import py4envi
from py4envi import products, search, token, util, scenes


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "error").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def _products_subparser(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    """
    adds products subparser
    """
    p = subparsers.add_parser("products", help="lists available products")
    return p


def _search_args_parser_init(parser: argparse.ArgumentParser):
    """
    initializes given parser with all search-related arguments
    """
    search_args = parser.add_argument_group("search arguments")
    search_args.add_argument(
        "--product-type",
        type=str,
        default=None,
        required=True,
        help="product type to query REQUIRED",
    )
    # add specific optionals here
    search_args.add_argument(
        "--footprint",
        type=str,
        default=None,
        help="local path to geojson file (1 feature) to use as spatial selection",
    )

    search_args.add_argument(
        "--sensing-from",
        type=str,
        default=None,
        help="start time of sensing ISO-8601",
    )

    search_args.add_argument(
        "--sensing-to",
        type=str,
        default=None,
        help="end time of sensing ISO-8601",
    )

    search_args.add_argument(
        "--ingestion-from",
        type=str,
        default=None,
        help="start time of ingestion ISO-8601",
    )

    search_args.add_argument(
        "--ingestion-to",
        type=str,
        default=None,
        help="end time of ingestion ISO-8601",
    )

    # add generic optionals in a loop
    # function does not make a difference, args are the same
    optionals = util.extract_optional_args_with_types(search.count_artifacts)
    for n, t in optionals.items():
        search_args.add_argument(
            f"--{n.replace('_','-')}",
            type=t,
            default=None,
            help=f"openapi parameter: {n}",
        )


def _search_subparser(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    """
    add search subparser
    """
    p = subparsers.add_parser("search", help="searches available products")

    # add all search params
    _search_args_parser_init(p)

    p.add_argument(
        "--count", action="store_true", help="returns a count of found artifacts"
    )

    return p


def _download_subparser(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    """
    add download subparser
    """
    p = subparsers.add_parser(
        "download", help="downloads specified or searched artifacts"
    )

    dp = p.add_argument_group("download arguments")
    dp.add_argument(
        "-n", "--name", type=str, required=True, help="artifact name to download"
    )
    dp.add_argument(
        "-d",
        "--directory",
        type=str,
        default="./",
        help="download folder (default: %(default)s)",
    )
    dp.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite the downloaded file if it already exists",
    )

    dsp = p.add_subparsers(
        help="specify download type", dest="download_type", required=True
    )

    # ARTIFACT
    scp_main = dsp.add_parser("artifact", help="downloads specific scene artifact")
    scp = scp_main.add_argument_group("artifact parameters")
    scp.add_argument(
        "-i", "--id", type=int, required=True, help="artifact id to download"
    )

    # SEARCH
    sep = dsp.add_parser("search", help="downloads searched artifacts")
    # add all search params
    _search_args_parser_init(sep)

    sep.add_argument(
        "-i",
        "--index",
        type=int,
        default=1,
        help=(
            "downloads the 'ith' entry in the returned data (default: %(default)s)\n"
            "use search arguments to sort and filter and get the correct results"
        ),
    )

    return p


def _main_parser() -> argparse.ArgumentParser:
    """
    main application parser
    """
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # misc
    p.add_argument(
        "--version", action="store_true", help="shows current library version"
    )

    p.add_argument(
        "-w",
        "--width",
        type=int,
        default=2000,
        help=(
            "max width of the printed dataframe (default: %(default)s)\n"
            "applicable to 'search' and 'products' only"
        ),
    )

    p.add_argument(
        "--json",
        action="store_true",
        help=(
            "prints json instead of dataframes\n"
            "applicable to 'search' and 'products' only"
        ),
    )

    # creds
    auth = p.add_argument_group("authentication")
    auth.add_argument(
        "-e",
        "--email",
        type=str,
        default=None,
        help="email to use to get access token (default: %(default)s)",
    )
    auth.add_argument(
        "-p",
        "--password",
        type=str,
        default=None,
        help="password to use to get access token (default: %(default)s)",
    )
    auth.add_argument(
        "--new-token", action="store_true", help="forces query for a new token"
    )

    # actions
    subparsers = p.add_subparsers(help="specify a command", dest="command")
    _ = _products_subparser(subparsers)
    _ = _search_subparser(subparsers)
    _ = _download_subparser(subparsers)

    return p


def _version() -> str:
    """Gets current version of the library"""
    return py4envi.__version__


def cmd_products(ns: argparse.Namespace, tkn: str):
    df = products.get_products(tkn)
    util.print_df(df, width=ns.width, json=ns.json)


def __validate_and_clean_search_kwargs(args: Dict[str, Any]) -> Dict[str, Any]:
    ret = {}
    optionals = list(
        util.extract_optional_args_with_types(search.count_artifacts).keys()
    )
    for k, v in args.items():
        if k == "footprint" and v is not None:
            gjs_file = Path(v)
            assert gjs_file.exists(), "passed geojson file has to exist"
            with open(gjs_file) as f:
                ret[k] = json.load(f)
        elif k == "sensing_from" and v is not None:
            ret[k] = dateutil.parser.parse(v)
        elif k == "sensing_to" and v is not None:
            ret[k] = dateutil.parser.parse(v)
        elif k == "ingestion_from" and v is not None:
            ret[k] = dateutil.parser.parse(v)
        elif k == "ingestion_to" and v is not None:
            ret[k] = dateutil.parser.parse(v)
        elif k in optionals:
            ret[k] = v
    return ret


def cmd_search(ns: argparse.Namespace, tkn: str):
    kwargs = __validate_and_clean_search_kwargs(ns.__dict__)

    if ns.count:
        print(search.count_artifacts(tkn, ns.product_type, **kwargs))
    else:
        df = search.search_artifacts(tkn, ns.product_type, **kwargs)
        util.print_df(df, width=ns.width, json=ns.json)


def cmd_download(ns: argparse.Namespace, tkn: str):
    if ns.download_type == "artifact":
        sa = scenes.get_scene_artifact(tkn, ns.id, ns.name)
        if not sa:
            print("specified artifact does not exist")
            return
        print(scenes.download_scene_artifact(sa, ns.directory, ns.overwrite))
    elif ns.download_type == "search":
        kwargs = __validate_and_clean_search_kwargs(ns.__dict__)
        kwargs["limit"] = ns.index

        df = search.search_artifacts(tkn, ns.product_type, **kwargs)
        if df.empty:
            print("empty search results")
            return

        artifact_name = ns.name
        artifacts = df["artifacts"][ns.index - 1]
        assert (
            artifact_name in artifacts
        ), f"requested artifact name is not in the available ones: {artifacts}"
        id = int(cast(int, df["id"][ns.index - 1]))  # pandas int to python int
        sa = scenes.get_scene_artifact(tkn, id, artifact_name)
        if not sa:
            print("specified artifact does not exist")
            return
        print(scenes.download_scene_artifact(sa, ns.directory, ns.overwrite))
    else:
        print("no download type specified")


def run():
    configure_logging()
    if sys.version_info < (3, 6, 0):
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit(1)

    parser = _main_parser()
    namespace = parser.parse_args()
    lazy_token = lambda: token.get_or_request_token(
        namespace.email, namespace.password, force=namespace.new_token
    )
    if namespace.version:
        print(_version())
    elif namespace.command == "products":
        cmd_products(namespace, lazy_token())
    elif namespace.command == "search":
        cmd_search(namespace, lazy_token())
    elif namespace.command == "download":
        cmd_download(namespace, lazy_token())
    else:
        parser.print_help()
