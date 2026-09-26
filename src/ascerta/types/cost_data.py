# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .shared.ascerta_common_models_budget_management_cost_details_base import AscertaCommonModelsBudgetManagementCostDetailsBase

from .cost_details import CostDetails

__all__ = ["CostData"]

class CostData(BaseModel):
    input: AscertaCommonModelsBudgetManagementCostDetailsBase

    output: AscertaCommonModelsBudgetManagementCostDetailsBase

    total: CostDetails