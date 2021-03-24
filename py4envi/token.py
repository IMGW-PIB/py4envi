import time
from . import openapi_client
from .openapi_client.api import auth_api
from .openapi_client.model.token_response import TokenResponse
from .openapi_client.model.login_request import LoginRequest
from pprint import pprint

def get_new_token():
    # Configure Bearer authorization (JWT): bearer-token
    configuration = openapi_client.Configuration(
        access_token = 'YOUR_BEARER_TOKEN'
    )

    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        login_request = LoginRequest(
            email="email_example",
            password="password_example",
        ) # LoginRequest | 

        # example passing only required values which don't have defaults set
        try:
            # Get authorization token
            api_response = api_instance.token(login_request)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling AuthApi->token: %s\n" % e)
