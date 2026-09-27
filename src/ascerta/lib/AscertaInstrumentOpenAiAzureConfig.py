from __future__ import annotations

from typing import Sequence, TypedDict

from .AscertaInstrumentModelMapping import AscertaInstrumentModelMapping


class AscertaInstrumentOpenAiAzureConfig(TypedDict, total=False):
    # map deployment name known model
    model_mappings: Sequence[AscertaInstrumentModelMapping]
