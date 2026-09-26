# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TypeVar, Generic, List, Optional

from typing_extensions import override

import re
from typing_extensions import TypedDict, Literal, Annotated, Protocol, runtime_checkable

from httpx import URL, Response

from ._models import BaseModel
from ._utils import PropertyInfo, is_mapping
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage, PageInfo

__all__ = ["SyncCursorPage", "AsyncCursorPage"]

_T = TypeVar('_T')

class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
          return None

        return PageInfo(params={"cursor": cursor})

class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
          return None

        return PageInfo(params={"cursor": cursor})