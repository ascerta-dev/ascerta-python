# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from typing_extensions import TypedDict, Required

__all__ = ["AscertaCommonModelsAPIRouterHeaderInfoParam"]

class AscertaCommonModelsAPIRouterHeaderInfoParam(TypedDict, total=False):
    name: Required[str]

    value: Optional[str]