# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Dict, Optional, Union, Iterable

from .shared_params.ingest_units import IngestUnits

from datetime import datetime

from .._utils import PropertyInfo

from .ascerta_common_models_api_router_header_info_param import AscertaCommonModelsAPIRouterHeaderInfoParam

from .function_call_info_param import FunctionCallInfoParam

from .._types import SequenceNotStr

__all__ = ["IngestUnitsParams"]

class IngestUnitsParams(TypedDict, total=False):
    category: Required[str]

    units: Required[Dict[str, IngestUnits]]

    end_to_end_latency_ms: Optional[int]

    event_timestamp: Annotated[Union[str, datetime, None], PropertyInfo(format = "iso8601")]

    http_status_code: Optional[int]

    properties: Optional[Dict[str, Optional[str]]]

    provider_request_headers: Optional[Iterable[AscertaCommonModelsAPIRouterHeaderInfoParam]]

    provider_request_json: Optional[str]

    provider_request_reasoning_json: Optional[str]

    provider_response_function_calls: Optional[Iterable[FunctionCallInfoParam]]

    provider_response_headers: Optional[Iterable[AscertaCommonModelsAPIRouterHeaderInfoParam]]

    provider_response_id: Optional[str]

    provider_response_json: Union[str, SequenceNotStr[str], None]

    provider_uri: Optional[str]

    resource: Optional[str]

    time_to_first_completion_token_ms: Optional[int]

    time_to_first_token_ms: Optional[int]

    use_case_properties: Optional[Dict[str, Optional[str]]]

    account_name: Annotated[str, PropertyInfo(alias="xProxy-Account-Name")]

    limit_ids: Annotated[str, PropertyInfo(alias="xProxy-Limit-IDs")]

    disable_logging: Annotated[str, PropertyInfo(alias="xProxy-Logging-Disable")]

    resource_scope: Annotated[str, PropertyInfo(alias="xProxy-Resource-Scope")]

    use_case_id: Annotated[str, PropertyInfo(alias="xProxy-UseCase-ID")]

    use_case_name: Annotated[str, PropertyInfo(alias="xProxy-UseCase-Name")]

    use_case_step: Annotated[str, PropertyInfo(alias="xProxy-UseCase-Step")]

    use_case_version: Annotated[int, PropertyInfo(alias="xProxy-UseCase-Version")]

    user_id: Annotated[str, PropertyInfo(alias="xProxy-User-ID")]