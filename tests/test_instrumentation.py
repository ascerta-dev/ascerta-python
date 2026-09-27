from __future__ import annotations

import importlib
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import Mock

import pytest

from ascerta import Ascerta
from ascerta.lib import helpers, instrument
from ascerta.lib.ProviderRequest import _StreamingType, _ProviderRequest
from ascerta.lib.BedrockInstrumentor import BEDROCK_REQUEST_NAMES, BedrockInstrumentor, _redirect_to_ascerta


@pytest.mark.parametrize("module", sorted(p.stem for p in Path(helpers.__file__).parent.glob("*.py")))
def test_instrumentation_imports(module: str) -> None:
    imported = importlib.import_module(f"ascerta.lib.{module}")
    assert not any("Payi" in name or "PayI" in name for name in vars(imported))


@pytest.mark.parametrize("primary", [None, "", "https://primary.example"])
@pytest.mark.parametrize("legacy", [None, "", "https://legacy.example"])
def test_proxy_url_precedence(monkeypatch: pytest.MonkeyPatch, primary: str | None, legacy: str | None) -> None:
    for name, value in (("ASCERTA_BASE_URL", primary), ("PAYI_BASE_URL", legacy)):
        if value is None:
            monkeypatch.delenv(name, raising=False)
        else:
            monkeypatch.setenv(name, value)
    base = primary or legacy or "https://api.ascerta.com"
    assert helpers.ascerta_openai_url() == base + "/api/v1/proxy/openai/v1"
    assert helpers.ascerta_anthropic_url() == base + "/api/v1/proxy/anthropic"
    assert helpers.ascerta_openai_url("https://explicit.example") == "https://explicit.example/api/v1/proxy/openai/v1"


@pytest.mark.parametrize("primary", [None, "", "primary-key"])
def test_bedrock_credential_fallback(monkeypatch: pytest.MonkeyPatch, primary: str | None) -> None:
    monkeypatch.setenv("PAYI_API_KEY", "legacy-key")
    monkeypatch.setenv("ASCERTA_BASE_URL", "https://proxy.example")
    if primary is None:
        monkeypatch.delenv("ASCERTA_API_KEY", raising=False)
    else:
        monkeypatch.setenv("ASCERTA_API_KEY", primary)
    monkeypatch.setattr(
        BedrockInstrumentor, "_instrumentor", Mock(_create_extra_headers=Mock(return_value={})), raising=False
    )
    request = SimpleNamespace(url="https://bedrock.example/model/test", headers={})
    _redirect_to_ascerta(request, next(iter(BEDROCK_REQUEST_NAMES)))
    assert request.url == "https://proxy.example/api/v1/proxy/aws.bedrock/model/test"
    assert request.headers[helpers.AscertaHeaderNames.api_key] == (primary or "legacy-key")
    assert request.headers[helpers.AscertaHeaderNames.provider_base_uri] == "https://bedrock.example"


def test_instrumentation_context_and_payload(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(instrument, "_instrumentor", None)
    monkeypatch.setattr(instrument._AscertaInstrumentor, "_instrument_futures", Mock(return_value=None))
    with Ascerta(api_key="test-key") as client:
        instrument.ascerta_instrument(
            ascerta=client,
            instruments=set(),
            config={"global_instrumentation": False, "ingest_retry": {"queue_enabled": False}},
        )
        active = instrument._instrumentor
        assert active is not None
        assert active._ascerta is client
        with instrument.track_context(use_case_name="migration-test", user_id="user-1"):
            assert instrument.get_context().get("use_case_name") == "migration-test"
            assert instrument.get_context().get("user_id") == "user-1"
        assert instrument.get_context().get("use_case_name") is None

        request = _ProviderRequest(active, "system.openai", _StreamingType.generator, "test", "1.0")
        request.add_synchronous_function_call("lookup", '{"id":1}')
        assert request._ingest.get("provider_response_function_calls") == [{"name": "lookup", "arguments": '{"id":1}'}]
        request.add_streaming_function_call(0, "look", '{"id":')
        request.add_streaming_function_call(0, "up", "1}")
        assert request._function_call_builder == {0: {"name": "lookup", "arguments": '{"id":1}'}}
        request.add_response_headers({"x-request-id": "request-1", "content-type": "application/json"})
        assert request._ingest.get("provider_response_headers") == [{"name": "x-request-id", "value": "request-1"}]
