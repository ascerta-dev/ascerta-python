# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

__all__ = ["DefaultResponse"]

class DefaultResponse(BaseModel):
    request_id: str

    message: Optional[str] = None