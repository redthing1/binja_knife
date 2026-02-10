from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass(frozen=True)
class ServerlibCall:
    tool: str
    params: Dict[str, Any]


def _bootstrap_lines(tool_root: Path) -> list[str]:
    root = str(tool_root.resolve())
    return [
        "import sys",
        f"tool_root = {root!r}",
        "if tool_root not in sys.path:",
        "    sys.path.insert(0, tool_root)",
        "for _k in list(sys.modules.keys()):",
        "    if _k == 'bnk_serverlib' or _k.startswith('bnk_serverlib.'):",
        "        del sys.modules[_k]",
    ]


def make_tool_call_code(tool_root: Path, call: ServerlibCall) -> str:
    payload = {"tool": call.tool, "params": call.params}
    payload_json = json.dumps(payload, sort_keys=False)

    # note: we keep this bootstrap tiny and explicit so debugging is easy
    lines = ["import json"]
    lines.extend(_bootstrap_lines(tool_root))
    lines.extend(
        [
            "from bnk_serverlib.registry import call_tool",
            f"payload = json.loads({payload_json!r})",
            "__result__ = call_tool(payload['tool'], bv=bv, **(payload.get('params') or {}))",
        ]
    )
    return "\n".join(lines)


def make_tool_list_code(tool_root: Path) -> str:
    lines = _bootstrap_lines(tool_root)
    lines.extend(
        [
            "from bnk_serverlib.registry import list_tools",
            "__result__ = list_tools()",
        ]
    )
    return "\n".join(lines)
