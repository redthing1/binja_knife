# unicode module

| Function | Description |
| --- | --- |
| [`binaryninja.unicode.escape_unicode_string`](#binaryninja.unicode.escape_unicode_string "binaryninja.unicode.escape_unicode_string") | Escapes a string for display, passing through any text that decodes to a codepoint in one of the… |
| [`binaryninja.unicode.unicode_display_width`](#binaryninja.unicode.unicode_display_width "binaryninja.unicode.unicode_display_width") | Width of a string in character cells, following Unicode Standard Annex #11 (East Asian Width). |

## escape_unicode_string

escape_unicode_string(*data: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/unicode.html#escape_unicode_string)
:   Escapes a string for display, passing through any text that decodes to a codepoint in
    one of the enabled Unicode blocks as unaltered UTF-8.

    Which blocks are enabled is controlled by the `analysis.unicode.blocks` setting,
    resolved against `view` when one is given. Passthrough additionally requires
    `analysis.unicode.utf8` to be enabled. Everything else is escaped, including bytes
    belonging to a truncated or otherwise invalid encoding, so `data` need not be valid
    UTF-8.

    This is the escaping used when rendering string contents in HLIL, Pseudo C and Pseudo
    Rust.

    Parameters:
    :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
          v3.14)") *|* [*bytearray*](https://docs.python.org/3/library/stdtypes.html#bytearray
          "(in Python v3.14)")) – string or raw bytes to escape
        - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
          "binaryninja.binaryview.BinaryView") *|* *None*) – view whose settings select the
          enabled blocks, or None to use the global settings

    Returns:
    :   the escaped string

    Example:
    :   ```
        >>> Settings().set_string_list("analysis.unicode.blocks", ["Hiragana"], bv)
        True
        >>> escape_unicode_string("Unicode: \u3053\u3093\u306b\u3061\u306f", bv)
        'Unicode: こんにちは'
        >>> escape_unicode_string(b"\xff\xfe", bv)
        '\\xff\\xfe'
        ```

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## unicode_display_width

unicode_display_width(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/unicode.html#unicode_display_width)
:   Width of a string in character cells, following Unicode Standard Annex #11 (East Asian
    Width).

    Wide and fullwidth codepoints, such as CJK ideographs and kana, occupy two cells;
    combining marks and other zero width codepoints occupy none; everything else occupies
    one.

    Binary Ninja renders text on a fixed character cell grid, so this, rather than a
    character count, is the measurement that `InstructionTextToken.width` is expressed in.

    Parameters:
    :   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – string to measure

    Returns:
    :   width of the string in character cells

    Example:
    :   ```
        >>> display_width("hello")
        5
        >>> display_width("\u3053\u3093\u306b\u3061\u306f")
        10
        ```

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
