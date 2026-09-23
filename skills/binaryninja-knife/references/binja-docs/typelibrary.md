# typelibrary module

| Class | Description |
| --- | --- |
| [`binaryninja.typelibrary.TypeLibrary`](#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary") |  |

## TypeLibrary

*class* TypeLibrary[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: LP_BNTypeLibrary*)[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.__init__)
    :   Parameters:
        :   **handle** (*LP_BNTypeLibrary*) –

    add_alternate_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.add_alternate_name)
    :   Adds an extra name to this type library used during library lookups and dependency
        resolution

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   *None*

    add_named_object(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.add_named_object)
    :   add_named_object directly inserts a named object into the type library’s object store.
        This is not done recursively, so care should be taken that types referring to other
        types through NamedTypeReferences are already appropriately prepared.

        To add types and objects from an existing BinaryView, it is recommended to use
        `export_object_to_library`, which will automatically pull in all referenced types and
        record additional dependencies as needed.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **t** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   *None*

    add_named_type(*name: types.QualifiedNameType*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.add_named_type)
    :   add_named_type directly inserts a named object into the type library’s object store.
        This is not done recursively, so care should be taken that types referring to other
        types through NamedTypeReferences are already appropriately prepared.

        To add types and objects from an existing BinaryView, it is recommended to use
        `export_type_to_library`, which will automatically pull in all referenced types and
        record additional dependencies as needed.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **t** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   *None*

    add_platform(*plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.add_platform)
    :   Associate a platform with a type library instance that has not been finalized.

        This will cause the library to be searchable by `Platform.get_type_libraries_by_name`
        when loaded.

        This does not have side affects until finalization of the type library.

        Parameters:
        :   **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
            "binaryninja.platform.Platform")) –

        Return type:
        :   *None*

    add_type_source(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.add_type_source)
    :   Manually flag NamedTypeReferences to the given QualifiedName as originating from another
        source TypeLibrary with the given dependency name.

        Warning

        Use this api with extreme caution.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName") *|*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –
            - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    clear_platforms() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.clear_platforms)
    :   Clears the list of platforms associated with a type library instance that has not been
        finalized

        Return type:
        :   *None*

    decompress_to_file(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.decompress_to_file)
    :   Decompresses the type library file to a file on disk.

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Raises:
        :   OSError if saving the file fails

    duplicate() → [TypeLibrary](#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.duplicate)
    :   Creates a new type library instance with a random GUID and the same data as the current
        instance.

        Return type:
        :   [*TypeLibrary*](#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")

    finalize() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.finalize)
    :   Flags a newly created type library instance as finalized and makes it available for
        Platform and Architecture type library searches

        Return type:
        :   True if the type library was successfully finalized, False otherwise

    *static* from_guid(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.from_guid)
    :   from_guid attempts to grab a type library associated with the provided Architecture and
        GUID pair

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*TypeLibrary*](#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")

    *static* from_name(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.from_name)
    :   from_name looks up the first type library found with a matching name. Keep in mind that
        names are not necessarily unique.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*TypeLibrary*](#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")

    get_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → metadata.MetadataValueType | Any[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.get_metadata)
    :   get_metadata retrieves a metadata value associated with the given key stored in the
        current BinaryView.

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
            >>> tl.store_metadata("integer", 1337)
            >>> tl.get_metadata("integer")
            1337L
            >>> tl.get_metadata("missing")
            None
            >>> tl.get_metadata("missing", 42)
            42
            ```

    get_named_object(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.get_named_object)
    :   get_named_object direct extracts a reference to a contained object – when attempting to
        extract types from a library into a BinaryView, consider using `import_library_object`
        instead.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")

    get_named_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.get_named_type)
    :   get_named_type direct extracts a reference to a contained type – when attempting to
        extract types from a library into a BinaryView, consider using `import_library_type`
        instead.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")

    *static* load_from_file(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeLibrary](#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.load_from_file)
    :   Loads a finalized type library instance from file

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*TypeLibrary*](#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")

    *static* new(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeLibrary](#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.new)
    :   Creates an empty type library object with a random GUID and the provided name.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   [*TypeLibrary*](#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")

    query_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → metadata.MetadataValueType[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.query_metadata)
    :   query_metadata retrieves a metadata associated with the given key stored in the type
        library

        Note

        As of Binary Ninja 5.3 this API now raises KeyError on failure. Please use get_metadata
        for a non-raising version of the API.

        Parameters:
        :   **key** (*string*) – key to query

        Return type:
        :   metadata associated with the key

        Example:
        :   ```
            >>> lib.store_metadata("ordinals", {"9": "htons"})
            >>> lib.query_metadata("ordinals")["9"]
            "htons"
            ```

    register() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.register)
    :   Make a created or loaded Type Library available for Platforms to use when loading
        binaries.

        Return type:
        :   *None*

    remove_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.remove_metadata)
    :   remove_metadata removes the metadata associated with key from the current type library.

        Parameters:
        :   **key** (*string*) – key associated with metadata

        Return type:
        :   *None*

        Example:
        :   ```
            >>> lib.store_metadata("integer", 1337)
            >>> lib.remove_metadata("integer")
            ```

    remove_named_object(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.remove_named_object)
    :   remove_named_object removes a named object from the type library’s object store. This
        does not remove any types that are referenced by the object, only the object itself.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) –

        Return type:
        :   *None*

    remove_named_type(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.remove_named_type)
    :   remove_named_type removes a named type from the type library’s type store. This does not
        remove any objects that reference the type, only the type itself.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName") *|*
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –

        Return type:
        :   *None*

    store_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *md: [Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.store_metadata)
    :   store_metadata stores an object for the given key in the current type library. Objects
        stored using store_metadata can be retrieved from any reference to the library. Objects
        stored are not arbitrary python objects! The values stored must be able to be held in a
        Metadata object. See `Metadata` for more information. Python objects could obviously be
        serialized using pickle but this intentionally a task left to the user since there is
        the potential security issues.

        This is primarily intended as a way to store Platform specific information relevant to
        BinaryView implementations; for example the PE BinaryViewType uses type library metadata
        to retrieve ordinal information, when available.

        Parameters:
        :   - **key** (*string*) – key value to associate the Metadata object with
            - **md** (*Varies*) – object to store.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> lib.store_metadata("ordinals", {"9": "htons"})
            >>> lib.query_metadata("ordinals")["9"]
            "htons"
            ```

    write_to_file(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typelibrary.html#TypeLibrary.write_to_file)
    :   Saves a finalized type library instance to file

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   *None*

        Raises:
        :   OSError if saving the file fails

    *property* alternate_names*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   A list of extra names that will be considered a match by
        `Platform.get_type_libraries_by_name`

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*
    :   The Architecture this type library is associated with

    *property* dependency_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The dependency_name of a library is the name used to record dependencies across type
        libraries. This allows, for example, a library with the name “musl_libc” to have
        dependencies on it recorded as “libc_generic”, allowing a type library to be used across
        multiple platforms where each has a specific libc that also provides the name
        “libc_generic” as an alternate_name.

    *property* guid*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the GUID associated with the type library

    *property* metadata*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), metadata.MetadataValueType]*
    :   metadata retrieves the metadata associated with the current type library.

        Return type:
        :   Metadata object

        Example:
        :   ```
            >>> lib.store_metadata("integer", 1337)
            >>> lib.metadata["integer"]
            1337
            ```

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The primary name associated with this type library

    *property* named_objects*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*
    :   A dict containing all named objects (functions, exported variables) provided by a type
        library (read-only)

    *property* named_types*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*
    :   A dict containing all named types provided by a type library (read-only)

    *property* platform_names*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Returns a list of all platform names that this type library will register with during
        platform type registration.

        This returns strings, not Platform objects, as type libraries can be distributed with
        support for Platforms that may not be present.

    *property* type_container*: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*
    :   Type Container for all TYPES within the Type Library. Objects are not included. The Type
        Container’s Platform will be the first platform associated with the Type Library.
        :return: Type Library Type Container
