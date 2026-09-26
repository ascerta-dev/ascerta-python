# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

__all__ = ["CostDetails"]

class CostDetails(BaseModel):
    base: float

    overrun_base: Optional[float] = None