# Py4Envi

Py4Envi is a python library developed at IMGW-PIB that allows for easy and efficient programatic access to sat4envi resources.
https://dane.sat4envi.imgw.pl/

Tested for Python >= 3.7.

It also provides a simple CLI tool to explore and obtain those resources without writing code.

See below for examples on both use-cases.

- [top](#py4envi)
- [installation](#installation)
- [CLI](#exemplary-usage-cli)
- [code](#exemplary-usage-code)

## Installation

For now only installation from the source code is available:

```bash
$ python -m pip install .
```

## Docs

See [OpenAPI docs](openapi_docs/README.md) folder for openapi specification.

## Authentication

The tool supports `.netrc` file for automatically reading credentials if you want.
It's contents should look like this:

```
machine dane.sat4envi.imgw.pl
login email@email.com
password some-fake-password
```

Otherwise you can just provide email and password (or just token) directly. See examples below.

## Exemplary usage (cli)

The most important thing about CLI is... help ;) show it by executing `-h` and any level of the tool (any subcommand etc.).

It is always available and varies for different levels of this tool.
Be sure to check it very often and investigate available arguments and their order (order is important here and can be a little tricky so be sure to double check it in the help).

`jq` tool is highly recommended to parse large json responses.

```bash
# you can omit specifying email and password
# they will be read from netrc automatically
# you can also specify email and pwd explicitly for every command listed below like so:
$ py4envi -e example@example.com -p "fake password" <other arguments>

# obtained token is cached as a temporary file
# if for some reason token gets out-of-date but your temp files were not cleaned
# you can force getting a new token as below
$ py4envi -e example@example.com -p "fake password" --new-token <other arguments>

# let's query API for all available products
# this returns a dataframe
$ py4envi products
# a convinience param is avaiable to return json, this can be later piped to for example `jq` and used in scripts:
$ py4envi --json products
# this is also a good example of how important is the ordering of arguments. `--json` provided at the very end won't work!

# count a number of specific artifacts of a product in the specified geometry (geojson file)
# filtered by cloud cover (there are many parameters to pass here, see help or OpenAPI docs)
$ py4envi search --product-type Sentinel-2-L2A --footprint ./tests/geojson.json --cloud-cover 30.1 --count
# omit `---count` to return all results (again, dataframe or json, depending on the flag)
$ py4envi --json search --product-type Sentinel-2-L2A --footprint ./tests/geojson.json --cloud-cover 30.1

# download a specific artifact knowing its name and id
$ py4envi -n product_archive artifact -i 6675430
# specify different directory
$ py4envi download -n product_archive -d /tmp artifact -i 6675430

# one can also execute download on 'ith' result of search
# the same arguments as for search are available, but again, check the help
# here we explicitly download the first result (this is also the default)
$ py4envi download -n quicklook search --product-type Sentinel-2-L2A --cloud-cover 30.1

# interrupted download can be resumed by just calling the same command once more
# if you with to overwrite the previous download, just pass `--overwrite` flag (see help)
```

## Exemplary usage (code)

```python
from py4envi import products, scenes, search, token

# you can omit specifying email and password (don't pass them to functions or set them as None)
# they will be read from netrc automatically
# you can also specify email and pwd explicitly
email = "example@example.com"
pwd = "fake password"

# request token to use during this session
tkn = token.get_or_request_token(email, pwd)
# token is cached as a temporary file
# if for some reason token gets out-of-date but your temp files were not cleaned
# you can force getting a new token as below
#tkn = token.get_or_request_token(email, pwd, force=True)

# let's query API for all available products
# this returns a dataframe
prds = products.get_products(tkn)
print("products:")
print(prds)

# let's define some geometry (geoJSON) to work with
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

# count a number of specific artifacts of a product in the specified geometry
# filtered by cloud cover (there are many parameters to pass here, see function definition or OpenAPI docs)
# return value is an integer
count = search.count_artifacts(
    tkn, "Sentinel-2-L2A", cloud_cover=30.1, footprint=gjs
)
print("count:")
print(count)

# search for specific artifacts that satisfy other predicates
# and limit the number of results to 5
# this returns a geodataframe
srch = search.search_artifacts(
    tkn,
    "Sentinel-2-L2A",
    limit=5,
    ingestion_from=datetime.now() - timedelta(days=60),
)
print("search results:")
print(srch)

# get a specific artifact knowing its id and name
# this returns a scene artifact class
scene = scenes.get_scene_artifact(tkn, 6675430, "product_archive")
print("scene")
print(scene)

# now we can download that scene artifact to the current directory
# this method returns the path to the downloaded file
downloaded = scenes.download_scene_artifact(scene, Path("."))
print(downloaded)

# interrupted download can be resumed by just calling the same function once more
# if you with to overwrite the previous download, just pass 'overwrite' flag
_ = scenes.download_scene_artifact(scene, Path("."), overwrite=True)

```

## Misc

- `sat4envi_fixed_spec.json` contains modifies OpenAPI schema that includes datatypes for `search` endpoint

