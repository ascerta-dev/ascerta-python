# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from ..shared.ascerta_common_models_budget_management_create_limit_base import AscertaCommonModelsBudgetManagementCreateLimitBase

from typing_extensions import Literal

__all__ = ["UseCaseDefinitionResponse"]

class UseCaseDefinitionResponse(BaseModel):
    description: str

    name: str

    request_id: str

    limit_config: Optional[AscertaCommonModelsBudgetManagementCreateLimitBase] = None

    logging_enabled: Optional[bool] = None

    system_integration: Optional[Literal["none", "claude_code", "github_copilot"]] = None
    """
    Identifies which known integration populates an entity's data (provenance). This
    axis says who writes the data — commercial tiering belongs to ApplicationSku.
    Add values only when a consumer reads them.
    """

    type_version: Optional[int] = None