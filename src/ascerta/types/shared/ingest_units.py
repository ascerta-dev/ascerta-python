# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["IngestUnits"]

class IngestUnits(BaseModel):
    input: Optional[int] = None

    output: Optional[int] = None