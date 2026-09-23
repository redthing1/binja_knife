# databuffer module

| Class | Description |
| --- | --- |
| [`binaryninja.databuffer.DataBuffer`](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.databuffer.escape_string`](#binaryninja.databuffer.escape_string "binaryninja.databuffer.escape_string") |  |
| [`binaryninja.databuffer.unescape_string`](#binaryninja.databuffer.unescape_string "binaryninja.databuffer.unescape_string") |  |

## DataBuffer

*class* DataBuffer[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [DataBuffer](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = b''*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.__init__)
    :   Parameters:
        :   **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
            v3.14)") *|* [*DataBuffer*](#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer") *|*
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"))

    base64_decode() → [DataBuffer](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.base64_decode)
    :   Return type:
        :   [*DataBuffer*](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")

    base64_encode() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.base64_encode)
    :   Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    escape(*null_terminates=False*, *escape_printable=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.escape)
    :   Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    unescape() → [DataBuffer](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.unescape)
    :   Return type:
        :   [*DataBuffer*](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")

    zlib_compress() → [DataBuffer](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.zlib_compress)
    :   Return type:
        :   [*DataBuffer*](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") |
            *None*

    zlib_decompress() → [DataBuffer](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#DataBuffer.zlib_decompress)
    :   Return type:
        :   [*DataBuffer*](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") |
            *None*

## escape_string

escape_string(*text: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#escape_string)
:   Parameters:
    :   **text** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
        v3.14)"))

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## unescape_string

unescape_string(*text: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [DataBuffer](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/databuffer.html#unescape_string)
:   Parameters:
    :   **text** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
        v3.14)"))

    Return type:
    :   [*DataBuffer*](#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")
