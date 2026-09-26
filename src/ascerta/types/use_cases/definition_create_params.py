# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

from ..shared_params.ascerta_common_models_budget_management_create_limit_base import AscertaCommonModelsBudgetManagementCreateLimitBase

__all__ = ["DefinitionCreateParams"]

class DefinitionCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    limit_config: Optional[AscertaCommonModelsBudgetManagementCreateLimitBase]

    logging_enabled: Optional[bool]

    system_integration: Optional[Literal["none", "claude_code", "github_copilot"]]
    """
    Identifies which known integration populates an entity's data (provenance). This
    axis says who writes the data — commercial tiering belongs to ApplicationSku.
    Add values only when a consumer reads them.
    """