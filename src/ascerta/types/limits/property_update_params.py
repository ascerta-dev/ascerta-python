# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Dict, Optional

__all__ = ["PropertyUpdateParams"]

class PropertyUpdateParams(TypedDict, total=False):
    properties: Required[Dict[str, Optional[str]]]