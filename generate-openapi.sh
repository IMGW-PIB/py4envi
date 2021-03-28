#!/bin/bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/sat4envi_fixed_spec.json \
    -g python \
    -o /local/openapi_out
