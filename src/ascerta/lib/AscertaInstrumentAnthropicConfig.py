from __future__ import annotations

from typing import Optional, Sequence, TypedDict

from .AscertaInstrumentModelMapping import AscertaInstrumentModelMapping


class AscertaInstrumentAnthropicConfig(TypedDict, total=False):
    model_mappings: Optional[Sequence[AscertaInstrumentModelMapping]]
