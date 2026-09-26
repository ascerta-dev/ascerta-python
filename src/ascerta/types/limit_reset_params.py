# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import datetime

from .._utils import PropertyInfo

__all__ = ["LimitResetParams"]

class LimitResetParams(TypedDict, total=False):
    reset_date: Annotated[Union[str, datetime], PropertyInfo(alias="resetDate", format = "iso8601")]
    """Effective reset date"""