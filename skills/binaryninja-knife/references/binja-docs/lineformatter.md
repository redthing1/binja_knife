# lineformatter module

| Class | Description |
| --- | --- |
| [`binaryninja.lineformatter.CoreLineFormatter`](#binaryninja.lineformatter.CoreLineFormatter "binaryninja.lineformatter.CoreLineFormatter") | `class LineFormatter` represents a custom line formatter, which can reformat code in High… |
| [`binaryninja.lineformatter.LineFormatter`](#binaryninja.lineformatter.LineFormatter "binaryninja.lineformatter.LineFormatter") | `class LineFormatter` represents a custom line formatter, which can reformat code in High… |
| [`binaryninja.lineformatter.LineFormatterSettings`](#binaryninja.lineformatter.LineFormatterSettings "binaryninja.lineformatter.LineFormatterSettings") |  |

## CoreLineFormatter

*class* CoreLineFormatter[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#CoreLineFormatter)
:   Bases: [`LineFormatter`](#binaryninja.lineformatter.LineFormatter
    "binaryninja.lineformatter.LineFormatter")

    __init__(*handle: BNLineFormatter*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#CoreLineFormatter.__init__)
    :   Parameters:
        :   **handle** (*BNLineFormatter*)

    format_lines(*in_lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*, *settings: [LineFormatterSettings](#binaryninja.lineformatter.LineFormatterSettings "binaryninja.lineformatter.LineFormatterSettings")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#CoreLineFormatter.format_lines)
    :   Reformats the given list of lines. Returns a new list of lines containing the
        reformatted code.

        Parameters:
        :   - **in_lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*)
            - **settings** ([*LineFormatterSettings*](#binaryninja.lineformatter.LineFormatterSettings
              "binaryninja.lineformatter.LineFormatterSettings"))

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

## LineFormatter

*class* LineFormatter[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatter)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class LineFormatter` represents a custom line formatter, which can reformat code in
    High Level IL and high level language representations.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatter.__init__)

    format_lines(*in_lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*, *settings: [LineFormatterSettings](#binaryninja.lineformatter.LineFormatterSettings "binaryninja.lineformatter.LineFormatterSettings")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatter.format_lines)
    :   Reformats the given list of lines. Returns a new list of lines containing the
        reformatted code.

        Parameters:
        :   - **in_lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*)
            - **settings** ([*LineFormatterSettings*](#binaryninja.lineformatter.LineFormatterSettings
              "binaryninja.lineformatter.LineFormatterSettings"))

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatter.register)
    :   Registers the line formatter.

    formatter_name *= None*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## LineFormatterSettings

*class* LineFormatterSettings[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatterSettings)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*hlil: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *desired_line_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *minimum_content_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tab_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *language_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *comment_start_string: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *comment_end_string: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *annotation_start_string: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *annotation_end_string: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **hlil**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))
            - **desired_line_length** ([*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)"))
            - **minimum_content_length** ([*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)"))
            - **tab_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **language_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* *None*)
            - **comment_start_string** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)"))
            - **comment_end_string** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **annotation_start_string** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)"))
            - **annotation_end_string** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)"))

        Return type:
        :   *None*

    *static* default(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *hlil: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*) → [LineFormatterSettings](#binaryninja.lineformatter.LineFormatterSettings "binaryninja.lineformatter.LineFormatterSettings")[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatterSettings.default)
    :   Gets the default line formatter settings for High Level IL code.

        Parameters:
        :   - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*)
            - **hlil**
              ([*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction"))

        Return type:
        :   [*LineFormatterSettings*](#binaryninja.lineformatter.LineFormatterSettings
            "binaryninja.lineformatter.LineFormatterSettings")

    *static* language_representation_settings(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *func: [LanguageRepresentationFunction](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction "binaryninja.languagerepresentation.LanguageRepresentationFunction")*) → [LineFormatterSettings](#binaryninja.lineformatter.LineFormatterSettings "binaryninja.lineformatter.LineFormatterSettings")[[source]](https://api.binary.ninja/_modules/binaryninja/lineformatter.html#LineFormatterSettings.language_representation_settings)
    :   Gets the default line formatter settings for a language representation function.

        Parameters:
        :   - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") *|* *None*)
            - **func**
              ([*LanguageRepresentationFunction*](languagerepresentation.md#binaryninja.languagerepresentation.LanguageRepresentationFunction
              "binaryninja.languagerepresentation.LanguageRepresentationFunction"))

        Return type:
        :   [*LineFormatterSettings*](#binaryninja.lineformatter.LineFormatterSettings
            "binaryninja.lineformatter.LineFormatterSettings")

    annotation_end_string*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    annotation_start_string*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    comment_end_string*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    comment_start_string*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    desired_line_length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    hlil*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    language_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    minimum_content_length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    tab_width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
