from __future__ import annotations

from typing import Optional, Sequence, TypedDict

from .AscertaInstrumentModelConfig import AscertaInstrumentModelConfig
from .AscertaInstrumentModelMapping import AscertaInstrumentModelMapping


class AscertaInstrumentAwsBedrockConfig(TypedDict, total=False):
    guardrail_trace: Optional[bool]
    add_streaming_xproxy_result: Optional[bool]
    model_mappings: Optional[Sequence[AscertaInstrumentModelMapping]]
    model_config: Optional[dict[str, AscertaInstrumentModelConfig]]
