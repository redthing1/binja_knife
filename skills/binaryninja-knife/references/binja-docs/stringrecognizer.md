# stringrecognizer module

| Class | Description |
| --- | --- |
| [`binaryninja.stringrecognizer.CoreStringRecognizer`](#binaryninja.stringrecognizer.CoreStringRecognizer "binaryninja.stringrecognizer.CoreStringRecognizer") | `class StringRecognizer` recognizes custom strings found in high level expressions. |
| [`binaryninja.stringrecognizer.CustomStringType`](#binaryninja.stringrecognizer.CustomStringType "binaryninja.stringrecognizer.CustomStringType") | Represents a custom string type. String types contain the name of the string type and the prefix… |
| [`binaryninja.stringrecognizer.StringRecognizer`](#binaryninja.stringrecognizer.StringRecognizer "binaryninja.stringrecognizer.StringRecognizer") | `class StringRecognizer` recognizes custom strings found in high level expressions. |

## CoreStringRecognizer

*class* CoreStringRecognizer[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer)
:   Bases: [`StringRecognizer`](#binaryninja.stringrecognizer.StringRecognizer
    "binaryninja.stringrecognizer.StringRecognizer")

    __init__(*handle: BNStringRecognizer*)[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer.__init__)
    :   Parameters:
        :   **handle** (*BNStringRecognizer*) –

    is_valid_for_type(*func: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer.is_valid_for_type)
    :   Determines if the string recognizer should be called for the given expression type. It
        is optional to override this method. If the method isn’t overridden, all expression
        types are passed to the string recognizer.

        Parameters:
        :   - **func**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) – HighLevelILFunction representing the
              high level function to be queried
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression

        Returns:
        :   True if the expression should be passed to the string recognizer, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    recognize_constant(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer.recognize_constant)
    :   Can be overridden to recognize strings for a constant that is not a pointer. The
        expression type and value of the expression are given. If no string is found for this
        expression, this method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    recognize_constant_pointer(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer.recognize_constant_pointer)
    :   Can be overridden to recognize strings for a constant pointer. The expression type and
        value of the expression are given. If no string is found for this expression, this
        method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    recognize_extern_pointer(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer.recognize_extern_pointer)
    :   Can be overridden to recognize strings for an external symbol. The expression type and
        value of the expression are given. If no string is found for this expression, this
        method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Offset into the external symbol

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    recognize_import(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CoreStringRecognizer.recognize_import)
    :   Can be overridden to recognize strings for an imported symbol. The expression type and
        value of the expression are given. If no string is found for this expression, this
        method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

## CustomStringType

*class* CustomStringType[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CustomStringType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Represents a custom string type. String types contain the name of the string type and
    the prefix and postfix used to render them in code.

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CustomStringType.__init__)

    *static* register(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *string_prefix=''*, *string_postfix=''*) → [CustomStringType](#binaryninja.stringrecognizer.CustomStringType "binaryninja.stringrecognizer.CustomStringType")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#CustomStringType.register)
    :   Registers a new custom string type. This can be used when creating new
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") objects.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*CustomStringType*](#binaryninja.stringrecognizer.CustomStringType
            "binaryninja.stringrecognizer.CustomStringType")

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Name of the custom string type.

    *property* string_postfix*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Postfix added after the closing quote in a custom string.

    *property* string_prefix*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Prefix added before the opening quote in a custom string.

## StringRecognizer

*class* StringRecognizer[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class StringRecognizer` recognizes custom strings found in high level expressions.

    The
    [`recognize_constant`](#binaryninja.stringrecognizer.StringRecognizer.recognize_constant
    "binaryninja.stringrecognizer.StringRecognizer.recognize_constant"),
    [`recognize_constant_pointer`](#binaryninja.stringrecognizer.StringRecognizer.recognize_constant_pointer
    "binaryninja.stringrecognizer.StringRecognizer.recognize_constant_pointer"),
    [`recognize_extern_pointer`](#binaryninja.stringrecognizer.StringRecognizer.recognize_extern_pointer
    "binaryninja.stringrecognizer.StringRecognizer.recognize_extern_pointer"), and
    [`recognize_import`](#binaryninja.stringrecognizer.StringRecognizer.recognize_import
    "binaryninja.stringrecognizer.StringRecognizer.recognize_import") methods will be called
    for the respective expression types. These methods can return a
    [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
    "binaryninja.binaryview.DerivedString") containing the string information if a custom
    string is found for the expression. The
    [`is_valid_for_type`](#binaryninja.stringrecognizer.StringRecognizer.is_valid_for_type
    "binaryninja.stringrecognizer.StringRecognizer.is_valid_for_type") method can be
    optionally overridden to call the recognizer methods only when the expression type
    matches a custom filter.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.__init__)

    is_valid_for_type(*func: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.is_valid_for_type)
    :   Determines if the string recognizer should be called for the given expression type. It
        is optional to override this method. If the method isn’t overridden, all expression
        types are passed to the string recognizer.

        Parameters:
        :   - **func**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) – HighLevelILFunction representing the
              high level function to be queried
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression

        Returns:
        :   True if the expression should be passed to the string recognizer, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    recognize_constant(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.recognize_constant)
    :   Can be overridden to recognize strings for a constant that is not a pointer. The
        expression type and value of the expression are given. If no string is found for this
        expression, this method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    recognize_constant_pointer(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.recognize_constant_pointer)
    :   Can be overridden to recognize strings for a constant pointer. The expression type and
        value of the expression are given. If no string is found for this expression, this
        method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    recognize_extern_pointer(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.recognize_extern_pointer)
    :   Can be overridden to recognize strings for an external symbol. The expression type and
        value of the expression are given. If no string is found for this expression, this
        method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Offset into the external symbol

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    recognize_import(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.recognize_import)
    :   Can be overridden to recognize strings for an imported symbol. The expression type and
        value of the expression are given. If no string is found for this expression, this
        method should return None.

        If a string is found, return a
        [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
        "binaryninja.binaryview.DerivedString") with the string information.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression

        Returns:
        :   Optional [`DerivedString`](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") for any string that is found.

        Return type:
        :   [*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
            "binaryninja.binaryview.DerivedString") | *None*

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/stringrecognizer.html#StringRecognizer.register)
    :   Registers the string recognizer.

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    recognizer_name *= None*
