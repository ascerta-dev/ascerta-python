# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional, Dict

__all__ = ["LimitCreateParams"]

class LimitCreateParams(TypedDict, total=False):
    limit_name: Required[str]

    max: Required[float]

    limit_id: Optional[str]

    limit_type: Literal["block", "allow"]

    properties: Optional[Dict[str, Optional[str]]]

    threshold: Optional[float]