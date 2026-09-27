from __future__ import annotations

from typing import Optional, Sequence, TypedDict

from .AscertaInstrumentModelMapping import AscertaInstrumentModelMapping
from .AscertaInstrumentOpenAiAzureConfig import AscertaInstrumentOpenAiAzureConfig


class AscertaInstrumentOpenAiConfig(TypedDict, total=False):
    model_mappings: Optional[Sequence[AscertaInstrumentModelMapping]]
    # deprecated: use model_mappings instead
    azure: AscertaInstrumentOpenAiAzureConfig
