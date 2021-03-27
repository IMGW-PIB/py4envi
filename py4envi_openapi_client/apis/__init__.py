
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.auth_api import AuthApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from py4envi_openapi_client.api.auth_api import AuthApi
from py4envi_openapi_client.api.product_api import ProductApi
from py4envi_openapi_client.api.scene_api import SceneApi
from py4envi_openapi_client.api.search_api import SearchApi
