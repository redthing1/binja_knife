# typearchive module

| Class | Description |
| --- | --- |
| [`binaryninja.typearchive.TypeArchive`](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | Type Archives are a collection of types which can be shared between different analysis sessions… |
| [`binaryninja.typearchive.TypeArchiveNotification`](#binaryninja.typearchive.TypeArchiveNotification "binaryninja.typearchive.TypeArchiveNotification") | Class providing an interface to receive event notifications for updates that happen to a Type… |
| [`binaryninja.typearchive.TypeArchiveNotificationCallbacks`](#binaryninja.typearchive.TypeArchiveNotificationCallbacks "binaryninja.typearchive.TypeArchiveNotificationCallbacks") |  |

## TypeArchive

*class* TypeArchive[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Type Archives are a collection of types which can be shared between different analysis
    sessions and are backed by a database file on disk. Their types can be modified, and a
    history of previous versions of types is stored in snapshots in the archive.

    Internal-use constructor. API users will want to use
    [`TypeArchive.open`](#binaryninja.typearchive.TypeArchive.open
    "binaryninja.typearchive.TypeArchive.open") or
    [`TypeArchive.create`](#binaryninja.typearchive.TypeArchive.create
    "binaryninja.typearchive.TypeArchive.create") instead to get an instance of a
    TypeArchive.

    Parameters:
    :   **handle** – Handle pointer (Internal use only.)

    __init__(*handle: LP_BNTypeArchive*)[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.__init__)
    :   Internal-use constructor. API users will want to use :py:func:TypeArchive.open or
        :py:func:TypeArchive.create instead to get an instance of a TypeArchive.

        Parameters:
        :   **handle** (*LP_BNTypeArchive*) – Handle pointer (Internal use only.)

    add_type(*name: _types.QualifiedNameType*, *type: _types.Type*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.add_type)
    :   Add named types to the type archive. Type must have all dependent named types added
        prior to being added, or this function will fail. If the type already exists, it will be
        overwritten.

        Parameters:
        :   - **name** (*_types.QualifiedNameType*) – Name of new type
            - **type** (*_types.Type*) – Definition of new type

        Return type:
        :   *None*

    add_types(*new_types: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[_types.QualifiedNameType, _types.Type]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.add_types)
    :   Add named types to the type archive. Types must have all dependent named types added
        prior to the parent types being added (or included in the list) or this function will
        fail. Types already existing with any added names will be overwritten.

        Parameters:
        :   **new_types** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
            "(in Python v3.14)")*[**_types.QualifiedNameType**,* *_types.Type**]**]*) – Names and
            definitions of new types

        Return type:
        :   *None*

    *static* create(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*) → [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.create)
    :   Create a Type Archive at the given path.

        Parameters:
        :   - **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Path to Type Archive file
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Relevant platform for types in the archive

        Returns:
        :   Type Archive, or None if it could not be created.

        Return type:
        :   [*TypeArchive*](#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive") | *None*

    delete_type(*name: _types.QualifiedNameType*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.delete_type)
    :   Delete an existing type in the type archive.

        Parameters:
        :   **name** (*_types.QualifiedNameType*) – Type name

        Return type:
        :   *None*

    delete_type_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.delete_type_by_id)
    :   Delete an existing type in the type archive.

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Type id

        Return type:
        :   *None*

    deserialize_snapshot(*data: databuffer.DataBufferInputType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.deserialize_snapshot)
    :   Take a serialized snapshot data stream and create a new snapshot from it

        Parameters:
        :   **data** (*databuffer.DataBufferInputType*) – Snapshot data

        Returns:
        :   String of created snapshot id

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_incoming_direct_references(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_incoming_direct_references)
    :   Get all types that reference a given type

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Target type id
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or empty string to search the
              latest snapshot

        Returns:
        :   Source type ids

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_incoming_recursive_references(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_incoming_recursive_references)
    :   Get all types that reference a given type, and all types that reference them,
        recursively

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Target type id
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or empty string to search the
              latest snapshot

        Returns:
        :   Source type ids

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → metadata.MetadataValueType | Any[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_metadata)
    :   get_metadata retrieves a metadata value associated with the given key stored in the
        current TypeArchive.

        This method behaves like dict.get():

        - If the key exists, its metadata value is returned.
        - If the key does not exist and default is not provided, None is returned.
        - If the key does not exist and default is provided, default is returned.

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – key to query
            - **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")) – value to return if the key does not exist (defaults to None)

        Return type:
        :   metadata associated with the key or the default value

        Example:
        :   ```
            >>> ta.store_metadata("integer", 1337)
            >>> ta.get_metadata("integer")
            1337L
            >>> ta.get_metadata("missing")
            None
            >>> ta.get_metadata("missing", 42)
            42
            ```

    get_outgoing_direct_references(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_outgoing_direct_references)
    :   Get all types a given type references directly

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source type id
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or empty string to search the
              latest snapshot

        Returns:
        :   Target type ids

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_outgoing_recursive_references(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_outgoing_recursive_references)
    :   Get all types a given type references, and any types that the referenced types reference

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source type id
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or empty string to search the
              latest snapshot

        Returns:
        :   Target type ids

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_snapshot_child_ids(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_snapshot_child_ids)
    :   Get the ids of the children to the given snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Parent snapshot id

        Returns:
        :   Child snapshot ids, or empty list if the snapshot is a leaf

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")] | *None*

    get_snapshot_parent_ids(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_snapshot_parent_ids)
    :   Get the ids of the parents to the given snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Child snapshot id

        Returns:
        :   Parent snapshot ids, or empty list if the snapshot is a root

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")] | *None*

    get_type_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_by_id)
    :   Retrieve a stored type in the archive by id

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Type id
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
              snapshot

        Returns:
        :   Type, if it exists. Otherwise None

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*

    get_type_by_name(*name: _types.QualifiedNameType*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_by_name)
    :   Retrieve a stored type in the archive

        Parameters:
        :   - **name** (*_types.QualifiedNameType*) – Type name
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
              snapshot

        Returns:
        :   Type, if it exists. Otherwise None

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*

    get_type_id(*name: _types.QualifiedNameType*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_id)
    :   Retrieve a type’s id by its name

        Parameters:
        :   - **name** (*_types.QualifiedNameType*) – Type name
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
              snapshot

        Returns:
        :   Type id, if it exists. Otherwise None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_type_ids(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_ids)
    :   Get a list of all types’ ids in the archive at a snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
            snapshot

        Returns:
        :   All type ids

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_type_name_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_name_by_id)
    :   Retrieve a type’s name by its id

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Type id
            - **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
              snapshot

        Returns:
        :   Type name, if it exists. Otherwise None

        Return type:
        :   [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName") | *None*

    get_type_names(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_names)
    :   Get a list of all types’ names in the archive at a snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
            snapshot

        Returns:
        :   All type names

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")]

    get_type_names_and_ids(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_type_names_and_ids)
    :   Get a list of all types’ names and ids in the archive at a current snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
            snapshot

        Returns:
        :   Mapping of all type ids to names

        Return type:
        :   [*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")]

    get_types(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_types)
    :   Retrieve all stored types in the archive at a snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
            snapshot

        Returns:
        :   Map of all types, by name

        Return type:
        :   [*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
            v3.14)")[[*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName"), [*Type*](types.md#binaryninja.types.Type
            "binaryninja.types.Type")]

    get_types_and_ids(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]][[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.get_types_and_ids)
    :   Retrieve all stored types in the archive at a snapshot

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) – Snapshot id to search for types, or None to search the latest
            snapshot

        Returns:
        :   Map of type id to type name and definition

        Return type:
        :   [*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName"), [*Type*](types.md#binaryninja.types.Type
            "binaryninja.types.Type")]]

    *static* lookup_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.lookup_by_id)
    :   Get a reference to the Type Archive with the known id, if one exists.

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Type Archive id

        Returns:
        :   Type archive, or None if it could not be found.

        Return type:
        :   [*TypeArchive*](#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive") | *None*

    *static* open(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.open)
    :   Open the Type Archive at the given path, if it exists.

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Path to Type Archive file

        Returns:
        :   Type Archive, or None if it could not be loaded.

        Return type:
        :   [*TypeArchive*](#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive") | *None*

    query_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → metadata.MetadataValueType[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.query_metadata)
    :   Look up a metadata entry in the archive

        Note

        As of Binary Ninja 5.3 this API now raises KeyError on failure. Please use get_metadata
        for a non-raising version of the API.

        Parameters:
        :   **key** (*string*) – key to query

        Return type:
        :   Metadata associated with the key, if it exists. Otherwise, *None*

        Example:
        :   ```
            >>> ta: TypeArchive
            >>> ta.store_metadata("ordinals", {"9": "htons"})
            >>> ta.query_metadata("ordinals")["9"]
            "htons"
            ```

    register_notification(*notify: [TypeArchiveNotification](#binaryninja.typearchive.TypeArchiveNotification "binaryninja.typearchive.TypeArchiveNotification")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.register_notification)
    :   Register a notification listener

        Parameters:
        :   **notify** ([*TypeArchiveNotification*](#binaryninja.typearchive.TypeArchiveNotification
            "binaryninja.typearchive.TypeArchiveNotification")) – Object to receive notifications

        Return type:
        :   *None*

    remove_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.remove_metadata)
    :   Delete a given metadata entry in the archive

        Parameters:
        :   **key** (*string*) – key associated with metadata

        Example:
        :   ```
            >>> ta: TypeArchive
            >>> ta.store_metadata("integer", 1337)
            >>> ta.remove_metadata("integer")
            ```

        Return type:
        :   *None*

    rename_type(*old_name: _types.QualifiedNameType*, *new_name: _types.QualifiedNameType*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.rename_type)
    :   Change the name of an existing type in the type archive.

        Parameters:
        :   - **old_name** (*_types.QualifiedNameType*) – Old type name in archive
            - **new_name** (*_types.QualifiedNameType*) – New type name

        Return type:
        :   *None*

    rename_type_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *new_name: _types.QualifiedNameType*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.rename_type_by_id)
    :   Change the name of an existing type in the type archive.

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Old id of type in archive
            - **new_name** (*_types.QualifiedNameType*) – New type name

        Return type:
        :   *None*

    serialize_snapshot(*snapshot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.serialize_snapshot)
    :   Turn a given snapshot into a data stream

        Parameters:
        :   **snapshot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Snapshot id

        Returns:
        :   Buffer containing serialized snapshot data

        Return type:
        :   [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer")

    store_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *md: metadata.MetadataValueType*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.store_metadata)
    :   Store a key/value pair in the archive’s metadata storage

        Parameters:
        :   - **key** (*string*) – key value to associate the Metadata object with
            - **md** (*Varies*) – object to store.

        Example:
        :   ```
            >>> ta: TypeArchive
            >>> ta.store_metadata("ordinals", {"9": "htons"})
            >>> ta.query_metadata("ordinals")["9"]
            "htons"
            ```

        Return type:
        :   *None*

    unregister_notification(*notify: [TypeArchiveNotification](#binaryninja.typearchive.TypeArchiveNotification "binaryninja.typearchive.TypeArchiveNotification")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchive.unregister_notification)
    :   Unregister a notification listener

        Parameters:
        :   **notify** ([*TypeArchiveNotification*](#binaryninja.typearchive.TypeArchiveNotification
            "binaryninja.typearchive.TypeArchiveNotification")) – Object to no longer receive
            notifications

        Return type:
        :   *None*

    *property* all_snapshot_ids*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get a list of every snapshot’s id

        Returns:
        :   All ids (including the empty first snapshot)

    *property* current_snapshot_id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the id of the current snapshot in the type archive

        Returns:
        :   Snapshot id

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the GUID for a Type Archive

        Returns:
        :   Guid string

    *property* path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the path to the Type Archive’s file

        Returns:
        :   File path

    *property* platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*
    :   Get the associated Platform for a Type Archive

        Returns:
        :   Platform object

    *property* type_ids*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get a list of all types’ ids in the archive at the current snapshot

        Returns:
        :   All type ids

    *property* type_names*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")]*
    :   Get a list of all types’ names in the archive at the current snapshot :return: All type
        names

    *property* type_names_and_ids*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")]*
    :   Get a list of all types’ names and ids in the archive at the current snapshot

        Returns:
        :   Mapping of all type ids to names

    *property* types*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*
    :   Retrieve all stored types in the archive at the current snapshot

        Returns:
        :   Map of all types, by name

    *property* types_and_ids*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*
    :   Retrieve all stored types in the archive at the current snapshot

        Returns:
        :   Map of type id to type name and definition

## TypeArchiveNotification

*class* TypeArchiveNotification[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotification)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class providing an interface to receive event notifications for updates that happen to a
    Type Archive.

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotification.__init__)

    type_added(*archive: [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *definition: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotification.type_added)
    :   Called when a type is added to the archive

        Parameters:
        :   - **archive** ([*TypeArchive*](#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Source Type archive
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of type added
            - **definition** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
              Definition of type

        Return type:
        :   *None*

    type_deleted(*archive: [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *definition: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotification.type_deleted)
    :   Called when a type in the archive is deleted from the archive

        Parameters:
        :   - **archive** ([*TypeArchive*](#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Source Type archive
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of type deleted
            - **definition** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
              Definition of type deleted

        Return type:
        :   *None*

    type_renamed(*archive: [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *old_name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *new_name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotification.type_renamed)
    :   Called when a type in the archive is renamed

        Parameters:
        :   - **archive** ([*TypeArchive*](#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Source Type archive
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Type id
            - **old_name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Previous name
            - **new_name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Current name

        Return type:
        :   *None*

    type_updated(*archive: [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *old_definition: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *new_definition: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotification.type_updated)
    :   Called when a type in the archive is updated to a new definition

        Parameters:
        :   - **archive** ([*TypeArchive*](#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Source Type archive
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of type
            - **old_definition** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))
              – Previous definition
            - **new_definition** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))
              – Current definition

        Return type:
        :   *None*

## TypeArchiveNotificationCallbacks

*class* TypeArchiveNotificationCallbacks[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotificationCallbacks)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*archive: [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *notify: [TypeArchiveNotification](#binaryninja.typearchive.TypeArchiveNotification "binaryninja.typearchive.TypeArchiveNotification")*)[[source]](https://api.binary.ninja/_modules/binaryninja/typearchive.html#TypeArchiveNotificationCallbacks.__init__)
    :   Parameters:
        :   - **archive** ([*TypeArchive*](#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive"))
            - **notify** ([*TypeArchiveNotification*](#binaryninja.typearchive.TypeArchiveNotification
              "binaryninja.typearchive.TypeArchiveNotification"))

    *property* archive*: [TypeArchive](#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*

    *property* notify*: [TypeArchiveNotification](#binaryninja.typearchive.TypeArchiveNotification "binaryninja.typearchive.TypeArchiveNotification")*
