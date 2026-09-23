# variable module

| Class | Description |
| --- | --- |
| [`binaryninja.variable.AddressRange`](#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange") |  |
| [`binaryninja.variable.ArchitectureVariable`](#binaryninja.variable.ArchitectureVariable "binaryninja.variable.ArchitectureVariable") | `class ArchitectureVariable` is a wrapper around [`CoreVariable`](#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable") that is bound to an… |
| [`binaryninja.variable.ConstantData`](#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") |  |
| [`binaryninja.variable.ConstantDataRegisterValue`](#binaryninja.variable.ConstantDataRegisterValue "binaryninja.variable.ConstantDataRegisterValue") |  |
| [`binaryninja.variable.ConstantPointerRegisterValue`](#binaryninja.variable.ConstantPointerRegisterValue "binaryninja.variable.ConstantPointerRegisterValue") |  |
| [`binaryninja.variable.ConstantReference`](#binaryninja.variable.ConstantReference "binaryninja.variable.ConstantReference") |  |
| [`binaryninja.variable.ConstantRegisterValue`](#binaryninja.variable.ConstantRegisterValue "binaryninja.variable.ConstantRegisterValue") |  |
| [`binaryninja.variable.CoreVariable`](#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable") | `class CoreVariable` is the base class for other variable types, such as… |
| [`binaryninja.variable.EntryRegisterValue`](#binaryninja.variable.EntryRegisterValue "binaryninja.variable.EntryRegisterValue") |  |
| [`binaryninja.variable.ExternalPointerRegisterValue`](#binaryninja.variable.ExternalPointerRegisterValue "binaryninja.variable.ExternalPointerRegisterValue") |  |
| [`binaryninja.variable.ImportedAddressRegisterValue`](#binaryninja.variable.ImportedAddressRegisterValue "binaryninja.variable.ImportedAddressRegisterValue") |  |
| [`binaryninja.variable.IndirectBranchInfo`](#binaryninja.variable.IndirectBranchInfo "binaryninja.variable.IndirectBranchInfo") |  |
| [`binaryninja.variable.LookupTableEntry`](#binaryninja.variable.LookupTableEntry "binaryninja.variable.LookupTableEntry") |  |
| [`binaryninja.variable.ParameterLocations`](#binaryninja.variable.ParameterLocations "binaryninja.variable.ParameterLocations") | Note  This object is a “passive” object. Any changes you make to it will not be reflected in… |
| [`binaryninja.variable.ParameterPointerRegisterValue`](#binaryninja.variable.ParameterPointerRegisterValue "binaryninja.variable.ParameterPointerRegisterValue") |  |
| [`binaryninja.variable.ParameterVariables`](#binaryninja.variable.ParameterVariables "binaryninja.variable.ParameterVariables") | Note  This object is a “passive” object. Any changes you make to it will not be reflected in… |
| [`binaryninja.variable.PossibleValueSet`](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet") | class PossibleValueSet PossibleValueSet is used to define possible values that a variable can… |
| [`binaryninja.variable.RegisterValue`](#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue") |  |
| [`binaryninja.variable.ResultPointerRegisterValue`](#binaryninja.variable.ResultPointerRegisterValue "binaryninja.variable.ResultPointerRegisterValue") |  |
| [`binaryninja.variable.ReturnAddressRegisterValue`](#binaryninja.variable.ReturnAddressRegisterValue "binaryninja.variable.ReturnAddressRegisterValue") |  |
| [`binaryninja.variable.StackFrameOffsetRegisterValue`](#binaryninja.variable.StackFrameOffsetRegisterValue "binaryninja.variable.StackFrameOffsetRegisterValue") |  |
| [`binaryninja.variable.StackVariableReference`](#binaryninja.variable.StackVariableReference "binaryninja.variable.StackVariableReference") |  |
| [`binaryninja.variable.Undetermined`](#binaryninja.variable.Undetermined "binaryninja.variable.Undetermined") |  |
| [`binaryninja.variable.ValueRange`](#binaryninja.variable.ValueRange "binaryninja.variable.ValueRange") |  |
| [`binaryninja.variable.Variable`](#binaryninja.variable.Variable "binaryninja.variable.Variable") | `class Variable` represents variables in Binary Ninja. Variables are resolved in medium level… |
| [`binaryninja.variable.VariableNameAndType`](#binaryninja.variable.VariableNameAndType "binaryninja.variable.VariableNameAndType") | `class VariableNameAndType` is a lightweight wrapper around a variable and its name, useful… |

## AddressRange

*class* AddressRange[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#AddressRange)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## ArchitectureVariable

*class* ArchitectureVariable[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable)
:   Bases: [`CoreVariable`](#binaryninja.variable.CoreVariable
    "binaryninja.variable.CoreVariable")

    `class ArchitectureVariable` is a wrapper around
    [`CoreVariable`](#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")
    that is bound to an architecture (for register/flag naming) but not a function. This is
    typically used in calling conventions for specifying value locations. Calling
    conventions can be used outside functions to resolve type information, so only an
    architecture is required.

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *source_type: [VariableSourceType](enums.md#binaryninja.enums.VariableSourceType "binaryninja.enums.VariableSourceType")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *storage: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **source_type** ([*VariableSourceType*](enums.md#binaryninja.enums.VariableSourceType
              "binaryninja.enums.VariableSourceType"))
            - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **storage** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *classmethod* flag(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *flag: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.flag)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *classmethod* from_BNVariable(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *var: BNVariable*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.from_BNVariable)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **var** (*BNVariable*)

    *classmethod* from_core_variable(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *var: [CoreVariable](#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.from_core_variable)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **var** ([*CoreVariable*](#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable"))

    *classmethod* from_identifier(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *identifier: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.from_identifier)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **identifier** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *classmethod* reg(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *reg: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.reg)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *classmethod* stack_offset(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ArchitectureVariable.stack_offset)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## ConstantData

*class* ConstantData[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ConstantData)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.UndeterminedValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *function: _function.Function = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **function** (*_function.Function*)

        Return type:
        :   *None*

    *property* data*: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*

    *property* data_and_builtin*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [BuiltinType](enums.md#binaryninja.enums.BuiltinType "binaryninja.enums.BuiltinType")]*

    function*: _function.Function* *= None*

## ConstantDataRegisterValue

*class* ConstantDataRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ConstantDataRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.UndeterminedValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

## ConstantPointerRegisterValue

*class* ConstantPointerRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ConstantPointerRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ConstantPointerValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 3*

## ConstantReference

*class* ConstantReference[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ConstantReference)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *pointer: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *intermediate: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **pointer** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)"))
            - **intermediate** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)"))

        Return type:
        :   *None*

    intermediate*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    pointer*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## ConstantRegisterValue

*class* ConstantRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ConstantRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ConstantValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 2*

## CoreVariable

*class* CoreVariable[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class CoreVariable` is the base class for other variable types, such as
    [`VariableNameAndType`](#binaryninja.variable.VariableNameAndType
    "binaryninja.variable.VariableNameAndType") and
    [`Variable`](#binaryninja.variable.Variable "binaryninja.variable.Variable")

    Variables:
    :   - **index** – Internal identifier
        - **storage** – If this variable is a stack variable (source_type ==
          VariableSourceType.StackVariableSourceType), then the storage location is the offset
          onto the stack that contains the first byte of this variable. Otherwise it’s used as an
          internal identifier.

    __init__(*_source_type: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *storage: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **_source_type** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **storage** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    *classmethod* flag(*flag: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable.flag)
    :   Parameters:
        :   **flag** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

    *classmethod* from_BNVariable(*var: BNVariable*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable.from_BNVariable)
    :   Parameters:
        :   **var** (*BNVariable*)

    *classmethod* from_identifier(*identifier*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable.from_identifier)

    *classmethod* reg(*reg: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable.reg)
    :   Parameters:
        :   **reg** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

    *classmethod* stack_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable.stack_offset)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

    to_BNVariable()[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#CoreVariable.to_BNVariable)

    *property* identifier*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   A UID for a variable within a function.

    index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* source_type*: [VariableSourceType](enums.md#binaryninja.enums.VariableSourceType "binaryninja.enums.VariableSourceType")*
    :   Whether this variable was created based off of an underlying register, stack location,
        or flag.

    storage*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## EntryRegisterValue

*class* EntryRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#EntryRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.EntryValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *reg: RegisterName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **reg** (*RegisterName* *|* *None*)

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    reg*: binaryninja.architecture.RegisterName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 1*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

## ExternalPointerRegisterValue

*class* ExternalPointerRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ExternalPointerRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ExternalPointerValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 4*

## ImportedAddressRegisterValue

*class* ImportedAddressRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ImportedAddressRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ImportedAddressValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 7*

## IndirectBranchInfo

*class* IndirectBranchInfo[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#IndirectBranchInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*source_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *source_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest_arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *dest_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **source_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **source_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **dest_arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture"))
            - **dest_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)"))

        Return type:
        :   *None*

    auto_defined*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    dest_addr*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    dest_arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    source_addr*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    source_arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

## LookupTableEntry

*class* LookupTableEntry[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#LookupTableEntry)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*from_values: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *to_value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.LookupTableValue*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **from_values** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]*)
            - **to_value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))

        Return type:
        :   *None*

    from_values*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

    to_value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 12*

## ParameterLocations

*class* ParameterLocations[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterLocations)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Note

    This object is a “passive” object. Any changes you make to it will not be reflected in
    the core and vice-versa. If you wish to update a core version of this object you should
    use the appropriate API.

    __init__(*location_list: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterLocations.__init__)
    :   Parameters:
        :   - **location_list** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*]*)
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*)

    with_confidence(*confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ParameterLocations](#binaryninja.variable.ParameterLocations "binaryninja.variable.ParameterLocations")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterLocations.with_confidence)
    :   Parameters:
        :   **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*ParameterLocations*](#binaryninja.variable.ParameterLocations
            "binaryninja.variable.ParameterLocations")

    *property* confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* locations*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*

## ParameterPointerRegisterValue

*class* ParameterPointerRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterPointerRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ParameterPointerValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 9*

## ParameterVariables

*class* ParameterVariables[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterVariables)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Note

    This object is a “passive” object. Any changes you make to it will not be reflected in
    the core and vice-versa. If you wish to update a core version of this object you should
    use the appropriate API.

    __init__(*var_list: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterVariables.__init__)
    :   Parameters:
        :   - **var_list** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Variable*](#binaryninja.variable.Variable
              "binaryninja.variable.Variable")*]*)
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*)

    with_confidence(*confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ParameterVariables](#binaryninja.variable.ParameterVariables "binaryninja.variable.ParameterVariables")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ParameterVariables.with_confidence)
    :   Parameters:
        :   **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*ParameterVariables*](#binaryninja.variable.ParameterVariables
            "binaryninja.variable.ParameterVariables")

    *property* confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

## PossibleValueSet

*class* PossibleValueSet[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    class PossibleValueSet PossibleValueSet is used to define possible values that a
    variable can take. It contains methods to instantiate different value sets such as
    Constant, Signed/Unsigned Ranges, etc.

    Note

    This object is a “passive” object. Any changes you make to it will not be reflected in
    the core and vice-versa. If you wish to update a core version of this object you should
    use the appropriate API.

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *value: BNPossibleValueSet | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)
            - **value** (*BNPossibleValueSet* *|* *None*)

    add(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.add)
    :   Add two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    and_(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.and_)
    :   Perform bitwise AND of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    arith_shift_right(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.arith_shift_right)
    :   Perform arithmetic right shift of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* constant(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.constant)
    :   Create a constant valued PossibleValueSet object.

        Parameters:
        :   **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Integer value of the constant

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* constant_ptr(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.constant_ptr)
    :   Create constant pointer valued PossibleValueSet object.

        Parameters:
        :   **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Integer value of the constant pointer

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* in_set_of_values(*values: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.in_set_of_values)
    :   Create a PossibleValueSet object for a value in a set of values.

        Parameters:
        :   **values** (*Iterable**[*[*int*](https://docs.python.org/3/library/functions.html#int
            "(in Python v3.14)")*]*) – Iterable of integer values

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    intersection(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.intersection)
    :   Compute the intersection of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    logical_shift_right(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.logical_shift_right)
    :   Perform logical right shift of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* lookup_table_value(*lookup_table: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LookupTableEntry](#binaryninja.variable.LookupTableEntry "binaryninja.variable.LookupTableEntry")]*, *mapping: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.lookup_table_value)
    :   Create a PossibleValueSet object for a value which is a member of a lookup table.

        Parameters:
        :   - **lookup_table** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*(*[*LookupTableEntry*](#binaryninja.variable.LookupTableEntry
              "binaryninja.variable.LookupTableEntry")*)*) – List of table entries
            - **mapping** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]*) – Mapping used for resolution
            - **mapping**

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    multiply(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.multiply)
    :   Multiply two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    negate(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.negate)
    :   Negate a PossibleValueSet.

        Parameters:
        :   **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    not_(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.not_)
    :   Perform bitwise NOT of a PossibleValueSet.

        Parameters:
        :   **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* not_in_set_of_values(*values: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.not_in_set_of_values)
    :   Create a PossibleValueSet object for a value NOT in a set of values.

        Parameters:
        :   **values** (*Iterable**[*[*int*](https://docs.python.org/3/library/functions.html#int
            "(in Python v3.14)")*]*) – Iterable of integer values

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    or_(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.or_)
    :   Perform bitwise OR of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* parameter_pointer(*idx: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.parameter_pointer)
    :   Create a PossibleValueSet object for a pointer to a parameter when the parameter is
        stored at an unknown location in memory. This is typically used for calling conventions
        that pass in a pointer to the storage location for parameters (usually larger than can
        be held in a register).

        Parameters:
        :   - **idx** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Index of the parameter
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Integer value of the offset

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* result_pointer(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.result_pointer)
    :   Create a PossibleValueSet object for a pointer to the return value when the return value
        is stored at an unknown location in memory. This is typically used for calling
        conventions that pass in a pointer to the storage location for the return value.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Integer value of the offset

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    rotate_left(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.rotate_left)
    :   Perform left rotation of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    rotate_right(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.rotate_right)
    :   Perform right rotation of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    shift_left(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.shift_left)
    :   Perform left shift of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    signed_divide(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.signed_divide)
    :   Perform signed division of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    signed_mod(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.signed_mod)
    :   Perform signed modulo of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* signed_range_value(*ranges: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueRange](#binaryninja.variable.ValueRange "binaryninja.variable.ValueRange")]*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.signed_range_value)
    :   Create a PossibleValueSet object for a signed range of values.

        Parameters:
        :   **ranges** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*(*[*ValueRange*](#binaryninja.variable.ValueRange
            "binaryninja.variable.ValueRange")*)*) – List of ValueRanges

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

        Example:
        :   ```
            >>> v_1 = ValueRange(-5, -1, 1)
            >>> v_2 = ValueRange(7, 10, 1)
            >>> val = PossibleValueSet.signed_range_value([v_1, v_2])
            <signed ranges: [<range: -0x5 to -0x1>, <range: 0x7 to 0xa>]>
            ```

    *static* stack_frame_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.stack_frame_offset)
    :   Create a PossibleValueSet object for a stack frame offset.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Integer value of the offset

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    subtract(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.subtract)
    :   Subtract two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* undetermined() → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.undetermined)
    :   Create a PossibleValueSet object of type UndeterminedValue.

        Returns:
        :   PossibleValueSet object of type UndeterminedValue

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    union(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.union)
    :   Compute the union of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    unsigned_divide(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.unsigned_divide)
    :   Perform unsigned division of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    unsigned_mod(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.unsigned_mod)
    :   Perform unsigned modulo of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *static* unsigned_range_value(*ranges: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueRange](#binaryninja.variable.ValueRange "binaryninja.variable.ValueRange")]*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.unsigned_range_value)
    :   Create a PossibleValueSet object for a unsigned signed range of values.

        Parameters:
        :   **ranges** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*(*[*ValueRange*](#binaryninja.variable.ValueRange
            "binaryninja.variable.ValueRange")*)*) – List of ValueRanges

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

        Example:
        :   ```
            >>> v_1 = ValueRange(0, 5, 1)
            >>> v_2 = ValueRange(7, 10, 1)
            >>> val = PossibleValueSet.unsigned_range_value([v_1, v_2])
            <unsigned ranges: [<range: 0x0 to 0x5>, <range: 0x7 to 0xa>]>
            ```

    xor(*other: [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [PossibleValueSet](#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#PossibleValueSet.xor)
    :   Perform bitwise XOR of two PossibleValueSets.

        Parameters:
        :   - **other** ([*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*PossibleValueSet*](#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    *property* count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* mapping*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueRange](#binaryninja.variable.ValueRange "binaryninja.variable.ValueRange")]*

    *property* reg*: RegisterName*

    *property* size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* table*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LookupTableEntry](#binaryninja.variable.LookupTableEntry "binaryninja.variable.LookupTableEntry")]*

    *property* type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")*

    *property* value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* values*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

## RegisterValue

*class* RegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#RegisterValue)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.UndeterminedValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    *classmethod* from_BNRegisterValue(*reg_value: BNRegisterValue | BNRegisterValueWithConfidence*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [RegisterValue](#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#RegisterValue.from_BNRegisterValue)
    :   Parameters:
        :   - **reg_value** (*BNRegisterValue* *|* *BNRegisterValueWithConfidence*)
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   [*RegisterValue*](#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    *classmethod* to_BNRegisterValue(*reg_value: [RegisterValue](#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*) → BNRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#RegisterValue.to_BNRegisterValue)
    :   Parameters:
        :   **reg_value** ([*RegisterValue*](#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue"))

        Return type:
        :   *BNRegisterValue*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 0*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## ResultPointerRegisterValue

*class* ResultPointerRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ResultPointerRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ResultPointerValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 8*

## ReturnAddressRegisterValue

*class* ReturnAddressRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ReturnAddressRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.ReturnAddressValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 6*

## StackFrameOffsetRegisterValue

*class* StackFrameOffsetRegisterValue[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#StackFrameOffsetRegisterValue)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.StackFrameOffset*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 5*

## StackVariableReference

*class* StackVariableReference[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#StackVariableReference)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*_source_operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *var: [Variable](#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *referenced_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **_source_operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*)
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **var** ([*Variable*](#binaryninja.variable.Variable "binaryninja.variable.Variable"))
            - **referenced_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    referenced_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* source_operand

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

    var*: [Variable](#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## Undetermined

*class* Undetermined[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Undetermined)
:   Bases: [`RegisterValue`](#binaryninja.variable.RegisterValue
    "binaryninja.variable.RegisterValue")

    __init__(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *type: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") = RegisterValueType.UndeterminedValue*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    type*: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")* *= 0*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

## ValueRange

*class* ValueRange[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#ValueRange)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *step: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **step** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    step*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## Variable

*class* Variable[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable)
:   Bases: [`CoreVariable`](#binaryninja.variable.CoreVariable
    "binaryninja.variable.CoreVariable")

    `class Variable` represents variables in Binary Ninja. Variables are resolved in medium
    level IL, so variables objects are only valid for MLIL and above.

    __init__(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *source_type: [VariableSourceType](enums.md#binaryninja.enums.VariableSourceType "binaryninja.enums.VariableSourceType")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *storage: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.__init__)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))
            - **source_type** ([*VariableSourceType*](enums.md#binaryninja.enums.VariableSourceType
              "binaryninja.enums.VariableSourceType"))
            - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **storage** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *classmethod* from_BNVariable(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *var: BNVariable*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.from_BNVariable)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))
            - **var** (*BNVariable*)

    *classmethod* from_core_variable(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *var: [CoreVariable](#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.from_core_variable)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))
            - **var** ([*CoreVariable*](#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable"))

    *classmethod* from_identifier(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *identifier: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.from_identifier)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))
            - **identifier** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    *classmethod* from_variable_name_and_type(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *var: [VariableNameAndType](#binaryninja.variable.VariableNameAndType "binaryninja.variable.VariableNameAndType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.from_variable_name_and_type)
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))
            - **var** ([*VariableNameAndType*](#binaryninja.variable.VariableNameAndType
              "binaryninja.variable.VariableNameAndType"))

    set_name_and_type_async(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *new_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.set_name_and_type_async)
    :   `set_name_and_type_async` provides a way to asynchronously set both the name and type of
        a variable. This method should be used when speed is of concern.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)
            - **new_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))

        Return type:
        :   *None*

    set_name_async(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.set_name_async)
    :   `set_name_async` provides a way to asynchronously set the name of a variable. This
        method should be used when speed is of concern.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*)

        Return type:
        :   *None*

    set_type_async(*new_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#Variable.set_type_async)
    :   `set_type_async` provides a way to asynchronously set the type of a variable. This
        method should be used when speed is of concern.

        Parameters:
        :   **new_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))

        Return type:
        :   *None*

    *property* core_variable*: [CoreVariable](#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*
    :   Retrieve the underlying [`CoreVariable`](#binaryninja.variable.CoreVariable
        "binaryninja.variable.CoreVariable") class

    *property* dead_store_elimination*: [DeadStoreElimination](enums.md#binaryninja.enums.DeadStoreElimination "binaryninja.enums.DeadStoreElimination")*
    :   returns the dead store elimination setting for this variable

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*
    :   returns the source Function object which this variable belongs to

    *property* il_function*: function.ILFunctionType*
    :   returns the IL Function object which this variable belongs to

    *property* is_parameter_variable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   returns whether this variable is a function parameter

    *property* last_seen_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Name of the variable, or the name most recently assigned if the variable has since been
        removed (read-only).

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Name of the variable, Settings this property is slow because it ensures that analysis
        has been updated. If you are renaming many variables, use
        [`set_name_async`](#binaryninja.variable.Variable.set_name_async
        "binaryninja.variable.Variable.set_name_async"), then call `update_analysis` when
        complete.

    *property* offset_to_next_variable*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   returns number of bytes to the next variable on the stack

    *property* ssa_versions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   Returns the SSA versions associated with this variable. Doesn’t return anything for
        aliased variables.

    *property* type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* var_name_and_type*: [VariableNameAndType](#binaryninja.variable.VariableNameAndType "binaryninja.variable.VariableNameAndType")*
    :   Convert to [`VariableNameAndType`](#binaryninja.variable.VariableNameAndType
        "binaryninja.variable.VariableNameAndType")

## VariableNameAndType

*class* VariableNameAndType[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#VariableNameAndType)
:   Bases: [`CoreVariable`](#binaryninja.variable.CoreVariable
    "binaryninja.variable.CoreVariable")

    `class VariableNameAndType` is a lightweight wrapper around a variable and its name,
    useful for shuttling between APIs that require them both. While
    [`Variable`](#binaryninja.variable.Variable "binaryninja.variable.Variable") has
    [`Variable.name`](#binaryninja.variable.Variable.name
    "binaryninja.variable.Variable.name") and
    [`Variable.type`](#binaryninja.variable.Variable.type
    "binaryninja.variable.Variable.type") fields, those require additional core calls each
    time you fetch them.

    Variables:
    :   - **name** – The variable’s name
        - **type** – The variable’s type

    __init__(*_source_type: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *storage: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **_source_type** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **storage** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))

        Return type:
        :   *None*

    *classmethod* from_core_variable(*var*, *name*, *type*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#VariableNameAndType.from_core_variable)

    *classmethod* from_identifier(*identifier*, *name*, *type*)[[source]](https://api.binary.ninja/_modules/binaryninja/variable.html#VariableNameAndType.from_identifier)

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*
