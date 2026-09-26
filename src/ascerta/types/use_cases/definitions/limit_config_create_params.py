# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional, Dict

__all__ = ["LimitConfigCreateParams"]

class LimitConfigCreateParams(TypedDict, total=False):
    max: Required[float]

    limit_type: Literal["block", "allow"]

    properties: Optional[Dict[str, Optional[str]]]

    threshold: Optional[float]