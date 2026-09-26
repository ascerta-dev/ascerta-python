# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from .shared.api_error import APIError

from datetime import datetime

__all__ = ["BulkIngestResponse", "Error"]

class Error(BaseModel):
    item_index: Optional[int] = None

    xproxy_result: Optional[APIError] = None

class BulkIngestResponse(BaseModel):
    ingest_count: int

    ingest_timestamp: datetime

    request_id: str

    error_count: Optional[int] = None

    errors: Optional[List[Error]] = None

    item_error_count: Optional[int] = None

    total_count: Optional[int] = None