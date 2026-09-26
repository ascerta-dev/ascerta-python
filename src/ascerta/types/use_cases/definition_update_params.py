# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Optional

__all__ = ["DefinitionUpdateParams"]

class DefinitionUpdateParams(TypedDict, total=False):
    description: Optional[str]

    logging_enabled: Optional[bool]

    system_integration: Optional[Literal["none", "claude_code", "github_copilot"]]
    """
    Identifies which known integration populates an entity's data (provenance). This
    axis says who writes the data — commercial tiering belongs to ApplicationSku.
    Add values only when a consumer reads them.
    """