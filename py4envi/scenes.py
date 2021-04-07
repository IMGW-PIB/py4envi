from __future__ import annotations
import os
import logging
from dataclasses import dataclass
from typing import Callable, Optional
from urllib3.response import HTTPResponse
from py4envi import util
import py4envi_openapi_client
from py4envi_openapi_client.apis import SceneApi

logger = logging.getLogger(__name__)


@dataclass
class SceneArtifact:
    id: int
    artifact_name: str
    download_link: str
    file_name: str


def _get_redirection(
    token: str,
    id: int,
    artifact_name: str,
    scene_api_fun: Callable[[py4envi_openapi_client.ApiClient], SceneApi],
) -> Optional[HTTPResponse]:
    """
    returns a redirection to a download link for the specified artifact
    """
    logger.info("Requesting new api token")
    configuration = py4envi_openapi_client.Configuration(
        access_token=token,
    )
    with py4envi_openapi_client.ApiClient(configuration) as api_client:
        api_instance = scene_api_fun(api_client)
        try:
            api_response: HTTPResponse = api_instance.generate_download_link(
                id, artifact_name, _return_http_data_only=False, _preload_content=False
            )
            return api_response
        except py4envi_openapi_client.ApiException:
            logger.error(
                "Exception when calling ProductApi->get_products", exc_info=True
            )
        return None


def get_scene_artifact(
    token: str,
    id: int,
    artifact_name: str,
    scene_api_fun: Callable[
        [py4envi_openapi_client.ApiClient], SceneApi
    ] = lambda c: SceneApi(c),
) -> Optional[SceneArtifact]:
    """
    returns a scene artifact object containing id and artifact name (those requested) as well as
    filename and download link
    """
    response = _get_redirection(token, id, artifact_name, scene_api_fun)
    if response is None:
        logger.error("response was None")
        return None
    elif response.status == 200:
        url = response.geturl()
        return SceneArtifact(
            id,
            artifact_name,
            url,
            util.filename_from_url(url),
        )
    logger.error("response status was %d, not 200", response.status)
    return None


def download_scene_artifact(
    sa: SceneArtifact, dest_folder: os.PathLike, overwrite: bool = False
) -> os.PathLike:
    return util.download(sa.download_link, dest_folder, overwrite=overwrite)
