# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .limit import Limit

from typing import Optional

__all__ = ["LimitResponse"]

class LimitResponse(BaseModel):
    limit: Limit

    request_id: str

    message: Optional[str] = None