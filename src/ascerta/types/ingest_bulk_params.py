# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Iterable

from .bulk_ingest_request_param import BulkIngestRequestParam

__all__ = ["IngestBulkParams"]

class IngestBulkParams(TypedDict, total=False):
    events: Iterable[BulkIngestRequestParam]