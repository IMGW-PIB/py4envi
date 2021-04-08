# TODO

- cli tool

# Py4Envi

Py4Envi is a python library that allows for easy and efficient programatic access to sat4envi resources.
It also provides a simple CLI tool to explore and obtain those resources without writing code.

## Docs

See `openapi_docs` folder for openapi specification.

## Exemplary usage (cli)

```
# TODO
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
# if for some reason token gets out-of-date but your temp files were not clened
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
