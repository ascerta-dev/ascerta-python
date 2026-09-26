# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ascerta import Ascerta, AsyncAscerta

from ascerta.types.shared import PropertiesResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from ascerta import Ascerta, AsyncAscerta
from tests.utils import assert_matches_type
from ascerta.types.requests.request_id import property_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: Ascerta) -> None:
        property = client.requests.request_id.properties.update(
            request_id="request_id",
            properties={
                "foo": "string"
            },
        )
        assert_matches_type(PropertiesResponse, property, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Ascerta) -> None:

        response = client.requests.request_id.properties.with_raw_response.update(
            request_id="request_id",
            properties={
                "foo": "string"
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        property = response.parse()
        assert_matches_type(PropertiesResponse, property, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Ascerta) -> None:
        with client.requests.request_id.properties.with_streaming_response.update(
            request_id="request_id",
            properties={
                "foo": "string"
            },
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            property = response.parse()
            assert_matches_type(PropertiesResponse, property, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Ascerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
          client.requests.request_id.properties.with_raw_response.update(
              request_id="",
              properties={
                  "foo": "string"
              },
          )
class TestAsyncProperties:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @parametrize
    async def test_method_update(self, async_client: AsyncAscerta) -> None:
        property = await async_client.requests.request_id.properties.update(
            request_id="request_id",
            properties={
                "foo": "string"
            },
        )
        assert_matches_type(PropertiesResponse, property, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAscerta) -> None:

        response = await async_client.requests.request_id.properties.with_raw_response.update(
            request_id="request_id",
            properties={
                "foo": "string"
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        property = await response.parse()
        assert_matches_type(PropertiesResponse, property, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAscerta) -> None:
        async with async_client.requests.request_id.properties.with_streaming_response.update(
            request_id="request_id",
            properties={
                "foo": "string"
            },
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            property = await response.parse()
            assert_matches_type(PropertiesResponse, property, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncAscerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
          await async_client.requests.request_id.properties.with_raw_response.update(
              request_id="",
              properties={
                  "foo": "string"
              },
          )