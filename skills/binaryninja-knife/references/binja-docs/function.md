# function module

| Class | Description |
| --- | --- |
| [`binaryninja.function.AdvancedFunctionAnalysisDataRequestor`](#binaryninja.function.AdvancedFunctionAnalysisDataRequestor "binaryninja.function.AdvancedFunctionAnalysisDataRequestor") |  |
| [`binaryninja.function.ArchAndAddr`](#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr") |  |
| [`binaryninja.function.BasicBlockList`](#binaryninja.function.BasicBlockList "binaryninja.function.BasicBlockList") |  |
| [`binaryninja.function.DisassemblySettings`](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | `class DisassemblySettings` contains the options used when rendering disassembly or IL text. |
| [`binaryninja.function.DisassemblyTextLine`](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine") |  |
| [`binaryninja.function.DisassemblyTextLineTypeInfo`](#binaryninja.function.DisassemblyTextLineTypeInfo "binaryninja.function.DisassemblyTextLineTypeInfo") |  |
| [`binaryninja.function.DisassemblyTextRenderer`](#binaryninja.function.DisassemblyTextRenderer "binaryninja.function.DisassemblyTextRenderer") |  |
| [`binaryninja.function.Function`](#binaryninja.function.Function "binaryninja.function.Function") |  |
| [`binaryninja.function.FunctionViewType`](#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType") |  |
| [`binaryninja.function.HighLevelILBasicBlockList`](#binaryninja.function.HighLevelILBasicBlockList "binaryninja.function.HighLevelILBasicBlockList") |  |
| [`binaryninja.function.ILReferenceSource`](#binaryninja.function.ILReferenceSource "binaryninja.function.ILReferenceSource") |  |
| [`binaryninja.function.LowLevelILBasicBlockList`](#binaryninja.function.LowLevelILBasicBlockList "binaryninja.function.LowLevelILBasicBlockList") |  |
| [`binaryninja.function.MediumLevelILBasicBlockList`](#binaryninja.function.MediumLevelILBasicBlockList "binaryninja.function.MediumLevelILBasicBlockList") |  |
| [`binaryninja.function.TagList`](#binaryninja.function.TagList "binaryninja.function.TagList") |  |
| [`binaryninja.function.VariableReferenceSource`](#binaryninja.function.VariableReferenceSource "binaryninja.function.VariableReferenceSource") |  |

## AdvancedFunctionAnalysisDataRequestor

*class* AdvancedFunctionAnalysisDataRequestor[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#AdvancedFunctionAnalysisDataRequestor)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*func: [Function](#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#AdvancedFunctionAnalysisDataRequestor.__init__)
    :   Parameters:
        :   **func** ([*Function*](#binaryninja.function.Function "binaryninja.function.Function")
            *|* *None*)

    close() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#AdvancedFunctionAnalysisDataRequestor.close)
    :   Return type:
        :   *None*

    *property* function*: [Function](#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## ArchAndAddr

*class* ArchAndAddr[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#ArchAndAddr)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    addr*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

## BasicBlockList

*class* BasicBlockList[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#BasicBlockList)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*function: [Function](#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#BasicBlockList.__init__)
    :   Parameters:
        :   **function** ([*Function*](#binaryninja.function.Function
            "binaryninja.function.Function") *|*
            [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
            "binaryninja.lowlevelil.LowLevelILFunction") *|*
            [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
            "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
            [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
            "binaryninja.highlevelil.HighLevelILFunction"))

## DisassemblySettings

*class* DisassemblySettings[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class DisassemblySettings` contains the options used when rendering disassembly or IL
    text.

    Note

    Not every [`DisassemblyOption`](enums.md#binaryninja.enums.DisassemblyOption
    "binaryninja.enums.DisassemblyOption") applies to every representation. `IndentHLILBody`
    and `ShowAddress` are applied by linear view, not by
    [`get_lines`](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction.get_lines
    "binaryninja.highlevelil.HighLevelILInstruction.get_lines"); options acting on nested
    bodies, such as `ShowCollapseIndicators`, only apply to HLIL in AST form. See [AST and
    Non-AST Forms](https://docs.binary.ninja/dev/bnil-hlil.html#ast-and-non-ast-forms).

    __init__(*handle: LP_BNDisassemblySettings | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings.__init__)
    :   Parameters:
        :   **handle** (*LP_BNDisassemblySettings* *|* *None*)

    *static* default_graph_settings() → [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings.default_graph_settings)
    :   Return type:
        :   [*DisassemblySettings*](#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings")

    *static* default_linear_settings() → [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings.default_linear_settings)
    :   Return type:
        :   [*DisassemblySettings*](#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings")

    *static* default_settings() → [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings.default_settings)
    :   Return type:
        :   [*DisassemblySettings*](#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings")

    is_option_set(*option: [DisassemblyOption](enums.md#binaryninja.enums.DisassemblyOption "binaryninja.enums.DisassemblyOption")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings.is_option_set)
    :   Parameters:
        :   **option** ([*DisassemblyOption*](enums.md#binaryninja.enums.DisassemblyOption
            "binaryninja.enums.DisassemblyOption"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_option(*option: [DisassemblyOption](enums.md#binaryninja.enums.DisassemblyOption "binaryninja.enums.DisassemblyOption")*, *state: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblySettings.set_option)
    :   Parameters:
        :   - **option** ([*DisassemblyOption*](enums.md#binaryninja.enums.DisassemblyOption
              "binaryninja.enums.DisassemblyOption"))
            - **state** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)"))

        Return type:
        :   *None*

    *property* max_symbol_width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## DisassemblyTextLine

*class* DisassemblyTextLine[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextLine)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*tokens: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *il_instr: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *color: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor") | [HighlightStandardColor](enums.md#binaryninja.enums.HighlightStandardColor "binaryninja.enums.HighlightStandardColor") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *tags: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *type_info: [DisassemblyTextLineTypeInfo](#binaryninja.function.DisassemblyTextLineTypeInfo "binaryninja.function.DisassemblyTextLineTypeInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextLine.__init__)
    :   Parameters:
        :   - **tokens** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
              "binaryninja.architecture.InstructionTextToken")*]*)
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)
            - **il_instr**
              ([*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction") *|*
              [*MediumLevelILInstruction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction") *|*
              [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction") *|* *None*)
            - **color** ([*HighlightColor*](highlight.md#binaryninja.highlight.HighlightColor
              "binaryninja.highlight.HighlightColor") *|*
              [*HighlightStandardColor*](enums.md#binaryninja.enums.HighlightStandardColor
              "binaryninja.enums.HighlightStandardColor") *|* *None*)
            - **tags** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tag*](binaryview.md#binaryninja.binaryview.Tag
              "binaryninja.binaryview.Tag")*]* *|* *None*)
            - **type_info**
              ([*DisassemblyTextLineTypeInfo*](#binaryninja.function.DisassemblyTextLineTypeInfo
              "binaryninja.function.DisassemblyTextLineTypeInfo") *|* *None*)

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* address_and_indentation_tokens

    *property* address_and_indentation_width

    highlight*: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor")*

    il_instruction*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    tags*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]*

    tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*

    *property* total_width

    type_info*: [DisassemblyTextLineTypeInfo](#binaryninja.function.DisassemblyTextLineTypeInfo "binaryninja.function.DisassemblyTextLineTypeInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## DisassemblyTextLineTypeInfo

*class* DisassemblyTextLineTypeInfo[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextLineTypeInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*parent_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *field_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **parent_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              *None*)
            - **field_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    field_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    parent_type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## DisassemblyTextRenderer

*class* DisassemblyTextRenderer[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*func: [Function](#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *settings: [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: BNDisassemblySettings | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.__init__)
    :   Parameters:
        :   - **func** ([*Function*](#binaryninja.function.Function "binaryninja.function.Function")
              *|* [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction") *|* *None*)
            - **settings** ([*DisassemblySettings*](#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*)
            - **handle** (*BNDisassemblySettings* *|* *None*)

    add_integer_token(*tokens: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*, *int_token: [InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.add_integer_token)
    :   Parameters:
        :   - **tokens** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
              "binaryninja.architecture.InstructionTextToken")*]*)
            - **int_token**
              ([*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
              "binaryninja.architecture.InstructionTextToken"))
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    add_stack_var_reference_tokens(*tokens: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*, *ref: [StackVariableReference](variable.md#binaryninja.variable.StackVariableReference "binaryninja.variable.StackVariableReference")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.add_stack_var_reference_tokens)
    :   Parameters:
        :   - **tokens** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
              "binaryninja.architecture.InstructionTextToken")*]*)
            - **ref**
              ([*StackVariableReference*](variable.md#binaryninja.variable.StackVariableReference
              "binaryninja.variable.StackVariableReference"))

        Return type:
        :   *None*

    add_symbol_token(*tokens: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.add_symbol_token)
    :   Parameters:
        :   - **tokens** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
              "binaryninja.architecture.InstructionTextToken")*]*)
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_disassembly_text(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[DisassemblyTextLine](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.get_disassembly_text)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*DisassemblyTextLine*](#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine") | *None*,
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")],
            *None*, *None*]

    *static* get_display_string_for_integer(*binary_view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *display_type: [IntegerDisplayType](enums.md#binaryninja.enums.IntegerDisplayType "binaryninja.enums.IntegerDisplayType")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *input_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *is_signed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.get_display_string_for_integer)
    :   Parameters:
        :   - **binary_view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)
            - **display_type** ([*IntegerDisplayType*](enums.md#binaryninja.enums.IntegerDisplayType
              "binaryninja.enums.IntegerDisplayType"))
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **input_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **is_signed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_instruction_annotations(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.get_instruction_annotations)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    get_instruction_text(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[DisassemblyTextLine](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.get_instruction_text)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*DisassemblyTextLine*](#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine") | *None*,
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")],
            *None*, *None*]

    *static* is_integer_token(*token: [InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.is_integer_token)
    :   Parameters:
        :   **token**
            ([*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    post_process_lines(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *in_lines: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*, *indent_spaces: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.post_process_lines)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **in_lines** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*DisassemblyTextLine*](#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*)
            - **indent_spaces** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))

    reset_deduplicated_comments() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.reset_deduplicated_comments)
    :   Return type:
        :   *None*

    wrap_comment(*lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*, *cur_line: [DisassemblyTextLine](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")*, *comment: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *has_auto_annotations: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *leading_spaces: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '  '*, *indent_spaces: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#DisassemblyTextRenderer.wrap_comment)
    :   Parameters:
        :   - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DisassemblyTextLine*](#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*)
            - **cur_line** ([*DisassemblyTextLine*](#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine"))
            - **comment** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **has_auto_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)"))
            - **leading_spaces** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **indent_spaces** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))

        Return type:
        :   *None*

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    *property* basic_block*: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* function*: [Function](#binaryninja.function.Function "binaryninja.function.Function")*

    *property* has_data_flow*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* il*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* il_function*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* settings*: [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings")*

## Function

*class* Function[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: LP_BNFunction | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)
            - **handle** (*LP_BNFunction* *|* *None*)

    add_guided_source_blocks(*addresses: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.add_guided_source_blocks)
    :   `add_guided_source_blocks` adds blocks to the guided source block list for this
        function. The specified blocks will have their direct outgoing branch targets analyzed.
        This automatically enables the `analysis.guided.enable` setting if it is not already
        enabled.

        Parameters:
        :   - **addresses** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python
              v3.14)")*[*[*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]**]*)
              – List of (architecture, address) tuples to add
            - **addresses**

        Return type:
        :   *None*

    add_tag(*tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *data: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.add_tag)
    :   `add_tag` creates and adds a `Tag` object on either a function, or on an address inside
        of a function.

        “Function tags” appear at the top of a function and are a good way to label an entire
        function with some information. If you include an address when you call
        Function.add_tag, you’ll create an “address tag”. These are good for labeling specific
        instructions.

        For tagging arbitrary data, consider
        [`add_tag`](binaryview.md#binaryninja.binaryview.BinaryView.add_tag
        "binaryninja.binaryview.BinaryView.add_tag").

        Parameters:
        :   - **tag_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The name of the tag type for this Tag
            - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – additional data for the Tag
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to add the tag
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether or not an auto tag
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for the block in which the Tag
              is added (optional)

        Example:
        :   ```
            >>> current_function.add_tag("Important", "I think this is the main function")
            >>> current_function.add_tag("Crashes", "Nullpointer dereference", here)
            ```

        Warning: For performance reasons, this function does not ensure the address you have
        supplied is within the function’s bounds.

    add_user_code_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *to_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.add_user_code_ref)
    :   `add_user_code_ref` places a user-defined cross-reference from the instruction at the
        given address and architecture to the specified target address. If the specified source
        instruction is not contained within this function, no action is performed. To remove the
        reference, use
        [`remove_user_code_ref`](#binaryninja.function.Function.remove_user_code_ref
        "binaryninja.function.Function.remove_user_code_ref").

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the source instruction
            - **to_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the xref’s destination.
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) architecture of the source
              instruction

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.add_user_code_ref(here, 0x400000)
            ```

    add_user_type_field_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: types.QualifiedNameType*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *from_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.add_user_type_field_ref)
    :   `add_user_type_field_ref` places a user-defined type field cross-reference from the
        instruction at the given address and architecture to the specified type. If the
        specified source instruction is not contained within this function, no action is
        performed. To remove the reference, use
        [`remove_user_type_field_ref`](#binaryninja.function.Function.remove_user_type_field_ref
        "binaryninja.function.Function.remove_user_type_field_ref").

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the source instruction
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of the referenced type
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field, relative to the type
            - **from_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) architecture of the source
              instruction
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – (optional) the size of the access

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.add_user_type_field_ref(here, 'A', 0x8)
            ```

    add_user_type_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: types.QualifiedNameType*, *from_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.add_user_type_ref)
    :   `add_user_type_ref` places a user-defined type cross-reference from the instruction at
        the given address and architecture to the specified type. If the specified source
        instruction is not contained within this function, no action is performed. To remove the
        reference, use
        [`remove_user_type_ref`](#binaryninja.function.Function.remove_user_type_ref
        "binaryninja.function.Function.remove_user_type_ref").

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the source instruction
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of the referenced type
            - **from_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) architecture of the source
              instruction

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.add_user_code_ref(here, 'A')
            ```

    analyze() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.analyze)
    :   `analyze` causes this function to be analyzed if it’s out of date. This function does
        not wait for the analysis to finish.

        Return type:
        :   *None*

    apply_auto_discovered_type(*func_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.apply_auto_discovered_type)
    :   Parameters:
        :   **func_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
            [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))

        Return type:
        :   *None*

    apply_imported_types(*sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.apply_imported_types)
    :   Parameters:
        :   - **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol"))
            - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")
              *|* *None*)

        Return type:
        :   *None*

    check_for_debug_report(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.check_for_debug_report)
    :   `check_for_debug_report` checks if a function has had a debug report requested with the
        given name, and then, if one has been requested, clears the request internally so that
        future calls to this function for that report will return False.

        If a function has had a debug report requested, it is the caller of this function’s
        responsibility to actually generate and show the debug report. You can use
        [`binaryninja.interaction.show_report_collection`](interaction.md#binaryninja.interaction.show_report_collection
        "binaryninja.interaction.show_report_collection") for showing a debug report from a
        workflow activity.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the debug report

        Returns:
        :   True if the report has been requested (and not checked for yet)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    clear_all_user_var_values() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.clear_all_user_var_values)
    :   Clear all user defined variable values.

        Return type:
        :   *None*

    clear_forced_var_version(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *def_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.clear_forced_var_version)
    :   Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable"))
            - **def_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    clear_user_var_value(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *def_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *after: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.clear_user_var_value)
    :   Clears a previously defined user variable value.

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – Variable for which the value was informed
            - **def_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the definition site of the variable
            - **after** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)"))

        Return type:
        :   *None*

    collapse_region(*hash*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.collapse_region)
    :   Collapse a region during rendering :param hash: Hash value of region

    create_auto_stack_var(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *var_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_auto_stack_var)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **var_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    create_auto_var(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *var_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ignore_disjoint_uses: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_auto_var)
    :   Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable"))
            - **var_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **ignore_disjoint_uses** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)"))

        Return type:
        :   *None*

    create_forced_var_version(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *def_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_forced_var_version)
    :   Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable"))
            - **def_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    create_graph(*graph_type: [FunctionViewType](#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType") | [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = FunctionGraphType.NormalFunctionGraph*, *settings: [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_graph)
    :   Create a flow graph with the disassembly of this function.

        Note

        This graph waits for function analysis, so Workflow Activities should instead use
        [`create_graph_immediate`](#binaryninja.function.Function.create_graph_immediate
        "binaryninja.function.Function.create_graph_immediate") to create graphs with the
        function contents as-is.

        Parameters:
        :   - **graph_type** ([*FunctionViewType*](#binaryninja.function.FunctionViewType
              "binaryninja.function.FunctionViewType") *|*
              [*FunctionGraphType*](enums.md#binaryninja.enums.FunctionGraphType
              "binaryninja.enums.FunctionGraphType") *|*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – IL
              form of the disassembly in the graph
            - **settings** ([*DisassemblySettings*](#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) – Optional settings for the
              disassembly text renderer

        Returns:
        :   Flow graph object

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    create_graph_immediate(*graph_type: [FunctionViewType](#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType") | [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = FunctionGraphType.NormalFunctionGraph*, *settings: [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_graph_immediate)
    :   Create a flow graph with the disassembly of this function, specifically using the
        instructions as they are in the function when this is called. You probably want to use
        this if you are creating a Debug Report in a Workflow Activity.

        Parameters:
        :   - **graph_type** ([*FunctionViewType*](#binaryninja.function.FunctionViewType
              "binaryninja.function.FunctionViewType") *|*
              [*FunctionGraphType*](enums.md#binaryninja.enums.FunctionGraphType
              "binaryninja.enums.FunctionGraphType") *|*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – IL
              form of the disassembly in the graph
            - **settings** ([*DisassemblySettings*](#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) – Optional settings for the
              disassembly text renderer

        Returns:
        :   Flow graph object

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    create_user_stack_var(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *var_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_user_stack_var)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **var_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    create_user_var(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *var_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ignore_disjoint_uses: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.create_user_var)
    :   Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable"))
            - **var_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **ignore_disjoint_uses** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)"))

        Return type:
        :   *None*

    delete_auto_stack_var(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.delete_auto_stack_var)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   *None*

    delete_user_stack_var(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.delete_user_stack_var)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   *None*

    delete_user_var(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.delete_user_var)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable"))

        Return type:
        :   *None*

    expand_all()[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.expand_all)
    :   Expand all regions in the function

    expand_region(*hash*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.expand_region)
    :   Un-collapse a region during rendering :param hash: Hash value of region

    get_all_user_var_values() → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable"), [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")]][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_all_user_var_values)
    :   Returns a map of current defined user variable values.

        Returns:
        :   Map of user current defined user variable values and their definition sites.

        Type:
        :   [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of
            ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable"),
            [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of
            ([*ArchAndAddr*](#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"),
            [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")))

        Return type:
        :   [*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
            v3.14)")[[*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable"),
            [*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
            v3.14)")[[*ArchAndAddr*](#binaryninja.function.ArchAndAddr
            "binaryninja.function.ArchAndAddr"),
            [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")]]

    get_basic_block_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_basic_block_at)
    :   `get_basic_block_at` returns the BasicBlock of the optionally specified Architecture
        `arch` at the given address `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the BasicBlock to retrieve.
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the basic block
              if different from the Function’s self.arch

        Example:
        :   ```
            >>> current_function.get_basic_block_at(current_function.start)
            <block: x86_64@0x100000f30-0x100000f50>
            ```

        Return type:
        :   [*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock") | *None*

    get_block_annotations(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_block_annotations)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]]

    get_block_sort_hint(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_block_sort_hint)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    get_call_reg_stack_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [RegisterStackAdjustmentWithConfidence](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_call_reg_stack_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
            v3.14)")[*RegisterStackName*,
            [*RegisterStackAdjustmentWithConfidence*](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence
            "binaryninja.types.RegisterStackAdjustmentWithConfidence")]

    get_call_reg_stack_adjustment_for_reg_stack(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: RegisterStackName | [ILRegisterStack](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | RegisterStackIndex*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterStackAdjustmentWithConfidence](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_call_reg_stack_adjustment_for_reg_stack)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **reg_stack** (*RegisterStackName* *|*
              [*ILRegisterStack*](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack
              "binaryninja.lowlevelil.ILRegisterStack") *|* *RegisterStackIndex*)
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*RegisterStackAdjustmentWithConfidence*](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence
            "binaryninja.types.RegisterStackAdjustmentWithConfidence")

    get_call_stack_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [OffsetWithConfidence](types.md#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_call_stack_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*OffsetWithConfidence*](types.md#binaryninja.types.OffsetWithConfidence
            "binaryninja.types.OffsetWithConfidence")

    get_call_type_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_call_type_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*

    get_callee_for_analysis(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *exact: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Function](#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_callee_for_analysis)
    :   `get_callee_for_analysis` retrieves the callee function for the specified address and
        platform.

        Note

        This method is intended for use by architecture plugins only.

        Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform of the callee function
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the callee function
            - **exact** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If True, only return a function if it exactly matches the address and
              platform

        Returns:
        :   The callee function or None if not found

        Return type:
        :   *Optional*[[*Function*](#binaryninja.function.Function "binaryninja.function.Function")]

    get_comment_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_comment_at)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_constant_data(*state: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_constant_data)
    :   Parameters:
        :   - **state** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer")

    get_constant_data_and_builtin(*state: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [BuiltinType](enums.md#binaryninja.enums.BuiltinType "binaryninja.enums.BuiltinType")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_constant_data_and_builtin)
    :   Parameters:
        :   - **state** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer"),
            [*BuiltinType*](enums.md#binaryninja.enums.BuiltinType "binaryninja.enums.BuiltinType")]

    get_constants_referenced_by(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ConstantReference](variable.md#binaryninja.variable.ConstantReference "binaryninja.variable.ConstantReference")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_constants_referenced_by)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ConstantReference*](variable.md#binaryninja.variable.ConstantReference
            "binaryninja.variable.ConstantReference")]

    get_constants_referenced_by_address_if_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ConstantReference](variable.md#binaryninja.variable.ConstantReference "binaryninja.variable.ConstantReference")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_constants_referenced_by_address_if_available)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ConstantReference*](variable.md#binaryninja.variable.ConstantReference
            "binaryninja.variable.ConstantReference")]

    get_early_return(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → [EarlyReturn](enums.md#binaryninja.enums.EarlyReturn "binaryninja.enums.EarlyReturn")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_early_return)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|*
            [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction"))

        Return type:
        :   [*EarlyReturn*](enums.md#binaryninja.enums.EarlyReturn "binaryninja.enums.EarlyReturn")

    get_expr_folding(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → [ExprFolding](enums.md#binaryninja.enums.ExprFolding "binaryninja.enums.ExprFolding")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_expr_folding)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|*
            [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction"))

        Return type:
        :   [*ExprFolding*](enums.md#binaryninja.enums.ExprFolding "binaryninja.enums.ExprFolding")

    get_flags_read_by_lifted_il_instruction(*i: InstructionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_flags_read_by_lifted_il_instruction)
    :   Parameters:
        :   **i** (*InstructionIndex*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[*FlagName*]

    get_flags_written_by_lifted_il_instruction(*i: InstructionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_flags_written_by_lifted_il_instruction)
    :   Parameters:
        :   **i** (*InstructionIndex*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[*FlagName*]

    get_function_tags(*auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_function_tags)
    :   `get_function_tags` gets a list of function Tags for the function.

        Parameters:
        :   - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If None, gets all tags, if True, gets auto tags, if False, gets user tags
            - **tag_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – If None, gets all tags, otherwise only gets tags of the given type

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))

    get_guided_source_blocks() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_guided_source_blocks)
    :   `get_guided_source_blocks` returns the current list of guided source blocks for this
        function. These blocks have their direct outgoing branch targets analyzed.

        Return type:
        :   *List*[*Tuple*[[*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]

        Returns:
        :   List of (architecture, address) tuples representing current guided source blocks

    get_hlil_var_refs(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILReferenceSource](#binaryninja.function.ILReferenceSource "binaryninja.function.ILReferenceSource")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_hlil_var_refs)
    :   `get_hlil_var_refs` returns a list of ILReferenceSource objects (IL xrefs or
        cross-references) that reference the given variable. The variable is a local variable
        that can be either on the stack, in a register, or in a flag.

        Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) – Variable for which to query the xref

        Returns:
        :   List of IL References for the given variable

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*ILReferenceSource*](#binaryninja.function.ILReferenceSource
            "binaryninja.function.ILReferenceSource"))

        Example:
        :   ```
            >>> mlil_var = current_hlil[0].operands[0]
            >>> current_function.get_hlil_var_refs(mlil_var)
            ```

    get_hlil_var_refs_from(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[VariableReferenceSource](#binaryninja.function.VariableReferenceSource "binaryninja.function.VariableReferenceSource")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_hlil_var_refs_from)
    :   `get_hlil_var_refs_from` returns a list of variables referenced by code in the function
        `func`, of the architecture `arch`, and at the address `addr`. If no function is
        specified, references from all functions and containing the address will be returned. If
        no architecture is specified, the architecture of the function will be used.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for variable references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – optional architecture of query

        Returns:
        :   list of variables reference sources

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*VariableReferenceSource*](#binaryninja.function.VariableReferenceSource
            "binaryninja.function.VariableReferenceSource"))

    get_indirect_branches_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IndirectBranchInfo](variable.md#binaryninja.variable.IndirectBranchInfo "binaryninja.variable.IndirectBranchInfo")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_indirect_branches_at)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*IndirectBranchInfo*](variable.md#binaryninja.variable.IndirectBranchInfo
            "binaryninja.variable.IndirectBranchInfo")]

    get_instr_highlight(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_instr_highlight)
    :   Example:
        :   ```
            >>> current_function.set_user_instr_highlight(here, highlight.HighlightColor(red=0xff, blue=0xff, green=0))
            >>> current_function.get_instr_highlight(here)
            <color: #ff00ff>
            ```

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*HighlightColor*](highlight.md#binaryninja.highlight.HighlightColor
            "binaryninja.highlight.HighlightColor")

    get_instruction_containing_address(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_instruction_containing_address)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    get_int_display_type(*instr_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [IntegerDisplayType](enums.md#binaryninja.enums.IntegerDisplayType "binaryninja.enums.IntegerDisplayType")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_int_display_type)
    :   Get the current text display type for an integer token in the disassembly or IL views

        See also see
        [`get_int_display_type_and_typeid`](#binaryninja.function.Function.get_int_display_type_and_typeid
        "binaryninja.function.Function.get_int_display_type_and_typeid")

        Parameters:
        :   - **instr_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the instruction or IL line containing the token
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – `value` field of the InstructionTextToken object for the token, usually the
              constant displayed
            - **operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Operand index of the token, defined as the number of OperandSeparatorTokens
              in the disassembly line before the token
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              or IL line containing the token

        Return type:
        :   [*IntegerDisplayType*](enums.md#binaryninja.enums.IntegerDisplayType
            "binaryninja.enums.IntegerDisplayType")

    get_int_display_type_and_typeid(*instr_addr: int*, *value: int*, *operand: int*, *arch: ~binaryninja.architecture.Architecture | None = None) -> (<enum 'IntegerDisplayType'>*, *<class 'str'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_int_display_type_and_typeid)
    :   Get the current text display type for an integer token in the disassembly or IL views

        Parameters:
        :   - **instr_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the instruction or IL line containing the token
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – `value` field of the InstructionTextToken object for the token, usually the
              constant displayed
            - **operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Operand index of the token, defined as the number of OperandSeparatorTokens
              in the disassembly line before the token
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              or IL line containing the token

        Return type:
        :   (<enum ‘IntegerDisplayType’>, <class ‘str’>)

    get_int_enum_display_typeid(*instr_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_int_enum_display_typeid)
    :   Get the current text display enum type for an integer token in the disassembly or IL
        views.

        See also see
        [`get_int_display_type_and_typeid`](#binaryninja.function.Function.get_int_display_type_and_typeid
        "binaryninja.function.Function.get_int_display_type_and_typeid")

        Parameters:
        :   - **instr_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the instruction or IL line containing the token
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – `value` field of the InstructionTextToken object for the token, usually the
              constant displayed
            - **operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Operand index of the token, defined as the number of OperandSeparatorTokens
              in the disassembly line before the token
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              or IL line containing the token

        Returns:
        :   TypeID for the integer token

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_lifted_il_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_lifted_il_at)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction") | *None*

    get_lifted_il_flag_definitions_for_use(*i: InstructionIndex*, *flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[InstructionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_lifted_il_flag_definitions_for_use)
    :   Parameters:
        :   - **i** (*InstructionIndex*)
            - **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
              "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[*InstructionIndex*]

    get_lifted_il_flag_uses_for_definition(*i: InstructionIndex*, *flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_lifted_il_flag_uses_for_definition)
    :   Parameters:
        :   - **i** (*InstructionIndex*)
            - **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
              "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")]

    get_lifted_ils_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_lifted_ils_at)
    :   `get_lifted_ils_at` gets the Lifted IL Instruction(s) corresponding to the given virtual
        address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the function to be queried
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction"))

        Example:
        :   ```
            >>> func = next(bv.functions)
            >>> func.get_lifted_ils_at(func.start)
            [<il: push(rbp)>]
            ```

    get_llil_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_llil_at)
    :   `get_llil_at` gets the LowLevelILInstruction corresponding to the given virtual address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be queried
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")

        Example:
        :   ```
            >>> func = next(bv.functions)
            >>> func.get_llil_at(func.start)
            <il: push(rbp)>
            ```

    get_llils_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_llils_at)
    :   `get_llils_at` gets the LowLevelILInstruction(s) corresponding to the given virtual
        address See the [developer
        docs](https://dev-docs.binary.ninja/dev/concepts.html#mapping-between-ils) for more
        information.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be queried
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction"))

        Example:
        :   ```
            >>> func = next(bv.functions)
            >>> func.get_llils_at(func.start)
            [<il: push(rbp)>]
            ```

    get_low_level_il_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_low_level_il_at)
    :   `get_low_level_il_at` gets the LowLevelILInstruction corresponding to the given virtual
        address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the function to be queried
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")

        Example:
        :   ```
            >>> func = next(bv.functions)
            >>> func.get_low_level_il_at(func.start)
            <il: push(rbp)>
            ```

    get_low_level_il_exits_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_low_level_il_exits_at)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]

    get_low_level_ils_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_low_level_ils_at)
    :   `get_low_level_ils_at` gets the LowLevelILInstruction(s) corresponding to the given
        virtual address See the [developer
        docs](https://dev-docs.binary.ninja/dev/concepts.html#mapping-between-ils) for more
        information.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be queried
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction"))

        Example:
        :   ```
            >>> func = next(bv.functions)
            >>> func.get_low_level_ils_at(func.start)
            [<il: push(rbp)>]
            ```

    get_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → metadata.MetadataValueType | Any[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_metadata)
    :   get_metadata retrieves a metadata value associated with the given key stored in the
        current Function.

        This method behaves like dict.get():

        - If the key exists, its metadata value is returned.
        - If the key does not exist and default is not provided, None is returned.
        - If the key does not exist and default is provided, default is returned.

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – key to query
            - **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")) – value to return if the key does not exist (defaults to None)

        Return type:
        :   metadata associated with the key or the default value

        Example:
        :   ```
            >>> current_function.store_metadata("integer", 1337)
            >>> current_function.get_metadata("integer")
            1337L
            >>> current_function.get_metadata("missing")
            None
            >>> current_function.get_metadata("missing", 42)
            42
            ```

    get_mlil_var_refs(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILReferenceSource](#binaryninja.function.ILReferenceSource "binaryninja.function.ILReferenceSource")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_mlil_var_refs)
    :   `get_mlil_var_refs` returns a list of ILReferenceSource objects (IL xrefs or
        cross-references) that reference the given variable. The variable is a local variable
        that can be either on the stack, in a register, or in a flag. This function is related
        to get_hlil_var_refs(), which returns variable references collected from HLIL. The two
        can be different in several cases, e.g., multiple variables in MLIL can be merged into a
        single variable in HLIL.

        Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) – Variable for which to query the xref

        Returns:
        :   List of IL References for the given variable

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*ILReferenceSource*](#binaryninja.function.ILReferenceSource
            "binaryninja.function.ILReferenceSource"))

        Example:
        :   ```
            >>> mlil_var = current_mlil[0].operands[0]
            >>> current_function.get_mlil_var_refs(mlil_var)
            ```

    get_mlil_var_refs_from(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[VariableReferenceSource](#binaryninja.function.VariableReferenceSource "binaryninja.function.VariableReferenceSource")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_mlil_var_refs_from)
    :   `get_mlil_var_refs_from` returns a list of variables referenced by code in the function
        `func`, of the architecture `arch`, and at the address `addr`. If no function is
        specified, references from all functions and containing the address will be returned. If
        no architecture is specified, the architecture of the function will be used. This
        function is related to get_hlil_var_refs_from(), which returns variable references
        collected from HLIL. The two can be different in several cases, e.g., multiple variables
        in MLIL can be merged into a single variable in HLIL.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for variable references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – optional architecture of query

        Returns:
        :   list of variable reference sources

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*VariableReferenceSource*](#binaryninja.function.VariableReferenceSource
            "binaryninja.function.VariableReferenceSource"))

    get_parameter_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *func_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_parameter_at)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **func_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              *None*)
            - **i** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_parameter_at_low_level_il_instruction(*instr: InstructionIndex*, *func_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_parameter_at_low_level_il_instruction)
    :   Parameters:
        :   - **instr** (*InstructionIndex*)
            - **func_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))
            - **i** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_reg_value_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_reg_value_after)
    :   `get_reg_value_after` gets the value instruction address corresponding to the given
        virtual address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to query
            - **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – string value of native register to query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

        Example:
        :   ```
            >>> current_function.get_reg_value_after(0x400dbe, 'rdi')
            <undetermined>
            ```

    get_reg_value_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_reg_value_at)
    :   `get_reg_value_at` gets the value the provided string register address corresponding to
        the given virtual address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to query
            - **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – string value of native register to query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

        Example:
        :   ```
            >>> current_function.get_reg_value_at(0x400dbe, 'rdi')
            <const 0x2>
            ```

    get_reg_value_at_exit(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_reg_value_at_exit)
    :   Parameters:
        :   **reg** (*RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*)

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_regs_read_by(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_regs_read_by)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[*RegisterName*]

    get_regs_written_by(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_regs_written_by)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[*RegisterName*]

    get_stack_contents_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_stack_contents_after)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_stack_contents_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_stack_contents_at)
    :   `get_stack_contents_at` returns the RegisterValue for the item on the stack in the
        current function at the given virtual address `addr`, stack offset `offset` and size of
        `size`. Optionally specifying the architecture.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to query
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – stack offset base of stack
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of memory to query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

        Note

        Stack base is zero on entry into the function unless the architecture places the return
        address on the stack as in (x86/x86_64) where the stack base will start at address_size

        Example:
        :   ```
            >>> current_function.get_stack_contents_at(0x400fad, -16, 4)
            <range: 0x8 to 0xffffffff>
            ```

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_stack_var_at_frame_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_stack_var_at_frame_offset)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")
            | *None*

    get_stack_var_at_frame_offset_after_instruction(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_stack_var_at_frame_offset_after_instruction)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")
            | *None*

    get_stack_vars_referenced_by(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StackVariableReference](variable.md#binaryninja.variable.StackVariableReference "binaryninja.variable.StackVariableReference")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_stack_vars_referenced_by)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*StackVariableReference*](variable.md#binaryninja.variable.StackVariableReference
            "binaryninja.variable.StackVariableReference")]

    get_stack_vars_referenced_by_address_if_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StackVariableReference](variable.md#binaryninja.variable.StackVariableReference "binaryninja.variable.StackVariableReference")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_stack_vars_referenced_by_address_if_available)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*StackVariableReference*](variable.md#binaryninja.variable.StackVariableReference
            "binaryninja.variable.StackVariableReference")]

    get_switch_recovery(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → [SwitchRecovery](enums.md#binaryninja.enums.SwitchRecovery "binaryninja.enums.SwitchRecovery")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_switch_recovery)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|*
            [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction"))

        Return type:
        :   [*SwitchRecovery*](enums.md#binaryninja.enums.SwitchRecovery
            "binaryninja.enums.SwitchRecovery")

    get_tags_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_tags_at)
    :   `get_tags` gets a list of Tags (but not function tags).

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address to get tags from.
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If None, gets all tags, if True, gets auto tags, if False, gets user tags
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(([*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"),
            [*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")))

    get_tags_in_range(*address_range: [AddressRange](variable.md#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_tags_in_range)
    :   `get_address_tags_in_range` gets a list of all Tags in the function at a given address.
        Range is inclusive at the start, exclusive at the end.

        Parameters:
        :   - **address_range** ([*AddressRange*](variable.md#binaryninja.variable.AddressRange
              "binaryninja.variable.AddressRange")) – Address range from which to get tags
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for the block in which the Tag
              is located (optional)
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If None, gets all tags, if True, gets auto tags, if False, gets user tags

        Returns:
        :   A list of (arch, address, Tag) tuples

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(([*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"),
            [*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")))

    get_type_tokens(*settings: [DisassemblySettings](#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_type_tokens)
    :   Parameters:
        :   **settings** ([*DisassemblySettings*](#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    get_variable_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.get_variable_by_name)
    :   Get a specific variable or None if it doesn’t exist

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")
            | *None*

    has_guided_source_blocks() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.has_guided_source_blocks)
    :   `has_guided_source_blocks` checks if this function has any guided source blocks
        configured. This indicates whether guided analysis is active for this function.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Returns:
        :   True if the function has guided source blocks, False otherwise

    is_call_instruction(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.is_call_instruction)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_condition_inverted(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.is_condition_inverted)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|*
            [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_guided_source_block(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.is_guided_source_block)
    :   `is_guided_source_block` checks if the given address is a guided source block.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture of the address to check
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address to check

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_instruction_collapsed(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *discriminator: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.is_instruction_collapsed)
    :   Determine if a given HLIL instruction (with discriminator) is collapsed during
        rendering. :param instr: Instruction which might be collapsed :param discriminator:
        Unique discriminator id for the region :return: True if the instruction should be
        rendered as collapsed

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction"))
            - **discriminator** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_region_collapsed(*hash*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.is_region_collapsed)
    :   Determine if a given region is collapsed during rendering. :param hash: Hash value of
        region :return: True if the region should be rendered as collapsed

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_var_user_defined(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.is_var_user_defined)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    language_representation(*language: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [LanguageRepresentationFunction](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.language_representation)
    :   Parameters:
        :   **language** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*LanguageRepresentationFunction*](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction
            "binaryninja.languagerepresentation.LanguageRepresentationFunction") | *None*

    language_representation_if_available(*language: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [LanguageRepresentationFunction](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.language_representation_if_available)
    :   Parameters:
        :   **language** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*LanguageRepresentationFunction*](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction
            "binaryninja.languagerepresentation.LanguageRepresentationFunction") | *None*

    mark_caller_updates_required(*update_type: [FunctionUpdateType](enums.md#binaryninja.enums.FunctionUpdateType "binaryninja.enums.FunctionUpdateType") = FunctionUpdateType.UserFunctionUpdate*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.mark_caller_updates_required)
    :   `mark_caller_updates_required` indicates that callers of this function need to be
        reanalyzed during the next update cycle

        Parameters:
        :   **update_type** ([*FunctionUpdateType*](enums.md#binaryninja.enums.FunctionUpdateType
            "binaryninja.enums.FunctionUpdateType")) – (optional) Desired update type

        Return type:
        :   *None*

    mark_recent_use() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.mark_recent_use)
    :   Return type:
        :   *None*

    mark_updates_required(*update_type: [FunctionUpdateType](enums.md#binaryninja.enums.FunctionUpdateType "binaryninja.enums.FunctionUpdateType") = FunctionUpdateType.UserFunctionUpdate*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.mark_updates_required)
    :   `mark_updates_required` indicates that this function needs to be reanalyzed during the
        next update cycle

        Parameters:
        :   **update_type** ([*FunctionUpdateType*](enums.md#binaryninja.enums.FunctionUpdateType
            "binaryninja.enums.FunctionUpdateType")) – (optional) Desired update type

        Return type:
        :   *None*

    merge_vars(*target: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *sources: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.merge_vars)
    :   `merge_vars` merges one or more variables in `sources` into the `target` variable. All
        variable accesses to the variables in `sources` will be rewritten to use `target`.

        Parameters:
        :   - **target** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – target variable
            - **sources** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")*)*) – list of source variables

        Return type:
        :   *None*

    query_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → metadata.MetadataValueType[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.query_metadata)
    :   query_metadata retrieves metadata associated with the given key stored in the current
        Function.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – key to query

        Return type:
        :   metadata associated with the key

    reanalyze(*update_type: [FunctionUpdateType](enums.md#binaryninja.enums.FunctionUpdateType "binaryninja.enums.FunctionUpdateType") = FunctionUpdateType.UserFunctionUpdate*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.reanalyze)
    :   `reanalyze` causes this function to be reanalyzed. This function does not wait for the
        analysis to finish.

        Parameters:
        :   **update_type** ([*FunctionUpdateType*](enums.md#binaryninja.enums.FunctionUpdateType
            "binaryninja.enums.FunctionUpdateType")) – (optional) Desired update type

        Return type:
        :   *None*

        Warning

        If analysis_skipped is True, using this API will not trigger re-analysis. Instead, set
        analysis_skipped to False.

        Return type:
        :   *None*

        Parameters:
        :   **update_type** ([*FunctionUpdateType*](enums.md#binaryninja.enums.FunctionUpdateType
            "binaryninja.enums.FunctionUpdateType"))

    release_advanced_analysis_data() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.release_advanced_analysis_data)
    :   Return type:
        :   *None*

    remove_auto_address_tag(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag: [Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_auto_address_tag)
    :   `remove_auto_address_tag` removes a Tag object at a given address.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address at which to add the tag
            - **tag** ([*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))
              – Tag object to be added
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for the block in which the Tag
              is added (optional)

        Return type:
        :   *None*

    remove_auto_address_tags_of_type(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *arch=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_auto_address_tags_of_type)
    :   `remove_auto_address_tags_of_type` removes all tags at the given address of the given
        type.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address at which to remove the tags
            - **tag_type** ([*Tag*](binaryview.md#binaryninja.binaryview.Tag
              "binaryninja.binaryview.Tag")) – TagType object to match for removing
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for the block in which the Tags
              is located (optional)

        Return type:
        :   *None*

    remove_auto_function_tag(*tag: [Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_auto_function_tag)
    :   `remove_user_function_tag` removes a Tag object as a function tag.

        Parameters:
        :   **tag** ([*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))
            – Tag object to be added

        Return type:
        :   *None*

    remove_auto_function_tags_of_type(*tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_auto_function_tags_of_type)
    :   `remove_user_function_tags_of_type` removes all function Tag objects on a function of a
        given type

        Parameters:
        :   **tag_type** ([*TagType*](binaryview.md#binaryninja.binaryview.TagType
            "binaryninja.binaryview.TagType")) – TagType object to match for removing

        Return type:
        :   *None*

    remove_guided_source_blocks(*addresses: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_guided_source_blocks)
    :   `remove_guided_source_blocks` removes blocks from the guided source block list for this
        function. The specified blocks will no longer have their direct outgoing branch targets
        analyzed. This automatically enables the `analysis.guided.enable` setting if it is not
        already enabled.

        Parameters:
        :   - **addresses** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python
              v3.14)")*[*[*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]**]*)
              – List of (architecture, address) tuples to remove
            - **addresses**

        Return type:
        :   *None*

    remove_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_metadata)
    :   remove_metadata removes the metadata associated with key from the current function.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – key associated with metadata to remove from the function

        Return type:
        :   *None*

    remove_user_address_tag(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag: [Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_address_tag)
    :   `remove_user_address_tag` removes a Tag object at a given address. Since this removes a
        user tag, it will be added to the current undo buffer.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address at which to remove the tag
            - **tag** ([*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))
              – Tag object to be added
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for the block in which the Tag
              is added (optional)

        Return type:
        :   *None*

    remove_user_address_tags_of_type(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *arch=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_address_tags_of_type)
    :   `remove_user_address_tags_of_type` removes all tags at the given address of the given
        type. Since this removes user tags, it will be added to the current undo buffer.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address at which to remove the tag
            - **tag_type** ([*Tag*](binaryview.md#binaryninja.binaryview.Tag
              "binaryninja.binaryview.Tag")) – TagType object to match for removing
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for the block in which the Tags
              is located (optional)

        Return type:
        :   *None*

    remove_user_code_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *to_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *from_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_code_ref)
    :   `remove_user_code_ref` removes a user-defined cross-reference. If the given address is
        not contained within this function, or if there is no such user-defined cross-reference,
        no action is performed.

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the source instruction
            - **to_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the xref’s destination.
            - **from_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) architecture of the source
              instruction

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.remove_user_code_ref(here, 0x400000)
            ```

    remove_user_function_tag(*tag: [Tag](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_function_tag)
    :   `remove_user_function_tag` removes a Tag object as a function tag. Since this removes a
        user tag, it will be added to the current undo buffer.

        Parameters:
        :   **tag** ([*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))
            – Tag object to be added

        Return type:
        :   *None*

    remove_user_function_tags_of_type(*tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_function_tags_of_type)
    :   `remove_user_function_tags_of_type` removes all function Tag objects on a function of a
        given type Since this removes user tags, it will be added to the current undo buffer.

        Parameters:
        :   **tag_type** ([*TagType*](binaryview.md#binaryninja.binaryview.TagType
            "binaryninja.binaryview.TagType")) – TagType object to match for removing

        Return type:
        :   *None*

    remove_user_type_field_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: types.QualifiedNameType*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *from_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_type_field_ref)
    :   `remove_user_type_field_ref` removes a user-defined type field cross-reference. If the
        given address is not contained within this function, or if there is no such user-defined
        cross-reference, no action is performed.

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the source instruction
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of the referenced type
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field, relative to the type
            - **from_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) architecture of the source
              instruction
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – (optional) the size of the access

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.remove_user_type_field_ref(here, 'A', 0x8)
            ```

    remove_user_type_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: types.QualifiedNameType*, *from_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.remove_user_type_ref)
    :   `remove_user_type_ref` removes a user-defined type cross-reference. If the given address
        is not contained within this function, or if there is no such user-defined
        cross-reference, no action is performed.

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the source instruction
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of the referenced type
            - **from_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) architecture of the source
              instruction

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.remove_user_type_ref(here, 'A')
            ```

    request_advanced_analysis_data() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.request_advanced_analysis_data)
    :   Return type:
        :   *None*

    request_debug_report(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.request_debug_report)
    :   `request_debug_report` can generate internal debug reports for a variety of analysis.
        Current list of possible values include:

        - mlil_translator
        - stack_adjust_graph
        - high_level_il

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the debug report

        Return type:
        :   *None*

    set_auto_call_reg_stack_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *adjust: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_call_reg_stack_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **adjust** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping
              "(in Python v3.14)")*[**RegisterStackName**,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]*)
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_auto_call_reg_stack_adjustment_for_reg_stack(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: RegisterStackName | [ILRegisterStack](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | RegisterStackIndex*, *adjust*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_call_reg_stack_adjustment_for_reg_stack)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **reg_stack** (*RegisterStackName* *|*
              [*ILRegisterStack*](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack
              "binaryninja.lowlevelil.ILRegisterStack") *|* *RegisterStackIndex*)
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_auto_call_stack_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *adjust: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](types.md#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_call_stack_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **adjust** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* [*OffsetWithConfidence*](types.md#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_auto_calling_convention(*value: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_calling_convention)
    :   Parameters:
        :   **value**
            ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention"))

        Return type:
        :   *None*

    set_auto_can_return(*value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_can_return)
    :   Parameters:
        :   **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)") *|* [*BoolWithConfidence*](types.md#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence"))

        Return type:
        :   *None*

    set_auto_clobbered_regs(*value: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_clobbered_regs)
    :   Parameters:
        :   **value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[**RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex**]*)

        Return type:
        :   *None*

    set_auto_has_variable_arguments(*value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_has_variable_arguments)
    :   Parameters:
        :   **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)") *|* [*BoolWithConfidence*](types.md#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence"))

        Return type:
        :   *None*

    set_auto_indirect_branches(*source: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *branches: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*, *source_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_indirect_branches)
    :   Parameters:
        :   - **source** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **branches** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python
              v3.14)")*[*[*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]**]*)
            - **source_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_auto_inline_during_analysis(*value: [InlineDuringAnalysis](enums.md#binaryninja.enums.InlineDuringAnalysis "binaryninja.enums.InlineDuringAnalysis") | [InlineDuringAnalysisWithConfidence](types.md#binaryninja.types.InlineDuringAnalysisWithConfidence "binaryninja.types.InlineDuringAnalysisWithConfidence") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_inline_during_analysis)
    :   Parameters:
        :   **value** ([*InlineDuringAnalysis*](enums.md#binaryninja.enums.InlineDuringAnalysis
            "binaryninja.enums.InlineDuringAnalysis") *|*
            [*InlineDuringAnalysisWithConfidence*](types.md#binaryninja.types.InlineDuringAnalysisWithConfidence
            "binaryninja.types.InlineDuringAnalysisWithConfidence") *|*
            [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") *|*
            [*BoolWithConfidence*](types.md#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence"))

    set_auto_instr_highlight(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *color: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor") | [HighlightStandardColor](enums.md#binaryninja.enums.HighlightStandardColor "binaryninja.enums.HighlightStandardColor")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_instr_highlight)
    :   `set_auto_instr_highlight` highlights the instruction at the specified address with the
        supplied color

        Warning

        Use only in analysis plugins. Do not use in regular plugins, as colors won’t be saved to
        the database.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be highlighted
            - **color** ([*HighlightStandardColor*](enums.md#binaryninja.enums.HighlightStandardColor
              "binaryninja.enums.HighlightStandardColor")*|*[*HighlightColor*](highlight.md#binaryninja.highlight.HighlightColor
              "binaryninja.highlight.HighlightColor")) – Color value to use for highlighting
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              if different from self.arch

    set_auto_parameter_locations(*value: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")] | [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable") | [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [ParameterLocations](variable.md#binaryninja.variable.ParameterLocations "binaryninja.variable.ParameterLocations") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_parameter_locations)
    :   Parameters:
        :   **value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation") *|*
            [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")*]* *|*
            [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable") *|*
            [*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation") *|*
            [*ParameterLocations*](variable.md#binaryninja.variable.ParameterLocations
            "binaryninja.variable.ParameterLocations") *|* *None*)

        Return type:
        :   *None*

    set_auto_parameter_vars(*value: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")] | [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable") | [ParameterVariables](variable.md#binaryninja.variable.ParameterVariables "binaryninja.variable.ParameterVariables") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_parameter_vars)
    :   Parameters:
        :   **value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")*]* *|*
            [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable") *|*
            [*ParameterVariables*](variable.md#binaryninja.variable.ParameterVariables
            "binaryninja.variable.ParameterVariables") *|* *None*)

        Return type:
        :   *None*

    set_auto_pure(*value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_pure)
    :   Parameters:
        :   **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)") *|* [*BoolWithConfidence*](types.md#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence"))

        Return type:
        :   *None*

    set_auto_reg_stack_adjustments(*value: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[RegisterStackName, [RegisterStackAdjustmentWithConfidence](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_reg_stack_adjustments)
    :   Parameters:
        :   **value** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in
            Python v3.14)")*[**RegisterStackName**,*
            [*RegisterStackAdjustmentWithConfidence*](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence
            "binaryninja.types.RegisterStackAdjustmentWithConfidence")*]*)

    set_auto_return_type(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_return_type)
    :   Parameters:
        :   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
            [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))

        Return type:
        :   *None*

    set_auto_return_value_location(*value: types.OptionalLocation*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_return_value_location)
    :   Parameters:
        :   **value** (*types.OptionalLocation*)

    set_auto_stack_adjustment(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](types.md#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_stack_adjustment)
    :   Parameters:
        :   **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|* [*OffsetWithConfidence*](types.md#binaryninja.types.OffsetWithConfidence
            "binaryninja.types.OffsetWithConfidence"))

        Return type:
        :   *None*

    set_auto_type(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_auto_type)
    :   Parameters:
        :   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
            [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))

        Return type:
        :   *None*

    set_call_reg_stack_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *adjust: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [RegisterStackAdjustmentWithConfidence](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence")]*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_call_reg_stack_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **adjust** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping
              "(in Python v3.14)")*[**RegisterStackName**,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|*
              [*RegisterStackAdjustmentWithConfidence*](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence
              "binaryninja.types.RegisterStackAdjustmentWithConfidence")*]*)
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_call_reg_stack_adjustment_for_reg_stack(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: RegisterStackName | [ILRegisterStack](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | RegisterStackIndex*, *adjust: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [RegisterStackAdjustmentWithConfidence](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_call_reg_stack_adjustment_for_reg_stack)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **reg_stack** (*RegisterStackName* *|*
              [*ILRegisterStack*](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack
              "binaryninja.lowlevelil.ILRegisterStack") *|* *RegisterStackIndex*)
            - **adjust** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|*
              [*RegisterStackAdjustmentWithConfidence*](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence
              "binaryninja.types.RegisterStackAdjustmentWithConfidence"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_call_stack_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *adjust: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](types.md#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_call_stack_adjustment)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **adjust** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* [*OffsetWithConfidence*](types.md#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence"))
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

    set_call_type_adjustment(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *adjust_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_call_type_adjustment)
    :   `set_call_type_adjustment` sets or removes the call type override at a call site to the
        given type.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the call instruction to adjust
            - **adjust_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*|*[*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*|*[*TypeBuilder*](types.md#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder")) – (optional) overridden call type, or None to remove
              an existing adjustment
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              if different from self.arch

        Example:
        :   ```
            >>> # Change the current call site to no-return
            >>> target = bv.get_function_at(list(filter(lambda ref: ref.address == here, current_function.call_sites))[0].mlil.dest.value.value)
            >>> ft = target.type.mutable_copy()
            >>> ft.can_return = False
            >>> current_function.set_call_type_adjustment(here, ft)
            ```

        Return type:
        :   *None*

    set_comment_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *comment: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_comment_at)
    :   `set_comment_at` sets a comment for the current function at the address specified

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address within the current function to apply the comment to
            - **comment** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – string comment to apply

        Return type:
        :   *None*

        Example:
        :   ```
            >>> current_function.set_comment_at(here, "hi")
            ```

    set_condition_inverted(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *invert: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_condition_inverted)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|*
              [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction"))
            - **invert** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)"))

    *static* set_default_session_data(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_default_session_data)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    set_early_return(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [EarlyReturn](enums.md#binaryninja.enums.EarlyReturn "binaryninja.enums.EarlyReturn")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_early_return)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|*
              [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction"))
            - **value** ([*EarlyReturn*](enums.md#binaryninja.enums.EarlyReturn
              "binaryninja.enums.EarlyReturn"))

    set_expr_folding(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [ExprFolding](enums.md#binaryninja.enums.ExprFolding "binaryninja.enums.ExprFolding")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_expr_folding)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|*
              [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction"))
            - **value** ([*ExprFolding*](enums.md#binaryninja.enums.ExprFolding
              "binaryninja.enums.ExprFolding"))

    set_guided_source_blocks(*addresses: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_guided_source_blocks)
    :   `set_guided_source_blocks` sets the complete list of guided source blocks for this
        function. Only blocks in this set will have their direct outgoing branch targets
        analyzed. This replaces any existing guided source blocks and automatically enables or
        disables the `analysis.guided.enable` setting based on whether addresses are provided.

        Parameters:
        :   - **addresses** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python
              v3.14)")*[*[*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]**]*)
              – List of (architecture, address) tuples
            - **addresses**

        Return type:
        :   *None*

    set_int_display_type(*instr_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *display_type: [IntegerDisplayType](enums.md#binaryninja.enums.IntegerDisplayType "binaryninja.enums.IntegerDisplayType")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *enum_display_typeid=None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_int_display_type)
    :   Change the text display type for an integer token in the disassembly or IL views

        Parameters:
        :   - **instr_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the instruction or IL line containing the token
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – `value` field of the InstructionTextToken object for the token, usually the
              constant displayed
            - **operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Operand index of the token, defined as the number of OperandSeparatorTokens
              in the disassembly line before the token
            - **display_type** ([*IntegerDisplayType*](enums.md#binaryninja.enums.IntegerDisplayType
              "binaryninja.enums.IntegerDisplayType")) – Desired display type
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              or IL line containing the token
            - **enum_display_typeid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)")) – (optional) Whenever passing EnumDisplayType to `display_type`,
              passing a type ID here will specify the Enumeration display type. Must be a valid type
              ID and resolve to an enumeration type.

        Return type:
        :   *None*

    set_switch_recovery(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [SwitchRecovery](enums.md#binaryninja.enums.SwitchRecovery "binaryninja.enums.SwitchRecovery")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_switch_recovery)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|*
              [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction"))
            - **value** ([*SwitchRecovery*](enums.md#binaryninja.enums.SwitchRecovery
              "binaryninja.enums.SwitchRecovery"))

    set_user_indirect_branches(*source: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *branches: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*, *source_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_user_indirect_branches)
    :   Parameters:
        :   - **source** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **branches** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python
              v3.14)")*[*[*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]**]*)
            - **source_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    set_user_inline_during_analysis(*value: [InlineDuringAnalysis](enums.md#binaryninja.enums.InlineDuringAnalysis "binaryninja.enums.InlineDuringAnalysis") | [InlineDuringAnalysisWithConfidence](types.md#binaryninja.types.InlineDuringAnalysisWithConfidence "binaryninja.types.InlineDuringAnalysisWithConfidence") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_user_inline_during_analysis)
    :   Parameters:
        :   **value** ([*InlineDuringAnalysis*](enums.md#binaryninja.enums.InlineDuringAnalysis
            "binaryninja.enums.InlineDuringAnalysis") *|*
            [*InlineDuringAnalysisWithConfidence*](types.md#binaryninja.types.InlineDuringAnalysisWithConfidence
            "binaryninja.types.InlineDuringAnalysisWithConfidence") *|*
            [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") *|*
            [*BoolWithConfidence*](types.md#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence"))

    set_user_instr_highlight(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *color: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor") | [HighlightStandardColor](enums.md#binaryninja.enums.HighlightStandardColor "binaryninja.enums.HighlightStandardColor")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_user_instr_highlight)
    :   `set_user_instr_highlight` highlights the instruction at the specified address with the
        supplied color

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be highlighted
            - **color** ([*HighlightStandardColor*](enums.md#binaryninja.enums.HighlightStandardColor
              "binaryninja.enums.HighlightStandardColor")*|*[*HighlightColor*](highlight.md#binaryninja.highlight.HighlightColor
              "binaryninja.highlight.HighlightColor")) – Color value to use for highlighting
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture of the instruction
              if different from self.arch

        Example:
        :   ```
            >>> current_function.set_user_instr_highlight(here, HighlightStandardColor.BlueHighlightColor)
            >>> current_function.set_user_instr_highlight(here, highlight.HighlightColor(red=0xff, blue=0xff, green=0))
            ```

        Warning: For performance reasons, this function does not ensure the address you have
        supplied is within the function’s bounds.

    set_user_type(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_user_type)
    :   Parameters:
        :   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
            [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))

        Return type:
        :   *None*

    set_user_var_value(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *def_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *after: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.set_user_var_value)
    :   set_user_var_value allows the user to specify a PossibleValueSet value for an MLIL
        variable at its definition site.

        Warning

        Setting the variable value, triggers a reanalysis of the function and allows the
        dataflow to compute and propagate values which depend on the current variable. This
        implies that branch conditions whose values can be determined statically will be
        computed, leading to potential branch elimination at the HLIL layer.

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – Variable for which the value is to be set
            - **def_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address where the variable is set
            - **value** ([*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet")) – Informed value of the variable
            - **after** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether the value happens before or after the instruction

        Return type:
        :   *None*

        Example:
        :   ```
            >>> mlil_var = current_mlil[0].operands[0]
            >>> def_address = 0x40108d
            >>> var_value = PossibleValueSet.constant(5)
            >>> current_function.set_user_var_value(mlil_var, def_address, var_value)
            ```

    split_var(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.split_var)
    :   `split_var` splits a variable at the definition site. The given `var` must be the
        variable unique to the definition and should be obtained by using
        `MediumLevelILInstruction.get_split_var_for_definition` at the definition site.

        This function is not meant to split variables that have been previously merged. Use
        `unmerge_vars` to split previously merged variables.

        Warning

        Binary Ninja automatically splits all variables that the analysis determines to be
        safely splittable. Splitting a variable manually with `split_var` can cause IL and
        decompilation to be incorrect. There are some patterns where variables can be safely
        split semantically but analysis cannot determine that it is safe. This function is
        provided to allow variable splitting to be performed in these cases by plugins or by the
        user.

        Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) – variable to split

        Return type:
        :   *None*

    store_metadata(*key: str*, *md: Metadata | int | bool | str | bytes | float | ~typing.List[MetadataValueType] | ~typing.Tuple[MetadataValueType] | dict*, *flags: MetadataStoreFlag | bool = <MetadataStoreFlag.MetadataStorePersistent: 1>*, *isAuto: bool | None = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.store_metadata)
    :   store_metadata stores an object for the given key in the current Function. See
        `BinaryView.store_metadata` for the meaning of `flags`.

        Unlike `BinaryView.store_metadata`, the default does not mark the file as modified,
        preserving the historical behavior of Function metadata writes.

        `flags` may also be passed as a legacy `isAuto` bool: `False` maps to the default
        (persist, don’t dirty) and `True` maps to `MetadataStoreEphemeral` (don’t persist, don’t
        dirty). The deprecated `isAuto` keyword is still accepted with the same meaning, taking
        precedence over `flags`.

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – key value to associate the Metadata object with
            - **md** (*Varies*) – object to store
            - **flags** ([*MetadataStoreFlag*](enums.md#binaryninja.enums.MetadataStoreFlag
              "binaryninja.enums.MetadataStoreFlag") *|*
              [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –
              storage flags (see `MetadataStoreFlag`), or a legacy `isAuto` bool.
            - **isAuto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – deprecated alias for passing the legacy bool by keyword.

        Return type:
        :   *None*

    toggle_region(*hash*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.toggle_region)
    :   Toggle the collapsed state of a region during rendering, by hash value :param hash: Hash
        value of region

    unmerge_vars(*target: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *sources: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.unmerge_vars)
    :   `unmerge_vars` undoes variable merging performed with `merge_vars`. The variables in
        `sources` will no longer be merged into the `target` variable.

        Parameters:
        :   - **target** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – target variable
            - **sources** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")*)*) – list of source variables

        Return type:
        :   *None*

    unsplit_var(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#Function.unsplit_var)
    :   `unsplit_var` undoes variable splitting performed with `split_var`. The given `var` must
        be the variable unique to the definition and should be obtained by using
        `MediumLevelILInstruction.get_split_var_for_definition` at the definition site.

        Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) – variable to unsplit

        Return type:
        :   *None*

    *property* address_ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[AddressRange](variable.md#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange")]*
    :   All of the address ranges covered by a function

    *property* analysis_performance_info*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

    *property* analysis_skip_override*: [FunctionAnalysisSkipOverride](enums.md#binaryninja.enums.FunctionAnalysisSkipOverride "binaryninja.enums.FunctionAnalysisSkipOverride")*
    :   Override for skipping of automatic analysis

    *property* analysis_skip_reason*: [AnalysisSkipReason](enums.md#binaryninja.enums.AnalysisSkipReason "binaryninja.enums.AnalysisSkipReason")*
    :   Function analysis skip reason

    *property* analysis_skipped*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether automatic analysis was skipped for this function. Can be set to false to
        re-enable analysis.

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*
    :   Function architecture (read-only)

    *property* auto*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether function was automatically discovered (read-only) as a result of some creation
        of a ‘user’ function. ‘user’ functions may or may not have been created by a user
        through the or API. For instance the entry point into a function is always created a
        ‘user’ function. ‘user’ functions should be considered the root of auto analysis.

    *property* auto_metadata*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), metadata.MetadataValueType]*
    :   metadata retrieves the metadata associated with the current function.

        Return type:
        :   metadata associated with the function

    *property* basic_blocks*: [BasicBlockList](#binaryninja.function.BasicBlockList "binaryninja.function.BasicBlockList")*
    :   function.BasicBlockList of BasicBlocks in the current function (read-only)

    *property* call_sites*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ReferenceSource](binaryview.md#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource")]*
    :   `call_sites` returns a list of possible call sites contained in this function. This
        includes ordinary calls, tail calls, and indirect jumps. Not all of the returned call
        sites are necessarily true call sites; some may simply be unresolved indirect jumps, for
        example.

        Returns:
        :   List of References that represent the sources of possible calls in this function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*ReferenceSource*](binaryview.md#binaryninja.binaryview.ReferenceSource
            "binaryninja.binaryview.ReferenceSource"))

    *property* callee_addresses*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*
    :   `callee_addresses` returns a list of start addresses for functions that this function
        calls. Does not point to the actual address where the call occurs, just the start of the
        function that contains the reference.

        Returns:
        :   List of start address for functions that this function calls

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

    *property* callees*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Function](#binaryninja.function.Function "binaryninja.function.Function")]*
    :   `callees` returns a list of functions that this function calls This does not include the
        address of those calls, rather just the function objects themselves. Use
        [`call_sites`](#binaryninja.function.Function.call_sites
        "binaryninja.function.Function.call_sites") to identify the location of these calls.
        This does not include calls to imported functions, as they do not have a function
        object, use [`callee_addresses`](#binaryninja.function.Function.callee_addresses
        "binaryninja.function.Function.callee_addresses") for that.

        Returns:
        :   List of Functions that this function calls

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Function*](#binaryninja.function.Function "binaryninja.function.Function"))

    *property* caller_sites*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[ReferenceSource](binaryview.md#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   `caller_sites` returns a list of ReferenceSource objects corresponding to the addresses
        in functions which call this function

        Returns:
        :   List of ReferenceSource objects of the call sites to this function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*ReferenceSource*](binaryview.md#binaryninja.binaryview.ReferenceSource
            "binaryninja.binaryview.ReferenceSource"))

    *property* callers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Function](#binaryninja.function.Function "binaryninja.function.Function")]*
    :   `callers` returns a list of functions that call this function Does not point to the
        actual address where the call occurs, just the start of the function that contains the
        call.

        Returns:
        :   List of Functions that call this function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Function*](#binaryninja.function.Function "binaryninja.function.Function"))

    *property* calling_convention*: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Calling convention used by the function

    *property* can_return*: [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether function can return

    *property* clobbered_regs*: [RegisterSet](types.md#binaryninja.types.RegisterSet "binaryninja.types.RegisterSet")*
    :   Registers that are modified by this function

    *property* comment*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Gets the comment for the current function

    *property* comments*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Dict of comments (read-only)

    *property* components

    *property* core_var_stack_layout*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")]*
    :   List of function stack variables (read-only)

    *property* core_vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")]*
    :   List of CoreVariable objects

    *property* global_pointer_value*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*
    :   Deprecated. Use
        [`global_pointer_values`](#binaryninja.function.Function.global_pointer_values
        "binaryninja.function.Function.global_pointer_values") instead.

    *property* global_pointer_values*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[RegisterName, [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")]]*
    :   Discovered values of the global pointer registers, if the function uses any (read-only)

    *property* has_explicitly_defined_type*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether function has explicitly defined types (read-only)

    *property* has_unresolved_indirect_branches*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Has unresolved indirect branches (read-only)

    *property* has_user_annotations*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the function has ever been ‘user’ modified

    *property* has_user_type*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   True if the function has a user-defined type

    *property* has_variable_arguments*: [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether the function takes a variable number of arguments

    *property* high_level_il*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns HighLevelILFunction used to represent high level IL, or None if an error occurs
        while loading the IL (read-only)

        Note

        This function causes high level IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* highest_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The highest (largest) virtual address contained in a function.

    *property* hlil*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns HighLevelILFunction used to represent high level IL, or None if an error occurs
        while loading the IL (read-only)

        Note

        This function causes high level IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* hlil_if_available*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns HighLevelILFunction used to represent high level IL, or None if not loaded or it
        cannot be generated (read-only)

        Note

        This function can be used to check if high level IL is available without generating it.

    *property* indirect_branches*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IndirectBranchInfo](variable.md#binaryninja.variable.IndirectBranchInfo "binaryninja.variable.IndirectBranchInfo")]*
    :   List of indirect branches (read-only)

    *property* inline_during_analysis*: [InlineDuringAnalysisWithConfidence](types.md#binaryninja.types.InlineDuringAnalysisWithConfidence "binaryninja.types.InlineDuringAnalysisWithConfidence")*
    :   Whether the function’s IL should be inlined into all callers’ IL

    *property* instructions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of instruction tokens and their start addresses for the current function

    *property* is_collapsed
    :   If the entire function is collapsed during rendering.

    *property* is_exported*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the function is exported (read-only).

        A function is considered exported when its symbol binding is global or weak.

    *property* is_pure*: [BoolWithConfidence](types.md#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether function is pure

    *property* is_thunk*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Returns True if the function starts with a Tailcall (read-only)

    *property* lifted_il*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns LowLevelILFunction used to represent lifted IL, or None if an error occurs while
        loading the IL (read-only)

        Note

        This function causes lifted IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* lifted_il_if_available*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns LowLevelILFunction used to represent lifted IL, or None if not loaded or it
        cannot be generated (read-only)

        Note

        This function can be used to check if lifted IL is available without generating it.

    *property* llil*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns LowLevelILFunction used to represent low level IL, or None if an error occurs
        while loading the IL (read-only)

        Note

        This function causes low level IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* llil_basic_blocks*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[LowLevelILBasicBlock](lowlevelil.md#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of all LowLevelILBasicBlock objects in the current function

    *property* llil_if_available*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns LowLevelILFunction used to represent low level IL, or None if not loaded or it
        cannot be generated (read-only)

        Note

        This function can be used to check if low level IL is available without generating it.

    *property* low_level_il*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns LowLevelILFunction used to represent low level IL, or None if an error occurs
        while loading the IL (read-only)

        Note

        This function causes low level IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* lowest_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The lowest (smallest) virtual address contained in a function.

    *property* mapped_medium_level_il*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns MediumLevelILFunction used to represent mapped medium level IL, or None if an
        error occurs while loading the IL (read-only)

        Note

        This function causes mapped medium level IL to be generated if it has not been already.
        It is recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* medium_level_il*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns MediumLevelILFunction used to represent medium level IL, or None if an error
        occurs while loading the IL (read-only)

        Note

        This function causes medium level IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* merged_vars*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]]*
    :   Map of merged variables, organized by target variable (read-only). Use `merge_vars` and
        `unmerge_vars` to update merged variables.

    *property* metadata*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), metadata.MetadataValueType]*
    :   metadata retrieves the metadata associated with the current function.

        Return type:
        :   metadata associated with the function

    *property* mlil*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns MediumLevelILFunction used to represent medium level IL, or None if an error
        occurs while loading the IL (read-only)

        Note

        This function causes medium level IL to be generated if it has not been already. It is
        recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* mlil_basic_blocks*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[MediumLevelILBasicBlock](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of all MediumLevelILBasicBlock objects in the current function

    *property* mlil_if_available*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns MediumLevelILFunction used to represent medium level IL, or None if not loaded
        or it cannot be generated (read-only)

        Note

        This function can be used to check if medium level IL is available without generating
        it.

    *property* mmlil*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns MediumLevelILFunction used to represent mapped medium level IL, or None if an
        error occurs while loading the IL (read-only)

        Note

        This function causes mapped medium level IL to be generated if it has not been already.
        It is recommended to generate IL on-demand to avoid excessive memory usage instead of
        generating IL for all functions at once.

    *property* mmlil_if_available*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns MediumLevelILFunction used to represent mapped medium level IL, or None if not
        loaded or it cannot be generated (read-only)

        Note

        This function can be used to check if mapped medium level IL is available without
        generating it.

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Symbol name for the function

    *property* needs_update*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the function has analysis that needs to be updated (read-only)

    *property* parameter_locations*: [ParameterLocations](variable.md#binaryninja.variable.ParameterLocations "binaryninja.variable.ParameterLocations")*
    :   List of locations for the incoming function parameters

    *property* parameter_vars*: [ParameterVariables](variable.md#binaryninja.variable.ParameterVariables "binaryninja.variable.ParameterVariables")*
    :   List of variables for the incoming function parameters

    *property* platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Function platform (read-only)

    *property* provenance
    :   `provenance` returns a string representing the provenance. This portion of the API is
        under development. Currently the provenance information is undocumented, not persistent,
        and not saved to a database.

        Returns:
        :   string representation of the provenance

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *property* pseudo_c*: [LanguageRepresentationFunction](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* pseudo_c_if_available*: [LanguageRepresentationFunction](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* reg_stack_adjustments*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [RegisterStackAdjustmentWithConfidence](types.md#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence")]*
    :   Number of entries removed from each register stack after return

    *property* return_regs*: [RegisterSet](types.md#binaryninja.types.RegisterSet "binaryninja.types.RegisterSet")*
    :   Registers that are used for the return value (read-only)

    *property* return_type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Return type of the function

    *property* return_value*: [ReturnValue](types.md#binaryninja.types.ReturnValue "binaryninja.types.ReturnValue")*
    :   Return type and location

    *property* return_value_location*: [ValueLocationWithConfidence](types.md#binaryninja.types.ValueLocationWithConfidence "binaryninja.types.ValueLocationWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The location of the return value, or None if there isn’t a return value. If the return
        value has been specified to be placed in the default location, this will return the
        default location.

    *property* session_data*: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*
    :   Dictionary object where plugins can store arbitrary data associated with the function

    *property* split_vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   Set of variables that have been split with `split_var`. These variables correspond to
        those unique to each definition site and are obtained by using
        `MediumLevelILInstruction.get_split_var_for_definition` at the definitions.

    *property* stack_adjustment*: [OffsetWithConfidence](types.md#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*
    :   Number of bytes removed from the stack after return

    *property* stack_layout*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of function stack variables (read-only)

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Function start address (read-only)

    *property* symbol*: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*
    :   Function symbol(read-only)

    *property* tags*: [TagList](#binaryninja.function.TagList "binaryninja.function.TagList")*
    :   `tags` gets a TagList of all Tags in the function (but not “function tags”). Tags are
        returned as an iterable indexable object TagList of (arch, address, Tag) tuples.

        Return type:
        :   [*TagList*](#binaryninja.function.TagList
            "binaryninja.function.TagList")(([*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"),
            [*Tag*](binaryview.md#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")))

    *property* too_large*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the function is too large to automatically perform analysis (read-only)

    *property* total_bytes*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Total bytes of a function calculated by summing each basic_block. Because basic blocks
        can overlap and have gaps between them this may or may not be equivalent to a .size
        property.

    *property* type*: [FunctionType](types.md#binaryninja.types.FunctionType "binaryninja.types.FunctionType")*
    :   Function type object, can be set with either a string representing the function
        prototype (str(function) shows examples) or a `Type` object

    *property* type_tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*
    :   Text tokens for this function’s prototype

    *property* unresolved_indirect_branches*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*
    :   List of unresolved indirect branches (read-only)

    *property* unresolved_stack_adjustment_graph*: [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Flow graph of unresolved stack adjustments (read-only)

    *property* uses_incoming_global_pointer*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the function uses the incoming global pointer value

    *property* vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of function variables (read-only)

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*
    :   Function view (read-only)

    *property* workflow

## FunctionViewType

*class* FunctionViewType[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#FunctionViewType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*view_type: [FunctionViewType](#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType") | [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#FunctionViewType.__init__)
    :   Parameters:
        :   **view_type** ([*FunctionViewType*](#binaryninja.function.FunctionViewType
            "binaryninja.function.FunctionViewType") *|*
            [*FunctionGraphType*](enums.md#binaryninja.enums.FunctionGraphType
            "binaryninja.enums.FunctionGraphType") *|*
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"))

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    view_type*: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*

## HighLevelILBasicBlockList

*class* HighLevelILBasicBlockList[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#HighLevelILBasicBlockList)
:   Bases: [`BasicBlockList`](#binaryninja.function.BasicBlockList
    "binaryninja.function.BasicBlockList")

## ILReferenceSource

*class* ILReferenceSource[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#ILReferenceSource)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*func: [Function](#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *il_type: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*, *expr_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **func** ([*Function*](#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*)
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **il_type** ([*FunctionGraphType*](enums.md#binaryninja.enums.FunctionGraphType
              "binaryninja.enums.FunctionGraphType"))
            - **expr_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    *static* get_il_name(*il_type: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#ILReferenceSource.get_il_name)
    :   Parameters:
        :   **il_type** ([*FunctionGraphType*](enums.md#binaryninja.enums.FunctionGraphType
            "binaryninja.enums.FunctionGraphType"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    expr_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    func*: [Function](#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    il_type*: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*

## LowLevelILBasicBlockList

*class* LowLevelILBasicBlockList[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#LowLevelILBasicBlockList)
:   Bases: [`BasicBlockList`](#binaryninja.function.BasicBlockList
    "binaryninja.function.BasicBlockList")

## MediumLevelILBasicBlockList

*class* MediumLevelILBasicBlockList[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#MediumLevelILBasicBlockList)
:   Bases: [`BasicBlockList`](#binaryninja.function.BasicBlockList
    "binaryninja.function.BasicBlockList")

## TagList

*class* TagList[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#TagList)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*function: [Function](#binaryninja.function.Function "binaryninja.function.Function")*)[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#TagList.__init__)
    :   Parameters:
        :   **function** ([*Function*](#binaryninja.function.Function
            "binaryninja.function.Function"))

## VariableReferenceSource

*class* VariableReferenceSource[[source]](https://api.binary.ninja/_modules/binaryninja/function.html#VariableReferenceSource)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *src: [ILReferenceSource](#binaryninja.function.ILReferenceSource "binaryninja.function.ILReferenceSource")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable"))
            - **src** ([*ILReferenceSource*](#binaryninja.function.ILReferenceSource
              "binaryninja.function.ILReferenceSource"))

        Return type:
        :   *None*

    src*: [ILReferenceSource](#binaryninja.function.ILReferenceSource "binaryninja.function.ILReferenceSource")*

    var*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*
