# constantrenderer module

| Class | Description |
| --- | --- |
| [`binaryninja.constantrenderer.ConstantRenderer`](#binaryninja.constantrenderer.ConstantRenderer "binaryninja.constantrenderer.ConstantRenderer") | `class ConstantRenderer` allows custom rendering of constants in high level representations. |
| [`binaryninja.constantrenderer.CoreConstantRenderer`](#binaryninja.constantrenderer.CoreConstantRenderer "binaryninja.constantrenderer.CoreConstantRenderer") | `class ConstantRenderer` allows custom rendering of constants in high level representations. |

## ConstantRenderer

*class* ConstantRenderer[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#ConstantRenderer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class ConstantRenderer` allows custom rendering of constants in high level
    representations.

    The [`render_constant`](#binaryninja.constantrenderer.ConstantRenderer.render_constant
    "binaryninja.constantrenderer.ConstantRenderer.render_constant") method will be called
    when rendering constants that aren’t pointers, while the
    [`render_constant_pointer`](#binaryninja.constantrenderer.ConstantRenderer.render_constant_pointer
    "binaryninja.constantrenderer.ConstantRenderer.render_constant_pointer") method will be
    called when rendering constant pointers. The
    [`is_valid_for_type`](#binaryninja.constantrenderer.ConstantRenderer.is_valid_for_type
    "binaryninja.constantrenderer.ConstantRenderer.is_valid_for_type") method can be
    optionally overridden to call the rendering methods only when the expression type
    matches a custom filter.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#ConstantRenderer.__init__)

    is_valid_for_type(*func: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#ConstantRenderer.is_valid_for_type)
    :   Determines if the rendering methods should be called for the given expression type. It
        is optional to override this method. If the method isn’t overridden, all expression
        types are passed to the rendering methods.

        Parameters:
        :   - **func**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) – HighLevelILFunction representing the
              high level function to be rendered
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression

        Returns:
        :   True if the constant should be passed to the rendering methods, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#ConstantRenderer.register)
    :   Registers the constant renderer.

    render_constant(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tokens: [HighLevelILTokenEmitter](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#ConstantRenderer.render_constant)
    :   Can be overridden to render a constant that is not a pointer. The expression type and
        value of the expression are given. If the expression is not handled by this constant
        renderer, this method should return False.

        To render a constant, emit the tokens to the tokens object and return True.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression
            - **tokens**
              ([*HighLevelILTokenEmitter*](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) – Token emitter for
              adding the rendered tokens
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) – Settings for rendering
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) – Operator precedence of the expression

        Returns:
        :   True if the constant was rendered, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    render_constant_pointer(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tokens: [HighLevelILTokenEmitter](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *symbol_display: [SymbolDisplayType](enums.md#binaryninja.enums.SymbolDisplayType "binaryninja.enums.SymbolDisplayType")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#ConstantRenderer.render_constant_pointer)
    :   Can be overridden to render a constant pointer. The expression type and value of the
        expression are given. If the expression is not handled by this constant renderer, this
        method should return False.

        To render a constant pointer, emit the tokens to the tokens object and return True.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression
            - **tokens**
              ([*HighLevelILTokenEmitter*](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) – Token emitter for
              adding the rendered tokens
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) – Settings for rendering
            - **symbol_display** ([*SymbolDisplayType*](enums.md#binaryninja.enums.SymbolDisplayType
              "binaryninja.enums.SymbolDisplayType")) – Type of symbol to display
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) – Operator precedence of the expression

        Returns:
        :   True if the constant was rendered, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    renderer_name *= None*

## CoreConstantRenderer

*class* CoreConstantRenderer[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#CoreConstantRenderer)
:   Bases: [`ConstantRenderer`](#binaryninja.constantrenderer.ConstantRenderer
    "binaryninja.constantrenderer.ConstantRenderer")

    __init__(*handle: BNConstantRenderer*)[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#CoreConstantRenderer.__init__)
    :   Parameters:
        :   **handle** (*BNConstantRenderer*) –

    is_valid_for_type(*func: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#CoreConstantRenderer.is_valid_for_type)
    :   Determines if the rendering methods should be called for the given expression type. It
        is optional to override this method. If the method isn’t overridden, all expression
        types are passed to the rendering methods.

        Parameters:
        :   - **func**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) – HighLevelILFunction representing the
              high level function to be rendered
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression

        Returns:
        :   True if the constant should be passed to the rendering methods, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    render_constant(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tokens: [HighLevelILTokenEmitter](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#CoreConstantRenderer.render_constant)
    :   Can be overridden to render a constant that is not a pointer. The expression type and
        value of the expression are given. If the expression is not handled by this constant
        renderer, this method should return False.

        To render a constant, emit the tokens to the tokens object and return True.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression
            - **tokens**
              ([*HighLevelILTokenEmitter*](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) – Token emitter for
              adding the rendered tokens
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) – Settings for rendering
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) – Operator precedence of the expression

        Returns:
        :   True if the constant was rendered, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    render_constant_pointer(*instr: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *val: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tokens: [HighLevelILTokenEmitter](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter "binaryninja.languagerepresentation.HighLevelILTokenEmitter")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *symbol_display: [SymbolDisplayType](enums.md#binaryninja.enums.SymbolDisplayType "binaryninja.enums.SymbolDisplayType")*, *precedence: [OperatorPrecedence](enums.md#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/constantrenderer.html#CoreConstantRenderer.render_constant_pointer)
    :   Can be overridden to render a constant pointer. The expression type and value of the
        expression are given. If the expression is not handled by this constant renderer, this
        method should return False.

        To render a constant pointer, emit the tokens to the tokens object and return True.

        Parameters:
        :   - **instr**
              ([*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) – High level expression
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – Type of
              the expression
            - **val** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Value of the expression
            - **tokens**
              ([*HighLevelILTokenEmitter*](languagerepresentation.md#binaryninja.languagerepresentation.HighLevelILTokenEmitter
              "binaryninja.languagerepresentation.HighLevelILTokenEmitter")) – Token emitter for
              adding the rendered tokens
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*) – Settings for rendering
            - **symbol_display** ([*SymbolDisplayType*](enums.md#binaryninja.enums.SymbolDisplayType
              "binaryninja.enums.SymbolDisplayType")) – Type of symbol to display
            - **precedence** ([*OperatorPrecedence*](enums.md#binaryninja.enums.OperatorPrecedence
              "binaryninja.enums.OperatorPrecedence")) – Operator precedence of the expression

        Returns:
        :   True if the constant was rendered, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
