# lineardisassembly module

| Class | Description |
| --- | --- |
| [`binaryninja.lineardisassembly.LinearDisassemblyLine`](#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine") |  |
| [`binaryninja.lineardisassembly.LinearViewCursor`](#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor") |  |
| [`binaryninja.lineardisassembly.LinearViewObject`](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") |  |
| [`binaryninja.lineardisassembly.LinearViewObjectIdentifier`](#binaryninja.lineardisassembly.LinearViewObjectIdentifier "binaryninja.lineardisassembly.LinearViewObjectIdentifier") |  |

## LinearDisassemblyLine

*class* LinearDisassemblyLine[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearDisassemblyLine)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*line_type: [LinearDisassemblyLineType](enums.md#binaryninja.enums.LinearDisassemblyLineType "binaryninja.enums.LinearDisassemblyLineType")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *block: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *contents: [DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearDisassemblyLine.__init__)
    :   Parameters:
        :   - **line_type**
              ([*LinearDisassemblyLineType*](enums.md#binaryninja.enums.LinearDisassemblyLineType
              "binaryninja.enums.LinearDisassemblyLineType")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **block** ([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock") *|* *None*) –
            - **contents**
              ([*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")) –

## LinearViewCursor

*class* LinearViewCursor[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*root_object: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.__init__)
    :   Parameters:
        :   **root_object** ([*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) –

    add_render_layer(*layer: [RenderLayer](renderlayer.md#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.add_render_layer)
    :   Add a Render Layer to be applied to this cursor. Note that layers will be applied in the
        order in which they are added.

        Parameters:
        :   **layer** ([*RenderLayer*](renderlayer.md#binaryninja.renderlayer.RenderLayer
            "binaryninja.renderlayer.RenderLayer")) – Render Layer to add

    *static* compare(*a: [LinearViewCursor](#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")*, *b: [LinearViewCursor](#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.compare)
    :   Parameters:
        :   - **a** ([*LinearViewCursor*](#binaryninja.lineardisassembly.LinearViewCursor
              "binaryninja.lineardisassembly.LinearViewCursor")) –
            - **b** ([*LinearViewCursor*](#binaryninja.lineardisassembly.LinearViewCursor
              "binaryninja.lineardisassembly.LinearViewCursor")) –

    duplicate() → [LinearViewCursor](#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.duplicate)
    :   Return type:
        :   [*LinearViewCursor*](#binaryninja.lineardisassembly.LinearViewCursor
            "binaryninja.lineardisassembly.LinearViewCursor")

    next() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.next)
    :   Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    previous() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.previous)
    :   Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_render_layer(*layer: [RenderLayer](renderlayer.md#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.remove_render_layer)
    :   Remove a Render Layer from being applied to this cursor

        Parameters:
        :   **layer** ([*RenderLayer*](renderlayer.md#binaryninja.renderlayer.RenderLayer
            "binaryninja.renderlayer.RenderLayer")) – Render Layer to remove

    seek_to_address(*addr*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.seek_to_address)

    seek_to_begin()[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.seek_to_begin)

    seek_to_end()[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.seek_to_end)

    seek_to_ordering_index(*idx*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.seek_to_ordering_index)

    seek_to_path(*path*, *addr=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewCursor.seek_to_path)

    *property* after_end

    *property* before_begin

    *property* current_object*: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* lines*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")]*

    *property* ordering_index

    *property* ordering_index_total

    *property* path*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearViewObjectIdentifier](#binaryninja.lineardisassembly.LinearViewObjectIdentifier "binaryninja.lineardisassembly.LinearViewObjectIdentifier")]*

    *property* path_objects*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")]*

    *property* render_layers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[RenderLayer](renderlayer.md#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer")]*
    :   Get the list of Render Layers which will be applied to this cursor, at the end of calls
        to lines().

        Returns:
        :   List of Render Layers

    *property* valid

## LinearViewObject

*class* LinearViewObject[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle*, *parent: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.__init__)
    :   Parameters:
        :   **parent** ([*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) –

    child_for_address(*addr*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.child_for_address)
    :   Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject") | *None*

    child_for_identifier(*ident*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.child_for_identifier)
    :   Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject") | *None*

    child_for_ordering_index(*idx*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.child_for_ordering_index)
    :   Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject") | *None*

    compare_children(*a*, *b*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.compare_children)

    *static* data_only(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.data_only)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* disassembly(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.disassembly)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    get_lines(*prev_obj*, *next_obj*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.get_lines)
    :   Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LinearDisassemblyLine*](#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine")]

    *static* hlil(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.hlil)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* hlil_ssa_form(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.hlil_ssa_form)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* language_representation(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *language: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'Pseudo C'*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.language_representation)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –
            - **language** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* lifted_il(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.lifted_il)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* llil(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.llil)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* llil_ssa_form(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.llil_ssa_form)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* mlil(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.mlil)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* mlil_ssa_form(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.mlil_ssa_form)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* mmlil(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.mmlil)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* mmlil_ssa_form(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.mmlil_ssa_form)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    ordering_index_for_child(*child*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.ordering_index_for_child)

    *static* single_function_disassembly(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_disassembly)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_hlil(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_hlil)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_hlil_ssa_form(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_hlil_ssa_form)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_language_representation(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *language: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'Pseudo C'*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_language_representation)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –
            - **language** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_lifted_il(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_lifted_il)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_llil(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_llil)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_llil_ssa_form(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_llil_ssa_form)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_mlil(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_mlil)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_mlil_ssa_form(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_mlil_ssa_form)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_mmlil(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_mmlil)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *static* single_function_mmlil_ssa_form(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObject.single_function_mmlil_ssa_form)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*LinearViewObject*](#binaryninja.lineardisassembly.LinearViewObject
            "binaryninja.lineardisassembly.LinearViewObject")

    *property* cursor*: [LinearViewCursor](#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")*

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* first_child*: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* identifier*: [LinearViewObjectIdentifier](#binaryninja.lineardisassembly.LinearViewObjectIdentifier "binaryninja.lineardisassembly.LinearViewObjectIdentifier")*

    *property* last_child*: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* next*: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* ordering_index

    *property* ordering_index_total

    *property* parent*: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* previous*: [LinearViewObject](#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LinearViewObjectIdentifier

*class* LinearViewObjectIdentifier[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObjectIdentifier)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineardisassembly.html#LinearViewObjectIdentifier.__init__)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

    *property* address

    *property* end

    *property* has_address

    *property* has_range

    *property* name

    *property* start
