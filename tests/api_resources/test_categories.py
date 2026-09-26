# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ascerta import Ascerta, AsyncAscerta

from ascerta.types import CategoryResponse, CategoryDeleteResponse, CategoryDeleteResourceResponse, CategoryResourceResponse

from ascerta.pagination import SyncCursorPage, AsyncCursorPage

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from ascerta import Ascerta, AsyncAscerta
from tests.utils import assert_matches_type
from ascerta.types import category_list_params
from ascerta.types import category_list_resources_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_list(self, client: Ascerta) -> None:
        category = client.categories.list()
        assert_matches_type(SyncCursorPage[CategoryResponse], category, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Ascerta) -> None:
        category = client.categories.list(
            active=True,
            cursor="cursor",
            limit=0,
            sort_ascending=True,
        )
        assert_matches_type(SyncCursorPage[CategoryResponse], category, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Ascerta) -> None:

        response = client.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = response.parse()
        assert_matches_type(SyncCursorPage[CategoryResponse], category, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Ascerta) -> None:
        with client.categories.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = response.parse()
            assert_matches_type(SyncCursorPage[CategoryResponse], category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Ascerta) -> None:
        category = client.categories.delete(
            "category",
        )
        assert_matches_type(CategoryDeleteResponse, category, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Ascerta) -> None:

        response = client.categories.with_raw_response.delete(
            "category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Ascerta) -> None:
        with client.categories.with_streaming_response.delete(
            "category",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ascerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category` but received ''"):
          client.categories.with_raw_response.delete(
              "",
          )

    @parametrize
    def test_method_delete_resource(self, client: Ascerta) -> None:
        category = client.categories.delete_resource(
            resource="resource",
            category="category",
        )
        assert_matches_type(CategoryDeleteResourceResponse, category, path=['response'])

    @parametrize
    def test_raw_response_delete_resource(self, client: Ascerta) -> None:

        response = client.categories.with_raw_response.delete_resource(
            resource="resource",
            category="category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = response.parse()
        assert_matches_type(CategoryDeleteResourceResponse, category, path=['response'])

    @parametrize
    def test_streaming_response_delete_resource(self, client: Ascerta) -> None:
        with client.categories.with_streaming_response.delete_resource(
            resource="resource",
            category="category",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = response.parse()
            assert_matches_type(CategoryDeleteResourceResponse, category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_resource(self, client: Ascerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category` but received ''"):
          client.categories.with_raw_response.delete_resource(
              resource="resource",
              category="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource` but received ''"):
          client.categories.with_raw_response.delete_resource(
              resource="",
              category="category",
          )

    @parametrize
    def test_method_list_resources(self, client: Ascerta) -> None:
        category = client.categories.list_resources(
            category="category",
        )
        assert_matches_type(SyncCursorPage[CategoryResourceResponse], category, path=['response'])

    @parametrize
    def test_method_list_resources_with_all_params(self, client: Ascerta) -> None:
        category = client.categories.list_resources(
            category="category",
            active=True,
            cursor="cursor",
            limit=0,
            sort_ascending=True,
        )
        assert_matches_type(SyncCursorPage[CategoryResourceResponse], category, path=['response'])

    @parametrize
    def test_raw_response_list_resources(self, client: Ascerta) -> None:

        response = client.categories.with_raw_response.list_resources(
            category="category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = response.parse()
        assert_matches_type(SyncCursorPage[CategoryResourceResponse], category, path=['response'])

    @parametrize
    def test_streaming_response_list_resources(self, client: Ascerta) -> None:
        with client.categories.with_streaming_response.list_resources(
            category="category",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = response.parse()
            assert_matches_type(SyncCursorPage[CategoryResourceResponse], category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_resources(self, client: Ascerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category` but received ''"):
          client.categories.with_raw_response.list_resources(
              category="",
          )
class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @parametrize
    async def test_method_list(self, async_client: AsyncAscerta) -> None:
        category = await async_client.categories.list()
        assert_matches_type(AsyncCursorPage[CategoryResponse], category, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAscerta) -> None:
        category = await async_client.categories.list(
            active=True,
            cursor="cursor",
            limit=0,
            sort_ascending=True,
        )
        assert_matches_type(AsyncCursorPage[CategoryResponse], category, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAscerta) -> None:

        response = await async_client.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = await response.parse()
        assert_matches_type(AsyncCursorPage[CategoryResponse], category, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAscerta) -> None:
        async with async_client.categories.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = await response.parse()
            assert_matches_type(AsyncCursorPage[CategoryResponse], category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAscerta) -> None:
        category = await async_client.categories.delete(
            "category",
        )
        assert_matches_type(CategoryDeleteResponse, category, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAscerta) -> None:

        response = await async_client.categories.with_raw_response.delete(
            "category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = await response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAscerta) -> None:
        async with async_client.categories.with_streaming_response.delete(
            "category",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = await response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAscerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category` but received ''"):
          await async_client.categories.with_raw_response.delete(
              "",
          )

    @parametrize
    async def test_method_delete_resource(self, async_client: AsyncAscerta) -> None:
        category = await async_client.categories.delete_resource(
            resource="resource",
            category="category",
        )
        assert_matches_type(CategoryDeleteResourceResponse, category, path=['response'])

    @parametrize
    async def test_raw_response_delete_resource(self, async_client: AsyncAscerta) -> None:

        response = await async_client.categories.with_raw_response.delete_resource(
            resource="resource",
            category="category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = await response.parse()
        assert_matches_type(CategoryDeleteResourceResponse, category, path=['response'])

    @parametrize
    async def test_streaming_response_delete_resource(self, async_client: AsyncAscerta) -> None:
        async with async_client.categories.with_streaming_response.delete_resource(
            resource="resource",
            category="category",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = await response.parse()
            assert_matches_type(CategoryDeleteResourceResponse, category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_resource(self, async_client: AsyncAscerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category` but received ''"):
          await async_client.categories.with_raw_response.delete_resource(
              resource="resource",
              category="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `resource` but received ''"):
          await async_client.categories.with_raw_response.delete_resource(
              resource="",
              category="category",
          )

    @parametrize
    async def test_method_list_resources(self, async_client: AsyncAscerta) -> None:
        category = await async_client.categories.list_resources(
            category="category",
        )
        assert_matches_type(AsyncCursorPage[CategoryResourceResponse], category, path=['response'])

    @parametrize
    async def test_method_list_resources_with_all_params(self, async_client: AsyncAscerta) -> None:
        category = await async_client.categories.list_resources(
            category="category",
            active=True,
            cursor="cursor",
            limit=0,
            sort_ascending=True,
        )
        assert_matches_type(AsyncCursorPage[CategoryResourceResponse], category, path=['response'])

    @parametrize
    async def test_raw_response_list_resources(self, async_client: AsyncAscerta) -> None:

        response = await async_client.categories.with_raw_response.list_resources(
            category="category",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        category = await response.parse()
        assert_matches_type(AsyncCursorPage[CategoryResourceResponse], category, path=['response'])

    @parametrize
    async def test_streaming_response_list_resources(self, async_client: AsyncAscerta) -> None:
        async with async_client.categories.with_streaming_response.list_resources(
            category="category",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            category = await response.parse()
            assert_matches_type(AsyncCursorPage[CategoryResourceResponse], category, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_resources(self, async_client: AsyncAscerta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category` but received ''"):
          await async_client.categories.with_raw_response.list_resources(
              category="",
          )