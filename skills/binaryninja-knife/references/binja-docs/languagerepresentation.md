# languagerepresentation module

| Class | Description |
| --- | --- |
| [`binaryninja.languagerepresentation.CoreLanguageRepresentationFunctionType`](#binaryninja.languagerepresentation.CoreLanguageRepresentationFunctionType "binaryninja.languagerepresentation.CoreLanguageRepresentationFunctionType") | `class LanguageRepresentationFunctionType` represents a custom language representation… |
| [`binaryninja.languagerepresentation.HighLevelILTokenEmitter`](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter") | `class HighLevelILTokenEmitter` contains methods for emitting text tokens for High Level IL… |
| [`binaryninja.languagerepresentation.LanguageRepresentationFunction`](#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction") | `class LanguageRepresentationFunction` represents a single function in a registered high level… |
| [`binaryninja.languagerepresentation.LanguageRepresentationFunctionType`](#binaryninja.languagerepresentation.LanguageRepresentationFunctionType "binaryninja.languagerepresentation.LanguageRepresentationFunctionType") | `class LanguageRepresentationFunctionType` represents a custom language representation… |

## CoreLanguageRepresentationFunctionType

*class* CoreLanguageRepresentationFunctionType[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#CoreLanguageRepresentationFunctionType)
:   Bases:
    [`LanguageRepresentationFunctionType`](#binaryninja.languagerepresentation.LanguageRepresentationFunctionType
    "binaryninja.languagerepresentation.LanguageRepresentationFunctionType")

    __init__(*handle: LP_BNLanguageRepresentationFunctionType*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#CoreLanguageRepresentationFunctionType.__init__)
    :   Parameters:
        :   **handle** (*LP_BNLanguageRepresentationFunctionType*) –

    create(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *owner: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *hlil: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*) → [LanguageRepresentationFunction](#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#CoreLanguageRepresentationFunctionType.create)
    :   This method must be overridden. This creates the `class LanguageRepresentationFunction`
        object for the given architecture, owner function, and High Level IL function.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **owner** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **hlil**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –

        Return type:
        :   [*LanguageRepresentationFunction*](#binaryninja.languagerepresentation.LanguageRepresentationFunction
            "binaryninja.languagerepresentation.LanguageRepresentationFunction")

    function_type_tokens(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#CoreLanguageRepresentationFunctionType.function_type_tokens)
    :   Returns a list of lines representing a function prototype in this language. If no lines
        are returned, the default C-style prototype will be used.

        Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    is_valid(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#CoreLanguageRepresentationFunctionType.is_valid)
    :   Returns whether the language is valid for the given binary view.

        Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* line_formatter*: [LineFormatter](lineformatter.md#binaryninja.lineformatter.LineFormatter "binaryninja.lineformatter.LineFormatter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the line formatter for formatting lines in this language. If `None` is returned,
        the default line formatter will be used.

    *property* type_parser*: [TypeParser](typeparser.md#binaryninja.typeparser.TypeParser "binaryninja.typeparser.TypeParser") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the type parser for parsing types in this language. If `None` is returned, the
        default type parser will be used.

    *property* type_printer*: [TypePrinter](typeprinter.md#binaryninja.typeprinter.TypePrinter "binaryninja.typeprinter.TypePrinter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the type printer for displaying types in this language. If `None` is returned,
        the default type printer will be used.

## HighLevelILTokenEmitter

*class* HighLevelILTokenEmitter[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class HighLevelILTokenEmitter` contains methods for emitting text tokens for High Level
    IL instructions. Methods are provided for typical patterns found in various high level
    languages.

    This class cannot be instantiated directly. An instance of the class will be provided
    when the methods in `class LanguageRepresentationFunction` are called.

    *class* ExprContext[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.ExprContext)
    :   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
        v3.14)")

        `class ExprContext` is a context manager that associates the tokens inside the context
        with the given High Level IL expression.

        __init__(*emitter: [HighLevelILTokenEmitter](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *hlil_expr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.ExprContext.__init__)
        :   Parameters:
            :   - **emitter**
                  ([*HighLevelILTokenEmitter*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter
                  "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) –
                - **hlil_expr**
                  ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
                  "binaryninja.highlevelil.HighLevelILInstruction")) –

    *class* ZeroConfidenceContext[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.ZeroConfidenceContext)
    :   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
        v3.14)")

        `class ZeroConfidenceContext` is a context manager that optionally forces tokens to be
        of zero confidence inside the context.

        __init__(*emitter: [HighLevelILTokenEmitter](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *enabled: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.ZeroConfidenceContext.__init__)
        :   Parameters:
            :   - **emitter**
                  ([*HighLevelILTokenEmitter*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter
                  "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) –
                - **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
                  v3.14)")) –

    __init__(*handle: LP_BNHighLevelILTokenEmitter*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.__init__)
    :   Parameters:
        :   **handle** (*LP_BNHighLevelILTokenEmitter*) –

    append(*tokens: [InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append)
    :   Appends a token or list of tokens to the output.

        Parameters:
        :   **tokens**
            ([*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken") *|*
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")*[*[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")*]*) –

    append_array_index_token(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_array_index_token)
    :   Appends tokens for accessing an array by index.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    append_close_brace()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_close_brace)
    :   Appends a close brace (`}`) to the output.

    append_close_bracket()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_close_bracket)
    :   Appends a close bracket (`]`) to the output.

    append_close_paren()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_close_paren)
    :   Appends a close parenthesis (``)``) to the output.

    append_constant_text_token(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_constant_text_token)
    :   Appends tokens for a constant value.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) –

    append_float_size_token(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *token_type: [InstructionTextTokenType](enums.md#binaryninja.enums.InstructionTextTokenType "binaryninja.enums.InstructionTextTokenType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_float_size_token)
    :   Appends a floating point size token for the given size in the High Level IL syntax.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **token_type**
              ([*InstructionTextTokenType*](enums.md#binaryninja.enums.InstructionTextTokenType
              "binaryninja.enums.InstructionTextTokenType")) –

    append_integer_text_token(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_integer_text_token)
    :   Appends tokens for a constant intenger value.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    append_open_brace()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_open_brace)
    :   Appends an open brace (`{`) to the output.

    append_open_bracket()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_open_bracket)
    :   Appends an open bracket (`[`) to the output.

    append_open_paren()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_open_paren)
    :   Appends an open parenthesis (`(`) to the output.

    append_pointer_text_token(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *symbol_display: [SymbolDisplayType](enums.md#binaryninja.enums.SymbolDisplayType "binaryninja.enums.SymbolDisplayType")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence")*, *allow_short_string: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [SymbolDisplayResult](enums.md#binaryninja.enums.SymbolDisplayResult "binaryninja.enums.SymbolDisplayResult")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_pointer_text_token)
    :   Appends tokens for displaying a constant pointer value.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –
            - **symbol_display** ([*SymbolDisplayType*](enums.md#binaryninja.enums.SymbolDisplayType
              "binaryninja.enums.SymbolDisplayType")) –
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) –
            - **allow_short_string** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –

        Return type:
        :   [*SymbolDisplayResult*](enums.md#binaryninja.enums.SymbolDisplayResult
            "binaryninja.enums.SymbolDisplayResult")

    append_semicolon()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_semicolon)
    :   Appends a semicolon (`;`) to the output.

    append_size_token(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *token_type: [InstructionTextTokenType](enums.md#binaryninja.enums.InstructionTextTokenType "binaryninja.enums.InstructionTextTokenType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_size_token)
    :   Appends a size token for the given size in the High Level IL syntax.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **token_type**
              ([*InstructionTextTokenType*](enums.md#binaryninja.enums.InstructionTextTokenType
              "binaryninja.enums.InstructionTextTokenType")) –

    append_var_text_token(*var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.append_var_text_token)
    :   Appends tokens for access to a variable.

        Parameters:
        :   - **var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) –
            - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    begin_scope(*scope_type: [ScopeType](enums.md#binaryninja.enums.ScopeType "binaryninja.enums.ScopeType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.begin_scope)
    :   Begins a new scope. Insertion of newlines and braces will be handled using the current
        settings.

        Parameters:
        :   **scope_type** ([*ScopeType*](enums.md#binaryninja.enums.ScopeType
            "binaryninja.enums.ScopeType")) –

    decrease_indent()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.decrease_indent)
    :   Decreases the indentation level by one.

    end_scope(*scope_type: [ScopeType](enums.md#binaryninja.enums.ScopeType "binaryninja.enums.ScopeType")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.end_scope)
    :   Ends the current scope.

        Parameters:
        :   **scope_type** ([*ScopeType*](enums.md#binaryninja.enums.ScopeType
            "binaryninja.enums.ScopeType")) –

    expr(*hlil_expr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → [ExprContext](#binaryninja.languagerepresentation.HighLevelILTokenEmitter.ExprContext "binaryninja.languagerepresentation.HighLevelILTokenEmitter.ExprContext")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.expr)
    :   Returns a context manager that associates the tokens inside the context with the given
        High Level IL expression.

        Parameters:
        :   **hlil_expr**
            ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")) –

        Return type:
        :   [*ExprContext*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter.ExprContext
            "binaryninja.languagerepresentation.HighLevelILTokenEmitter.ExprContext")

    finalize()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.finalize)
    :   Finalizes all tokens in the output.

    finalize_scope()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.finalize_scope)
    :   Finalizes the previous scope, indicating that there are no more associated scopes.

    force_zero_confidence(*enabled: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [ZeroConfidenceContext](#binaryninja.languagerepresentation.HighLevelILTokenEmitter.ZeroConfidenceContext "binaryninja.languagerepresentation.HighLevelILTokenEmitter.ZeroConfidenceContext")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.force_zero_confidence)
    :   Returns a context manager that forces tokens inside of it to be of zero confidence. If
        `False` is passed to this method, the context has no effect, allowing the caller to
        conditionally apply this behavior.

        Parameters:
        :   **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) –

        Return type:
        :   [*ZeroConfidenceContext*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter.ZeroConfidenceContext
            "binaryninja.languagerepresentation.HighLevelILTokenEmitter.ZeroConfidenceContext")

    increase_indent()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.increase_indent)
    :   Increases the indentation level by one.

    init_line()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.init_line)
    :   Initialize a new line, creating indentation tokens at the start.

    *static* names_for_outer_structure_members(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *struct_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *var: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.names_for_outer_structure_members)
    :   Gets the list of names for the outer structure members when accessing a structure
        member. This list can be passed for the `typeNames` parameter of the `class
        InstructionTextToken` constructor.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **struct_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **var**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    new_line()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.new_line)
    :   Starts a new line in the output.

    no_indent_for_this_line()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.no_indent_for_this_line)
    :   Forces there to be no indentation for the next line.

    prepend_blank_collapse_indicator()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.prepend_blank_collapse_indicator)
    :   Insert, at the beginning of the line, a collapse indicator token. The indicator will be
        a blank space and not have any functionality.

    prepend_instr_collapse_indicator(*function_: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *discriminator: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.prepend_instr_collapse_indicator)
    :   Insert, at the beginning of the line, a collapse indicator token.

        The indicator will allow the user to collapse the region specified by (instr,
        discriminator) on the function. Implementations can use
        `Function.is_instruction_collapsed` and `Function.is_region_collapsed` to account for
        collapsed regions in rendering.

        Parameters:
        :   - **function** – Function whose instructions are being emitted
            - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – Instruction being emitted which can
              be collapsed
            - **discriminator** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – Unique discriminator id for the region
            - **function_** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

    prepend_region_collapse_indicator(*context: [InstructionTextTokenContext](enums.md#binaryninja.enums.InstructionTextTokenContext "binaryninja.enums.InstructionTextTokenContext")*, *hash: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.prepend_region_collapse_indicator)
    :   Parameters:
        :   - **context**
              ([*InstructionTextTokenContext*](enums.md#binaryninja.enums.InstructionTextTokenContext
              "binaryninja.enums.InstructionTextTokenContext")) –
            - **hash** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    scope_continuation(*force_same_line: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.scope_continuation)
    :   Continues the previous scope with a new associated scope. This is most commonly used for
        `else` statements.

        Parameters:
        :   **force_same_line** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
            Python v3.14)")) –

    scope_separator()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#HighLevelILTokenEmitter.scope_separator)
    :   Indicates that visual separation of scopes is desirable at the current position. By
        default, this will insert a blank line, but this can be configured by the user.

    *property* brace_requirement*: [BraceRequirement](enums.md#binaryninja.enums.BraceRequirement "binaryninja.enums.BraceRequirement")*
    :   The requirement for insertion of braces around scopes in the output.

    *property* braces_around_switch_cases
    :   Whether cases within switch statements should always have braces around them.

    *property* current_tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*
    :   The list of tokens on the current line.

    *property* default_braces_on_same_line
    :   Whether braces should default to being on the same line as the statement that begins the
        scope. If the user has explicitly set a preference, this setting will be ignored and the
        user’s preference will be used instead.

    *property* has_collapsable_regions*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   If the emitter can emit regions which can be collapsed

    *property* lines*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*
    :   The list of lines in the output (read-only).

    *property* simple_scope_allowed
    :   Whether omitting braces around single-line scopes is allowed.

## LanguageRepresentationFunction

*class* LanguageRepresentationFunction[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class LanguageRepresentationFunction` represents a single function in a registered high
    level language.

    __init__(*func_type: [LanguageRepresentationFunctionType](#binaryninja.languagerepresentation.LanguageRepresentationFunctionType "binaryninja.languagerepresentation.LanguageRepresentationFunctionType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *owner: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *hlil: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.__init__)
    :   Parameters:
        :   - **func_type**
              ([*LanguageRepresentationFunctionType*](#binaryninja.languagerepresentation.LanguageRepresentationFunctionType
              "binaryninja.languagerepresentation.LanguageRepresentationFunctionType") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **owner** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **hlil**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction") *|* *None*) –

    get_block_lines(*block: [HighLevelILBasicBlock](highlevelil.md#binaryninja.highlevelil.HighLevelILBasicBlock "binaryninja.highlevelil.HighLevelILBasicBlock")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.get_block_lines)
    :   Generates lines for a single High Level IL basic block.

        Parameters:
        :   - **block**
              ([*HighLevelILBasicBlock*](highlevelil.md#binaryninja.highlevelil.HighLevelILBasicBlock
              "binaryninja.highlevelil.HighLevelILBasicBlock")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    get_expr_text(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence") = OperatorPrecedence.TopLevelOperatorPrecedence*, *statement: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.get_expr_text)
    :   Gets the lines of tokens for a given High Level IL instruction.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) –
            - **statement** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    get_linear_lines(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.get_linear_lines)
    :   Generates lines for the given High Level IL instruction in the style of the linear view.
        To get the lines for the entire function, pass the `root` property of a `class
        HighLevelILFunction`.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    perform_begin_lines(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *tokens: [HighLevelILTokenEmitter](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.perform_begin_lines)
    :   This method can be overridden to emit tokens at the start of a function.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **tokens**
              ([*HighLevelILTokenEmitter*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) –

    perform_end_lines(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *tokens: [HighLevelILTokenEmitter](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.perform_end_lines)
    :   This method can be overridden to emit tokens at the end of a function.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **tokens**
              ([*HighLevelILTokenEmitter*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) –

    perform_get_expr_text(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *tokens: [HighLevelILTokenEmitter](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence") = OperatorPrecedence.TopLevelOperatorPrecedence*, *statement: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.perform_get_expr_text)
    :   This method must be overridden by all language representation plugins.

        This method is called to emit the tokens for a given High Level IL instruction.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **tokens**
              ([*HighLevelILTokenEmitter*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) –
            - **statement** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    perform_init_token_emitter(*emitter: [HighLevelILTokenEmitter](#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunction.perform_init_token_emitter)
    :   Override this method to initialize the options for the token emitter before it is used.

        Parameters:
        :   **emitter**
            ([*HighLevelILTokenEmitter*](#binaryninja.languagerepresentation.HighLevelILTokenEmitter
            "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) –

    annotation_end_string *= '}'*

    annotation_start_string *= '{'*

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    comment_end_string *= ''*

    comment_start_string *= '// '*

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*

    *property* high_level_il*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* hlil*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

## LanguageRepresentationFunctionType

*class* LanguageRepresentationFunctionType[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunctionType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class LanguageRepresentationFunctionType` represents a custom language representation
    function type. This class provides methods to create `class
    LanguageRepresentationFunction` instances for functions, as well as manage the printing
    and parsing of types.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunctionType.__init__)

    create(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *owner: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *hlil: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*) → [LanguageRepresentationFunction](#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunctionType.create)
    :   This method must be overridden. This creates the `class LanguageRepresentationFunction`
        object for the given architecture, owner function, and High Level IL function.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **owner** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **hlil**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –

        Return type:
        :   [*LanguageRepresentationFunction*](#binaryninja.languagerepresentation.LanguageRepresentationFunction
            "binaryninja.languagerepresentation.LanguageRepresentationFunction")

    function_type_tokens(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunctionType.function_type_tokens)
    :   Returns a list of lines representing a function prototype in this language. If no lines
        are returned, the default C-style prototype will be used.

        Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    is_valid(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunctionType.is_valid)
    :   Returns whether the language is valid for the given binary view.

        Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/languagerepresentation.html#LanguageRepresentationFunctionType.register)
    :   Registers the language representation function type.

    language_name *= None*

    *property* line_formatter*: [LineFormatter](lineformatter.md#binaryninja.lineformatter.LineFormatter "binaryninja.lineformatter.LineFormatter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the line formatter for formatting lines in this language. If `None` is returned,
        the default line formatter will be used.

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* type_parser*: [TypeParser](typeparser.md#binaryninja.typeparser.TypeParser "binaryninja.typeparser.TypeParser") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the type parser for parsing types in this language. If `None` is returned, the
        default type parser will be used.

    *property* type_printer*: [TypePrinter](typeprinter.md#binaryninja.typeprinter.TypePrinter "binaryninja.typeprinter.TypePrinter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the type printer for displaying types in this language. If `None` is returned,
        the default type printer will be used.
