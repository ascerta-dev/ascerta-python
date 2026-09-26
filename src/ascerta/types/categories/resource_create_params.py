# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Dict, Optional, Union

from ..category_resource_price_units_param import CategoryResourcePriceUnitsParam

from datetime import datetime

from ..._utils import PropertyInfo

__all__ = ["ResourceCreateParams"]

class ResourceCreateParams(TypedDict, total=False):
    category: Required[str]

    units: Required[Dict[str, CategoryResourcePriceUnitsParam]]

    max_input_units: Optional[int]

    max_output_units: Optional[int]

    max_total_units: Optional[int]

    start_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format = "iso8601")]