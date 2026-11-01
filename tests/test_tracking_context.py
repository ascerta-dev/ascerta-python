from __future__ import annotations

import sys
import socket
import asyncio
import contextvars
import concurrent.futures
from typing import Any, Iterator

import httpx
import pytest

from ascerta import Ascerta, track, get_context, track_context, ascerta_instrument
from ascerta.lib import instrument
from ascerta.lib.helpers import AscertaHeaderNames
from ascerta.lib.ProviderRequest import _StreamingType, _ProviderRequest
from ascerta.types.shared.xproxy_result import XproxyResult


# ---------------- Test helpers ------------------------------------------
@pytest.fixture
def active(monkeypatch: pytest.MonkeyPatch) -> Iterator[instrument._AscertaInstrumentor]:
    """Exercise real hooks without leaving process-wide wrappers or network access behind."""

    def deny_connect(*_args: Any, **_kwargs: Any) -> Any:
        raise AssertionError("Real sockets are prohibited")

    monkeypatch.setattr(socket.socket, "connect", deny_connect)
    monkeypatch.setattr(socket.socket, "connect_ex", deny_connect)
    monkeypatch.setattr(instrument, "_instrumentor", None)
    # Register originals with monkeypatch before the SDK installs its real hooks.
    monkeypatch.setattr(asyncio, "create_task", asyncio.create_task)
    monkeypatch.setattr(asyncio, "gather", asyncio.gather)
    monkeypatch.setattr(concurrent.futures.ThreadPoolExecutor, "submit", concurrent.futures.ThreadPoolExecutor.submit)
    with Ascerta(
        api_key="synthetic-tracking-key",
        http_client=httpx.Client(transport=httpx.MockTransport(deny_connect), trust_env=False),
    ) as client:
        ascerta_instrument(
            ascerta=client,
            instruments=set(),
            config={"global_instrumentation": False, "ingest_retry": {"queue_enabled": False}},
        )
        assert instrument._instrumentor is not None
        yield instrument._instrumentor


def metadata(active: instrument._AscertaInstrumentor) -> dict[str, Any]:
    """Observe both public metadata and the downstream ingest preparation that consumes it."""
    headers: dict[str, str] = {}
    active._update_extra_headers(active._context_safe, headers, proxy=False)
    request = _ProviderRequest(active, "synthetic.category", _StreamingType.generator, "synthetic", "1")
    active._before_invoke_update_request(request, headers, (), {})
    proxy_headers = active._create_extra_headers()
    return {
        "context": get_context().get("user_id"),
        "header": proxy_headers.get(AscertaHeaderNames.user_id),
        "ingest": request._ingest.get("user_id"),
        "properties": request._ingest.get("properties"),
    }


# ---------------- End test helpers --------------------------------------


@pytest.mark.parametrize("factory", ["create_task", "loop", "gather"])
@pytest.mark.parametrize("exit_mode", ["return", "error", "cancel"])
def test_overlapping_tracking(active: instrument._AscertaInstrumentor, factory: str, exit_mode: str) -> None:
    async def scenario() -> None:
        entered_a, entered_b = asyncio.Event(), asyncio.Event()
        release_a, release_b = asyncio.Event(), asyncio.Event()
        observations: dict[str, dict[str, Any]] = {}
        completed_a = asyncio.Event()
        task_a: asyncio.Task[None] | None = None

        @track(user_id="A", use_case_name="synthetic-A", request_properties={"owner": "A"})
        async def a() -> None:
            entered_a.set()
            try:
                await release_a.wait()
                if exit_mode == "error":
                    raise ValueError("synthetic error")
            finally:
                observations["A"] = metadata(active)

        async def b() -> None:
            await entered_a.wait()
            with track_context(user_id="B", use_case_name="synthetic-B", request_properties={"owner": "B"}):
                entered_b.set()
                await release_b.wait()
                observations["B"] = metadata(active)

        async def run_a() -> None:
            nonlocal task_a
            task_a = asyncio.current_task()
            try:
                await a()
            finally:
                completed_a.set()

        loop = asyncio.get_running_loop()
        future: asyncio.Future[str] = loop.create_future()
        future.set_result("future-result")
        if factory == "gather":
            joined = asyncio.gather(run_a(), b(), future, return_exceptions=True)
        else:
            create = asyncio.create_task if factory == "create_task" else loop.create_task
            first, second = create(run_a()), create(b())
            joined = asyncio.gather(first, second, future, return_exceptions=True)

        await entered_b.wait()
        observations["parent"] = metadata(active)
        if exit_mode == "cancel":
            assert task_a is not None
            task_a.cancel()
        else:
            release_a.set()
        # Completion is signalled after the tracked scope has unwound.
        await completed_a.wait()
        release_b.set()
        results = await joined
        assert results[2] == "future-result"
        if exit_mode == "error":
            assert isinstance(results[0], ValueError)
        elif exit_mode == "cancel":
            assert isinstance(results[0], asyncio.CancelledError)
        assert observations == {
            "A": {"context": "A", "header": "A", "ingest": "A", "properties": {"owner": "A"}},
            "B": {"context": "B", "header": "B", "ingest": "B", "properties": {"owner": "B"}},
            "parent": {"context": None, "header": None, "ingest": None, "properties": None},
        }
        assert get_context() == {}

    asyncio.run(asyncio.wait_for(scenario(), 5))


@pytest.mark.usefixtures("active")
def test_inherited_context_is_a_snapshot() -> None:
    async def scenario() -> None:
        entered, release = asyncio.Event(), asyncio.Event()
        observed: list[dict[str, Any]] = []

        async def child() -> None:
            inherited = get_context()
            inherited["request_properties"]["owner"] = "mutated"  # type: ignore[index]
            inherited["limit_ids"].append("mutated")  # type: ignore[union-attr]
            observed.append(dict(get_context()))
            with track_context(user_id="child", request_properties={"child": "yes"}):
                entered.set()
                await release.wait()
                observed.append(dict(get_context()))
            observed.append(dict(get_context()))

        properties = {"owner": "parent"}
        limits = ["parent-limit"]
        with track_context(user_id="parent", request_properties=properties, limit_ids=limits):
            task = asyncio.get_running_loop().create_task(child())
            await entered.wait()
            properties["owner"] = "caller-mutated"
            limits.append("caller-mutated")
            parent = get_context()
            release.set()
            await task
            assert parent["user_id"] == "parent"
            assert parent["request_properties"] == {"owner": "parent"}
            assert parent["limit_ids"] == ["parent-limit"]
        assert observed[0] == observed[2] == parent
        assert observed[1]["user_id"] == "child"
        assert observed[1]["request_properties"] == {"owner": "parent", "child": "yes"}
        assert get_context() == {}

    asyncio.run(asyncio.wait_for(scenario(), 5))


@pytest.mark.usefixtures("active")
def test_nesting_and_thread_propagation() -> None:
    @track(user_id="nested", request_properties={"nested": "yes"})
    def nested() -> None:
        assert get_context()["user_id"] == "nested"
        raise ValueError("synthetic error")

    def worker() -> str | None:
        assert get_context()["user_id"] == "parent"
        with pytest.raises(ValueError, match="synthetic error"):
            nested()
        assert get_context()["request_properties"] == {"owner": "parent"}
        return get_context().get("user_id")

    with track_context(user_id="parent", request_properties={"owner": "parent"}):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            assert pool.submit(worker).result(timeout=5) == "parent"
        assert get_context()["user_id"] == "parent"
    assert get_context() == {}


@pytest.mark.skipif(sys.version_info < (3, 11), reason="Task context argument and TaskGroup require Python 3.11")
@pytest.mark.usefixtures("active")
def test_explicit_task_context() -> None:
    async def scenario() -> None:
        marker: contextvars.ContextVar[str] = contextvars.ContextVar("synthetic-marker", default="empty")
        with track_context(user_id="selected"):
            marker.set("selected")
            selected = contextvars.copy_context()
        observed: list[tuple[str | None, str]] = []

        async def child() -> None:
            observed.append((get_context().get("user_id"), marker.get()))
            with track_context(user_id="child"):
                assert get_context()["user_id"] == "child"

        with track_context(user_id="caller"):
            await asyncio.create_task(child(), name="synthetic-selected", context=selected)
            await asyncio.create_task(coro=child(), context=contextvars.Context())
            async with asyncio.TaskGroup() as group:
                group.create_task(child(), context=selected)
            assert get_context()["user_id"] == "caller"
        assert observed == [("selected", "selected"), (None, "empty"), ("selected", "selected")]
        assert selected.run(get_context)["user_id"] == "selected"
        assert get_context() == {}

    asyncio.run(scenario())


def test_last_result_is_local(active: instrument._AscertaInstrumentor) -> None:
    async def scenario() -> None:
        entered, release = asyncio.Event(), asyncio.Event()
        result = XproxyResult(request_id="synthetic-child-result")

        async def child() -> None:
            active.set_xproxy_result(result)
            entered.set()
            await release.wait()
            assert get_context()["last_result"] == result

        task = asyncio.create_task(child())
        await entered.wait()
        parent = get_context()
        release.set()
        await task
        assert "last_result" not in parent
        assert "last_result" not in get_context()
        with track_context(user_id="nested"):
            active.set_xproxy_result(result)
        assert get_context()["last_result"] == result

    asyncio.run(scenario())


@pytest.mark.usefixtures("active")
def test_metadata_inheritance_and_clearing() -> None:
    with track_context(
        use_case_name="parent",
        use_case_id="parent-id",
        use_case_version=2,
        use_case_step="parent-step",
        use_case_properties={"owner": "parent"},
        request_properties={"owner": "parent"},
        limit_ids=["parent-limit"],
        user_id="parent",
        account_name="parent",
        price_as_category="parent-category",
        price_as_resource="parent-resource",
        resource_scope="parent-scope",
        log_prompt_and_response=False,
    ):
        parent = get_context()
        with track_context(request_properties={"child": "yes"}, limit_ids=["child-limit"]):
            child = get_context()
            assert child["request_properties"] == {"owner": "parent", "child": "yes"}
            assert set(child["limit_ids"] or []) == {"parent-limit", "child-limit"}
            assert child["use_case_id"] == "parent-id"
            assert child["log_prompt_and_response"] is False
        with track_context(
            use_case_name="",
            request_properties={},
            use_case_properties={},
            limit_ids=[],
            user_id="",
            account_name="",
            price_as_category="",
            price_as_resource="",
            resource_scope="",
        ):
            assert get_context() == {"log_prompt_and_response": False}
        with track_context(use_case_name="different"):
            assert get_context()["use_case_id"] != "parent-id"
        assert get_context() == parent
    assert get_context() == {}


@pytest.mark.usefixtures("active")
def test_gather_preserves_awaitable_identity() -> None:
    async def scenario() -> None:
        calls = 0

        async def child() -> str | None:
            nonlocal calls
            calls += 1
            return get_context().get("user_id")

        with track_context(user_id="parent"):
            coro = child()
            future = asyncio.get_running_loop().create_future()
            future.set_result("future")
            assert await asyncio.gather(coro, coro, future) == ["parent", "parent", "future"]
            assert calls == 1
            assert await asyncio.gather() == []

    asyncio.run(scenario())


def test_executor_reuse_and_async_to_thread(active: instrument._AscertaInstrumentor) -> None:
    result = XproxyResult(request_id="synthetic-worker-result")

    def worker() -> str | None:
        user = get_context().get("user_id")
        active.set_xproxy_result(result)
        return user

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        with track_context(user_id="parent"):
            assert pool.submit(worker).result(timeout=5) == "parent"
        assert pool.submit(get_context).result(timeout=5) == {}
    assert get_context() == {}

    async def scenario() -> None:
        with track_context(user_id="async-parent"):
            assert await asyncio.to_thread(worker) == "async-parent"
            assert "last_result" not in get_context()
        assert get_context() == {}

    asyncio.run(scenario())


def test_global_defaults(active: instrument._AscertaInstrumentor, monkeypatch: pytest.MonkeyPatch) -> None:
    # Use the same real client while replacing the fixture's disabled global configuration.
    monkeypatch.setattr(instrument, "_instrumentor", None)
    ascerta_instrument(
        ascerta=active._ascerta,
        instruments=set(),
        config={
            "user_id": "global",
            "request_properties": {"owner": "global"},
            "ingest_retry": {"queue_enabled": False},
        },
    )
    global_context = get_context()
    assert global_context["user_id"] == "global"
    assert global_context["use_case_name"]

    async def child() -> None:
        assert get_context() == global_context
        with track_context(user_id="child"):
            assert get_context()["user_id"] == "child"
        assert get_context() == global_context

    asyncio.run(child())
    with track_context(user_id="sync-child"):
        assert get_context()["request_properties"] == {"owner": "global"}
    assert get_context() == global_context
