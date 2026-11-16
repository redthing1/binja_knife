from __future__ import annotations

from dataclasses import dataclass
from itertools import islice
from typing import Any

from .sessions import SessionError


@dataclass(frozen=True)
class NamedType:
    name: Any
    id: str
    ty: Any


def is_type_target(target: str) -> bool:
    return target.startswith("type:")


def _kind(ty: Any) -> str:
    return ty.type_class.name.removesuffix("Class").removesuffix("Type")


class TypeInfo:
    """Type lookup and description within one request."""

    def __init__(self, view: Any) -> None:
        self.view = view
        self._ids: dict[str, NamedType] | None = None
        self._names: dict[str, list[NamedType]] = {}

    def _load(self) -> dict[str, NamedType]:
        if self._ids is None:
            self._ids = {}
            for name, ty in self.view.types.items():
                entry = NamedType(name, self.view.get_type_id(name), ty)
                self._ids[entry.id] = entry
                self._names.setdefault(str(name), []).append(entry)
        return self._ids

    def selector(self, entry: NamedType) -> str:
        name = str(entry.name)
        if (
            name.isprintable()
            and not name.startswith("#")
            and len(self._names[name]) == 1
        ):
            return f"type:{name}"
        return f"type:#{entry.id}"

    def resolve(self, selector: str) -> NamedType:
        entries = self._load()
        name = selector.removeprefix("type:")
        if name.startswith("#"):
            entry = entries.get(name[1:])
            matches = [entry] if entry is not None else []
        else:
            matches = self._names.get(name, [])
        if len(matches) == 1:
            return matches[0]
        if matches:
            raise SessionError(
                f"type name '{name}' is ambiguous",
                kind="target_ambiguous",
                details={"candidates": [f"type:#{item.id}" for item in matches[:8]]},
            )
        raise SessionError(f"type not found: {name}", kind="target_not_found")

    def find(
        self, query: str | None, case_sensitive: bool, limit: int
    ) -> tuple[list[dict], bool]:
        needle = query or ""
        if not case_sensitive:
            needle = needle.casefold()
        found = []
        for entry in self._load().values():
            name = str(entry.name)
            if needle not in (name if case_sensitive else name.casefold()):
                continue
            found.append(
                {**self.summary(entry.ty), "name": name, "target": self.selector(entry)}
            )
            if len(found) > limit:
                break
        return found[:limit], len(found) > limit

    def _brief(self, ty: Any) -> dict:
        result = {
            "text": str(ty),
            "kind": _kind(ty),
            "size": int(ty.width),
            "alignment": int(ty.alignment),
        }
        reference = ty.registered_name
        if reference is None and _kind(ty) == "NamedTypeReference":
            reference = ty
        if reference is not None:
            entry = self._load().get(reference.type_id)
            if entry is not None:
                result["target"] = self.selector(entry)
        return result

    def summary(self, ty: Any) -> dict:
        result = self._brief(ty)
        if _kind(ty) == "Pointer":
            result["pointee"] = self._brief(ty.target)
        elif _kind(ty) == "Array":
            result["element"] = self._brief(ty.element_type)
            result["count"] = int(ty.count)
        return result

    def _unalias(self, ty: Any) -> tuple[Any, list[str], str | None]:
        seen = set()
        aliases = []
        while _kind(ty) == "NamedTypeReference":
            key = (ty.type_id, str(ty.name))
            if key in seen:
                return ty, aliases, "cyclic type reference"
            seen.add(key)
            aliases.append(str(ty.name))
            target = ty.target(self.view)
            if target is None:
                return ty, aliases, f"unresolved type: {ty.name}"
            ty = target
        return ty, aliases, None

    def _layout(self, ty: Any) -> tuple[Any, list[str], str | None, int | None]:
        ty, aliases, problem = self._unalias(ty)
        pointer_size = None
        if problem is None and _kind(ty) == "Pointer":
            pointer_size = int(ty.width)
            ty, more, problem = self._unalias(ty.target)
            aliases.extend(more)
        return ty, aliases, problem, pointer_size

    def _member(self, inherited: Any) -> dict:
        member = inherited.member
        # The API has already adjusted inherited member offsets to the containing structure.
        result = {
            "name": member.name,
            "offset": int(member.offset),
            "type": self.summary(member.type),
            "bits": int(member.bit_width),
            "bit_position": int(member.bit_position),
        }
        if inherited.base is not None:
            result["base"] = {
                **self._brief(inherited.base),
                "offset": int(inherited.base_offset),
            }
        return result

    def describe(
        self, ty: Any, *, fields: list[str], limit: int, named: NamedType | None = None
    ) -> dict:
        result: dict = {"type": self.summary(ty), "steps": []}
        if named is not None:
            result.update(
                name=str(named.name),
                target=self.selector(named),
                exact=f"type:#{named.id}",
            )
        for field in fields:
            parent, _, problem, _ = self._layout(ty)
            if problem:
                raise SessionError(problem, kind="type")
            if _kind(parent) != "Structure":
                raise SessionError(f"{parent} has no fields", kind="type")
            matches = [
                m
                for m in parent.members_including_inherited(self.view)
                if m.member.name == field
            ]
            if len(matches) != 1:
                message = "ambiguous field" if matches else "field not found"
                raise SessionError(f"{message}: {field}", kind="type")
            selected = matches[0]
            result["steps"].append({"parent": str(parent), **self._member(selected)})
            ty = selected.member.type
        if fields:
            result["selected"] = self.summary(ty)
        layout, aliases, problem, pointer_size = self._layout(ty)
        result.update(layout=self.summary(layout), aliases=aliases)
        if pointer_size is not None:
            result["pointer_size"] = pointer_size
        if problem:
            result["unresolved"] = problem
        elif _kind(layout) == "Structure":
            result["variant"] = layout.type.name.removesuffix("StructureType").lower()
            members = list(
                islice(layout.members_including_inherited(self.view), limit + 1)
            )
            result["members"] = [self._member(m) for m in members[:limit]]
            result["more"] = len(members) > limit
        elif _kind(layout) == "Enumeration":
            values = list(islice(layout.members, limit + 1))
            result["values"] = [
                {"name": value.name, "value": value.value} for value in values[:limit]
            ]
            result["more"] = len(values) > limit
        return result
