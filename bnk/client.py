from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import rpyc
from rpyc.utils.classic import obtain


@dataclass(frozen=True)
class ConnectConfig:
    host: str
    port: int
    timeout: float


class KnifeClient:
    def __init__(self, cfg: ConnectConfig):
        self._cfg = cfg
        timeout = None if cfg.timeout == 0 else float(cfg.timeout)
        self._conn = rpyc.connect(
            cfg.host,
            int(cfg.port),
            config={"sync_request_timeout": timeout},
        )
        self.root = self._conn.root

    def _obtain(self, value: Any) -> Any:
        return obtain(value)

    def close(self) -> None:
        try:
            self._conn.close()
        except Exception:
            pass

    def __enter__(self) -> "KnifeClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    # root ops

    def core_version(self) -> str:
        return str(self._obtain(self.root.binaryninja.core_version()))

    # session ops

    def session_open(self, name: str) -> str:
        return str(self._obtain(self.root.session_open(name)))

    def session_list(self) -> List[str]:
        return list(self._obtain(self.root.session_list()))

    def session_close(self, name: str) -> bool:
        return bool(self._obtain(self.root.session_close(name)))

    def session_reset(self, name: str, *, keep_bv: bool = True) -> bool:
        return bool(self._obtain(self.root.session_reset(name, keep_bv=keep_bv)))

    # view ops

    def view_list(
        self,
        session: str,
        *,
        include_unnamed: bool = False,
        full: bool = False,
    ) -> List[Dict[str, Any]]:
        return list(
            self._obtain(
                self.root.view_list(session, include_unnamed=include_unnamed, full=full)
            )
        )

    def view_attach(
        self,
        session: str,
        *,
        index: Optional[int] = None,
        match: Optional[str] = None,
        include_unnamed: bool = False,
    ) -> Dict[str, Any]:
        return dict(
            self._obtain(
                self.root.view_attach(
                    session,
                    index=index,
                    match=match,
                    include_unnamed=include_unnamed,
                )
            )
        )

    def view_status(self, session: str) -> Dict[str, Any]:
        return dict(self._obtain(self.root.view_status(session)))

    def view_load(
        self,
        session: str,
        path: str,
        *,
        update_analysis: bool = True,
        options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        options_json = None
        if options is not None:
            options_json = json.dumps(options)
        return dict(
            self._obtain(
                self.root.view_load(
                    session,
                    path,
                    update_analysis=update_analysis,
                    options_json=options_json,
                )
            )
        )

    # code exec

    def run_code(
        self,
        session: str,
        code: str,
        *,
        argv: Optional[List[str]] = None,
        capture_output: bool = True,
    ) -> Dict[str, Any]:
        return dict(
            self._obtain(
                self.root.run_code(
                    session,
                    code,
                    argv=argv or [],
                    capture_output=bool(capture_output),
                )
            )
        )
