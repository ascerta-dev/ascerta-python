# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing_extensions import Literal

from .total_cost_data import TotalCostData

from typing import Optional

__all__ = ["Limit"]

class Limit(BaseModel):
    limit_creation_timestamp: datetime

    limit_id: str

    limit_name: str

    limit_type: Literal["block", "allow"]

    limit_update_timestamp: datetime

    max: float

    totals: TotalCostData

    threshold: Optional[float] = None