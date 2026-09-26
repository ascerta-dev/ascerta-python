# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["XproxyError"]

class XproxyError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None