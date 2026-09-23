# typeprinter module

| Class | Description |
| --- | --- |
| [`binaryninja.typeprinter.CoreTypePrinter`](#binaryninja.typeprinter.CoreTypePrinter "binaryninja.typeprinter.CoreTypePrinter") | Class for turning Type objects into strings and tokens. |
| [`binaryninja.typeprinter.TypePrinter`](#binaryninja.typeprinter.TypePrinter "binaryninja.typeprinter.TypePrinter") | Class for turning Type objects into strings and tokens. |

| Function | Description |
| --- | --- |
| [`binaryninja.typeprinter.to_bytes`](#binaryninja.typeprinter.to_bytes "binaryninja.typeprinter.to_bytes") |  |

## CoreTypePrinter

*class* CoreTypePrinter[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter)
:   Bases: [`TypePrinter`](#binaryninja.typeprinter.TypePrinter
    "binaryninja.typeprinter.TypePrinter")

    get_type_lines(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *container: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *padding_cols=64*, *collapsed=False*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeDefinitionLine](types.md#binaryninja.types.TypeDefinitionLine "binaryninja.types.TypeDefinitionLine")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_lines)
    :   Generate a multi-line representation of a type

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **container**
              ([*TypeContainer*](typecontainer.md#binaryninja.typecontainer.TypeContainer
              "binaryninja.typecontainer.TypeContainer")) – Type Container containing the type and
              dependencies
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type
            - **padding_cols** – Maximum number of bytes represented by each padding line
            - **collapsed** – Whether to collapse structure/enum blocks
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of type definition lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeDefinitionLine*](types.md#binaryninja.types.TypeDefinitionLine
            "binaryninja.types.TypeDefinitionLine")]

    get_type_string(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") = ''*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_string)
    :   Generate a single-line text representation of a type

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   String representing the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_type_string_after_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_string_after_name)
    :   In a single-line text representation of a type, generate the string that should be
        printed after the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   String representing the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_type_string_before_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_string_before_name)
    :   In a single-line text representation of a type, generate the string that should be
        printed before the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   String representing the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_type_tokens(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") = ''*, *base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_tokens)
    :   Generate a single-line text representation of a type

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type
            - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence to use for tokens created for this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of text tokens representing the type

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    get_type_tokens_after_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *parent_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_tokens_after_name)
    :   In a single-line text representation of a type, generate the tokens that should be
        printed after the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence to use for tokens created for this type
            - **parent_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              *None*) – Type of the parent of this type, or None
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of text tokens representing the type

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    get_type_tokens_before_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *parent_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.get_type_tokens_before_name)
    :   In a single-line text representation of a type, generate the tokens that should be
        printed before the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence to use for tokens created for this type
            - **parent_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              *None*) – Type of the parent of this type, or None
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of text tokens representing the type

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    print_all_types(*types_: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*, *data: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *padding_cols=64*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#CoreTypePrinter.print_all_types)
    :   Print all types to a single big string, including headers, sections, etc

        Parameters:
        :   - **types** – All types to print
            - **data** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – Binary View in which all the types are defined
            - **padding_cols** – Maximum number of bytes represented by each padding line
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable
            - **types_** ([*Sequence*](https://docs.python.org/3/library/typing.html#typing.Sequence
              "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python
              v3.14)")*[*[*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]**]*)

        Returns:
        :   All the types in a string

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## TypePrinter

*class* TypePrinter[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class for turning Type objects into strings and tokens.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.__init__)

    *abstract* get_type_lines(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *container: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *padding_cols=64*, *collapsed=False*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeDefinitionLine](types.md#binaryninja.types.TypeDefinitionLine "binaryninja.types.TypeDefinitionLine")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_lines)
    :   Generate a multi-line representation of a type

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **container**
              ([*TypeContainer*](typecontainer.md#binaryninja.typecontainer.TypeContainer
              "binaryninja.typecontainer.TypeContainer")) – Type Container containing the type and
              dependencies
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type
            - **padding_cols** – Maximum number of bytes represented by each padding line
            - **collapsed** – Whether to collapse structure/enum blocks
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of type definition lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeDefinitionLine*](types.md#binaryninja.types.TypeDefinitionLine
            "binaryninja.types.TypeDefinitionLine")]

    get_type_string(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") = ''*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_string)
    :   Generate a single-line text representation of a type

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   String representing the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_type_string_after_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_string_after_name)
    :   In a single-line text representation of a type, generate the string that should be
        printed after the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   String representing the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_type_string_before_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_string_before_name)
    :   In a single-line text representation of a type, generate the string that should be
        printed before the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   String representing the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_type_tokens(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") = ''*, *base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_tokens)
    :   Generate a single-line text representation of a type

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type
            - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence to use for tokens created for this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of text tokens representing the type

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    *abstract* get_type_tokens_after_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *parent_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_tokens_after_name)
    :   In a single-line text representation of a type, generate the tokens that should be
        printed after the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence to use for tokens created for this type
            - **parent_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              *None*) – Type of the parent of this type, or None
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of text tokens representing the type

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    *abstract* get_type_tokens_before_name(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *parent_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.get_type_tokens_before_name)
    :   In a single-line text representation of a type, generate the tokens that should be
        printed before the type’s name.

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type to
              print
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform responsible for this type
            - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence to use for tokens created for this type
            - **parent_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              *None*) – Type of the parent of this type, or None
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   List of text tokens representing the type

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    print_all_types(*types: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*, *data: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *padding_cols=64*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.BackticksTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.print_all_types)
    :   Print all types to a single big string, including headers, sections, etc

        Parameters:
        :   - **types** ([*Sequence*](https://docs.python.org/3/library/typing.html#typing.Sequence
              "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python
              v3.14)")*[*[*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]**]*) – All types to print
            - **data** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – Binary View in which all the types are defined
            - **padding_cols** – Maximum number of bytes represented by each padding line
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – Style of escaping literals which may not be
              parsable

        Returns:
        :   All the types in a string

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#TypePrinter.register)

    name *= None*

## to_bytes

to_bytes(*field*)[[source]](https://api.binary.ninja/_modules/binaryninja/typeprinter.html#to_bytes)
