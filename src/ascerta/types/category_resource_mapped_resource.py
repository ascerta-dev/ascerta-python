# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

__all__ = ["CategoryResourceMappedResource"]

class CategoryResourceMappedResource(BaseModel):
    category: Optional[str] = None

    host_name: Optional[str] = None

    host_names: Optional[List[str]] = None

    mapping_name: Optional[str] = None

    resource: Optional[str] = None

    scope: Optional[Literal["global", "datazone", "region"]] = None

    sub_scope: Optional[str] = None