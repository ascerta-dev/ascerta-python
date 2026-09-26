# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

__all__ = ["KpiCreateParams"]

class KpiCreateParams(TypedDict, total=False):
    description: Required[str]

    goal: Required[float]

    kpi_type: Required[Literal["boolean", "number", "percentage", "likert5", "likert7", "likert10"]]

    kpi_id: Optional[str]

    kpi_name: Optional[str]