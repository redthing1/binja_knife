# firmwareninja module

| Class | Description |
| --- | --- |
| [`binaryninja.firmwareninja.FirmwareNinja`](#binaryninja.firmwareninja.FirmwareNinja "binaryninja.firmwareninja.FirmwareNinja") | `class FirmwareNinja` is a class that aids in analysis of firmware binaries. This class is… |
| [`binaryninja.firmwareninja.FirmwareNinjaDevice`](#binaryninja.firmwareninja.FirmwareNinjaDevice "binaryninja.firmwareninja.FirmwareNinjaDevice") | `class FirmwareNinjaDevice` is a class that stores information about a hardware device,… |
| [`binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses`](#binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses "binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses") | `class FirmwareNinjaDeviceAccesses` is a class that stores information on the number of… |
| [`binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses`](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses") | `class FirmwareNinjaFunctionMemoryAccesses` is a class that stores information on accesses… |
| [`binaryninja.firmwareninja.FirmwareNinjaMemoryAccess`](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess") | `class FirmwareNinjaMemoryAccess` is a class that stores information on instructions that… |
| [`binaryninja.firmwareninja.FirmwareNinjaReferenceNode`](#binaryninja.firmwareninja.FirmwareNinjaReferenceNode "binaryninja.firmwareninja.FirmwareNinjaReferenceNode") | `class FirmwareNinjaReferenceNode` is a class for building reference trees for functions, data… |
| [`binaryninja.firmwareninja.FirmwareNinjaRelationship`](#binaryninja.firmwareninja.FirmwareNinjaRelationship "binaryninja.firmwareninja.FirmwareNinjaRelationship") | `class FirmwareNinjaRelationship` is a class for representing inter-binary and cross-binary… |
| [`binaryninja.firmwareninja.FirmwareNinjaSection`](#binaryninja.firmwareninja.FirmwareNinjaSection "binaryninja.firmwareninja.FirmwareNinjaSection") | `class FirmwareNinjaSection` is a class that stores information about a section identified… |

## FirmwareNinja

*class* FirmwareNinja[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinja` is a class that aids in analysis of firmware binaries. This class
    is only available in the Ultimate Edition of Binary Ninja.

    Example:
    :   ```
        >>> from binaryninja import *
        >>> view = load("path/to/firmware.bin", options={"loader.imageBase": 0x100000})
        >>> fwn = FirmwareNinja(view)
        >>> fwn.get_function_memory_accesses()[0].accesses[0].mem_address
        <const ptr 0x40090028>
        ```

    __init__(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.__init__)
    :   Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   *None*

    add_relationship(*relationship: [FirmwareNinjaRelationship](#binaryninja.firmwareninja.FirmwareNinjaRelationship "binaryninja.firmwareninja.FirmwareNinjaRelationship")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.add_relationship)
    :   `add_relationship` adds a relationship to the binary view metadata

        Parameters:
        :   **relationship**
            ([*FirmwareNinjaRelationship*](#binaryninja.firmwareninja.FirmwareNinjaRelationship
            "binaryninja.firmwareninja.FirmwareNinjaRelationship")) – Relationship to add

        Return type:
        :   *None*

    get_board_device_accesses(*fma: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaFunctionMemoryAccesses](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaDeviceAccesses](#binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses "binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses")][[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.get_board_device_accesses)
    :   `get_board_device_accesses` counts accesses made to memory-mapped hardware devices for
        each board that is compatible with the current architecture. This function can be used
        to help identify a board.

        Example:
        :   ```
            >>> fwn = FirmwareNinja(bv)
            >>> fma = fwn.get_function_memory_accesses()
            >>> fwn.get_board_device_accesses(fma)[0]
            FirmwareNinjaDeviceAccesses(board_name='stm32mp157c-dhcom-picoitx', total=414, unique=2)
            ```

        Parameters:
        :   **fma** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*[*[*FirmwareNinjaFunctionMemoryAccesses*](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses
            "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")*]*) – List of function
            memory accesses

        Returns:
        :   List of device accesses

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaDeviceAccesses*](#binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses
            "binaryninja.firmwareninja.FirmwareNinjaDeviceAccesses")]

    get_devices_for_board(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaDevice](#binaryninja.firmwareninja.FirmwareNinjaDevice "binaryninja.firmwareninja.FirmwareNinjaDevice")][[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.get_devices_for_board)
    :   `get_devices_for_board` queries the hardware device information for a specific board

        Example:
        :   ```
            >>> fwn = FirmwareNinja(bv)
            >>> fwn.get_devices_for_board(fwn.boards[0])[0]
            FirmwareNinjaDevice(name='nand@12f', start=303, size=1024, info='marvell,orion-nand')
            ```

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the board

        Returns:
        :   List of Firmware Ninja devices

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaDevice*](#binaryninja.firmwareninja.FirmwareNinjaDevice
            "binaryninja.firmwareninja.FirmwareNinjaDevice")]

    get_function_memory_accesses(*progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaFunctionMemoryAccesses](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")][[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.get_function_memory_accesses)
    :   `get_function_memory_accesses` runs analysis to find accesses to memory regions that are
        not file-backed, such as memory-mapped I/O and RAM

        Parameters:
        :   **progress_func** (*callback*) – optional function to be called with the current
            progress and total count.

        Returns:
        :   List of function memory accesses

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaFunctionMemoryAccesses*](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses
            "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")]

    get_reference_tree(*location: [Section](binaryview.md#binaryninja.binaryview.Section "binaryninja.binaryview.Section") | [FirmwareNinjaDevice](#binaryninja.firmwareninja.FirmwareNinjaDevice "binaryninja.firmwareninja.FirmwareNinjaDevice") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [DataVariable](binaryview.md#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *fma: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaFunctionMemoryAccesses](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")]*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [FirmwareNinjaReferenceNode](#binaryninja.firmwareninja.FirmwareNinjaReferenceNode "binaryninja.firmwareninja.FirmwareNinjaReferenceNode")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.get_reference_tree)
    :   `get_reference_tree` returns a tree of reference nodes for a memory region, function, or
        address

        Parameters:
        :   - **location** ([*Section*](binaryview.md#binaryninja.binaryview.Section
              "binaryninja.binaryview.Section") *|*
              [*FirmwareNinjaDevice*](#binaryninja.firmwareninja.FirmwareNinjaDevice
              "binaryninja.firmwareninja.FirmwareNinjaDevice") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* [*DataVariable*](binaryview.md#binaryninja.binaryview.DataVariable
              "binaryninja.binaryview.DataVariable") *|*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) –
              Memory location to build the reference tree for
            - **fma** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*[*[*FirmwareNinjaFunctionMemoryAccesses*](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses
              "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")*]*) – List of function
              memory accesses or None to use cross references. None should only be supplied if
              location is a Function, DataVariable, or address.
            - **value** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)")*]*) – Only include the node in the tree if this value is written to
              the location
            - **location** –

        Returns:
        :   Root reference node containing the reference tree

        Return type:
        :   [*FirmwareNinjaReferenceNode*](#binaryninja.firmwareninja.FirmwareNinjaReferenceNode
            "binaryninja.firmwareninja.FirmwareNinjaReferenceNode")

    get_relationship_by_guid(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [FirmwareNinjaRelationship](#binaryninja.firmwareninja.FirmwareNinjaRelationship "binaryninja.firmwareninja.FirmwareNinjaRelationship")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.get_relationship_by_guid)
    :   `get_relationship_by_guid` queries a relationship from the binary view metadata by GUID

        Parameters:
        :   **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – GUID of the relationship

        Returns:
        :   Relationship

        Return type:
        :   [*FirmwareNinjaRelationship*](#binaryninja.firmwareninja.FirmwareNinjaRelationship
            "binaryninja.firmwareninja.FirmwareNinjaRelationship")

    get_sections_from_entropy(*high_code_entropy_threshold: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.91*, *low_code_entropy_threshold: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.5*, *block_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 4096*, *mode: [FirmwareNinjaSectionAnalysisMode](enums.md#binaryninja.enums.FirmwareNinjaSectionAnalysisMode "binaryninja.enums.FirmwareNinjaSectionAnalysisMode") = FirmwareNinjaSectionAnalysisMode.DetectStringsSectionAnalysisMode*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaSection](#binaryninja.firmwareninja.FirmwareNinjaSection "binaryninja.firmwareninja.FirmwareNinjaSection")][[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.get_sections_from_entropy)
    :   `get_sections_from_entropy` uses entropy analysis and heuristics to identify code, data,
        padding, and compressed sections in the file-backed regions of the binary view

        Example:
        :   ```
            >>> fwn = FirmwareNinja(bv)
            >>> fwn.get_sections_from_entropy(block_size=2048)[0].entropy
            0.48716872930526733
            >>> fwn.get_sections_from_entropy(block_size=2048)[0].type
            <FirmwareNinjaSectionType.DataSectionType: 1>
            ```

        Parameters:
        :   - **high_code_entropy_threshold**
              ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"))
              – High code entropy threshold
            - **low_code_entropy_threshold**
              ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"))
              – Low code entropy threshold
            - **block_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Block size
            - **mode**
              ([*FirmwareNinjaSectionAnalysisMode*](enums.md#binaryninja.enums.FirmwareNinjaSectionAnalysisMode
              "binaryninja.enums.FirmwareNinjaSectionAnalysisMode")) – Analysis mode

        Returns:
        :   List of sections

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaSection*](#binaryninja.firmwareninja.FirmwareNinjaSection
            "binaryninja.firmwareninja.FirmwareNinjaSection")]

    query_function_memory_accesses() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaFunctionMemoryAccesses](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")][[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.query_function_memory_accesses)
    :   `query_function_memory_accesses` queries information on function memory accesses from
        binary view metadata

        Returns:
        :   List of function memory accesses

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaFunctionMemoryAccesses*](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses
            "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")]

    remove_custom_device(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.remove_custom_device)
    :   `remove_custom_device` removes a user-defined Firmware Ninja device from the binary view
        metadata by device name

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the device

        Returns:
        :   True on success, False on failure

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_relationship_by_guid(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.remove_relationship_by_guid)
    :   `remove_relationship_by_guid` removes a relationship from the binary view metadata by
        GUID

        Parameters:
        :   **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – GUID of the relationship

        Return type:
        :   *None*

    store_custom_device(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *info: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.store_custom_device)
    :   `store_custom_device` stores a user-defined Firmware Ninja device in the binary view
        metadata

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the device
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Start address of the device
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Size of the device memory region
            - **info** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Information about the device

        Returns:
        :   True on success, False on failure

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    store_function_memory_accesses(*fma: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaFunctionMemoryAccesses](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinja.store_function_memory_accesses)
    :   `store_function_memory_accesses` saves information on function memory accesses to binary
        view metadata

        Example:
        :   ```
            >>> fwn = FirmwareNinja(bv)
            >>> fma = fwn.get_function_memory_accesses()
            >>> fwn.store_function_memory_accesses(fma)
            ```

        Parameters:
        :   **fma** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*[*[*FirmwareNinjaFunctionMemoryAccesses*](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses
            "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")*]*) – List of function
            memory accesses

        Return type:
        :   *None*

    *property* boards*: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   `boards` queries the name of all boards that are compatible with the current
        architecture

        Returns:
        :   List of board names

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    *property* relationships*: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaRelationship](#binaryninja.firmwareninja.FirmwareNinjaRelationship "binaryninja.firmwareninja.FirmwareNinjaRelationship")]*
    :   `relationships` queries all Firmware Ninja relationships from the binary view metadata

        Returns:
        :   List of relationships

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaRelationship*](#binaryninja.firmwareninja.FirmwareNinjaRelationship
            "binaryninja.firmwareninja.FirmwareNinjaRelationship")]

    *property* user_devices*: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaDevice](#binaryninja.firmwareninja.FirmwareNinjaDevice "binaryninja.firmwareninja.FirmwareNinjaDevice")]*
    :   `user_devices` queries user-defined Firmware Ninja devices from the binary view metadata

        Returns:
        :   List of Firmware Ninja devices

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaDevice*](#binaryninja.firmwareninja.FirmwareNinjaDevice
            "binaryninja.firmwareninja.FirmwareNinjaDevice")]

## FirmwareNinjaDevice

*class* FirmwareNinjaDevice[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaDevice)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinjaDevice` is a class that stores information about a hardware device,
    including the device name, start address, size, and information about the device. This
    class is only available in the Ultimate Edition of Binary Ninja.

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *info: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **info** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    info*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## FirmwareNinjaDeviceAccesses

*class* FirmwareNinjaDeviceAccesses[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaDeviceAccesses)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinjaDeviceAccesses` is a class that stores information on the number of
    accesses to hardware devices for each board that is compatible with the current
    architecture. This information can be used to identify a board based on the number of
    accesses to hardware devices. This class is only available in the Ultimate Edition of
    Binary Ninja.

    __init__(*board_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *total: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *unique: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **board_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **total** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **unique** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    board_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    total*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    unique*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## FirmwareNinjaFunctionMemoryAccesses

*class* FirmwareNinjaFunctionMemoryAccesses[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaFunctionMemoryAccesses)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinjaFunctionMemoryAccesses` is a class that stores information on
    accesses made by a function to memory regions that are not file-backed, such as
    memory-mapped I/O and RAM. This class is only available in the Ultimate Edition of
    Binary Ninja.

    __init__(*function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *accesses: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaMemoryAccess](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **accesses** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*[*[*FirmwareNinjaMemoryAccess*](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess
              "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")*]*) –

        Return type:
        :   *None*

    *classmethod* from_BNFirmwareNinjaFunctionMemoryAccesses(*info: BNFirmwareNinjaFunctionMemoryAccesses*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [FirmwareNinjaFunctionMemoryAccesses](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaFunctionMemoryAccesses.from_BNFirmwareNinjaFunctionMemoryAccesses)
    :   Parameters:
        :   - **info** (*BNFirmwareNinjaFunctionMemoryAccesses*) –
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*FirmwareNinjaFunctionMemoryAccesses*](#binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses
            "binaryninja.firmwareninja.FirmwareNinjaFunctionMemoryAccesses")

    accesses*: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaMemoryAccess](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")]*

    function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*

## FirmwareNinjaMemoryAccess

*class* FirmwareNinjaMemoryAccess[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaMemoryAccess)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinjaMemoryAccess` is a class that stores information on instructions
    that access regions of memory that are not file-backed, such as memory-mapped I/O and
    RAM. This class is only available in the Ultimate Edition of Binary Ninja.

    __init__(*instr_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *mem_address: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*, *heuristic: [FirmwareNinjaMemoryHeuristic](enums.md#binaryninja.enums.FirmwareNinjaMemoryHeuristic "binaryninja.enums.FirmwareNinjaMemoryHeuristic")*, *type: [FirmwareNinjaMemoryAccessType](enums.md#binaryninja.enums.FirmwareNinjaMemoryAccessType "binaryninja.enums.FirmwareNinjaMemoryAccessType")*, *value: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **instr_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **mem_address** ([*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
              "binaryninja.variable.RegisterValue")) –
            - **heuristic**
              ([*FirmwareNinjaMemoryHeuristic*](enums.md#binaryninja.enums.FirmwareNinjaMemoryHeuristic
              "binaryninja.enums.FirmwareNinjaMemoryHeuristic")) –
            - **type**
              ([*FirmwareNinjaMemoryAccessType*](enums.md#binaryninja.enums.FirmwareNinjaMemoryAccessType
              "binaryninja.enums.FirmwareNinjaMemoryAccessType")) –
            - **value** ([*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
              "binaryninja.variable.RegisterValue")) –

        Return type:
        :   *None*

    *classmethod* from_BNFirmwareNinjaMemoryAccess(*access: BNFirmwareNinjaMemoryAccess*) → [FirmwareNinjaMemoryAccess](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaMemoryAccess.from_BNFirmwareNinjaMemoryAccess)
    :   Parameters:
        :   **access** (*BNFirmwareNinjaMemoryAccess*) –

        Return type:
        :   [*FirmwareNinjaMemoryAccess*](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess
            "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")

    *classmethod* to_BNFirmwareNinjaMemoryAccess(*access: [FirmwareNinjaMemoryAccess](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")*) → BNFirmwareNinjaMemoryAccess[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaMemoryAccess.to_BNFirmwareNinjaMemoryAccess)
    :   Parameters:
        :   **access**
            ([*FirmwareNinjaMemoryAccess*](#binaryninja.firmwareninja.FirmwareNinjaMemoryAccess
            "binaryninja.firmwareninja.FirmwareNinjaMemoryAccess")) –

        Return type:
        :   *BNFirmwareNinjaMemoryAccess*

    heuristic*: [FirmwareNinjaMemoryHeuristic](enums.md#binaryninja.enums.FirmwareNinjaMemoryHeuristic "binaryninja.enums.FirmwareNinjaMemoryHeuristic")*

    instr_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    mem_address*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*

    type*: [FirmwareNinjaMemoryAccessType](enums.md#binaryninja.enums.FirmwareNinjaMemoryAccessType "binaryninja.enums.FirmwareNinjaMemoryAccessType")*

    value*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*

## FirmwareNinjaReferenceNode

*class* FirmwareNinjaReferenceNode[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaReferenceNode)
:   Bases: [`object`](#binaryninja.firmwareninja.FirmwareNinjaReferenceNode.object
    "binaryninja.firmwareninja.FirmwareNinjaReferenceNode.object")

    `class FirmwareNinjaReferenceNode` is a class for building reference trees for
    functions, data variables, and memory regions. This class is only available in the
    Ultimate Edition of Binary Ninja.

    __init__(*handle=None*, *view=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaReferenceNode.__init__)

    *property* children*: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FirmwareNinjaReferenceNode](#binaryninja.firmwareninja.FirmwareNinjaReferenceNode "binaryninja.firmwareninja.FirmwareNinjaReferenceNode")]*
    :   `children` returns the child nodes contained in the reference tree node

        Returns:
        :   Child nodes contained in the reference tree node

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*FirmwareNinjaReferenceNode*](#binaryninja.firmwareninja.FirmwareNinjaReferenceNode
            "binaryninja.firmwareninja.FirmwareNinjaReferenceNode")]

    *property* object*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [DataVariable](binaryview.md#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*
    :   `object` returns the function or data variable contained in the reference tree node, or
        None if the object is a root node and only contains children

        Returns:
        :   Object contained in the reference tree node

        Return type:
        :   *Union*[[*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function"),
            [*DataVariable*](binaryview.md#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")]

## FirmwareNinjaRelationship

*class* FirmwareNinjaRelationship[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaRelationship)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinjaRelationship` is a class for representing inter-binary and
    cross-binary relationships. This class is only available in the Ultimate Edition of
    Binary Ninja.

    __init__(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *handle=None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaRelationship.__init__)
    :   Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   *None*

    *property* description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   `description` returns the description of the relationship

        Returns:
        :   Description of the relationship

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *property* guid*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   `guid` returns the GUID of the relationship

        Returns:
        :   GUID of the relationship

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *property* primary*: [DataVariable](binaryview.md#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   `primary` returns the primary function, data variable, or address of the relationship

        Returns:
        :   Primary object of the relationship

        Return type:
        :   *Union*[[*DataVariable*](binaryview.md#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable"),
            [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]

    *property* provenance*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   `provenance` returns the provenance of the relationship

        Returns:
        :   Provenance of the relationship

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *property* secondary*: [DataVariable](binaryview.md#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")]*
    :   `secondary` returns the secondary function, data variable, address, external address, or
        external symbol of the relationship

        Returns:
        :   Secondary object of the relationship

        Return type:
        :   *Union*[[*DataVariable*](binaryview.md#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable"),
            [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"),
            [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*ProjectFile*](project.md#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")],
            [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*ProjectFile*](project.md#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")]]

## FirmwareNinjaSection

*class* FirmwareNinjaSection[[source]](https://api.binary.ninja/_modules/binaryninja/firmwareninja.html#FirmwareNinjaSection)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FirmwareNinjaSection` is a class that stores information about a section
    identified with Firmware Ninja analysis, including the section type, start address,
    size, and entropy. This class is only available in the Ultimate Edition of Binary Ninja.

    __init__(*type: [FirmwareNinjaSectionType](enums.md#binaryninja.enums.FirmwareNinjaSectionType "binaryninja.enums.FirmwareNinjaSectionType")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *entropy: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type**
              ([*FirmwareNinjaSectionType*](enums.md#binaryninja.enums.FirmwareNinjaSectionType
              "binaryninja.enums.FirmwareNinjaSectionType")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **entropy** ([*float*](https://docs.python.org/3/library/functions.html#float "(in
              Python v3.14)")) –

        Return type:
        :   *None*

    entropy*: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [FirmwareNinjaSectionType](enums.md#binaryninja.enums.FirmwareNinjaSectionType "binaryninja.enums.FirmwareNinjaSectionType")*
