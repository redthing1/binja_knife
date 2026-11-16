from __future__ import annotations

import unittest
from dataclasses import dataclass
from types import SimpleNamespace as NS

from knife.sessions import SessionError
from knife.type_info import TypeInfo


@dataclass(frozen=True)
class Name:
    parts: tuple[str, ...]

    def __str__(self):
        return "::".join(self.parts)


class Ty:
    def __init__(self, kind, text, width=4, **attrs):
        self.type_class = NS(
            name=kind + ("Class" if kind == "NamedTypeReference" else "TypeClass")
        )
        self.text, self.width, self.alignment = text, width, 1
        self.registered_name = None
        self.__dict__.update(attrs)

    def __str__(self):
        return self.text


def member(name, ty, offset=0, *, base=None, base_offset=0, bits=0, bit_position=0):
    return NS(
        base=base,
        base_offset=base_offset,
        member=NS(
            name=name, type=ty, offset=offset, bit_width=bits, bit_position=bit_position
        ),
    )


def structure(text, members, width=16, variant="Struct"):
    return Ty(
        "Structure",
        text,
        width,
        type=NS(name=variant + "StructureType"),
        members_including_inherited=lambda view: members,
    )


class View:
    def __init__(self, entries):
        self.types = {name: ty for name, _, ty in entries}
        self.ids = {name: identity for name, identity, _ in entries}
        self.by_id = {identity: ty for _, identity, ty in entries}

    def get_type_id(self, name):
        return self.ids[name]

    def get_type_by_id(self, identity):
        return self.by_id.get(identity)

    @property
    def functions(self):
        raise AssertionError("type inspection must not request function analysis")


def reference(view, identity, name):
    return Ty(
        "NamedTypeReference",
        name,
        4,
        type_id=identity,
        name=name,
        target=lambda _: view.get_type_by_id(identity),
    )


class TypeInfoTests(unittest.TestCase):
    def test_qualified_identity_and_ambiguous_spelling(self):
        first, second = Name(("demo", "T")), Name(("demo::T",))
        a, b = Ty("Integer", "a"), Ty("Integer", "b")
        info = TypeInfo(View([(first, "a", a), (second, "b", b)]))
        with self.assertRaises(SessionError) as error:
            info.resolve("type:demo::T")
        self.assertEqual(error.exception.details["candidates"], ["type:#a", "type:#b"])
        self.assertIs(info.resolve("type:#a").name, first)
        self.assertIs(info.resolve("type:#b").ty, b)
        found, _ = info.find("DEMO", False, 10)
        self.assertEqual([item["target"] for item in found], ["type:#a", "type:#b"])

    def test_find_limits_case_and_reserved_names(self):
        ty = Ty("Integer", "int")
        info = TypeInfo(
            View(
                [
                    (Name(("Packet",)), "p", ty),
                    (Name(("#Packet",)), "r", ty),
                    (Name(("Packet\nHeader",)), "s", ty),
                ]
            )
        )
        found, more = info.find("packet", False, 1)
        self.assertTrue(more)
        self.assertEqual(found[0]["target"], "type:Packet")
        self.assertEqual(info.find("packet", True, 10), ([], False))
        self.assertEqual(info.find("#Packet", True, 10)[0][0]["target"], "type:#r")
        self.assertEqual(
            info.find("Packet\nHeader", True, 10)[0][0]["target"], "type:#s"
        )

    def test_pointer_hops_preserve_local_offsets_and_inherited_members(self):
        integer = Ty("Integer", "uint32_t")
        base = Ty("NamedTypeReference", "Base", type_id="base", name="Base")
        child = structure(
            "Child", [member("id", integer, 10, base=base, base_offset=8)]
        )
        view = View([(Name(("Child",)), "c", child)])
        ptr = Ty("Pointer", "Child*", 4, target=reference(view, "c", "Child"))
        parent = structure("Parent", [member("parameters", ptr, 4)])
        info = TypeInfo(view)
        result = info.describe(parent, fields=["parameters", "id"], limit=10)
        self.assertEqual([s["offset"] for s in result["steps"]], [4, 10])
        self.assertEqual(result["steps"][1]["base"]["text"], "Base")
        self.assertEqual(result["steps"][1]["base"]["offset"], 8)
        self.assertEqual(result["selected"]["size"], 4)
        pointer_layout = info.describe(ptr, fields=[], limit=10)
        self.assertEqual(pointer_layout["pointer_size"], 4)
        self.assertEqual(pointer_layout["layout"]["size"], 16)
        view.by_id["ptr"] = ptr
        alias_layout = info.describe(
            reference(view, "ptr", "ChildPtr"), fields=[], limit=10
        )
        self.assertEqual(alias_layout["pointer_size"], 4)
        self.assertEqual(alias_layout["layout"]["size"], 16)

    def test_anonymous_union_bitfields_and_limits(self):
        integer = Ty("Integer", "unsigned int")
        union = structure(
            "union", [member("a", integer), member("b", integer)], 4, "Union"
        )
        parent = structure(
            "Parent",
            [
                member("payload", union, 4),
                member("flags", integer, 8, bits=3, bit_position=2),
            ],
        )
        info = TypeInfo(View([]))
        result = info.describe(parent, fields=["payload"], limit=1)
        self.assertEqual(result["variant"], "union")
        self.assertTrue(result["more"])
        result = info.describe(parent, fields=[], limit=10)
        self.assertEqual(
            (result["members"][1]["bits"], result["members"][1]["bit_position"]), (3, 2)
        )

    def test_alias_resolution_unresolved_and_cycles(self):
        integer = Ty("Integer", "int")
        view = View([(Name(("Int",)), "i", integer)])
        alias = reference(view, "i", "Int")
        info = TypeInfo(view)
        self.assertEqual(
            info.describe(alias, fields=[], limit=1)["layout"]["kind"], "Integer"
        )
        missing = reference(view, "missing", "Missing")
        self.assertIn("unresolved", info.describe(missing, fields=[], limit=1))
        view.by_id["loop"] = loop = reference(view, "loop", "Loop")
        self.assertEqual(
            info.describe(loop, fields=[], limit=1)["unresolved"],
            "cyclic type reference",
        )

    def test_recursive_pointer_is_summarized_without_expanding_children(self):
        members = []
        node = structure("Node", members)
        view = View([(Name(("Node",)), "n", node)])
        ptr = Ty("Pointer", "Node*", 8, target=reference(view, "n", "Node"))
        members.append(member("next", ptr))
        result = TypeInfo(view).describe(node, fields=[], limit=10)
        self.assertEqual(len(result["members"]), 1)
        self.assertEqual(result["members"][0]["type"]["pointee"]["target"], "type:Node")

    def test_enum_array_and_field_errors(self):
        integer = Ty("Integer", "byte", 1)
        enum = Ty(
            "Enumeration",
            "Mode",
            1,
            members=[NS(name="A", value=-1), NS(name="B", value=2)],
        )
        array = Ty("Array", "byte[3]", 3, element_type=integer, count=3)
        info = TypeInfo(View([]))
        self.assertTrue(info.describe(enum, fields=[], limit=1)["more"])
        self.assertEqual(info.describe(array, fields=[], limit=1)["layout"]["count"], 3)
        parent = structure("Parent", [member("x", integer), member("x", integer)])
        for target, field in [(parent, "x"), (parent, "missing"), (integer, "x")]:
            with self.assertRaises(SessionError):
                info.describe(target, fields=[field], limit=5)
