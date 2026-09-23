# database module

| Class | Description |
| --- | --- |
| [`binaryninja.database.Database`](#binaryninja.database.Database "binaryninja.database.Database") | `class Database` provides lower level access to raw snapshot data used to construct analysis data |
| [`binaryninja.database.KeyValueStore`](#binaryninja.database.KeyValueStore "binaryninja.database.KeyValueStore") | `class KeyValueStore` maintains access to the raw data stored in Snapshots and various other… |
| [`binaryninja.database.Snapshot`](#binaryninja.database.Snapshot "binaryninja.database.Snapshot") | `class Snapshot` is a model of an individual database snapshot, created on save. |

## Database

*class* Database[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class Database` provides lower level access to raw snapshot data used to construct
    analysis data

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.__init__)

    get_snapshot(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.get_snapshot)
    :   Get a snapshot by its id, or None if no snapshot with that id exists

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*Snapshot*](#binaryninja.database.Snapshot "binaryninja.database.Snapshot") | *None*

    read_global(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.read_global)
    :   Get a specific global by key

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    read_global_data(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.read_global_data)
    :   Get a specific global by key, as a binary buffer

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer")

    remove_snapshot(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.remove_snapshot)
    :   Remove a snapshot in the database by id, deleting its contents and references.
        Attempting to remove a snapshot with children will raise an exception.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

    trim_snapshot(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.trim_snapshot)
    :   Trim a snapshot’s contents in the database by id, but leave the parent/child hierarchy
        intact. Future references to this snapshot will return False for has_contents

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

    write_global(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.write_global)
    :   Write a global into the database

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

    write_global_data(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Database.write_global_data)
    :   Write a binary buffer into a global in the database

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer")) –

    *property* analysis_cache*: [KeyValueStore](#binaryninja.database.KeyValueStore "binaryninja.database.KeyValueStore")*
    :   Get the backing analysis cache kvs (read-only)

    *property* current_snapshot*: [Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the current snapshot

    *property* file*: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata")*
    :   Get the owning FileMetadata (read-only)

    *property* global_keys*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get a list of keys for all globals in the database (read-only)

    *property* globals*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get a dictionary of all globals (read-only)

    *property* snapshots*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot")]*
    :   Get a list of all snapshots in the database (read-only)

## KeyValueStore

*class* KeyValueStore[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#KeyValueStore)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class KeyValueStore` maintains access to the raw data stored in Snapshots and various
    other Database-related structures.

    __init__(*buffer: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#KeyValueStore.__init__)
    :   Parameters:
        :   **buffer** ([*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer") *|* *None*) –

    begin_namespace(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#KeyValueStore.begin_namespace)
    :   Begin storing new keys into a namespace

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    end_namespace()[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#KeyValueStore.end_namespace)
    :   End storing new keys into a namespace

    get_value(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#KeyValueStore.get_value)
    :   Get the value for a single key

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
            "binaryninja.databuffer.DataBuffer")

    set_value(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#KeyValueStore.set_value)
    :   Set the value for a single key

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer")) –

    *property* data_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Length of serialized data (read-only)

    *property* empty*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   If the kvs is empty (read-only)

    *property* keys
    :   Get a list of all keys stored in the kvs (read-only)

    *property* namespace_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Number of namespaces pushed with begin_namespace (read-only)

    *property* serialized_data*: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*
    :   Get the stored representation of the kvs (read-only)

    *property* value_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Number of values in the kvs (read-only)

    *property* value_storage_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Size of all data in storage (read-only)

## Snapshot

*class* Snapshot[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Snapshot)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class Snapshot` is a model of an individual database snapshot, created on save.

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Snapshot.__init__)

    has_ancestor(*other: [Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/database.html#Snapshot.has_ancestor)
    :   Determine if this snapshot has another as an ancestor

        Parameters:
        :   **other** ([*Snapshot*](#binaryninja.database.Snapshot "binaryninja.database.Snapshot"))
            –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot")]*
    :   Get a list of all child snapshots of the snapshot (read-only)

    *property* data*: [KeyValueStore](#binaryninja.database.KeyValueStore "binaryninja.database.KeyValueStore")*
    :   Get the backing kvs data with snapshot fields (read-only)

    *property* database*: [Database](#binaryninja.database.Database "binaryninja.database.Database")*
    :   Get the owning database (read-only)

    *property* file_contents*: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*
    :   Get a buffer of the raw data at the time of the snapshot (read-only)

    *property* file_contents_hash*: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*
    :   Get a hash of the data at the time of the snapshot (read-only)

    *property* first_parent*: [Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the first parent of the snapshot, or None if it has no parents (read-only)

    *property* has_contents*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   If the snapshot has contents, and has not been trimmed (read-only)

    *property* has_undo*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   If the snapshot has undo data (read-only)

    *property* id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Get the numerical id (read-only)

    *property* is_auto_save*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   If the snapshot was the result of an auto-save (read-only)

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the displayed snapshot name

    *property* parents*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Snapshot](#binaryninja.database.Snapshot "binaryninja.database.Snapshot")]*
    :   Get a list of all parent snapshots of the snapshot (read-only)

    *property* undo_entries
    :   Get a list of undo entries at the time of the snapshot (read-only)
