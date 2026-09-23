# debuginfo module

| Class | Description |
| --- | --- |
| [`binaryninja.debuginfo.DebugFunctionInfo`](#binaryninja.debuginfo.DebugFunctionInfo "binaryninja.debuginfo.DebugFunctionInfo") | `DebugFunctionInfo` collates ground-truth function attributes for use in BinaryNinja’s analysis. |
| [`binaryninja.debuginfo.DebugInfo`](#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo") | `class DebugInfo` provides an interface to both provide and query debug info. The DebugInfo… |
| [`binaryninja.debuginfo.DebugInfoParser`](#binaryninja.debuginfo.DebugInfoParser "binaryninja.debuginfo.DebugInfoParser") | [`DebugInfoParser`](#binaryninja.debuginfo.DebugInfoParser "binaryninja.debuginfo.DebugInfoParser") represents the registered parsers and providers of debug information… |

## DebugFunctionInfo

*class* DebugFunctionInfo[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugFunctionInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `DebugFunctionInfo` collates ground-truth function attributes for use in BinaryNinja’s
    analysis.

    When contributing function info, provide only what you know - BinaryNinja will figure
    out everything else that it can.

    Functions will not be created if an address is not provided, but are able to be queried
    by the user from bv.debug_info for later analysis.

    __init__(*address: int | None = None*, *short_name: str | None = None*, *full_name: str | None = None*, *raw_name: str | None = None*, *function_type: ~binaryninja.types.Type | None = None*, *platform: ~binaryninja.platform.Platform | None = None*, *components: ~typing.List[str] = <factory>*, *local_variables: ~typing.List[~binaryninja.variable.VariableNameAndType] = <factory>*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **short_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **full_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **raw_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **function_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")
              *|* *None*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **components** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) –
            - **local_variables** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python
              v3.14)")*[*[*VariableNameAndType*](variable.md#binaryninja.variable.VariableNameAndType
              "binaryninja.variable.VariableNameAndType")*]*) –

        Return type:
        :   *None*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    components*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

    full_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    function_type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    local_variables*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[VariableNameAndType](variable.md#binaryninja.variable.VariableNameAndType "binaryninja.variable.VariableNameAndType")]*

    platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    raw_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    short_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

## DebugInfo

*class* DebugInfo[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class DebugInfo` provides an interface to both provide and query debug info. The
    DebugInfo object is used internally by the binary view to which it is applied to
    determine the attributes of functions, types, and variables that would otherwise be
    costly to deduce.

    DebugInfo objects themselves are independent of binary views; their data can be sourced
    from any arbitrary binary views and be applied to any other arbitrary binary view. A
    DebugInfo object can also contain debug info from multiple DebugInfoParsers. This makes
    it possible to gather debug info that may be distributed across several different
    formats and files.

    DebugInfo cannot be instantiated by the user, instead you must get it from either the
    binary view (see `'binaryview.BinaryView'.debug_info`) or a debug-info parser (see
    `debuginfo.DebugInfoParser.parse_debug_info`).

    Note

    Please note that calling one of `add_*` functions will not work outside of a debuginfo
    plugin.

    __init__(*handle: BNDebugInfo*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.__init__)
    :   Parameters:
        :   **handle** (*BNDebugInfo*) –

        Return type:
        :   *None*

    add_data_variable(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *new_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *components: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.add_data_variable)
    :   Adds a data variable scoped under the current parser’s name to the debug info.
        Optionally, you can provide a path of component names under which that data variable
        should appear in the symbols sidebar.

        Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **new_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **components** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    add_function(*new_func: [DebugFunctionInfo](#binaryninja.debuginfo.DebugFunctionInfo "binaryninja.debuginfo.DebugFunctionInfo")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.add_function)
    :   Adds a function scoped under the current parser’s name to the debug info

        Parameters:
        :   **new_func** ([*DebugFunctionInfo*](#binaryninja.debuginfo.DebugFunctionInfo
            "binaryninja.debuginfo.DebugFunctionInfo")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    add_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *new_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *components: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.add_type)
    :   Adds a type scoped under the current parser’s name to the debug info. While you’re able
        to provide a list of components a type should live in, this is currently unused.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **new_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **components** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    data_variables_from_parser(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[DataVariableAndName](binaryview.md#binaryninja.binaryview.DataVariableAndName "binaryninja.binaryview.DataVariableAndName")][[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.data_variables_from_parser)
    :   Returns a generator of all data variables provided by a named DebugInfoParser

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) –

        Return type:
        :   [*Iterator*](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python
            v3.14)")[[*DataVariableAndName*](binaryview.md#binaryninja.binaryview.DataVariableAndName
            "binaryninja.binaryview.DataVariableAndName")]

    functions_from_parser(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[DebugFunctionInfo](#binaryninja.debuginfo.DebugFunctionInfo "binaryninja.debuginfo.DebugFunctionInfo")][[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.functions_from_parser)
    :   Returns a generator of all functions provided by a named DebugInfoParser

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) –

        Return type:
        :   [*Iterator*](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python
            v3.14)")[[*DebugFunctionInfo*](#binaryninja.debuginfo.DebugFunctionInfo
            "binaryninja.debuginfo.DebugFunctionInfo")]

    get_data_variable_by_address(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_data_variable_by_address)
    :   Parameters:
        :   - **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")] | *None*

    get_data_variable_by_name(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_data_variable_by_name)
    :   Parameters:
        :   - **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")] | *None*

    get_data_variables_by_address(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]][[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_data_variables_by_address)
    :   The values in the tuples returned in the list is (DebugInfoParserName, TypeName, type)

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")]]

    get_data_variables_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]][[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_data_variables_by_name)
    :   The values in the tuples returned in the list is (DebugInfoParserName, address, type)

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")]]

    get_type_by_name(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_type_by_name)
    :   Parameters:
        :   - **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*

    get_type_container(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_type_container)
    :   Type Container for all types in the DebugInfo that resulted from the parse of the given
        parser.

        Parameters:
        :   **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of parser

        Returns:
        :   Type Container for types from that parser

        Return type:
        :   [*TypeContainer*](typecontainer.md#binaryninja.typecontainer.TypeContainer
            "binaryninja.typecontainer.TypeContainer")

    get_types_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]][[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.get_types_by_name)
    :   The first element in the Tuple returned in the list is the name of the debug info parser
        the type came from

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")]]

    remove_data_variable_by_address(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_data_variable_by_address)
    :   Parameters:
        :   - **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    remove_function_by_index(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_function_by_index)
    :   Parameters:
        :   - **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    remove_parser_data_variables(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_parser_data_variables)
    :   Parameters:
        :   **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    remove_parser_functions(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_parser_functions)
    :   Parameters:
        :   **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    remove_parser_info(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_parser_info)
    :   Parameters:
        :   **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    remove_parser_types(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_parser_types)
    :   Parameters:
        :   **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    remove_type_by_name(*parser_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.remove_type_by_name)
    :   Parameters:
        :   - **parser_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

    types_from_parser(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]][[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfo.types_from_parser)
    :   Returns a generator of all types provided by a named DebugInfoParser

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) –

        Return type:
        :   [*Iterator*](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")]]

    *property* data_variables*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[DataVariableAndName](binaryview.md#binaryninja.binaryview.DataVariableAndName "binaryninja.binaryview.DataVariableAndName")]*
    :   A generator of all data variables provided by DebugInfoParsers

    *property* functions*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[DebugFunctionInfo](#binaryninja.debuginfo.DebugFunctionInfo "binaryninja.debuginfo.DebugFunctionInfo")]*
    :   A generator of all functions provided by DebugInfoParsers

    *property* parsers*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

    *property* types*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*
    :   A generator of all types provided by DebugInfoParsers

## DebugInfoParser

*class* DebugInfoParser[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfoParser)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    [`DebugInfoParser`](#binaryninja.debuginfo.DebugInfoParser
    "binaryninja.debuginfo.DebugInfoParser") represents the registered parsers and providers
    of debug information for Binary Ninja.

    The debug information is used by Binary Ninja as ground-truth information about the
    attributes of functions, types, and variables that Binary Ninja’s analysis pipeline
    would otherwise work to deduce. By providing debug info, Binary Ninja’s output can be
    generated quicker, more accurately, and more completely.

    A DebugInfoParser consists of:

    1. A name
    2. An `is_valid` function which takes a `binaryview.BinaryView` and returns a bool.
    3. A `parse` function which takes a [`DebugInfo`](#binaryninja.debuginfo.DebugInfo
       "binaryninja.debuginfo.DebugInfo") object and uses the member functions
       [`DebugInfo.add_type`](#binaryninja.debuginfo.DebugInfo.add_type
       "binaryninja.debuginfo.DebugInfo.add_type"),
       [`DebugInfo.add_function`](#binaryninja.debuginfo.DebugInfo.add_function
       "binaryninja.debuginfo.DebugInfo.add_function"), and
       [`DebugInfo.add_data_variable`](#binaryninja.debuginfo.DebugInfo.add_data_variable
       "binaryninja.debuginfo.DebugInfo.add_data_variable") to populate all the info it can.

    And finally calling `DebugInfoParser.register` to register it with the core.

    A working example:

    ```
    import binaryninja as bn

    def is_valid(bv: bn.binaryview.BinaryView) -> bool:
            return bv.view_type == "Raw"

    def parse_info(debug_info: bn.debuginfo.DebugInfo, bv: bn.binaryview.BinaryView, debug_file: bn.binaryview.BinaryView, progress: Callable[[int, int], bool]) -> None:
            debug_info.add_type("name", bn.types.Type.int(4, True))
            debug_info.add_data_variable(0x1234, bn.types.Type.int(4, True), "name")
            function_info = bn.debuginfo.DebugFunctionInfo(0xadd6355, "short_name", "full_name", "raw_name", bn.types.Type.function(bn.types.Type.int(4, False), None), components=["some", "namespaces"])
            debug_info.add_function(function_info)

    bn.debuginfo.DebugInfoParser.register("debug info parser", is_valid, parse_info)
    ```

    [`DebugInfo`](#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo") will
    then be automatically applied to binary views that contain debug information (via the
    setting analysis.debugInfo.internal), binary views that provide valid external debug
    info files (analysis.debugInfo.external), or manually fetched/applied as below:

    ```
    valid_parsers = bn.debuginfo.DebugInfoParser.get_parsers_for_view(bv)
    parser = valid_parsers[0]
    debug_info = parser.parse_debug_info(bv, bv)  # See docs for why BV is here twice
    bv.apply_debug_info(debug_info)
    ```

    Multiple debug-info parsers can manually contribute debug info for a binary view by
    simply calling `parse_debug_info` with the `DebugInfo` object just returned. This is
    automatic when opening a binary view with multiple valid debug info parsers. If you wish
    to set the debug info for a binary view without applying it as well, you can call
    `'binaryview.BinaryView'.set_debug_info`.

    __init__(*handle: BNDebugInfoParser*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfoParser.__init__)
    :   Parameters:
        :   **handle** (*BNDebugInfoParser*) –

        Return type:
        :   *None*

    is_valid_for_view(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfoParser.is_valid_for_view)
    :   Returns whether this debug-info parser is valid for the provided binary view

        Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    parse_debug_info(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *debug_view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *debug_info: [DebugInfo](#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *progress: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [DebugInfo](#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/debuginfo.html#DebugInfoParser.parse_debug_info)
    :   Returns a `DebugInfo` object populated with debug info by this debug-info parser. Only
        provide a `DebugInfo` object if you wish to append to the existing debug info.

        Some debug file formats need both the original `binaryview.BinaryView` (the binary being
        analyzed/having debug information applied to it) in addition to the
        `binaryview.BinaryView` of the file containing the debug information. For formats where
        you can get all the information you need from a single file, calls to `parse_debug_info`
        are required to provide that file for both arguments. For formats where you can get all
        the information you need from a single file, implementations of parse should only read
        from the second debug_file parameter and ignore the former.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **debug_view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **debug_info** ([*DebugInfo*](#binaryninja.debuginfo.DebugInfo
              "binaryninja.debuginfo.DebugInfo") *|* *None*) –
            - **progress** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
              "(in Python v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)")*]**,*
              [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*]*
              *|* *None*) –

        Return type:
        :   [*DebugInfo*](#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo") |
            *None*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Debug-info parser’s name (read-only)
