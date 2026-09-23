# types module

| Class | Description |
| --- | --- |
| [`binaryninja.types.ArrayBuilder`](#binaryninja.types.ArrayBuilder "binaryninja.types.ArrayBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.ArrayType`](#binaryninja.types.ArrayType "binaryninja.types.ArrayType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.BaseStructure`](#binaryninja.types.BaseStructure "binaryninja.types.BaseStructure") |  |
| [`binaryninja.types.BoolBuilder`](#binaryninja.types.BoolBuilder "binaryninja.types.BoolBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.BoolType`](#binaryninja.types.BoolType "binaryninja.types.BoolType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.BoolWithConfidence`](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") |  |
| [`binaryninja.types.CharBuilder`](#binaryninja.types.CharBuilder "binaryninja.types.CharBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.CharType`](#binaryninja.types.CharType "binaryninja.types.CharType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.CoreSymbol`](#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") |  |
| [`binaryninja.types.EnumerationBuilder`](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.EnumerationMember`](#binaryninja.types.EnumerationMember "binaryninja.types.EnumerationMember") |  |
| [`binaryninja.types.EnumerationType`](#binaryninja.types.EnumerationType "binaryninja.types.EnumerationType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.FloatBuilder`](#binaryninja.types.FloatBuilder "binaryninja.types.FloatBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.FloatType`](#binaryninja.types.FloatType "binaryninja.types.FloatType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.FunctionBuilder`](#binaryninja.types.FunctionBuilder "binaryninja.types.FunctionBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.FunctionParameter`](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter") |  |
| [`binaryninja.types.FunctionType`](#binaryninja.types.FunctionType "binaryninja.types.FunctionType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.InheritedStructureMember`](#binaryninja.types.InheritedStructureMember "binaryninja.types.InheritedStructureMember") |  |
| [`binaryninja.types.InlineDuringAnalysisWithConfidence`](#binaryninja.types.InlineDuringAnalysisWithConfidence "binaryninja.types.InlineDuringAnalysisWithConfidence") | Represents an InlineDuringAnalysis value with an associated confidence level. |
| [`binaryninja.types.IntegerBuilder`](#binaryninja.types.IntegerBuilder "binaryninja.types.IntegerBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.IntegerType`](#binaryninja.types.IntegerType "binaryninja.types.IntegerType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.MutableTypeBuilder`](#binaryninja.types.MutableTypeBuilder "binaryninja.types.MutableTypeBuilder") |  |
| [`binaryninja.types.NameSpace`](#binaryninja.types.NameSpace "binaryninja.types.NameSpace") |  |
| [`binaryninja.types.NamedTypeReferenceBuilder`](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.NamedTypeReferenceType`](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.OffsetWithConfidence`](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence") |  |
| [`binaryninja.types.PointerBuilder`](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.PointerType`](#binaryninja.types.PointerType "binaryninja.types.PointerType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.QualifiedName`](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") |  |
| [`binaryninja.types.RegisterSet`](#binaryninja.types.RegisterSet "binaryninja.types.RegisterSet") |  |
| [`binaryninja.types.RegisterStackAdjustmentWithConfidence`](#binaryninja.types.RegisterStackAdjustmentWithConfidence "binaryninja.types.RegisterStackAdjustmentWithConfidence") |  |
| [`binaryninja.types.StructureBuilder`](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.StructureMember`](#binaryninja.types.StructureMember "binaryninja.types.StructureMember") |  |
| [`binaryninja.types.StructureType`](#binaryninja.types.StructureType "binaryninja.types.StructureType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.Symbol`](#binaryninja.types.Symbol "binaryninja.types.Symbol") | Symbols are defined as one of the following types: |
| [`binaryninja.types.Type`](#binaryninja.types.Type "binaryninja.types.Type") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.TypeBuilderAttributes`](#binaryninja.types.TypeBuilderAttributes "binaryninja.types.TypeBuilderAttributes") | dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping… |
| [`binaryninja.types.TypeDefinitionLine`](#binaryninja.types.TypeDefinitionLine "binaryninja.types.TypeDefinitionLine") |  |
| [`binaryninja.types.TypeFieldReference`](#binaryninja.types.TypeFieldReference "binaryninja.types.TypeFieldReference") |  |
| [`binaryninja.types.TypeReferenceSource`](#binaryninja.types.TypeReferenceSource "binaryninja.types.TypeReferenceSource") |  |
| [`binaryninja.types.VoidBuilder`](#binaryninja.types.VoidBuilder "binaryninja.types.VoidBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.VoidType`](#binaryninja.types.VoidType "binaryninja.types.VoidType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |
| [`binaryninja.types.WideCharBuilder`](#binaryninja.types.WideCharBuilder "binaryninja.types.WideCharBuilder") | All TypeBuilder objects should not be instantiated directly but created via `.create` APIs. |
| [`binaryninja.types.WideCharType`](#binaryninja.types.WideCharType "binaryninja.types.WideCharType") | `class Type` allows you to interact with the Binary Ninja type system. Note that the `repr`… |

| Function | Description |
| --- | --- |
| [`binaryninja.types.convert_integer`](#binaryninja.types.convert_integer "binaryninja.types.convert_integer") |  |

## ArrayBuilder

*class* ArrayBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#ArrayBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *classmethod* create(*type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *element_count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [ArrayBuilder](#binaryninja.types.ArrayBuilder "binaryninja.types.ArrayBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#ArrayBuilder.create)
    :   Parameters:
        :   - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **element_count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*ArrayBuilder*](#binaryninja.types.ArrayBuilder "binaryninja.types.ArrayBuilder")

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")]*

    *property* count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* element_type*: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*

## ArrayType

*class* ArrayType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#ArrayType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*element_type: [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [ArrayType](#binaryninja.types.ArrayType "binaryninja.types.ArrayType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#ArrayType.create)
    :   Parameters:
        :   - **element_type** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) –
            - **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*ArrayType*](#binaryninja.types.ArrayType "binaryninja.types.ArrayType")

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")]*

    *property* count
    :   Type count (read-only)

    *property* element_type*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

## BaseStructure

*class* BaseStructure[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BaseStructure)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    BaseStructure(type: Union[ForwardRef(‘NamedTypeReferenceType’),
    ForwardRef(‘StructureType’)], offset: int, width: int = 0)

    __init__(*type: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType") | [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BaseStructure.__init__)
    :   Parameters:
        :   - **type** ([*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
              "binaryninja.types.NamedTypeReferenceType") *|*
              [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")*

    width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## BoolBuilder

*class* BoolBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *classmethod* create(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [BoolBuilder](#binaryninja.types.BoolBuilder "binaryninja.types.BoolBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolBuilder.create)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*BoolBuilder*](#binaryninja.types.BoolBuilder "binaryninja.types.BoolBuilder")

## BoolType

*class* BoolType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [BoolType](#binaryninja.types.BoolType "binaryninja.types.BoolType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolType.create)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*BoolType*](#binaryninja.types.BoolType "binaryninja.types.BoolType")

## BoolWithConfidence

*class* BoolWithConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolWithConfidence)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    BoolWithConfidence(value: bool, confidence: int = 255)

    __init__(*value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *classmethod* from_core_struct(*core_struct: BNBoolWithConfidence*) → [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolWithConfidence.from_core_struct)
    :   Parameters:
        :   **core_struct** (*BNBoolWithConfidence*) –

        Return type:
        :   [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence")

    *static* get_core_struct(*value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → BNBoolWithConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#BoolWithConfidence.get_core_struct)
    :   Parameters:
        :   - **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *BNBoolWithConfidence*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    value*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## CharBuilder

*class* CharBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CharBuilder)
:   Bases: [`IntegerBuilder`](#binaryninja.types.IntegerBuilder
    "binaryninja.types.IntegerBuilder")

    *classmethod* create(*alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [CharBuilder](#binaryninja.types.CharBuilder "binaryninja.types.CharBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CharBuilder.create)
    :   Parameters:
        :   - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*CharBuilder*](#binaryninja.types.CharBuilder "binaryninja.types.CharBuilder")

## CharType

*class* CharType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CharType)
:   Bases: [`IntegerType`](#binaryninja.types.IntegerType "binaryninja.types.IntegerType")

    *classmethod* create(*altname: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'char'*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [CharType](#binaryninja.types.CharType "binaryninja.types.CharType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CharType.create)
    :   Parameters:
        :   - **altname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*CharType*](#binaryninja.types.CharType "binaryninja.types.CharType")

## CoreSymbol

*class* CoreSymbol[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CoreSymbol)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: LP_BNSymbol*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CoreSymbol.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSymbol*) –

    imported_function_from_import_address_symbol(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [CoreSymbol](#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#CoreSymbol.imported_function_from_import_address_symbol)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*CoreSymbol*](#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | *None*

    *property* address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Symbol address (read-only)

    *property* auto*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the symbol was auto-defined

    *property* binding*: [SymbolBinding](enums.md#binaryninja.enums.SymbolBinding "binaryninja.enums.SymbolBinding")*
    :   Symbol binding (read-only)

    *property* full_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Symbol full name (read-only)

    *property* handle

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Symbol name (read-only)

    *property* namespace*: [NameSpace](#binaryninja.types.NameSpace "binaryninja.types.NameSpace")*
    :   Symbol namespace (read-only)

    *property* ordinal*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Symbol ordinal (read-only)

    *property* raw_bytes*: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*
    :   Bytes of the raw symbol (read-only)

    *property* raw_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Symbol raw name (read-only)

    *property* short_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Symbol short name (read-only)

    *property* type*: [SymbolType](enums.md#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType")*
    :   Symbol type (read-only)

## EnumerationBuilder

*class* EnumerationBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    __init__(*handle: LP_BNTypeBuilder*, *enum_builder_handle: LP_BNEnumerationBuilder*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationBuilder.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNTypeBuilder*) –
            - **enum_builder_handle** (*LP_BNEnumerationBuilder*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    append(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationBuilder.append)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Return type:
        :   [*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
            "binaryninja.types.EnumerationBuilder")

    *classmethod* create(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[EnumerationMember](#binaryninja.types.EnumerationMember "binaryninja.types.EnumerationMember")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationBuilder.create)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]**]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*EnumerationMember*](#binaryninja.types.EnumerationMember
              "binaryninja.types.EnumerationMember")*]* *|* *None*) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
            "binaryninja.types.EnumerationBuilder")

    remove(*i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationBuilder.remove)
    :   Parameters:
        :   **i** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
            "binaryninja.types.EnumerationBuilder")

    replace(*i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationBuilder.replace)
    :   Parameters:
        :   - **i** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
            "binaryninja.types.EnumerationBuilder")

    *property* members*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[EnumerationMember](#binaryninja.types.EnumerationMember "binaryninja.types.EnumerationMember")]*
    :   Enumeration member list (read-only)

## EnumerationMember

*class* EnumerationMember[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationMember)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    EnumerationMember(name: str, value: Optional[int] = None)

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Return type:
        :   *None*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

## EnumerationType

*class* EnumerationType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationType)
:   Bases: [`IntegerType`](#binaryninja.types.IntegerType "binaryninja.types.IntegerType")

    __init__(*handle*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationType.__init__)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *classmethod* create(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[EnumerationMember](#binaryninja.types.EnumerationMember "binaryninja.types.EnumerationMember")]*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [EnumerationType](#binaryninja.types.EnumerationType "binaryninja.types.EnumerationType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationType.create)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]**]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*EnumerationMember*](#binaryninja.types.EnumerationMember
              "binaryninja.types.EnumerationMember")*]*) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*EnumerationType*](#binaryninja.types.EnumerationType
            "binaryninja.types.EnumerationType")

    generate_named_type_reference(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationType.generate_named_type_reference)
    :   Parameters:
        :   - **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

    mutable_copy() → [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#EnumerationType.mutable_copy)
    :   Return type:
        :   [*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
            "binaryninja.types.EnumerationBuilder")

    *property* members
    :   Enumeration member list (read-only)

## FloatBuilder

*class* FloatBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FloatBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *classmethod* create(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [FloatBuilder](#binaryninja.types.FloatBuilder "binaryninja.types.FloatBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FloatBuilder.create)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*FloatBuilder*](#binaryninja.types.FloatBuilder "binaryninja.types.FloatBuilder")

## FloatType

*class* FloatType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FloatType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *altname: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [FloatType](#binaryninja.types.FloatType "binaryninja.types.FloatType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FloatType.create)
    :   `float` class method for creating floating point Types.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the floating point number in bytes
            - **altname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – alternate name for type
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*FloatType*](#binaryninja.types.FloatType "binaryninja.types.FloatType")

## FunctionBuilder

*class* FunctionBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    append(*type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionBuilder.append)
    :   Parameters:
        :   - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type") *|* [*FunctionParameter*](#binaryninja.types.FunctionParameter
              "binaryninja.types.FunctionParameter")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

    *classmethod* create(*return_type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *calling_convention: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](#binaryninja.types.Type "binaryninja.types.Type")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *var_args: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stack_adjust: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *platform: _platform.Platform | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *can_return: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *reg_stack_adjust: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[architecture.RegisterName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *return_regs: [RegisterSet](#binaryninja.types.RegisterSet "binaryninja.types.RegisterSet") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterType] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name_type: [NameType](enums.md#binaryninja.enums.NameType "binaryninja.enums.NameType") = NameType.NoNameType*, *pure: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [FunctionBuilder](#binaryninja.types.FunctionBuilder "binaryninja.types.FunctionBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionBuilder.create)
    :   Parameters:
        :   - **return_type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type") *|* *None*) –
            - **calling_convention**
              ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
              "binaryninja.callingconvention.CallingConvention") *|* *None*) –
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*FunctionParameter*](#binaryninja.types.FunctionParameter
              "binaryninja.types.FunctionParameter")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]**]* *|*
              *None*) –
            - **var_args** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence") *|* *None*) –
            - **stack_adjust** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* [*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence") *|* *None*) –
            - **platform** (*_platform.Platform* *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **can_return** ([*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence") *|* *None*) –
            - **reg_stack_adjust** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict
              "(in Python v3.14)")*[**architecture.RegisterName**,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|*
              [*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence")*]* *|* *None*) –
            - **return_regs** ([*RegisterSet*](#binaryninja.types.RegisterSet
              "binaryninja.types.RegisterSet") *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**architecture.RegisterType**]* *|* *None*) –
            - **name_type** ([*NameType*](enums.md#binaryninja.enums.NameType
              "binaryninja.enums.NameType")) –
            - **pure** ([*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence") *|* *None*) –

        Return type:
        :   [*FunctionBuilder*](#binaryninja.types.FunctionBuilder
            "binaryninja.types.FunctionBuilder")

    *property* calling_convention*: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention")*

    *property* can_return*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")]*

    *property* immutable_return_value*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

    *property* parameters*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")]*
    :   Type parameters list (read-only)

    *property* pure*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*

    *property* return_value*: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*

    *property* stack_adjust*: [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*

    *property* stack_adjustment*: [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*

    *property* variable_arguments*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*

## FunctionParameter

*class* FunctionParameter[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionParameter)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    FunctionParameter(type: Union[ForwardRef(‘TypeBuilder’), ForwardRef(‘Type’)], name: str
    = ‘’, location: Optional[ForwardRef(‘variable.VariableNameAndType’)] = None)

    __init__(*type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *location: [VariableNameAndType](variable.md#binaryninja.variable.VariableNameAndType "binaryninja.variable.VariableNameAndType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **location**
              ([*VariableNameAndType*](variable.md#binaryninja.variable.VariableNameAndType
              "binaryninja.variable.VariableNameAndType") *|* *None*) –

        Return type:
        :   *None*

    immutable_copy() → [FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionParameter.immutable_copy)
    :   Return type:
        :   [*FunctionParameter*](#binaryninja.types.FunctionParameter
            "binaryninja.types.FunctionParameter")

    mutable_copy() → [FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionParameter.mutable_copy)
    :   Return type:
        :   [*FunctionParameter*](#binaryninja.types.FunctionParameter
            "binaryninja.types.FunctionParameter")

    location*: [VariableNameAndType](variable.md#binaryninja.variable.VariableNameAndType "binaryninja.variable.VariableNameAndType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")* *= ''*

    type*: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*

## FunctionType

*class* FunctionType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*ret: [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](#binaryninja.types.Type "binaryninja.types.Type")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *calling_convention: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *variable_arguments: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *stack_adjust: [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence") = OffsetWithConfidence(value=0, confidence=255)*, *platform: _platform.Platform | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *can_return: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *reg_stack_adjust: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[architecture.RegisterName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *return_regs: [RegisterSet](#binaryninja.types.RegisterSet "binaryninja.types.RegisterSet") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterType] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name_type: [NameType](enums.md#binaryninja.enums.NameType "binaryninja.enums.NameType") = NameType.NoNameType*, *pure: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [FunctionType](#binaryninja.types.FunctionType "binaryninja.types.FunctionType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#FunctionType.create)
    :   Parameters:
        :   - **ret** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type") *|* *None*) –
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*FunctionParameter*](#binaryninja.types.FunctionParameter
              "binaryninja.types.FunctionParameter")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]**]* *|*
              *None*) –
            - **calling_convention**
              ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
              "binaryninja.callingconvention.CallingConvention") *|* *None*) –
            - **variable_arguments** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **stack_adjust** ([*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence")) –
            - **platform** (*_platform.Platform* *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **can_return** ([*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence") *|*
              [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –
            - **reg_stack_adjust** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict
              "(in Python v3.14)")*[**architecture.RegisterName**,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|*
              [*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence")*]* *|* *None*) –
            - **return_regs** ([*RegisterSet*](#binaryninja.types.RegisterSet
              "binaryninja.types.RegisterSet") *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**architecture.RegisterType**]* *|* *None*) –
            - **name_type** ([*NameType*](enums.md#binaryninja.enums.NameType
              "binaryninja.enums.NameType")) –
            - **pure** ([*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence") *|*
              [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –

        Return type:
        :   [*FunctionType*](#binaryninja.types.FunctionType "binaryninja.types.FunctionType")

    *property* calling_convention*: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Calling convention (read-only)

    *property* can_return*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether type can return

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")]*

    *property* has_variable_arguments*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether type has variable arguments (read-only)

    *property* parameters*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")]*
    :   Type parameters list (read-only)

    *property* parameters_with_all_locations*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")]*
    :   Type parameters list with default locations filled in with values (read-only)

    *property* pure*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether type is pure

    *property* return_value*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*
    :   Return value (read-only)

    *property* stack_adjustment*: [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*
    :   Stack adjustment for function (read-only)

## InheritedStructureMember

*class* InheritedStructureMember[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#InheritedStructureMember)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    InheritedStructureMember(base: ‘NamedTypeReferenceType’, base_offset: int, member:
    binaryninja.types.StructureMember, member_index: int)

    __init__(*base: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")*, *base_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *member: [StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")*, *member_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **base** ([*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
              "binaryninja.types.NamedTypeReferenceType")) –
            - **base_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **member** ([*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")) –
            - **member_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –

        Return type:
        :   *None*

    base*: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")*

    base_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    member*: [StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")*

    member_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## InlineDuringAnalysisWithConfidence

*class* InlineDuringAnalysisWithConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#InlineDuringAnalysisWithConfidence)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Represents an InlineDuringAnalysis value with an associated confidence level.

    __init__(*value: [InlineDuringAnalysis](enums.md#binaryninja.enums.InlineDuringAnalysis "binaryninja.enums.InlineDuringAnalysis")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*InlineDuringAnalysis*](enums.md#binaryninja.enums.InlineDuringAnalysis
              "binaryninja.enums.InlineDuringAnalysis")) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *classmethod* from_core_struct(*core_struct: BNInlineDuringAnalysisWithConfidence*) → [InlineDuringAnalysisWithConfidence](#binaryninja.types.InlineDuringAnalysisWithConfidence "binaryninja.types.InlineDuringAnalysisWithConfidence")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#InlineDuringAnalysisWithConfidence.from_core_struct)
    :   Parameters:
        :   **core_struct** (*BNInlineDuringAnalysisWithConfidence*) –

        Return type:
        :   [*InlineDuringAnalysisWithConfidence*](#binaryninja.types.InlineDuringAnalysisWithConfidence
            "binaryninja.types.InlineDuringAnalysisWithConfidence")

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    value*: [InlineDuringAnalysis](enums.md#binaryninja.enums.InlineDuringAnalysis "binaryninja.enums.InlineDuringAnalysis")*

## IntegerBuilder

*class* IntegerBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#IntegerBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *classmethod* create(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = True*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [IntegerBuilder](#binaryninja.types.IntegerBuilder "binaryninja.types.IntegerBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#IntegerBuilder.create)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*IntegerBuilder*](#binaryninja.types.IntegerBuilder "binaryninja.types.IntegerBuilder")

## IntegerType

*class* IntegerType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#IntegerType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    __init__(*handle*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#IntegerType.__init__)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *classmethod* create(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = True*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [IntegerType](#binaryninja.types.IntegerType "binaryninja.types.IntegerType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#IntegerType.create)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*IntegerType*](#binaryninja.types.IntegerType "binaryninja.types.IntegerType")

    *property* signed*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether type is signed (read-only)

## MutableTypeBuilder

*class* MutableTypeBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#MutableTypeBuilder)
:   Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in
    Python v3.14)")[`TB`]

    MutableTypeBuilder(type: ~TB, container: Union[ForwardRef(‘binaryview.BinaryView’),
    ForwardRef(‘typelibrary.TypeLibrary’)], name: binaryninja.types.QualifiedName, platform:
    Optional[ForwardRef(‘_platform.Platform’)], confidence: int, user: bool = True)

    __init__(*type: TB*, *container: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*, *name: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *user: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** (*TB*) –
            - **container** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) –
            - **name** ([*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **user** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    container*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*

    name*: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*

    platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    type*: TB*

    user*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")* *= True*

## NameSpace

*class* NameSpace[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NameSpace)
:   Bases: [`QualifiedName`](#binaryninja.types.QualifiedName
    "binaryninja.types.QualifiedName")

    *static* get_core_struct(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [NameSpace](#binaryninja.types.NameSpace "binaryninja.types.NameSpace") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → BNNameSpace | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NameSpace.get_core_struct)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]* *|* [*NameSpace*](#binaryninja.types.NameSpace
            "binaryninja.types.NameSpace") *|* *None*) –

        Return type:
        :   *BNNameSpace* | *None*

## NamedTypeReferenceBuilder

*class* NamedTypeReferenceBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    __init__(*handle: LP_BNTypeBuilder*, *ntr_builder_handle: LP_BNNamedTypeReferenceBuilder*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNTypeBuilder*) –
            - **ntr_builder_handle** (*LP_BNNamedTypeReferenceBuilder*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *classmethod* create(*type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass") = NamedTypeReferenceClass.UnknownNamedTypeClass*, *type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") = ''*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder.create)
    :   Parameters:
        :   - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass")) –
            - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type(*named_type: [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder.named_type)
    :   Parameters:
        :   - **named_type**
              ([*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
              "binaryninja.types.NamedTypeReferenceBuilder")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type_from_registered_type(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder.named_type_from_registered_type)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type_from_type(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder.named_type_from_type)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass") *|* *None*) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type_from_type_and_id(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceBuilder.named_type_from_type_and_id)
    :   Parameters:
        :   - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type") *|* *None*) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* name*: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*

    *property* named_type_class*: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*

    *property* type_id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## NamedTypeReferenceType

*class* NamedTypeReferenceType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    __init__(*handle*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *ntr_handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.__init__)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *classmethod* create(*named_type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*, *guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *alignment: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.create)
    :   Parameters:
        :   - **named_type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass")) –
            - **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **alignment** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *classmethod* create_from_handle(*ntr_handle*, *alignment: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.create_from_handle)
    :   Create a NamedTypeReferenceType from a BNNamedTypeReference handle

        Parameters:
        :   - **alignment** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

    *classmethod* create_from_registered_type(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.create_from_registered_type)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *classmethod* create_from_type(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.create_from_type)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type") *|* *None*) –
            - **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *static* generate_auto_demangled_type_ref(*type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.generate_auto_demangled_type_ref)
    :   Parameters:
        :   - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

    *static* generate_auto_type_ref(*type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*, *source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.generate_auto_type_ref)
    :   Parameters:
        :   - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass")) –
            - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

    mutable_copy()[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.mutable_copy)

    target(*bv: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#NamedTypeReferenceType.target)
    :   Returns the type pointed to by the current type

        Parameters:
        :   **bv** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) – The BinaryView in which this type is defined.

        Returns:
        :   The type this NamedTypeReference is referencing

        Return type:
        :   *Optional*[[*Type*](#binaryninja.types.Type "binaryninja.types.Type")]

    *property* name*: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*

    *property* named_type_class*: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*

    *property* type_id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## OffsetWithConfidence

*class* OffsetWithConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#OffsetWithConfidence)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    OffsetWithConfidence(value: int, confidence: int = 255)

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *classmethod* from_core_struct(*core_struct: BNOffsetWithConfidence*) → [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#OffsetWithConfidence.from_core_struct)
    :   Parameters:
        :   **core_struct** (*BNOffsetWithConfidence*) –

        Return type:
        :   [*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
            "binaryninja.types.OffsetWithConfidence")

    *static* get_core_struct(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → BNOffsetWithConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#OffsetWithConfidence.get_core_struct)
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* [*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence")) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *BNOffsetWithConfidence*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## PointerBuilder

*class* PointerBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    add_pointer_suffix(*suffix: [PointerSuffix](enums.md#binaryninja.enums.PointerSuffix "binaryninja.enums.PointerSuffix")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerBuilder.add_pointer_suffix)
    :   Append a suffix to the pointer, must be one defined in `PointerSuffix`. :param suffix:
        New suffix

        Parameters:
        :   **suffix** ([*PointerSuffix*](enums.md#binaryninja.enums.PointerSuffix
            "binaryninja.enums.PointerSuffix")) –

    *classmethod* create(*type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 4*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") = ReferenceType.PointerReferenceType*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [PointerBuilder](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerBuilder.create)
    :   Parameters:
        :   - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*PointerBuilder*](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder")

    get_pointer_suffix_tokens(*base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerBuilder.get_pointer_suffix_tokens)
    :   Get the pointer suffix, as a list of tokens :param base_confidence: (optional)
        Confidence value to combine with the pointer’s confidence :return: Token list

        Parameters:
        :   **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    set_pointer_base(*base_type: [PointerBaseType](enums.md#binaryninja.enums.PointerBaseType "binaryninja.enums.PointerBaseType")*, *base_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerBuilder.set_pointer_base)
    :   Set the pointer base type and offset :param base_type: Base type, e.g. __based(start) is
        RelativeToBinaryStartPointerBaseType :param base_offset: Base offset, e.g.
        __based(start, 0x1000) is 0x1000

        Parameters:
        :   - **base_type** ([*PointerBaseType*](enums.md#binaryninja.enums.PointerBaseType
              "binaryninja.enums.PointerBaseType")) –
            - **base_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")]*

    *property* immutable_target*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Currently not used and has no effect (Leaving this in for compatibility)

    *property* origin*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* pointer_base_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Pointer base offset, e.g. __based(start, 0x1000) is 0x1000

    *property* pointer_base_type*: [PointerBaseType](enums.md#binaryninja.enums.PointerBaseType "binaryninja.enums.PointerBaseType")*
    :   Pointer base type, e.g. __based(start) is RelativeToBinaryStartPointerBaseType

    *property* pointer_suffix*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PointerSuffix](enums.md#binaryninja.enums.PointerSuffix "binaryninja.enums.PointerSuffix")]*
    :   Pointer suffix, e.g. __unaligned is [UnalignedSuffix] (read-only)

    *property* pointer_suffix_string*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Pointer suffix, but as a string, e.g. “__unaligned” (read-only)

    *property* target*: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*

## PointerType

*class* PointerType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") = ReferenceType.PointerReferenceType*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [PointerType](#binaryninja.types.PointerType "binaryninja.types.PointerType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerType.create)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*PointerType*](#binaryninja.types.PointerType "binaryninja.types.PointerType")

    *classmethod* create_with_width(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [PointerType](#binaryninja.types.PointerType "binaryninja.types.PointerType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerType.create_with_width)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType") *|* *None*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*PointerType*](#binaryninja.types.PointerType "binaryninja.types.PointerType")

    *static* from_bools(*const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence"), [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerType.from_bools)
    :   Parameters:
        :   - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence"),
            [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
            "binaryninja.types.BoolWithConfidence")]

    get_pointer_suffix_tokens(*base_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerType.get_pointer_suffix_tokens)
    :   Get the pointer suffix, as a list of tokens :param base_confidence: (optional)
        Confidence value to combine with the pointer’s confidence :return: Token list

        Parameters:
        :   **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")]

    origin(*bv: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#PointerType.origin)
    :   Parameters:
        :   **bv** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView") *|* *None*) –

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*QualifiedName*](#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] |
            *None*

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")]*

    *property* pointer_base_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Pointer base offset, e.g. __based(start, 0x1000) is 0x1000 (read-only)

    *property* pointer_base_type*: [PointerBaseType](enums.md#binaryninja.enums.PointerBaseType "binaryninja.enums.PointerBaseType")*
    :   Pointer base type, e.g. __based(start) is RelativeToBinaryStartPointerBaseType
        (read-only)

    *property* pointer_suffix*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PointerSuffix](enums.md#binaryninja.enums.PointerSuffix "binaryninja.enums.PointerSuffix")]*
    :   Pointer suffix, e.g. __unaligned is [UnalignedSuffix] (read-only)

    *property* pointer_suffix_string*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Pointer suffix, but as a string, e.g. “__unaligned” (read-only)

    *property* ref_type*: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType")*

    *property* target*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*
    :   Target (read-only)

## QualifiedName

*class* QualifiedName[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#QualifiedName)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *join: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '::'*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#QualifiedName.__init__)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName") *|* *None*) –
            - **join** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

    *static* escape(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#QualifiedName.escape)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *static* unescape(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#QualifiedName.unescape)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *property* join*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* name*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

## RegisterSet

*class* RegisterSet[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#RegisterSet)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    RegisterSet(regs: List[ForwardRef(‘architecture.RegisterName’)], confidence: int = 255)

    __init__(*regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**RegisterName**]*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    with_confidence(*confidence*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#RegisterSet.with_confidence)

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    regs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*

## RegisterStackAdjustmentWithConfidence

*class* RegisterStackAdjustmentWithConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#RegisterStackAdjustmentWithConfidence)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    RegisterStackAdjustmentWithConfidence(value: int, confidence: int = 255)

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## StructureBuilder

*class* StructureBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    __init__(*handle: LP_BNTypeBuilder*, *builder_handle: LP_BNStructureBuilder*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNTypeBuilder*) –
            - **builder_handle** (*LP_BNStructureBuilder*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    add_member_at_offset(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *overwrite_existing: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *access: [MemberAccess](enums.md#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess") = MemberAccess.NoAccess*, *scope: [MemberScope](enums.md#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope") = MemberScope.NoScope*, *bit_position: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *bit_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.add_member_at_offset)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **overwrite_existing** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –
            - **access** ([*MemberAccess*](enums.md#binaryninja.enums.MemberAccess
              "binaryninja.enums.MemberAccess")) –
            - **scope** ([*MemberScope*](enums.md#binaryninja.enums.MemberScope
              "binaryninja.enums.MemberScope")) –
            - **bit_position** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **bit_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    append(*type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *access: [MemberAccess](enums.md#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess") = MemberAccess.NoAccess*, *scope: [MemberScope](enums.md#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope") = MemberScope.NoScope*) → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.append)
    :   Parameters:
        :   - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **access** ([*MemberAccess*](enums.md#binaryninja.enums.MemberAccess
              "binaryninja.enums.MemberAccess")) –
            - **scope** ([*MemberScope*](enums.md#binaryninja.enums.MemberScope
              "binaryninja.enums.MemberScope")) –

        Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    *classmethod* create(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *type: [StructureVariant](enums.md#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant") = StructureVariant.StructStructureType*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.create)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **type** ([*StructureVariant*](enums.md#binaryninja.enums.StructureVariant
              "binaryninja.enums.StructureVariant")) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    index_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.index_by_name)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    index_by_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.index_by_offset)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    insert(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *overwrite_existing: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *access: [MemberAccess](enums.md#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess") = MemberAccess.NoAccess*, *scope: [MemberScope](enums.md#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope") = MemberScope.NoScope*, *bit_position: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *bit_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.insert)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **overwrite_existing** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –
            - **access** ([*MemberAccess*](enums.md#binaryninja.enums.MemberAccess
              "binaryninja.enums.MemberAccess")) –
            - **scope** ([*MemberScope*](enums.md#binaryninja.enums.MemberScope
              "binaryninja.enums.MemberScope")) –
            - **bit_position** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **bit_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    member_at_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.member_at_offset)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*StructureMember*](#binaryninja.types.StructureMember
            "binaryninja.types.StructureMember") | *None*

    remove(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.remove)
    :   Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

    replace(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *overwrite_existing: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureBuilder.replace)
    :   Parameters:
        :   - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **overwrite_existing** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –

    *property* alignment*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* base_structures*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BaseStructure](#binaryninja.types.BaseStructure "binaryninja.types.BaseStructure")]*
    :   Base structure list. Offsets that are not defined by this structure will be filled in by
        the fields of the base structure(s).

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")]*

    *property* members*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")]*
    :   Structure member list (read-only)

    *property* packed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* pointer_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* propagate_data_var_refs*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* type*: [StructureVariant](enums.md#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant")*

    *property* union*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## StructureMember

*class* StructureMember[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureMember)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    StructureMember(type: ‘Type’, name: str, offset: int, access:
    binaryninja.enums.MemberAccess = <MemberAccess.NoAccess: 0>, scope:
    binaryninja.enums.MemberScope = <MemberScope.NoScope: 0>, bit_position: int = 0,
    bit_width: int = 0)

    __init__(*type: [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *access: [MemberAccess](enums.md#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess") = MemberAccess.NoAccess*, *scope: [MemberScope](enums.md#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope") = MemberScope.NoScope*, *bit_position: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *bit_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **access** ([*MemberAccess*](enums.md#binaryninja.enums.MemberAccess
              "binaryninja.enums.MemberAccess")) –
            - **scope** ([*MemberScope*](enums.md#binaryninja.enums.MemberScope
              "binaryninja.enums.MemberScope")) –
            - **bit_position** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **bit_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    access*: [MemberAccess](enums.md#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess")* *= 0*

    *property* bit_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Total bit offset from the start of the structure.

        Computed as: offset * 8 + bit_position.

    bit_position*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    bit_width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    scope*: [MemberScope](enums.md#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope")* *= 0*

    type*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

## StructureType

*class* StructureType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    __init__(*handle*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.__init__)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *classmethod* create(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *type: [StructureVariant](enums.md#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant") = StructureVariant.StructStructureType*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.create)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **type** ([*StructureVariant*](enums.md#binaryninja.enums.StructureVariant
              "binaryninja.enums.StructureVariant")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    *classmethod* from_core_struct(*structure: BNStructure*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.from_core_struct)
    :   Parameters:
        :   **structure** (*BNStructure*) –

        Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    generate_named_type_reference(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.generate_named_type_reference)
    :   Parameters:
        :   - **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

    member_at_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.member_at_offset)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*StructureMember*](#binaryninja.types.StructureMember
            "binaryninja.types.StructureMember")

    member_at_offset_including_inherited(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [InheritedStructureMember](#binaryninja.types.InheritedStructureMember "binaryninja.types.InheritedStructureMember")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.member_at_offset_including_inherited)
    :   Returns the member (including inherited member at the specified offset

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*InheritedStructureMember*](#binaryninja.types.InheritedStructureMember
            "binaryninja.types.InheritedStructureMember")

    members_including_inherited(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InheritedStructureMember](#binaryninja.types.InheritedStructureMember "binaryninja.types.InheritedStructureMember")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.members_including_inherited)
    :   Returns structure member list, including those inherited by base structures

        Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView") *|*
            [*TypeContainer*](typecontainer.md#binaryninja.typecontainer.TypeContainer
            "binaryninja.typecontainer.TypeContainer")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InheritedStructureMember*](#binaryninja.types.InheritedStructureMember
            "binaryninja.types.InheritedStructureMember")]

    mutable_copy() → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.mutable_copy)
    :   Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    resolve_member_or_base_member(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *resolve_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType"), [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *member_index_hint: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.resolve_member_or_base_member)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **resolve_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
              "binaryninja.types.NamedTypeReferenceType")*,*
              [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,*
              [*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]**,* *None**]*) –
            - **member_index_hint** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    with_replaced_enumeration(*from_enum*, *to_enum*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.with_replaced_enumeration)
    :   Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    with_replaced_named_type_reference(*from_ref*, *to_ref*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.with_replaced_named_type_reference)
    :   Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    with_replaced_structure(*from_struct*, *to_struct*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#StructureType.with_replaced_structure)
    :   Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    *property* alignment
    :   Structure alignment

    *property* base_structures*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BaseStructure](#binaryninja.types.BaseStructure "binaryninja.types.BaseStructure")]*
    :   Base structure list (read-only). Offsets that are not defined by this structure will be
        filled in by the fields of the base structure(s).

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")]*

    *property* members
    :   Structure member list (read-only). This list will **not** contain members inherited from
        base structures. To get members including inherited ones, call
        members_including_inherited.

    *property* packed

    *property* pointer_offset
    :   Structure pointer offset. Pointers to this structure will implicitly have this offset
        subtracted from the pointer to arrive at the start of the structure. Effectively, the
        pointer offset becomes the new start of the structure, and fields before it are accessed
        using negative offsets from the pointer.

    *property* propagate_data_var_refs*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether structure field references propagate the references to data variable field
        values

    *property* type*: [StructureVariant](enums.md#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant")*

    *property* width
    :   Structure width

## Symbol

*class* Symbol[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Symbol)
:   Bases: [`CoreSymbol`](#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")

    Symbols are defined as one of the following types:

    > | SymbolType | Description |
    > | --- | --- |
    > | FunctionSymbol | Symbol for function that exists in the current binary |
    > | ImportAddressSymbol | Symbol defined in the Import Address Table |
    > | ImportedFunctionSymbol | Symbol for a function that is not defined in the current binary |
    > | DataSymbol | Symbol for data in the current binary |
    > | ImportedDataSymbol | Symbol for data that is not defined in the current binary |
    > | ExternalSymbol | Symbols for data and code that reside outside the BinaryView |
    > | LibraryFunctionSymbol | Symbols for functions identified as belonging to a shared library |
    > | SymbolicFunctionSymbol | Symbols for functions without a concrete implementation or which have been abstractly represented |
    > | LocalLabelSymbol | Symbol for a local label in the current binary |

    __init__(*sym_type*, *addr*, *short_name*, *full_name=None*, *raw_name=None*, *binding=None*, *namespace=None*, *ordinal=0*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Symbol.__init__)

## Type

*class* Type[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class Type` allows you to interact with the Binary Ninja type system. Note that the
    `repr` and `str` handlers respond differently on type objects.

    Other related functions that may be helpful include:

    `parse_type_string` `parse_types_from_source` `parse_types_from_source_file`

    __init__(*handle*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.__init__)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *static* array(*type: [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ArrayType](#binaryninja.types.ArrayType "binaryninja.types.ArrayType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.array)
    :   Parameters:
        :   - **type** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) –
            - **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*ArrayType*](#binaryninja.types.ArrayType "binaryninja.types.ArrayType")

    *static* bool() → [BoolType](#binaryninja.types.BoolType "binaryninja.types.BoolType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.bool)
    :   Return type:
        :   [*BoolType*](#binaryninja.types.BoolType "binaryninja.types.BoolType")

    *static* builder(*bv: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [MutableTypeBuilder](#binaryninja.types.MutableTypeBuilder "binaryninja.types.MutableTypeBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.builder)
    :   Parameters:
        :   - **bv** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName") *|* *None*) –
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
              *|* *None*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*MutableTypeBuilder*](#binaryninja.types.MutableTypeBuilder
            "binaryninja.types.MutableTypeBuilder")

    *static* char(*alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [CharType](#binaryninja.types.CharType "binaryninja.types.CharType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.char)
    :   Parameters:
        :   **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")) –

        Return type:
        :   [*CharType*](#binaryninja.types.CharType "binaryninja.types.CharType")

    *static* class_type(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.class_type)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    *classmethod* create(*handle: LP_BNType*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [Type](#binaryninja.types.Type "binaryninja.types.Type")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.create)
    :   Parameters:
        :   - **handle** (*LP_BNType*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*Type*](#binaryninja.types.Type "binaryninja.types.Type")

    deref_named_type_reference(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [Type](#binaryninja.types.Type "binaryninja.types.Type")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.deref_named_type_reference)
    :   Dereferences any named type references to find the underlying type. This may still
        return a named type reference if there are circular references. If the type isn’t a
        named type reference, the input type is returned unchanged.

        Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) – BinaryView object owning this Type

        Returns:
        :   Type with named type references resolved

        Return type:
        :   [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *static* enumeration(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[EnumerationMember](#binaryninja.types.EnumerationMember "binaryninja.types.EnumerationMember")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*) → [EnumerationType](#binaryninja.types.EnumerationType "binaryninja.types.EnumerationType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.enumeration)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]**]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*EnumerationMember*](#binaryninja.types.EnumerationMember
              "binaryninja.types.EnumerationMember")*]* *|* *None*) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*EnumerationType*](#binaryninja.types.EnumerationType
            "binaryninja.types.EnumerationType")

    *static* enumeration_type(*arch*, *enum: [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [EnumerationType](#binaryninja.types.EnumerationType "binaryninja.types.EnumerationType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.enumeration_type)
    :   Parameters:
        :   - **enum** ([*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
              "binaryninja.types.EnumerationBuilder")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*EnumerationType*](#binaryninja.types.EnumerationType
            "binaryninja.types.EnumerationType")

    *static* float(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [FloatType](#binaryninja.types.FloatType "binaryninja.types.FloatType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.float)
    :   `float` class method for creating floating point Types.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the floating point number in bytes
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – alternate name for type

        Return type:
        :   [*FloatType*](#binaryninja.types.FloatType "binaryninja.types.FloatType")

    *static* from_core_struct(*core_type: BNType*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.from_core_struct)
    :   Parameters:
        :   **core_type** (*BNType*) –

    *static* function(*ret: [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](#binaryninja.types.Type "binaryninja.types.Type")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *calling_convention: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *variable_arguments: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *stack_adjust: [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence") = OffsetWithConfidence(value=0, confidence=255)*) → [FunctionType](#binaryninja.types.FunctionType "binaryninja.types.FunctionType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.function)
    :   `function` class method for creating a function Type.

        Parameters:
        :   - **ret** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) – return Type of
              the function
            - **params** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*)*) – list of
              parameter Types
            - **calling_convention**
              ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
              "binaryninja.callingconvention.CallingConvention")) – optional argument for the function
              calling convention
            - **variable_arguments** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – optional boolean, true if the function has a variable number of
              arguments
            - **stack_adjust** ([*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence")) –

        Return type:
        :   [*FunctionType*](#binaryninja.types.FunctionType "binaryninja.types.FunctionType")

    *static* generate_auto_demangled_type_id(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.generate_auto_demangled_type_id)
    :   Parameters:
        :   **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
            "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
            Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *static* generate_auto_type_id(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.generate_auto_type_id)
    :   Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *static* generate_named_type_reference(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.generate_named_type_reference)
    :   Parameters:
        :   - **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *static* get_auto_demangled_type_id_source() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_auto_demangled_type_id_source)
    :   Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_builder(*bv: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [MutableTypeBuilder](#binaryninja.types.MutableTypeBuilder "binaryninja.types.MutableTypeBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_builder)
    :   Parameters:
        :   **bv** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*MutableTypeBuilder*](#binaryninja.types.MutableTypeBuilder
            "binaryninja.types.MutableTypeBuilder")

    get_lines(*bv: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *padding_cols: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 64*, *collapsed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeDefinitionLine](#binaryninja.types.TypeDefinitionLine "binaryninja.types.TypeDefinitionLine")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_lines)
    :   Get a list of [`TypeDefinitionLine`](#binaryninja.types.TypeDefinitionLine
        "binaryninja.types.TypeDefinitionLine") structures for representing a Type in a
        structured form. This structure uses the same logic as Types View and will expand
        structures and enumerations unless collapsed is set.

        Parameters:
        :   - **bv** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – BinaryView object owning this Type
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Displayed name of the Type
            - **padding_cols** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Maximum number of bytes represented by each padding line
            - **collapsed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – If the type should be collapsed, and not show fields/members
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   Returns a list of [`TypeDefinitionLine`](#binaryninja.types.TypeDefinitionLine
            "binaryninja.types.TypeDefinitionLine") structures

        Return type:
        :   [`TypeDefinitionLine`](#binaryninja.types.TypeDefinitionLine
            "binaryninja.types.TypeDefinitionLine")

    get_string(*escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_string)
    :   Get string representation for this type

        Parameters:
        :   **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
            "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   String for type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> Type.array(Type.int(4), 10).get_string()
            'int32_t[0xa]'
            ```

    get_string_after_name(*escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_string_after_name)
    :   Get the string to be printed after this type’s name in a representation

        Parameters:
        :   **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
            "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   String for type representation after the name

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> Type.array(Type.int(4), 10).get_string()
            'int32_t[0xa]'
            >>> Type.array(Type.int(4), 10).get_string_after_name()
            '[0xa]'
            ```

    get_string_before_name(*escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_string_before_name)
    :   Get the string to be printed before this type’s name in a representation of it

        Parameters:
        :   **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
            "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   String for type representation before the name

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> Type.array(Type.int(4), 10).get_string()
            'int32_t[0xa]'
            >>> Type.array(Type.int(4), 10).get_string_before_name()
            'int32_t'
            ```

    get_tokens(*base_confidence=255*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_tokens)
    :   Get a list of tokens for the definition of a type

        Parameters:
        :   - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence of this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   List of tokens

        Return type:
        :   *List*[_function.InstructionTextToken]

        Example:
        :   ```
            >>> Type.array(Type.int(4), 10).get_string()
            'int32_t[0xa]'
            >>> Type.array(Type.int(4), 10).get_tokens()
            ['int32_t', ' ', '[', '0xa', ']']
            ```

    get_tokens_after_name(*base_confidence=255*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_tokens_after_name)
    :   Get a list of tokens for the definition of a type that are placed after the type name

        Parameters:
        :   - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence of this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   List of tokens

        Return type:
        :   *List*[_function.InstructionTextToken]

        Example:
        :   ```
            >>> Type.array(Type.int(4), 10).get_string()
            'int32_t[0xa]'
            >>> Type.array(Type.int(4), 10).get_tokens_after_name()
            ['[', '0xa', ']']
            ```

    get_tokens_before_name(*base_confidence=255*, *escaping: [TokenEscapingType](enums.md#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") = TokenEscapingType.NoTokenEscapingType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.get_tokens_before_name)
    :   Get a list of tokens for the definition of a type that are placed before the type name

        Parameters:
        :   - **base_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Confidence of this type
            - **escaping** ([*TokenEscapingType*](enums.md#binaryninja.enums.TokenEscapingType
              "binaryninja.enums.TokenEscapingType")) – How to escape non-parsable strings in types

        Returns:
        :   List of tokens

        Return type:
        :   *List*[_function.InstructionTextToken]

        Example:
        :   ```
            >>> Type.array(Type.int(4), 10).get_string()
            'int32_t[0xa]'
            >>> Type.array(Type.int(4), 10).get_tokens_before_name()
            ['int32_t']
            ```

    immutable_copy() → [Type](#binaryninja.types.Type "binaryninja.types.Type")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.immutable_copy)
    :   Return type:
        :   [*Type*](#binaryninja.types.Type "binaryninja.types.Type")

    *static* int(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = True*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [IntegerType](#binaryninja.types.IntegerType "binaryninja.types.IntegerType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.int)
    :   `int` class method for creating an int Type.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the integer in bytes
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – optional variable representing signedness
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – alternate name for type

        Return type:
        :   [*IntegerType*](#binaryninja.types.IntegerType "binaryninja.types.IntegerType")

    mutable_copy() → [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.mutable_copy)
    :   Return type:
        :   [*TypeBuilder*](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *static* named_type(*named_type: [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.named_type)
    :   Parameters:
        :   **named_type**
            ([*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *static* named_type_from_registered_type(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.named_type_from_registered_type)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *static* named_type_from_type(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.named_type_from_type)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *static* named_type_from_type_and_id(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.named_type_from_type_and_id)
    :   Parameters:
        :   - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type") *|* *None*) –

        Return type:
        :   [*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
            "binaryninja.types.NamedTypeReferenceType")

    *static* named_type_reference(*type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alignment: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.named_type_reference)
    :   Parameters:
        :   - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **alignment** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

    *static* pointer(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") = ReferenceType.PointerReferenceType*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PointerType](#binaryninja.types.PointerType "binaryninja.types.PointerType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.pointer)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Return type:
        :   [*PointerType*](#binaryninja.types.PointerType "binaryninja.types.PointerType")

    *static* pointer_of_width(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = False*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") = ReferenceType.PointerReferenceType*) → [PointerType](#binaryninja.types.PointerType "binaryninja.types.PointerType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.pointer_of_width)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType")) –

        Return type:
        :   [*PointerType*](#binaryninja.types.PointerType "binaryninja.types.PointerType")

    *static* structure(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *type: [StructureVariant](enums.md#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant") = StructureVariant.StructStructureType*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.structure)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **type** ([*StructureVariant*](enums.md#binaryninja.enums.StructureVariant
              "binaryninja.enums.StructureVariant")) –

        Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    *static* structure_type(*structure: [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.structure_type)
    :   Parameters:
        :   **structure** ([*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")) –

        Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    *static* union(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.union)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureType*](#binaryninja.types.StructureType "binaryninja.types.StructureType")

    *static* void() → [VoidType](#binaryninja.types.VoidType "binaryninja.types.VoidType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.void)
    :   Return type:
        :   [*VoidType*](#binaryninja.types.VoidType "binaryninja.types.VoidType")

    *static* wide_char(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [WideCharType](#binaryninja.types.WideCharType "binaryninja.types.WideCharType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.wide_char)
    :   `wide_char` class method for creating wide char Types.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the wide character in bytes
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – alternate name for type

        Return type:
        :   [*WideCharType*](#binaryninja.types.WideCharType "binaryninja.types.WideCharType")

    with_confidence(*confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Type](#binaryninja.types.Type "binaryninja.types.Type")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.with_confidence)
    :   Parameters:
        :   **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*Type*](#binaryninja.types.Type "binaryninja.types.Type")

    with_replaced_enumeration(*from_enum: [EnumerationType](#binaryninja.types.EnumerationType "binaryninja.types.EnumerationType")*, *to_enum: [EnumerationType](#binaryninja.types.EnumerationType "binaryninja.types.EnumerationType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.with_replaced_enumeration)
    :   Parameters:
        :   - **from_enum** ([*EnumerationType*](#binaryninja.types.EnumerationType
              "binaryninja.types.EnumerationType")) –
            - **to_enum** ([*EnumerationType*](#binaryninja.types.EnumerationType
              "binaryninja.types.EnumerationType")) –

    with_replaced_named_type_reference(*from_ref: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")*, *to_ref: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.with_replaced_named_type_reference)
    :   Parameters:
        :   - **from_ref** ([*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
              "binaryninja.types.NamedTypeReferenceType")) –
            - **to_ref** ([*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
              "binaryninja.types.NamedTypeReferenceType")) –

    with_replaced_structure(*from_struct: [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")*, *to_struct: [StructureType](#binaryninja.types.StructureType "binaryninja.types.StructureType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#Type.with_replaced_structure)
    :   Parameters:
        :   - **from_struct** ([*StructureType*](#binaryninja.types.StructureType
              "binaryninja.types.StructureType")) –
            - **to_struct** ([*StructureType*](#binaryninja.types.StructureType
              "binaryninja.types.StructureType")) –

    *property* alignment*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Type alignment (read-only)

    *property* altname*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Alternative name for the type object

    *property* attributes*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Attribute names and their values

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")]*

    *property* confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* const
    :   Whether type is const (read/write)

    *property* handle

    *property* name*: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Offset into structure (read-only)

    *property* platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* registered_name*: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Name of type registered to binary view, if any (read-only)

    *property* system_call_number*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the system call number for a FunctionType object if one exists otherwise None

    *property* tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*
    :   Type string as a list of tokens (read-only)

    *property* type_class*: [TypeClass](enums.md#binaryninja.enums.TypeClass "binaryninja.enums.TypeClass")*
    :   Type class (read-only)

    *property* volatile
    :   Whether type is volatile (read/write)

    *property* width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Type width (read-only)

## TypeBuilder

*class* TypeBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    All TypeBuilder objects should not be instantiated directly but created via `.create`
    APIs.

    __init__(*handle: LP_BNTypeBuilder*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNTypeBuilder*) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *static* array(*type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ArrayBuilder](#binaryninja.types.ArrayBuilder "binaryninja.types.ArrayBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.array)
    :   Parameters:
        :   - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*ArrayBuilder*](#binaryninja.types.ArrayBuilder "binaryninja.types.ArrayBuilder")

    *static* bool() → [BoolBuilder](#binaryninja.types.BoolBuilder "binaryninja.types.BoolBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.bool)
    :   Return type:
        :   [*BoolBuilder*](#binaryninja.types.BoolBuilder "binaryninja.types.BoolBuilder")

    *classmethod* builder(*container: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*, *name: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *user: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [MutableTypeBuilder](#binaryninja.types.MutableTypeBuilder "binaryninja.types.MutableTypeBuilder")[TB][[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.builder)
    :   Parameters:
        :   - **container** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) –
            - **name** ([*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **user** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*MutableTypeBuilder*](#binaryninja.types.MutableTypeBuilder
            "binaryninja.types.MutableTypeBuilder")[*TB*]

    *static* char(*alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [CharBuilder](#binaryninja.types.CharBuilder "binaryninja.types.CharBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.char)
    :   Parameters:
        :   **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")) –

        Return type:
        :   [*CharBuilder*](#binaryninja.types.CharBuilder "binaryninja.types.CharBuilder")

    *static* class_type(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.class_type)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    clear_system_call() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.clear_system_call)
    :   Return type:
        :   *None*

    *classmethod* create()[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.create)

    *static* enumeration(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[EnumerationMember](#binaryninja.types.EnumerationMember "binaryninja.types.EnumerationMember")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*) → [EnumerationBuilder](#binaryninja.types.EnumerationBuilder "binaryninja.types.EnumerationBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.enumeration)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]**]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*EnumerationMember*](#binaryninja.types.EnumerationMember
              "binaryninja.types.EnumerationMember")*]* *|* *None*) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*EnumerationBuilder*](#binaryninja.types.EnumerationBuilder
            "binaryninja.types.EnumerationBuilder")

    *static* float(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *altname: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [FloatBuilder](#binaryninja.types.FloatBuilder "binaryninja.types.FloatBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.float)
    :   `float` class method for creating floating point Types.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the floating point number in bytes
            - **altname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – alternate name for type

        Return type:
        :   [*FloatBuilder*](#binaryninja.types.FloatBuilder "binaryninja.types.FloatBuilder")

    *static* function(*ret: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FunctionParameter](#binaryninja.types.FunctionParameter "binaryninja.types.FunctionParameter")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Type](#binaryninja.types.Type "binaryninja.types.Type")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *calling_convention: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *variable_arguments: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stack_adjust: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [OffsetWithConfidence](#binaryninja.types.OffsetWithConfidence "binaryninja.types.OffsetWithConfidence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [FunctionBuilder](#binaryninja.types.FunctionBuilder "binaryninja.types.FunctionBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.function)
    :   `function` class method for creating a function Type.

        Parameters:
        :   - **ret** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) – return Type of
              the function
            - **params** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*)*) – list of
              parameter Types
            - **calling_convention**
              ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
              "binaryninja.callingconvention.CallingConvention")) – optional argument for the function
              calling convention
            - **variable_arguments** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – optional boolean, true if the function has a variable number of
              arguments
            - **stack_adjust** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* [*OffsetWithConfidence*](#binaryninja.types.OffsetWithConfidence
              "binaryninja.types.OffsetWithConfidence") *|* *None*) –

        Return type:
        :   [*FunctionBuilder*](#binaryninja.types.FunctionBuilder
            "binaryninja.types.FunctionBuilder")

    immutable_copy()[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.immutable_copy)

    *static* int(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=True, confidence=255)*, *altname: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [IntegerBuilder](#binaryninja.types.IntegerBuilder "binaryninja.types.IntegerBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.int)
    :   `int` class method for creating an int Type.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the integer in bytes
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – optional variable representing signedness
            - **altname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – alternate name for type

        Return type:
        :   [*IntegerBuilder*](#binaryninja.types.IntegerBuilder "binaryninja.types.IntegerBuilder")

    mutable_copy() → [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.mutable_copy)
    :   Return type:
        :   [*TypeBuilder*](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *static* named_type_from_registered_type(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.named_type_from_registered_type)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type_from_type(*name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.named_type_from_type)
    :   Parameters:
        :   - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass") *|* *None*) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type_from_type_and_id(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.named_type_from_type_and_id)
    :   Parameters:
        :   - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **name** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type") *|* *None*) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* named_type_reference(*type_class: [NamedTypeReferenceClass](enums.md#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass")*, *name: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alignment: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*) → [NamedTypeReferenceBuilder](#binaryninja.types.NamedTypeReferenceBuilder "binaryninja.types.NamedTypeReferenceBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.named_type_reference)
    :   Parameters:
        :   - **type_class**
              ([*NamedTypeReferenceClass*](enums.md#binaryninja.enums.NamedTypeReferenceClass
              "binaryninja.enums.NamedTypeReferenceClass")) –
            - **name** ([*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **alignment** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –

        Return type:
        :   [*NamedTypeReferenceBuilder*](#binaryninja.types.NamedTypeReferenceBuilder
            "binaryninja.types.NamedTypeReferenceBuilder")

    *static* pointer(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") = ReferenceType.PointerReferenceType*) → [PointerBuilder](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.pointer)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType")) –

        Return type:
        :   [*PointerBuilder*](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder")

    *static* pointer_of_width(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *const: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *volatile: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence") = BoolWithConfidence(value=False, confidence=255)*, *ref_type: [ReferenceType](enums.md#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") = ReferenceType.PointerReferenceType*) → [PointerBuilder](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.pointer_of_width)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
              "binaryninja.types.TypeBuilder") *|* [*Type*](#binaryninja.types.Type
              "binaryninja.types.Type")) –
            - **const** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **volatile** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* [*BoolWithConfidence*](#binaryninja.types.BoolWithConfidence
              "binaryninja.types.BoolWithConfidence")) –
            - **ref_type** ([*ReferenceType*](enums.md#binaryninja.enums.ReferenceType
              "binaryninja.enums.ReferenceType")) –

        Return type:
        :   [*PointerBuilder*](#binaryninja.types.PointerBuilder "binaryninja.types.PointerBuilder")

    *static* structure(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *type: [StructureVariant](enums.md#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant") = StructureVariant.StructStructureType*) → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.structure)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **type** ([*StructureVariant*](enums.md#binaryninja.enums.StructureVariant
              "binaryninja.enums.StructureVariant")) –

        Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    *static* union(*members: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StructureMember](#binaryninja.types.StructureMember "binaryninja.types.StructureMember")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](#binaryninja.types.Type "binaryninja.types.Type"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *packed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [StructureBuilder](#binaryninja.types.StructureBuilder "binaryninja.types.StructureBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.union)
    :   Parameters:
        :   - **members** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*StructureMember*](#binaryninja.types.StructureMember
              "binaryninja.types.StructureMember")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*Type*](#binaryninja.types.Type "binaryninja.types.Type")*,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*
              *|* *None*) –
            - **packed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*StructureBuilder*](#binaryninja.types.StructureBuilder
            "binaryninja.types.StructureBuilder")

    *static* void() → [VoidBuilder](#binaryninja.types.VoidBuilder "binaryninja.types.VoidBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.void)
    :   Return type:
        :   [*VoidBuilder*](#binaryninja.types.VoidBuilder "binaryninja.types.VoidBuilder")

    *static* wide_char(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *altname: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [WideCharBuilder](#binaryninja.types.WideCharBuilder "binaryninja.types.WideCharBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilder.wide_char)
    :   `wide_char` class method for creating wide char Types.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the wide character in bytes
            - **altname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – alternate name for type

        Return type:
        :   [*WideCharBuilder*](#binaryninja.types.WideCharBuilder
            "binaryninja.types.WideCharBuilder")

    *property* alignment*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* alternate_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* attributes*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Attribute names and their values

    *property* child*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")]*

    *property* const*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether type is const (read/write)

    *property* signed*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*

    *property* system_call_number*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets/Sets the system call number for a FunctionType object if one exists otherwise None

    *property* type_class*: [TypeClass](enums.md#binaryninja.enums.TypeClass "binaryninja.enums.TypeClass")*

    *property* volatile*: [BoolWithConfidence](#binaryninja.types.BoolWithConfidence "binaryninja.types.BoolWithConfidence")*
    :   Whether type is volatile (read/write)

    *property* width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## TypeBuilderAttributes

*class* TypeBuilderAttributes[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilderAttributes)
:   Bases: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
    v3.14)")

    __init__(*builder: [TypeBuilder](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, **args*)[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeBuilderAttributes.__init__)
    :   Parameters:
        :   **builder** ([*TypeBuilder*](#binaryninja.types.TypeBuilder
            "binaryninja.types.TypeBuilder")) –

## TypeDefinitionLine

*class* TypeDefinitionLine[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeDefinitionLine)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    TypeDefinitionLine(line_type: binaryninja.enums.TypeDefinitionLineType, tokens:
    List[ForwardRef(‘_function.InstructionTextToken’)], type: ‘Type’, parent_type: ‘Type’,
    root_type: ‘Type’, root_type_name: str, base_type:
    Optional[ForwardRef(‘NamedTypeReferenceType’)], base_offset: int, offset: int,
    field_index: int)

    __init__(*line_type: [TypeDefinitionLineType](enums.md#binaryninja.enums.TypeDefinitionLineType "binaryninja.enums.TypeDefinitionLineType")*, *tokens: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*, *type: [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *parent_type: [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *root_type: [Type](#binaryninja.types.Type "binaryninja.types.Type")*, *root_type_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *base_type: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *base_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *field_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **line_type**
              ([*TypeDefinitionLineType*](enums.md#binaryninja.enums.TypeDefinitionLineType
              "binaryninja.enums.TypeDefinitionLineType")) –
            - **tokens** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
              "binaryninja.architecture.InstructionTextToken")*]*) –
            - **type** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) –
            - **parent_type** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) –
            - **root_type** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type")) –
            - **root_type_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **base_type** ([*NamedTypeReferenceType*](#binaryninja.types.NamedTypeReferenceType
              "binaryninja.types.NamedTypeReferenceType") *|* *None*) –
            - **base_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **field_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –

        Return type:
        :   *None*

    base_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    base_type*: [NamedTypeReferenceType](#binaryninja.types.NamedTypeReferenceType "binaryninja.types.NamedTypeReferenceType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    field_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    line_type*: [TypeDefinitionLineType](enums.md#binaryninja.enums.TypeDefinitionLineType "binaryninja.enums.TypeDefinitionLineType")*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    parent_type*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

    root_type*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

    root_type_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*

    type*: [Type](#binaryninja.types.Type "binaryninja.types.Type")*

## TypeFieldReference

*class* TypeFieldReference[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeFieldReference)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    TypeFieldReference(func: Optional[ForwardRef(‘_function.Function’)], arch:
    Optional[ForwardRef(‘architecture.Architecture’)], address: int, size: int,
    incomingType: Optional[binaryninja.types.Type])

    __init__(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *incomingType: [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **incomingType** ([*Type*](#binaryninja.types.Type "binaryninja.types.Type") *|* *None*)
              –

        Return type:
        :   *None*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    func*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    incomingType*: [Type](#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## TypeReferenceSource

*class* TypeReferenceSource[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#TypeReferenceSource)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    TypeReferenceSource(name: binaryninja.types.QualifiedName, offset: int, ref_type:
    binaryninja.enums.TypeReferenceType)

    __init__(*name: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *ref_type: [TypeReferenceType](enums.md#binaryninja.enums.TypeReferenceType "binaryninja.enums.TypeReferenceType")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** ([*QualifiedName*](#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **ref_type** ([*TypeReferenceType*](enums.md#binaryninja.enums.TypeReferenceType
              "binaryninja.enums.TypeReferenceType")) –

        Return type:
        :   *None*

    name*: [QualifiedName](#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    ref_type*: [TypeReferenceType](enums.md#binaryninja.enums.TypeReferenceType "binaryninja.enums.TypeReferenceType")*

## VoidBuilder

*class* VoidBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#VoidBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *classmethod* create(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [VoidBuilder](#binaryninja.types.VoidBuilder "binaryninja.types.VoidBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#VoidBuilder.create)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*VoidBuilder*](#binaryninja.types.VoidBuilder "binaryninja.types.VoidBuilder")

## VoidType

*class* VoidType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#VoidType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [VoidType](#binaryninja.types.VoidType "binaryninja.types.VoidType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#VoidType.create)
    :   Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*VoidType*](#binaryninja.types.VoidType "binaryninja.types.VoidType")

## WideCharBuilder

*class* WideCharBuilder[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#WideCharBuilder)
:   Bases: [`TypeBuilder`](#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")

    *classmethod* create(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [WideCharBuilder](#binaryninja.types.WideCharBuilder "binaryninja.types.WideCharBuilder")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#WideCharBuilder.create)
    :   Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*WideCharBuilder*](#binaryninja.types.WideCharBuilder
            "binaryninja.types.WideCharBuilder")

## WideCharType

*class* WideCharType[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#WideCharType)
:   Bases: [`Type`](#binaryninja.types.Type "binaryninja.types.Type")

    *classmethod* create(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *alternate_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*) → [WideCharType](#binaryninja.types.WideCharType "binaryninja.types.WideCharType")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#WideCharType.create)
    :   `wide_char` class method for creating wide char Types.

        Parameters:
        :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – width of the wide character in bytes
            - **alternate_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – alternate name for type
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*WideCharType*](#binaryninja.types.WideCharType "binaryninja.types.WideCharType")

## convert_integer

convert_integer(*value: [c_ulong](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "(in Python v3.14)")*, *signed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/types.html#convert_integer)
:   Parameters:
    :   - **value** ([*c_ulong*](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "(in
          Python v3.14)")) –
        - **signed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) –
        - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
          v3.14)")) –

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
