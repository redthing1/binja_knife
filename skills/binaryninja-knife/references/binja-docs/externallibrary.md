# externallibrary module

| Class | Description |
| --- | --- |
| [`binaryninja.externallibrary.ExternalLibrary`](#binaryninja.externallibrary.ExternalLibrary "binaryninja.externallibrary.ExternalLibrary") | An ExternalLibrary is an abstraction for a library that is optionally backed by a ProjectFile. |
| [`binaryninja.externallibrary.ExternalLocation`](#binaryninja.externallibrary.ExternalLocation "binaryninja.externallibrary.ExternalLocation") | An ExternalLocation is an association from a source symbol in a binary view to a target symbol… |

## ExternalLibrary

*class* ExternalLibrary[[source]](https://api.binary.ninja/_modules/binaryninja/externallibrary.html#ExternalLibrary)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    An ExternalLibrary is an abstraction for a library that is optionally backed by a
    ProjectFile.

    __init__(*handle: BNExternalLibrary*)[[source]](https://api.binary.ninja/_modules/binaryninja/externallibrary.html#ExternalLibrary.__init__)
    :   Parameters:
        :   **handle** (*BNExternalLibrary*) –

    *property* backing_file*: [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the file backing this external library

        Returns:
        :   The file backing this external library or None

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the name of this external library

        Returns:
        :   The name of this external library

## ExternalLocation

*class* ExternalLocation[[source]](https://api.binary.ninja/_modules/binaryninja/externallibrary.html#ExternalLocation)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    An ExternalLocation is an association from a source symbol in a binary view to a target
    symbol and/or address in an ExternalLibrary.

    __init__(*handle: BNExternalLocation*)[[source]](https://api.binary.ninja/_modules/binaryninja/externallibrary.html#ExternalLocation.__init__)
    :   Parameters:
        :   **handle** (*BNExternalLocation*) –

    *property* has_target_address*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this ExternalLocation has a target address

        Returns:
        :   True is this ExternalLocation has a target address, False otherwise

    *property* has_target_symbol*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this ExternalLocation has a target symbol

        Returns:
        :   True is this ExternalLocation has a target symbol, False otherwise

    *property* library*: [ExternalLibrary](#binaryninja.externallibrary.ExternalLibrary "binaryninja.externallibrary.ExternalLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the ExternalLibrary that this ExternalLocation targets

        Returns:
        :   The ExternalLibrary pointed in to by this ExternalLocation if one exists, None otherwise

    *property* source_symbol*: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*
    :   Get the source symbol for this ExternalLocation

        Returns:
        :   The source symbol for this ExternalLocation

    *property* target_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the address pointed to by this ExternalLocation

        Returns:
        :   The address pointed to by this ExternalLocation if one exists, None otherwise

    *property* target_symbol*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the symbol pointed to by this ExternalLocation

        Returns:
        :   The symbol pointed to by this ExternalLocation if one exists, None otherwise
