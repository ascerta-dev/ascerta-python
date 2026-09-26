# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

__all__ = ["CategoryResourcePriceUnits"]

class CategoryResourcePriceUnits(BaseModel):
    input_price: Optional[float] = None

    output_price: Optional[float] = None