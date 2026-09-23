# fileaccessor module

| Class | Description |
| --- | --- |
| [`binaryninja.fileaccessor.CoreFileAccessor`](#binaryninja.fileaccessor.CoreFileAccessor "binaryninja.fileaccessor.CoreFileAccessor") |  |
| [`binaryninja.fileaccessor.FileAccessor`](#binaryninja.fileaccessor.FileAccessor "binaryninja.fileaccessor.FileAccessor") |  |

## CoreFileAccessor

*class* CoreFileAccessor[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#CoreFileAccessor)
:   Bases: [`FileAccessor`](#binaryninja.fileaccessor.FileAccessor
    "binaryninja.fileaccessor.FileAccessor")

    __init__(*accessor*)[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#CoreFileAccessor.__init__)

    get_length()[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#CoreFileAccessor.get_length)

    read(*offset*, *length*)[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#CoreFileAccessor.read)

    write(*offset*, *value*)[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#CoreFileAccessor.write)

## FileAccessor

*class* FileAccessor[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#FileAccessor)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#FileAccessor.__init__)

    get_length()[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#FileAccessor.get_length)

    read(*offset*, *length*)[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#FileAccessor.read)

    write(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/fileaccessor.html#FileAccessor.write)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)"))
