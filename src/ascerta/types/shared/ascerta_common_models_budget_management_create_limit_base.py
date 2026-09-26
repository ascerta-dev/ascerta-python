# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Dict

from typing_extensions import Literal

__all__ = ["AscertaCommonModelsBudgetManagementCreateLimitBase"]

class AscertaCommonModelsBudgetManagementCreateLimitBase(BaseModel):
    max: float

    limit_type: Optional[Literal["block", "allow"]] = None

    properties: Optional[Dict[str, Optional[str]]] = None

    threshold: Optional[float] = None