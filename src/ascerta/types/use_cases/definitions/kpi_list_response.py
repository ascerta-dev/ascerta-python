# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from typing_extensions import Literal

__all__ = ["KpiListResponse"]

class KpiListResponse(BaseModel):
    description: str

    kpi_id: str

    kpi_name: str

    request_id: str

    created_timestamp: Optional[datetime] = None

    goal: Optional[float] = None

    kpi_type: Optional[Literal["boolean", "number", "percentage", "likert5", "likert7", "likert10"]] = None

    name: Optional[str] = None

    updated_timestamp: Optional[datetime] = None