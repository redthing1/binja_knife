from __future__ import annotations

import threading
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


Loader = Callable[..., Any]
Clock = Callable[[], float]

IMPORT_SYMBOL_TYPES = {
    "ImportedFunctionSymbol",
    "ImportAddressSymbol",
    "ImportedDataSymbol",
    "ExternalSymbol",
}


class SessionError(Exception):
    def __init__(
        self,
        message: str,
        *,
        kind: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.kind = kind
        self.details = details or {}


@dataclass
class OpeningSession:
    name: str
    path: str
    started_at: float


@dataclass
class Session:
    name: str
    path: str
    bv: Any
    created_at: float
    active_uses: int = 0
    changes: threading.Lock = field(default_factory=threading.Lock)


class SessionStore:
    def __init__(self, loader: Loader, *, clock: Clock = time.monotonic) -> None:
        self._loader = loader
        self._clock = clock
        self._lock = threading.Lock()
        self._sessions: dict[str, OpeningSession | Session] = {}

    def list_sessions(
        self,
        session_name: str | None,
        args: dict[str, Any],
    ) -> dict[str, Any]:
        del session_name
        _reject_args(args)
        now = self._clock()
        with self._lock:
            items = [self._session_item(session, now) for session in self._sessions.values()]
        return {"sessions": sorted(items, key=lambda item: item["name"])}

    def open(
        self,
        session_name: str | None,
        args: dict[str, Any],
    ) -> dict[str, Any]:
        path_value = args.get("path")
        server_path = args.get("server_path", False)
        if not isinstance(path_value, str) or not path_value:
            raise SessionError("path must be a non-empty string", kind="path")
        if type(server_path) is not bool:
            raise SessionError("server_path must be a boolean", kind="invalid_request")
        if set(args) - {"path", "server_path"}:
            raise SessionError("open received unknown arguments", kind="invalid_request")

        path = _resolve_path(path_value, server_path=server_path)
        name = session_name if session_name is not None else Path(path).name

        reservation: OpeningSession | None = None
        reused: Session | None = None
        with self._lock:
            if session_name is None:
                reused = self._unnamed_reuse(path)
                if reused is None:
                    reservation = self._reserve(name, path)
            else:
                existing = self._sessions.get(name)
                if existing is not None:
                    reused = self._named_reuse(existing, name, path)
                else:
                    reservation = self._reserve(name, path)

        if reused is not None:
            try:
                return _open_result(reused, reused=True)
            finally:
                self._release(reused)

        assert reservation is not None
        view: Any | None = None
        try:
            view = self._loader(path, update_analysis=True)
            if view is None:
                raise SessionError(
                    f"Binary Ninja could not open {path}",
                    kind="load",
                    details={"session": name, "path": path},
                )
            ready = Session(name=name, path=path, bv=view, created_at=self._clock())
            result = _open_result(ready, reused=False)
            with self._lock:
                if self._sessions.get(name) is not reservation:
                    raise SessionError(
                        f"session '{name}' changed while it was opening",
                        kind="session_conflict",
                        details={"session": name, "path": path},
                    )
                self._sessions[name] = ready
            return result
        except Exception as error:
            if view is not None:
                try:
                    view.file.close()
                except Exception:
                    pass
            with self._lock:
                if self._sessions.get(name) is reservation:
                    del self._sessions[name]
            if isinstance(error, SessionError):
                raise
            raise SessionError(
                f"failed to open {path}: {error}",
                kind="load",
                details={"session": name, "path": path},
            ) from error

    def summary(
        self,
        session_name: str | None,
        args: dict[str, Any],
    ) -> dict[str, Any]:
        _reject_args(args)
        with self.use(session_name) as session:
            return _summary(session)

    def close(
        self,
        session_name: str | None,
        args: dict[str, Any],
    ) -> dict[str, Any]:
        discard = args.get("discard", False)
        if type(discard) is not bool:
            raise SessionError("discard must be a boolean", kind="invalid_request")
        if set(args) - {"discard"}:
            raise SessionError("close received unknown arguments", kind="invalid_request")

        with self._lock:
            session = self._select(session_name)
            if session.active_uses:
                raise SessionError(
                    f"session '{session.name}' is in use",
                    kind="session_busy",
                    details={"session": session.name, "active": session.active_uses},
                )
            analysis_changed = bool(session.bv.file.analysis_changed)
            modified = bool(session.bv.file.modified)
            if not discard and (analysis_changed or modified):
                raise SessionError(
                    f"session '{session.name}' has unsaved "
                    f"{_change_description(analysis_changed, modified)}; "
                    "save it or use --discard to close",
                    kind="dirty",
                    details={
                        "session": session.name,
                        "analysis_changed": analysis_changed,
                        "modified": modified,
                    },
                )
            del self._sessions[session.name]

        try:
            session.bv.file.close()
        except Exception as error:
            raise SessionError(
                f"failed to close session '{session.name}': {error}",
                kind="close",
                details={"session": session.name, "path": session.path},
            ) from error
        return {
            "session": session.name,
            "path": session.path,
            "analysis_changed": analysis_changed,
            "modified": modified,
            "discarded": discard and (analysis_changed or modified),
        }

    @contextmanager
    def use(self, session_name: str | None) -> Iterator[Session]:
        with self._lock:
            session = self._select(session_name)
            session.active_uses += 1
        try:
            yield session
        finally:
            self._release(session)

    def _unnamed_reuse(self, path: str) -> Session | None:
        matching = [
            session
            for session in self._sessions.values()
            if isinstance(session, Session) and session.path == path
        ]
        if matching:
            derived_name = Path(path).name
            derived = next((session for session in matching if session.name == derived_name), None)
            if derived is not None:
                derived.active_uses += 1
                return derived
            if len(matching) == 1:
                matching[0].active_uses += 1
                return matching[0]
            candidates = sorted(session.name for session in matching)
            raise SessionError(
                f"several sessions already have {path}; choose one with -s",
                kind="session_ambiguous",
                details={"path": path, "candidates": candidates},
            )

        opening = next(
            (
                session
                for session in self._sessions.values()
                if isinstance(session, OpeningSession) and session.path == path
            ),
            None,
        )
        if opening is not None:
            self._raise_opening(opening)
        return None

    def _named_reuse(
        self,
        existing: OpeningSession | Session,
        name: str,
        path: str,
    ) -> Session:
        if isinstance(existing, OpeningSession):
            if existing.path == path:
                self._raise_opening(existing)
            raise SessionError(
                f"session '{name}' is opening {existing.path}, not {path}",
                kind="session_conflict",
                details={"session": name, "path": path, "existing_path": existing.path},
            )
        if existing.path != path:
            raise SessionError(
                f"session '{name}' already refers to {existing.path}, not {path}",
                kind="session_conflict",
                details={"session": name, "path": path, "existing_path": existing.path},
            )
        existing.active_uses += 1
        return existing

    def _reserve(self, name: str, path: str) -> OpeningSession:
        existing = self._sessions.get(name)
        if existing is not None:
            if isinstance(existing, OpeningSession):
                self._raise_opening(existing)
            raise SessionError(
                f"session name '{name}' already refers to {existing.path}; choose another with -s",
                kind="session_conflict",
                details={"session": name, "path": path, "existing_path": existing.path},
            )
        reservation = OpeningSession(name, path, self._clock())
        self._sessions[name] = reservation
        return reservation

    def _select(self, session_name: str | None) -> Session:
        if session_name is not None:
            selected = self._sessions.get(session_name)
            if selected is None:
                raise SessionError(
                    f"unknown session '{session_name}'",
                    kind="session_not_found",
                    details={"session": session_name, "candidates": self._ready_names()},
                )
            if isinstance(selected, OpeningSession):
                self._raise_opening(selected)
            return selected

        ready = [session for session in self._sessions.values() if isinstance(session, Session)]
        if not ready:
            openings = sorted(
                session.name
                for session in self._sessions.values()
                if isinstance(session, OpeningSession)
            )
            raise SessionError(
                "no session is ready; open a binary first",
                kind="session_not_found",
                details={"openings": openings},
            )
        if len(ready) > 1:
            candidates = sorted(session.name for session in ready)
            raise SessionError(
                "several sessions are ready; choose one with -s",
                kind="session_ambiguous",
                details={"candidates": candidates},
            )
        return ready[0]

    def _session_item(
        self,
        session: OpeningSession | Session,
        now: float,
    ) -> dict[str, Any]:
        if isinstance(session, OpeningSession):
            return {
                "name": session.name,
                "state": "opening",
                "path": session.path,
                "elapsed_seconds": round(now - session.started_at, 3),
            }
        return {
            "name": session.name,
            "state": "ready",
            "path": session.path,
            "active": session.active_uses,
            "age_seconds": round(now - session.created_at, 3),
        }

    def _ready_names(self) -> list[str]:
        return sorted(
            session.name for session in self._sessions.values() if isinstance(session, Session)
        )

    def _raise_opening(self, session: OpeningSession) -> None:
        elapsed = round(self._clock() - session.started_at, 3)
        raise SessionError(
            f"session '{session.name}' is still opening {session.path} ({elapsed:.3f}s)",
            kind="session_opening",
            details={
                "session": session.name,
                "path": session.path,
                "elapsed_seconds": elapsed,
            },
        )

    def _release(self, session: Session) -> None:
        with self._lock:
            session.active_uses -= 1


def _resolve_path(value: str, *, server_path: bool) -> str:
    path = Path(value).expanduser()
    if not path.is_absolute():
        label = "server path" if server_path else "path"
        raise SessionError(f"{label} must be absolute", kind="path", details={"path": value})
    path = path.resolve()
    if not path.is_file():
        hint = "" if server_path else "; use --server-path for a path on Binary Ninja's filesystem"
        raise SessionError(
            f"not a regular file: {path}{hint}",
            kind="path",
            details={"path": str(path)},
        )
    return str(path)


def _reject_args(args: dict[str, Any]) -> None:
    if args:
        raise SessionError("action does not accept arguments", kind="invalid_request")


def _summary(session: Session) -> dict[str, Any]:
    view = session.bv
    return {
        "session": session.name,
        "path": session.path,
        "view": str(view.view_type),
        "architecture": _named(view.arch),
        "platform": _named(view.platform),
        "start": hex(view.start),
        "end": hex(view.end),
        "length": view.length,
        "entry": hex(view.entry_point),
        "analysis": _analysis_name(view.analysis_state),
        "function_count": len(view.functions),
        "import_count": _import_count(view),
        "string_count": sum(1 for _ in view.get_strings()),
        "section_count": len(view.sections),
        "segment_count": len(view.segments),
        "has_database": bool(view.file.has_database),
        "analysis_changed": bool(view.file.analysis_changed),
        "modified": bool(view.file.modified),
    }


def _open_result(session: Session, *, reused: bool) -> dict[str, Any]:
    view = session.bv
    return {
        "session": session.name,
        "path": session.path,
        "reused": reused,
        "view": str(view.view_type),
        "architecture": _named(view.arch),
        "analysis": _analysis_name(view.analysis_state),
        "function_count": len(view.functions),
    }


def _named(value: Any | None) -> str | None:
    return None if value is None else str(value.name)


def _analysis_name(value: Any) -> str:
    names = {
        "IdleState": "idle",
        "DisassembleState": "disassembling",
        "AnalyzeState": "analyzing",
        "ExtendedAnalyzeState": "extended_analysis",
        "HoldState": "hold",
    }
    name = str(value.name)
    return names.get(name, name)


def _import_count(view: Any) -> int:
    names = {
        str(getattr(symbol, "full_name", getattr(symbol, "name", "")))
        for symbol in view.get_symbols()
        if str(getattr(symbol.type, "name", symbol.type)) in IMPORT_SYMBOL_TYPES
    }
    return len(names)


def _change_description(analysis_changed: bool, modified: bool) -> str:
    if analysis_changed and modified:
        return "analysis and byte changes"
    if analysis_changed:
        return "analysis changes"
    return "byte changes"
