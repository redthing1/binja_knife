# typeparser module

| Class | Description |
| --- | --- |
| [`binaryninja.typeparser.BasicTypeParserResult`](#binaryninja.typeparser.BasicTypeParserResult "binaryninja.typeparser.BasicTypeParserResult") |  |
| [`binaryninja.typeparser.CoreTypeParser`](#binaryninja.typeparser.CoreTypeParser "binaryninja.typeparser.CoreTypeParser") |  |
| [`binaryninja.typeparser.ParsedType`](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType") |  |
| [`binaryninja.typeparser.QualifiedNameTypeAndId`](#binaryninja.typeparser.QualifiedNameTypeAndId "binaryninja.typeparser.QualifiedNameTypeAndId") |  |
| [`binaryninja.typeparser.TypeParser`](#binaryninja.typeparser.TypeParser "binaryninja.typeparser.TypeParser") |  |
| [`binaryninja.typeparser.TypeParserError`](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError") |  |
| [`binaryninja.typeparser.TypeParserResult`](#binaryninja.typeparser.TypeParserResult "binaryninja.typeparser.TypeParserResult") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.typeparser.to_bytes`](#binaryninja.typeparser.to_bytes "binaryninja.typeparser.to_bytes") |  |

## BasicTypeParserResult

*class* BasicTypeParserResult[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#BasicTypeParserResult)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    BasicTypeParserResult(types: Dict[ForwardRef(‘types.QualifiedName’),
    ForwardRef(‘types.Type’)], variables: Dict[ForwardRef(‘types.QualifiedName’),
    ForwardRef(‘types.Type’)], functions: Dict[ForwardRef(‘types.QualifiedName’),
    ForwardRef(‘types.Type’)])

    __init__(*types: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*, *variables: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*, *functions: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **types** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]*) –
            - **variables** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]*) –
            - **functions** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]*) –

        Return type:
        :   *None*

    functions*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*

    types*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*

    variables*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*

## CoreTypeParser

*class* CoreTypeParser[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#CoreTypeParser)
:   Bases: [`TypeParser`](#binaryninja.typeparser.TypeParser
    "binaryninja.typeparser.TypeParser")

    get_option_text(*option: [TypeParserOption](enums.md#binaryninja.enums.TypeParserOption "binaryninja.enums.TypeParserOption")*, *value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#CoreTypeParser.get_option_text)
    :   Get the string representation of an option for passing to parse_type_*

        Parameters:
        :   - **option** ([*TypeParserOption*](enums.md#binaryninja.enums.TypeParserOption
              "binaryninja.enums.TypeParserOption")) – Option type
            - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Option value

        Returns:
        :   A string representing the option if the parser supports it, otherwise None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    parse_type_string(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *existing_types: types.TypeContainerType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[types.QualifiedNameType, [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#CoreTypeParser.parse_type_string)
    :   Parse a single type and name from a string containing their definition.

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to parse
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform to assume the types are relevant to
            - **existing_types** (*types.TypeContainerType* *|* *None*) – Optional container of all
              existing types to use for parsing context

        Returns:
        :   A tuple of (result, errors) where result is a tuple of (type, name) or None of there was
            a fatal error.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[types.QualifiedNameType, [*Type*](types.md#binaryninja.types.Type
            "binaryninja.types.Type")] | *None*,
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeParserError*](#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    parse_types_from_source(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *file_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *existing_types: types.TypeContainerType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto_type_source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeParserResult](#binaryninja.typeparser.TypeParserResult "binaryninja.typeparser.TypeParserResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#CoreTypeParser.parse_types_from_source)
    :   Parse an entire block of source into types, variables, and functions

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to parse
            - **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the file containing the source (optional: exists on disk)
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform to assume the types are relevant to
            - **existing_types** (*types.TypeContainerType* *|* *None*) – Optional container of all
              existing types to use for parsing context
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional string arguments to pass as options, e.g.
              command line arguments
            - **include_dirs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of directories to include in the header
              search path
            - **auto_type_source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – Optional source of types if used for automatically generated types

        Returns:
        :   A tuple of (result, errors) where the result is None if there was a fatal error

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*TypeParserResult*](#binaryninja.typeparser.TypeParserResult
            "binaryninja.typeparser.TypeParserResult") | *None*,
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeParserError*](#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    preprocess_source(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *file_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *existing_types: types.TypeContainerType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#CoreTypeParser.preprocess_source)
    :   Preprocess a block of source, returning the source that would be parsed

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to process
            - **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the file containing the source (does not need to exist on disk)
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform to assume the source is relevant to
            - **existing_types** (*types.TypeContainerType* *|* *None*) – Optional collection of all
              existing types to use for parsing context
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional string arguments to pass as options, e.g.
              command line arguments
            - **include_dirs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of directories to include in the header
              search path

        Returns:
        :   A tuple of (preproccessed source, errors), where the preproccessed source is None if
            there was a fatal error.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") | *None*, [*List*](https://docs.python.org/3/library/typing.html#typing.List
            "(in Python v3.14)")[[*TypeParserError*](#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

## ParsedType

*class* ParsedType[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#ParsedType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ParsedType(name: ‘types.QualifiedNameType’, type: ‘types.Type’, is_user: bool)

    __init__(*name: types.QualifiedNameType*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *is_user: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** (*types.QualifiedNameType*) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **is_user** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    is_user*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    name*: types.QualifiedNameType*

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

## QualifiedNameTypeAndId

*class* QualifiedNameTypeAndId[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#QualifiedNameTypeAndId)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    QualifiedNameTypeAndId(name: ‘types.QualifiedNameType’, id: str, type: ‘types.Type’)

    __init__(*name: types.QualifiedNameType*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** (*types.QualifiedNameType*) –
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   *None*

    id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    name*: types.QualifiedNameType*

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

## TypeParser

*class* TypeParser[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser.__init__)

    get_option_text(*option: [TypeParserOption](enums.md#binaryninja.enums.TypeParserOption "binaryninja.enums.TypeParserOption")*, *value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser.get_option_text)
    :   Get the string representation of an option for passing to parse_type_*

        Parameters:
        :   - **option** ([*TypeParserOption*](enums.md#binaryninja.enums.TypeParserOption
              "binaryninja.enums.TypeParserOption")) – Option type
            - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Option value

        Returns:
        :   A string representing the option if the parser supports it, otherwise None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    parse_type_string(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *existing_types: types.TypeContainerType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[types.QualifiedNameType, [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser.parse_type_string)
    :   Parse a single type and name from a string containing their definition.

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to parse
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform to assume the types are relevant to
            - **existing_types** (*types.TypeContainerType* *|* *None*) – Optional container of all
              existing types to use for parsing context

        Returns:
        :   A tuple of (result, errors) where result is a tuple of (type, name) or None of there was
            a fatal error.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[types.QualifiedNameType, [*Type*](types.md#binaryninja.types.Type
            "binaryninja.types.Type")] | *None*,
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeParserError*](#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    parse_types_from_source(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *file_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *existing_types: types.TypeContainerType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto_type_source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeParserResult](#binaryninja.typeparser.TypeParserResult "binaryninja.typeparser.TypeParserResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser.parse_types_from_source)
    :   Parse an entire block of source into types, variables, and functions

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to parse
            - **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the file containing the source (optional: exists on disk)
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform to assume the types are relevant to
            - **existing_types** (*types.TypeContainerType* *|* *None*) – Optional container of all
              existing types to use for parsing context
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional string arguments to pass as options, e.g.
              command line arguments
            - **include_dirs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of directories to include in the header
              search path
            - **auto_type_source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – Optional source of types if used for automatically generated types

        Returns:
        :   A tuple of (result, errors) where the result is None if there was a fatal error

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*TypeParserResult*](#binaryninja.typeparser.TypeParserResult
            "binaryninja.typeparser.TypeParserResult") | *None*,
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeParserError*](#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    preprocess_source(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *file_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *existing_types: types.TypeContainerType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser.preprocess_source)
    :   Preprocess a block of source, returning the source that would be parsed

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to process
            - **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the file containing the source (does not need to exist on disk)
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform to assume the source is relevant to
            - **existing_types** (*types.TypeContainerType* *|* *None*) – Optional collection of all
              existing types to use for parsing context
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional string arguments to pass as options, e.g.
              command line arguments
            - **include_dirs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of directories to include in the header
              search path

        Returns:
        :   A tuple of (preproccessed source, errors), where the preproccessed source is None if
            there was a fatal error.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") | *None*, [*List*](https://docs.python.org/3/library/typing.html#typing.List
            "(in Python v3.14)")[[*TypeParserError*](#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParser.register)
    :   Register a custom parser with the API

    name *= None*

## TypeParserError

*class* TypeParserError[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParserError)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    TypeParserError(severity: binaryninja.enums.TypeParserErrorSeverity, message: str,
    file_name: str, line: int, column: int)

    __init__(*severity: [TypeParserErrorSeverity](enums.md#binaryninja.enums.TypeParserErrorSeverity "binaryninja.enums.TypeParserErrorSeverity")*, *message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *file_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *line: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *column: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **severity**
              ([*TypeParserErrorSeverity*](enums.md#binaryninja.enums.TypeParserErrorSeverity
              "binaryninja.enums.TypeParserErrorSeverity")) –
            - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **line** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **column** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    column*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    file_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    line*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    message*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    severity*: [TypeParserErrorSeverity](enums.md#binaryninja.enums.TypeParserErrorSeverity "binaryninja.enums.TypeParserErrorSeverity")*

## TypeParserResult

*class* TypeParserResult[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#TypeParserResult)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    TypeParserResult(types: List[binaryninja.typeparser.ParsedType], variables:
    List[binaryninja.typeparser.ParsedType], functions:
    List[binaryninja.typeparser.ParsedType])

    __init__(*types: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ParsedType](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType")]*, *variables: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ParsedType](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType")]*, *functions: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ParsedType](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **types** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ParsedType*](#binaryninja.typeparser.ParsedType
              "binaryninja.typeparser.ParsedType")*]*) –
            - **variables** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ParsedType*](#binaryninja.typeparser.ParsedType
              "binaryninja.typeparser.ParsedType")*]*) –
            - **functions** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ParsedType*](#binaryninja.typeparser.ParsedType
              "binaryninja.typeparser.ParsedType")*]*) –

        Return type:
        :   *None*

    functions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ParsedType](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType")]*

    types*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ParsedType](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType")]*

    variables*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ParsedType](#binaryninja.typeparser.ParsedType "binaryninja.typeparser.ParsedType")]*

## to_bytes

to_bytes(*field*)[[source]](https://api.binary.ninja/_modules/binaryninja/typeparser.html#to_bytes)
