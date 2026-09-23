# workflow module

| Class | Description |
| --- | --- |
| [`binaryninja.workflow.Activity`](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [`Activity`](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") in Binary Ninja represents an individual analysis or action to be performed on… |
| [`binaryninja.workflow.AnalysisContext`](#binaryninja.workflow.AnalysisContext "binaryninja.workflow.AnalysisContext") | [`AnalysisContext`](#binaryninja.workflow.AnalysisContext "binaryninja.workflow.AnalysisContext") is a proxy object that provides access to the current analysis context,… |
| [`binaryninja.workflow.Workflow`](#binaryninja.workflow.Workflow "binaryninja.workflow.Workflow") | `class Workflow` in Binary Ninja defines the set of analyses to perform on a binary, … |
| [`binaryninja.workflow.WorkflowMachine`](#binaryninja.workflow.WorkflowMachine "binaryninja.workflow.WorkflowMachine") |  |
| [`binaryninja.workflow.WorkflowMachineCLI`](#binaryninja.workflow.WorkflowMachineCLI "binaryninja.workflow.WorkflowMachineCLI") | A simple framework for writing line-oriented command interpreters. |

## Activity

*class* Activity[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Activity)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    [`Activity`](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") in Binary
    Ninja represents an individual analysis or action to be performed on a `BinaryView` or
    `Function` object.

    Activities are the fundamental units of execution within a
    [`Workflow`](#binaryninja.workflow.Workflow "binaryninja.workflow.Workflow"). Each
    Activity encapsulates a specific task and defines its own behavior, dependencies, and
    eligibility criteria. Activities are executed in the context of an
    [`AnalysisContext`](#binaryninja.workflow.AnalysisContext
    "binaryninja.workflow.AnalysisContext"), which provides access to binary data, analysis
    state, and utility functions.

    __init__(*configuration: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *handle: LP_BNActivity | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *eligibility: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Activity.__init__)
    :   Parameters:
        :   - **configuration** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **handle** (*LP_BNActivity* *|* *None*) –
            - **action** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
              "(in Python
              v3.14)")*[**[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]**,* *None**]* *|* *None*) –
            - **eligibility**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")*]* *|* *None*) –

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Activity name (read-only)

## AnalysisContext

*class* AnalysisContext[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    [`AnalysisContext`](#binaryninja.workflow.AnalysisContext
    "binaryninja.workflow.AnalysisContext") is a proxy object that provides access to the
    current analysis context, including the associated `BinaryView`, `Function`, and
    intermediate language (IL) representations. It provides APIs to retrieve and modify the
    in-progress analysis state and allows users to notify the analysis system of any changes
    or updates.

    __init__(*handle: LP_BNAnalysisContext*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.__init__)
    :   Parameters:
        :   **handle** (*LP_BNAnalysisContext*) –

    get_backed_address_ranges() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_backed_address_ranges)
    :   Get all backed address ranges from the cached memory map.

        Returns:
        :   List of (start, end) tuples

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")]

    get_end() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_end)
    :   Get the end address from the cached memory map.

        Returns:
        :   End address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_length() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_length)
    :   Get the length of the cached memory map.

        Returns:
        :   Length

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_mapped_address_ranges() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_mapped_address_ranges)
    :   Get all mapped address ranges from the cached memory map.

        Returns:
        :   List of (start, end) tuples

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")]

    get_next_backed_address(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_next_backed_address)
    :   Get the next backed address after the given address from the cached memory map.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Starting address
            - **flags** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Optional flags to filter by

        Returns:
        :   Next backed address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_next_mapped_address(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_next_mapped_address)
    :   Get the next mapped address after the given address from the cached memory map.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Starting address
            - **flags** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Optional flags to filter by

        Returns:
        :   Next mapped address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_next_valid_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_next_valid_offset)
    :   Get the next valid offset after the given offset from the cached memory map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Starting offset

        Returns:
        :   Next valid offset

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_section_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Section](binaryview.md#binaryninja.binaryview.Section "binaryninja.binaryview.Section") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_section_by_name)
    :   Get a section by name from the cached section map.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Section name

        Returns:
        :   Section with the given name, or None if not found

        Return type:
        :   [*Section*](binaryview.md#binaryninja.binaryview.Section
            "binaryninja.binaryview.Section") | *None*

    get_sections() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Section](binaryview.md#binaryninja.binaryview.Section "binaryninja.binaryview.Section")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_sections)
    :   Get all sections from the cached section map.

        Returns:
        :   List of all sections

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Section*](binaryview.md#binaryninja.binaryview.Section
            "binaryninja.binaryview.Section")]

    get_sections_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Section](binaryview.md#binaryninja.binaryview.Section "binaryninja.binaryview.Section")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_sections_at)
    :   Get all sections containing the given address from the cached section map.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Address to query

        Returns:
        :   List of sections containing the address

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Section*](binaryview.md#binaryninja.binaryview.Section
            "binaryninja.binaryview.Section")]

    get_segment_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Segment](binaryview.md#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_segment_at)
    :   Get the segment containing the given address from the cached memory map.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Address to query

        Returns:
        :   Segment containing the address, or None

        Return type:
        :   [*Segment*](binaryview.md#binaryninja.binaryview.Segment
            "binaryninja.binaryview.Segment") | *None*

    get_setting_bool(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_setting_bool)
    :   Get a boolean setting from the cached settings.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Setting key

        Returns:
        :   Boolean setting value

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_setting_double(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_setting_double)
    :   Get a double setting from the cached settings.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Setting key

        Returns:
        :   Double setting value

        Return type:
        :   [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")

    get_setting_int64(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_setting_int64)
    :   Get a 64-bit signed integer setting from the cached settings.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Setting key

        Returns:
        :   Int64 setting value

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_setting_string(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_setting_string)
    :   Get a string setting from the cached settings.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Setting key

        Returns:
        :   String setting value

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_setting_string_list(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_setting_string_list)
    :   Get a string list setting from the cached settings.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Setting key

        Returns:
        :   List of strings

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_setting_uint64(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_setting_uint64)
    :   Get a 64-bit unsigned integer setting from the cached settings.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Setting key

        Returns:
        :   UInt64 setting value

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_start() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.get_start)
    :   Get the start address from the cached memory map.

        Returns:
        :   Start address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    inform(*request: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.inform)
    :   Parameters:
        :   **request** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_backed_by_file(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_backed_by_file)
    :   Check if an offset is backed by the file in the cached memory map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset is backed by file

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_code_semantics(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_code_semantics)
    :   Check if an offset has code semantics in the cached section map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset has code semantics

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_executable(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_executable)
    :   Check if an offset is executable in the cached memory map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset is executable

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_extern_semantics(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_extern_semantics)
    :   Check if an offset has external semantics in the cached section map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset has external semantics

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_readable(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_readable)
    :   Check if an offset is readable in the cached memory map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset is readable

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_readonly_semantics(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_readonly_semantics)
    :   Check if an offset has read-only semantics in the cached section map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset has read-only semantics

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_writable(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_writable)
    :   Check if an offset is writable in the cached memory map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset is writable

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_writable_semantics(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_offset_writable_semantics)
    :   Check if an offset has writable semantics in the cached section map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset has writable semantics

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_valid_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.is_valid_offset)
    :   Check if an offset is mapped in the cached memory map.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Offset to check

        Returns:
        :   True if offset is mapped

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_mlil_function(*new_func: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *llil_ssa_to_mlil_instr_map: mediumlevelil.LLILSSAToMLILInstructionMapping | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *llil_ssa_to_mlil_expr_map: mediumlevelil.LLILSSAToMLILExpressionMapping | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#AnalysisContext.set_mlil_function)
    :   Set the Medium Level IL function in the current analysis, giving updated Low Level IL
        (SSA) to Medium Level IL instruction and expression mappings. :param new_func: New MLIL
        function :param llil_ssa_to_mlil_instr_map: Mapping from every LLIL SSA instruction to
        every MLIL instruction :param llil_ssa_to_mlil_expr_map: Mapping from every LLIL SSA
        expression to one or more MLIL expressions (first expression will be the primary)

        Parameters:
        :   - **new_func**
              ([*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **llil_ssa_to_mlil_instr_map** (*mediumlevelil.LLILSSAToMLILInstructionMapping* *|*
              *None*) –
            - **llil_ssa_to_mlil_expr_map** (*mediumlevelil.LLILSSAToMLILExpressionMapping* *|*
              *None*) –

        Return type:
        :   *None*

    *property* basic_blocks*: [BasicBlockList](function.md#binaryninja.function.BasicBlockList "binaryninja.function.BasicBlockList")*
    :   function.BasicBlockList of BasicBlocks in the current function (writable)

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Function for the current AnalysisContext (read-only)

    *property* hlil*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   HighLevelILFunction used to represent High Level IL (writable)

    *property* lifted_il*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   LowLevelILFunction used to represent lifted IL (writable)

    *property* llil*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   LowLevelILFunction used to represent Low Level IL (writable)

    *property* mlil*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   MediumLevelILFunction used to represent Medium Level IL (writable)

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   BinaryView for the current AnalysisContext (writable)

## Workflow

*class* Workflow[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    > `class Workflow` in Binary Ninja defines the set of analyses to perform on a binary,
    > including their dependencies and execution order.
    >
    > Workflows are represented as Directed Acyclic Graphs (DAGs), where each node corresponds
    > to an [`Activity`](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") (an
    > individual analysis or action). Workflows are used to tailor the analysis process for
    > `BinaryView` or `Function` objects, providing granular control over analysis tasks at
    > module or function levels.
    >
    > A Workflow starts in an unregistered state, either by creating a new empty Workflow or
    > by cloning an existing one. While unregistered, it is possible to add and remove
    > [`Activity`](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") objects, as
    > well as modify the execution strategy. To apply a Workflow to a binary, it must be
    > registered. Once registered, the Workflow becomes immutable and is available for use.
    >
    > Example:

    ```
    # Define the custom activity configuration
    configuration = json.dumps({
            "name": "analysis.plugins.xorStringDecoder",
            "title": "XOR String Decoder",
            "description": "This analysis step transforms XOR-encoded strings within the current function.",
            "eligibility": {
                    "auto": {
                            "default": False
                    }
            }
    })

    # Clone the meta function workflow for customization
    workflow = Workflow("core.function.metaAnalysis").clone()

    # Register a new activity
    workflow.register_activity(Activity(
            configuration,
            action=lambda analysis_context: log_warn(
                    f"Decoder running for function: {hex(analysis_context.function.start)}"
                    # Insert decoder logic here :P
            )
    ))

    # Insert the new activity before the "generateHighLevelIL" step
    workflow.insert("core.function.generateHighLevelIL", ["analysis.plugins.xorStringDecoder"])

    # Register the modified meta function workflow
    workflow.register()
    ```

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *handle: LP_BNWorkflow | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *query_registry: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *object_handle: LP_BNFunction | LP_BNBinaryView | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.__init__)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **handle** (*LP_BNWorkflow* *|* *None*) –
            - **query_registry** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **object_handle** (*LP_BNFunction* *|* *LP_BNBinaryView* *|* *None*) –

    activity_roots(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.activity_roots)
    :   `activity_roots` Retrieve the list of activity roots for the Workflow, or if specified
        just for the given `activity`.

        Parameters:
        :   **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – if specified, return the roots for the `activity`

        Returns:
        :   list of root activity names

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    assign_subactivities(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity")*, *activities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.assign_subactivities)
    :   `assign_subactivities` Assign the list of `activities` as the new set of children for
        the specified `activity`.

        Parameters:
        :   - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the Activity node to assign children
            - **activities** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – the list of Activities to assign

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    clear() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.clear)
    :   `clear` Remove all Activity nodes from this Workflow.

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    clone(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [Workflow](#binaryninja.workflow.Workflow "binaryninja.workflow.Workflow")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.clone)
    :   `clone` Clone a new Workflow, copying all Activities and the execution strategy.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – if specified, name the new Workflow, otherwise the name is copied from the
              original
            - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – if specified, perform the clone operation using `activity` as the root

        Returns:
        :   a new Workflow

        Return type:
        :   [*Workflow*](#binaryninja.workflow.Workflow "binaryninja.workflow.Workflow")

    configuration(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.configuration)
    :   `configuration` Retrieve the configuration as an adjacency list in JSON for the
        Workflow, or if specified just for the given `activity`.

        Parameters:
        :   **activity** (*ActivityType*) – if specified, return the configuration for the
            `activity`

        Returns:
        :   an adjacency list representation of the configuration in JSON

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    contains(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.contains)
    :   `contains` Determine if an Activity exists in this Workflow.

        Parameters:
        :   **activity** (*ActivityType*) – the Activity name

        Returns:
        :   True if the Activity exists, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    eligibility_settings() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.eligibility_settings)
    :   `eligibility_settings` Retrieve the list of eligibility settings for the Workflow.

        Returns:
        :   list of eligibility settings

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_activity(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.get_activity)
    :   `get_activity` Retrieve the Activity object for the specified `activity`.

        Parameters:
        :   **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – the Activity name

        Returns:
        :   the Activity object

        Return type:
        :   [*Activity*](#binaryninja.workflow.Activity "binaryninja.workflow.Activity")

    graph(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *sequential: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *show: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.graph)
    :   `graph` Generate a FlowGraph object for the current Workflow and optionally show it in
        the UI.

        Parameters:
        :   - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – if specified, generate the Flowgraph using `activity` as the root
            - **sequential** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – whether to generate a **Composite** or **Sequential** style graph
            - **show** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – whether to show the graph in the UI or not

        Returns:
        :   FlowGraph object on success, None on failure

        Return type:
        :   [*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph")

    insert(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *activities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.insert)
    :   `insert` Insert the list of `activities` before the specified `activity` and at the same
        level.

        Parameters:
        :   - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the Activity node for which to insert `activities` before
            - **activities** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – the list of Activities to insert

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    insert_after(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *activities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.insert_after)
    :   `insert_after` Insert the list of `activities` after the specified `activity` and at the
        same level.

        Parameters:
        :   - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the Activity node for which to insert `activities` after
            - **activities** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – the list of Activities to insert

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    register(*configuration: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.register)
    :   `register` Register this Workflow, making it immutable and available for use.

        Parameters:
        :   **configuration** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")) – a JSON representation of the workflow configuration

        Returns:
        :   True on Success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    register_activity(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity")*, *subactivities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = []*) → [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.register_activity)
    :   `register_activity` Register an Activity with this Workflow.

        Parameters:
        :   - **activity** ([*Activity*](#binaryninja.workflow.Activity
              "binaryninja.workflow.Activity")) – the Activity to register
            - **subactivities** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – the list of Activities to assign

        Returns:
        :   the registered Activity

        Return type:
        :   [*Activity*](#binaryninja.workflow.Activity "binaryninja.workflow.Activity")

    remove(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.remove)
    :   `remove` Remove the specified `activity`.

        Parameters:
        :   **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – the Activity to remove

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    replace(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *new_activity: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.replace)
    :   `replace` Replace the specified `activity`.

        Parameters:
        :   - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the Activity to replace
            - **new_activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – the replacement Activity

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    show_topology() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.show_topology)
    :   `show_topology` Show the Workflow topology in the UI.

        Return type:
        :   *None*

    subactivities(*activity: [Activity](#binaryninja.workflow.Activity "binaryninja.workflow.Activity") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *immediate: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#Workflow.subactivities)
    :   `subactivities` Retrieve the list of all activities, or optionally a filtered list.

        Parameters:
        :   - **activity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – if specified, return the direct children and optionally the descendants of
              the `activity` (includes `activity`)
            - **immediate** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – whether to include only direct children of `activity` or all
              descendants

        Returns:
        :   list of activity names

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    *property* machine

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* registered*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   `registered` Whether this Workflow is registered or not. A Workflow becomes immutable
        once it is registered.

        Type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## WorkflowMachine

*class* WorkflowMachine[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: LP_BNFunction | LP_BNBinaryView | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.__init__)
    :   Parameters:
        :   **handle** (*LP_BNFunction* *|* *LP_BNBinaryView* *|* *None*) –

    breakpoint_delete(*activities*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.breakpoint_delete)

    breakpoint_query()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.breakpoint_query)

    breakpoint_set(*activities*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.breakpoint_set)

    cli()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.cli)

    configure(*advanced: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *incremental: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.configure)
    :   Parameters:
        :   - **advanced** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **incremental** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    delay(*duration*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.delay)

    disable()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.disable)

    dump()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.dump)

    enable()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.enable)

    halt()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.halt)

    log(*enable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *is_global: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.log)
    :   Parameters:
        :   - **enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **is_global** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    metrics(*enable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *is_global: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.metrics)
    :   Parameters:
        :   - **enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **is_global** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    override_clear(*activity*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.override_clear)

    override_query(*activity=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.override_query)

    override_set(*activity*, *enable*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.override_set)

    request(*request*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.request)

    reset()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.reset)

    resume(*advanced: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *incremental: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.resume)
    :   Parameters:
        :   - **advanced** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **incremental** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    run(*advanced: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *incremental: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.run)
    :   Parameters:
        :   - **advanced** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **incremental** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    show_metrics() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.show_metrics)
    :   Return type:
        :   *None*

    show_topology() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.show_topology)
    :   Return type:
        :   *None*

    show_trace() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.show_trace)
    :   Return type:
        :   *None*

    status()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.status)

    step()[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachine.step)

## WorkflowMachineCLI

*class* WorkflowMachineCLI[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI)
:   Bases: [`Cmd`](https://docs.python.org/3/library/cmd.html#cmd.Cmd "(in Python v3.14)")

    __init__(*machine: [WorkflowMachine](#binaryninja.workflow.WorkflowMachine "binaryninja.workflow.WorkflowMachine")*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.__init__)
    :   Instantiate a line-oriented interpreter framework.

        The optional argument ‘completekey’ is the readline name of a completion key; it
        defaults to the Tab key. If completekey is not None and the readline module is
        available, command completion is done automatically. The optional arguments stdin and
        stdout specify alternate input and output file objects; if not specified, sys.stdin and
        sys.stdout are used.

        Parameters:
        :   **machine** ([*WorkflowMachine*](#binaryninja.workflow.WorkflowMachine
            "binaryninja.workflow.WorkflowMachine")) –

    do_breakpoint(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_breakpoint)
    :   Handle breakpoint commands.

    do_configure(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_configure)
    :   Configure the workflow machine.

    do_disable(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_disable)
    :   Disable the workflow machine.

    do_dump(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_dump)
    :   Dump metrics from the workflow system.

    do_enable(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_enable)
    :   Enable the workflow machine.

    do_halt(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_halt)
    :   Halt the workflow machine.

    do_log(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_log)
    :   Control workflow logging.

    do_metrics(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_metrics)
    :   Control workflow metrics collection.

    do_override(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_override)
    :   Handle override commands.

    do_quit(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_quit)
    :   Exit the WorkflowMachine CLI.

    do_reset(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_reset)
    :   Reset the workflow machine.

    do_resume(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_resume)
    :   Continue/Resume execution of a workflow.

    do_run(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_run)
    :   Run the workflow machine and generate a default configuration if the workflow is not
        configured.

    do_status(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_status)
    :   Retrieve the current machine status.

    do_step(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.do_step)
    :   Step to the next activity in the workflow machine.

    help(*arg*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.help)

    precmd(*line*)[[source]](https://api.binary.ninja/_modules/binaryninja/workflow.html#WorkflowMachineCLI.precmd)
    :   Hook method executed just before the command line is interpreted, but after the input
        prompt is generated and issued.

    aliases *= {'b': 'breakpoint', 'c': 'resume', 'd': 'dump', 'h': 'halt', 'l': 'log', 'm': 'metrics', 'o': 'override', 'q': 'quit', 'r': 'run', 's': 'step'}*

    intro *= "Welcome to the Workflow Orchestrator. Type 'help' to list available commands."*

    prompt *= '(dechora) '*
