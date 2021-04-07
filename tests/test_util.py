from py4envi import util

URL = "https://sat4envi-data.s3.cloud.cyfronet.pl/Sentinel-2/2021-03-29/S2B_MSIL2A_20210329T100609_N0214_R022_T34VCH_20210329T135553.SAFE.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210330T090254Z&X-Amz-SignedHeaders=host&X-Amz-Expires=60&X-Amz-Credential=BU23B2BK6MX2O6C46KNB%2F20210330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=e2e93374e437b183b56328f4457c7f2cf4a85b68eb7eacb18810545f925080cd"


def test_filename_from_url():
    assert (
        util.filename_from_url(URL)
        == "S2B_MSIL2A_20210329T100609_N0214_R022_T34VCH_20210329T135553.SAFE.zip"
    )
