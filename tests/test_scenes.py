import tempfile
from unittest.mock import patch, Mock
from typing import Callable
from urllib3.response import HTTPResponse
from py4envi import scenes
from py4envi_openapi_client.apis import SceneApi
from py4envi_openapi_client import ApiClient

URL = "https://sat4envi-data.s3.cloud.cyfronet.pl/Sentinel-2/2021-03-29/S2B_MSIL2A_20210329T100609_N0214_R022_T34VCH_20210329T135553.SAFE.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210330T090254Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=BU23B2BK6MX2O6C46KNB%2F20210330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=e2e93374e437b183b56328f4457c7f2cf4a85b68eb7eacb18810545f925080cd"


def _gen_mocked_scene_api(status: int = 200) -> Callable[[ApiClient], SceneApi]:
    class MockedSceneApi(SceneApi):
        def __init__(self):
            # initialize super to later overwrite
            super().__init__()

            def f(id: int, artifact_name: str, **kwargs):
                r = HTTPResponse(status=status)
                r.geturl = lambda: URL
                return r

            self.generate_download_link = f

    return lambda _: MockedSceneApi()


def test_get_redirection():
    redirection = scenes._get_redirection(
        "fake token", 1, "some artifact", scene_api_fun=_gen_mocked_scene_api(200)
    )
    assert redirection.status == 200
    assert redirection.geturl().startswith("http")

    redirection = scenes._get_redirection(
        "fake token", 1, "some artifact", scene_api_fun=_gen_mocked_scene_api(404)
    )
    assert redirection.status == 404


def test_get_scene_artifact():
    scene = scenes.get_scene_artifact(
        "fake token", 1, "some artifact", scene_api_fun=_gen_mocked_scene_api(200)
    )
    assert scene is not None
    assert scene.id == 1
    assert scene.artifact_name == "some artifact"
    assert scene.download_link == URL
    assert (
        scene.file_name
        == "S2B_MSIL2A_20210329T100609_N0214_R022_T34VCH_20210329T135553.SAFE.zip"
    )

    scene = scenes.get_scene_artifact(
        "fake token", 1, "some artifact", scene_api_fun=_gen_mocked_scene_api(404)
    )
    assert scene is None


def test_download_scene_artifact():
    # download itself is already tested, so we test just basics
    sa = scenes.SceneArtifact(1, "test", "http://fake.pl/file.zip", "file.zip")
    bts = "abcd1234_%$#".encode()

    with tempfile.TemporaryDirectory() as dir:
        with patch("py4envi.util.requests.get") as mock_get:
            # Configure the mock to return a proper response
            mock_get.return_value.ok = True
            mock_get.return_value.iter_content = Mock(return_value=[bts])
            mock_get.return_value.headers = {
                "Content-Length": len(bts),
                "Content-Type": "application/zip",
            }

            # Call the service, which will send a request to the server.
            path = scenes.download_scene_artifact(sa, dir)
            assert str(path).endswith(sa.file_name)
