import tempfile
from unittest.mock import patch, Mock
from py4envi import util

URL = "https://sat4envi-data.s3.cloud.cyfronet.pl/Sentinel-2/2021-03-29/S2B_MSIL2A_20210329T100609_N0214_R022_T34VCH_20210329T135553.SAFE.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210330T090254Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=BU23B2BK6MX2O6C46KNB%2F20210330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=e2e93374e437b183b56328f4457c7f2cf4a85b68eb7eacb18810545f925080cd"


def test_filename_from_url():
    assert (
        util.filename_from_url(URL)
        == "S2B_MSIL2A_20210329T100609_N0214_R022_T34VCH_20210329T135553.SAFE.zip"
    )


def test_download():
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
            path = util.download("http://fake.pl/file.zip", dir)

            assert str(path).endswith("file.zip")
            with open(path, "rb") as f:
                read_bts = f.read()
                assert len(read_bts) == len(bts)
                assert read_bts == bts
