# basedetection module

| Class | Description |
| --- | --- |
| [`binaryninja.basedetection.BaseAddressDetection`](#binaryninja.basedetection.BaseAddressDetection "binaryninja.basedetection.BaseAddressDetection") | `class BaseAddressDetection` is a class that is used to detect candidate base addresses for… |
| [`binaryninja.basedetection.BaseAddressDetectionReason`](#binaryninja.basedetection.BaseAddressDetectionReason "binaryninja.basedetection.BaseAddressDetectionReason") | `class BaseAddressDetectionReason` is a class that stores information used to understand why a… |

## BaseAddressDetection

*class* BaseAddressDetection[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BaseAddressDetection` is a class that is used to detect candidate base addresses
    for position-dependent raw binaries

    Example:
    :   ```
        >>> from binaryninja import *
        >>> bad = BaseAddressDetection("firmware.bin")
        >>> bad.detect_base_address()
        True
        >>> hex(bad.preferred_base_address)
        '0x4000000'
        ```

    __init__(*view: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.__init__)
    :   Parameters:
        :   **view** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in
            Python v3.14)") *|* [*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   *None*

    abort() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.abort)
    :   `abort` aborts base address detection analysis

        Note

        `abort` does not stop base address detection until after initial analysis has completed
        and it is in the base address enumeration phase

        Return type:
        :   *None*

    detect_base_address(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *analysis: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['basic', 'controlFlow', 'full'] = 'full'*, *min_strlen: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 10*, *alignment: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1024*, *low_boundary: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *high_boundary: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 18446744073709551615*, *poi_analysis: [BaseAddressDetectionPOISetting](enums.md#binaryninja.enums.BaseAddressDetectionPOISetting "binaryninja.enums.BaseAddressDetectionPOISetting") = BaseAddressDetectionPOISetting.POIAnalysisAll*, *max_pointers: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 128*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.detect_base_address)
    :   `detect_base_address` runs initial analysis and attempts to identify candidate base
        addresses

        Note

        This operation can take a long time to complete depending on the size and complexity of
        the binary and the settings used

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – CPU architecture of the binary (defaults to
              using auto-detection)
            - **analysis** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – analysis mode (`basic`, `controlFlow`, or `full`)
            - **min_strlen** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – minimum length of a string to be considered a point-of-interest
            - **alignment** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – byte boundary to align the base address to while brute-forcing
            - **low_boundary** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – lower boundary of the base address range to test
            - **high_boundary** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – upper boundary of the base address range to test
            - **poi_analysis**
              ([*BaseAddressDetectionPOISetting*](enums.md#binaryninja.enums.BaseAddressDetectionPOISetting
              "binaryninja.enums.BaseAddressDetectionPOISetting")) – specifies types of
              points-of-interest to use for analysis
            - **max_pointers** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – maximum number of candidate pointers to collect per pointer cluster

        Returns:
        :   True if initial analysis completed with results, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_data_hits(*base_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.get_data_hits)
    :   `get_data_hits` returns the number of times a pointer pointed to a data variable at the
        specified base address

        Parameters:
        :   **base_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) – base address to get data hits for

        Returns:
        :   number of data hits for the specified base address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_function_hits(*base_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.get_function_hits)
    :   `get_function_hits` returns the number of times a pointer pointed to a function at the
        specified base address

        Parameters:
        :   **base_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) – base address to get function hits for

        Returns:
        :   number of function hits for the specified base address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_reasons(*base_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[BaseAddressDetectionReason](#binaryninja.basedetection.BaseAddressDetectionReason "binaryninja.basedetection.BaseAddressDetectionReason")][[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.get_reasons)
    :   `get_reasons` returns a list of reasons that can be used to determine why a base address
        is a candidate

        Parameters:
        :   **base_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) – base address to get reasons for

        Returns:
        :   list of reasons for the specified base address

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*BaseAddressDetectionReason*](#binaryninja.basedetection.BaseAddressDetectionReason
            "binaryninja.basedetection.BaseAddressDetectionReason")]

    get_string_hits(*base_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetection.get_string_hits)
    :   `get_string_hits` returns the number of times a pointer pointed to a string at the
        specified base address

        Note

        Data variables are only used as points-of-interest if analysis doesn’t discover enough
        strings and functions

        Parameters:
        :   **base_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) – base address to get string hits for

        Returns:
        :   number of string hits for the specified base address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    *property* aborted*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   `aborted` indicates whether or not base address detection analysis was aborted early

        Returns:
        :   True if the analysis was aborted, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* confidence*: [BaseAddressDetectionConfidence](enums.md#binaryninja.enums.BaseAddressDetectionConfidence "binaryninja.enums.BaseAddressDetectionConfidence")*
    :   `confidence` returns an enum that indicates confidence the preferred candidate base
        address is correct

        Returns:
        :   confidence of the base address detection results

        Return type:
        :   [*BaseAddressDetectionConfidence*](enums.md#binaryninja.enums.BaseAddressDetectionConfidence
            "binaryninja.enums.BaseAddressDetectionConfidence")

    *property* last_tested_base_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   `last_tested_base_address` returns the last candidate base address that was tested

        Note

        This is useful for situations where the user aborts the analysis and wants to restart
        from the last tested base address by setting the `low_boundary` parameter in
        [`BaseAddressDetection.detect_base_address`](#binaryninja.basedetection.BaseAddressDetection.detect_base_address
        "binaryninja.basedetection.BaseAddressDetection.detect_base_address")

        Returns:
        :   last candidate base address tested

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    *property* preferred_base_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   `preferred_base_address` returns the candidate base address which contains the most
        amount of pointers that align with discovered points-of-interest in the binary

        Note

        [`BaseAddressDetection.confidence`](#binaryninja.basedetection.BaseAddressDetection.confidence
        "binaryninja.basedetection.BaseAddressDetection.confidence") reports a confidence level
        that the preferred base is correct

        Note

        [`BaseAddressDetection.scores`](#binaryninja.basedetection.BaseAddressDetection.scores
        "binaryninja.basedetection.BaseAddressDetection.scores") returns a list of the top 10
        candidate base addresses and their scores and can be used to discover other potential
        candidates

        Returns:
        :   preferred candidate base address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    *property* scores*: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*
    :   `scores` returns a list of candidate base addresses and their scores

        Note

        The score is set to the number of times a pointer pointed to a point-of-interest at that
        base address

        Example:
        :   ```
            >>> from binaryninja import *
            >>> bad = BaseAddressDetection("firmware.bin")
            >>> bad.detect_base_address()
            True
            >>> for addr, score in bad.scores:
            ...     print(f"0x{addr:x}: {score}")
            ...
            0x4000000: 7
            0x400dc00: 1
            0x400d800: 1
            0x400cc00: 1
            0x400c400: 1
            0x400bc00: 1
            0x400b800: 1
            0x3fffc00: 1
            ```

        Returns:
        :   list of tuples containing each base address and score

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]]

## BaseAddressDetectionReason

*class* BaseAddressDetectionReason[[source]](https://api.binary.ninja/_modules/binaryninja/basedetection.html#BaseAddressDetectionReason)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BaseAddressDetectionReason` is a class that stores information used to understand
    why a base address is a candidate. It consists of a pointer, the offset of the
    point-of-interest that the pointer aligns with, and the type of point-of-interest
    (string, function, or data variable)

    __init__(*pointer: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [BaseAddressDetectionPOIType](enums.md#binaryninja.enums.BaseAddressDetectionPOIType "binaryninja.enums.BaseAddressDetectionPOIType")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **pointer** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type**
              ([*BaseAddressDetectionPOIType*](enums.md#binaryninja.enums.BaseAddressDetectionPOIType
              "binaryninja.enums.BaseAddressDetectionPOIType")) –

        Return type:
        :   *None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    pointer*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [BaseAddressDetectionPOIType](enums.md#binaryninja.enums.BaseAddressDetectionPOIType "binaryninja.enums.BaseAddressDetectionPOIType")*
