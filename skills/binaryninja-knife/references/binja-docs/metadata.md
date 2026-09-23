# metadata module

| Class | Description |
| --- | --- |
| [`binaryninja.metadata.Metadata`](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") |  |

## Metadata

*class* Metadata[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*value: [Metadata](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Metadata](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Metadata](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *signed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *raw: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: BNMetadata | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata.__init__)
    :   The ‘raw’ parameter is no longer needed it was a workaround for a Python 2 limitation.
        To pass raw data into this API, simply use a bytes object.

        Parameters:
        :   - **value** ([*Metadata*](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata")
              *|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
              *|* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
              *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") *|*
              [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
              *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*Metadata*](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata")
              *|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
              *|* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
              *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") *|*
              [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
              *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**MetadataValueType**]* *|*
              [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
              v3.14)")*[**MetadataValueType**]* *|*
              [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*]*
              *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
              v3.14)")*[*[*Metadata*](#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata")
              *|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
              *|* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
              *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") *|*
              [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
              *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**MetadataValueType**]* *|*
              [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
              v3.14)")*[**MetadataValueType**]* *|*
              [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*]*
              *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
              *|* *None*)
            - **signed** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* *None*)
            - **raw** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* *None*)
            - **handle** (*BNMetadata* *|* *None*)

    append(*value*)[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata.append)
    :   Appends a value to the Metadata array.

    get(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata.get)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)"))

        Return type:
        :   [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")

    get_dict()[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata.get_dict)

    get_json_string()[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata.get_json_string)

    remove(*key_or_index*)[[source]](https://api.binary.ninja/_modules/binaryninja/metadata.html#Metadata.remove)

    *property* is_array

    *property* is_boolean

    *property* is_bytes

    *property* is_dict

    *property* is_float

    *property* is_integer

    *property* is_raw
    :   deprecated in favor of is_bytes

    *property* is_signed_integer

    *property* is_string

    *property* is_unsigned_integer

    *property* type

    *property* value
