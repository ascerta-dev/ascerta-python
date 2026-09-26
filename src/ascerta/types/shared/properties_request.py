# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Dict, Optional

__all__ = ["PropertiesRequest"]

class PropertiesRequest(BaseModel):
    properties: Dict[str, Optional[str]]