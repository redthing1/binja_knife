# typecontainer module

| Class | Description |
| --- | --- |
| [`binaryninja.typecontainer.TypeContainer`](#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer") | A `TypeContainer` is a generic interface to access various Binary Ninja models that contain types. |

## TypeContainer

*class* TypeContainer[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    A `TypeContainer` is a generic interface to access various Binary Ninja models that
    contain types. Types are stored with both a unique id and a unique name.

    The `TypeContainer` class should not generally be instantiated directly. Instances can
    be retrieved from the following properties and methods in the API:

    - [`BinaryView.type_container`](binaryview.md#binaryninja.binaryview.BinaryView.type_container
      "binaryninja.binaryview.BinaryView.type_container")
    - [`BinaryView.auto_type_container`](binaryview.md#binaryninja.binaryview.BinaryView.auto_type_container
      "binaryninja.binaryview.BinaryView.auto_type_container")
    - [`BinaryView.user_type_container`](binaryview.md#binaryninja.binaryview.BinaryView.user_type_container
      "binaryninja.binaryview.BinaryView.user_type_container")
    - [`Platform.type_container`](platform.md#binaryninja.platform.Platform.type_container
      "binaryninja.platform.Platform.type_container")
    - [`TypeLibrary.type_container`](typelibrary.md#binaryninja.typelibrary.TypeLibrary.type_container
      "binaryninja.typelibrary.TypeLibrary.type_container")
    - [`DebugInfo.get_type_container`](debuginfo.md#binaryninja.debuginfo.DebugInfo.get_type_container
      "binaryninja.debuginfo.DebugInfo.get_type_container")

    Parameters:
    :   **handle** – Handle pointer (Internal use only.)

    __init__(*handle: LP_BNTypeContainer*)[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.__init__)
    :   Construct a Type Container, internal use only

        Parameters:
        :   **handle** (*LP_BNTypeContainer*) – Handle pointer

    add_types(*types: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[_types.QualifiedNameType, _types.Type]*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[_types.QualifiedName, [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.add_types)
    :   Add or update types to a Type Container. If the Type Container already contains a type
        with the same name as a type being added, the existing type will be replaced with the
        definition given to this function, and references will be updated in the source model.

        An optional progress callback is included because adding many types can be a slow
        operation.

        Parameters:
        :   - **types** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in
              Python v3.14)")*[**_types.QualifiedNameType**,* *_types.Type**]*) – Dict from name ->
              definition of new types to add
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*) – Optional function to call for progress updates

        Returns:
        :   Dict from name -> id of type in Type Container for all added types if successful, None
            otherwise.

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[_types.QualifiedName,
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] |
            *None*

    delete_type(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.delete_type)
    :   Delete a type in the Type Container. Behavior of references to this type is not
        specified and you may end up with broken references if any still exist.

        Parameters:
        :   **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of type to delete

        Returns:
        :   True if successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *classmethod* empty()[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.empty)
    :   Get an empty Type Container which contains no types (immutable) Useful when a function
        requires a Type Container but you don’t have one. :return: Empty type container

    get_type_by_id(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.get_type_by_id)
    :   Get the definition of the type in the Type Container with the given id. If no type with
        that id exists, returns None.

        Parameters:
        :   **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of type

        Returns:
        :   Type object, if exists, else, None

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*

    get_type_by_name(*type_name: _types.QualifiedNameType*) → _types.Type | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.get_type_by_name)
    :   Get the definition of the type in the Type Container with the given name. If no type
        with that name exists, returns None.

        Parameters:
        :   **type_name** (*_types.QualifiedNameType*) – Name of type

        Returns:
        :   Type object, if exists, else, None

        Return type:
        :   _types.Type | *None*

    get_type_id(*type_name: _types.QualifiedNameType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.get_type_id)
    :   Get the unique id of the type in the Type Container with the given name. If no type with
        that name exists, returns None.

        Parameters:
        :   **type_name** (*_types.QualifiedNameType*) – Name of type

        Returns:
        :   Type id, if exists, else, None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_type_name(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.get_type_name)
    :   Get the unique name of the type in the Type Container with the given id. If no type with
        that id exists, returns None.

        Parameters:
        :   **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of type

        Returns:
        :   Type name, if exists, else, None

        Return type:
        :   [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName") | *None*

    parse_type_string(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *import_dependencies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[_types.QualifiedNameType, _types.Type] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](typeparser.md#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.parse_type_string)
    :   Parse a single type and name from a string containing their definition, with knowledge
        of the types in the Type Container.

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to parse
            - **import_dependencies** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – If Type Library / Type Archive types should be imported during
              parsing

        Returns:
        :   A tuple of (result, errors) where result is a tuple of (type, name) or None of there was
            a fatal error.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[_types.QualifiedNameType, _types.Type] | *None*,
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeParserError*](typeparser.md#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    parse_types_from_source(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *file_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto_type_source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *import_dependencies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeParserResult](typeparser.md#binaryninja.typeparser.TypeParserResult "binaryninja.typeparser.TypeParserResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeParserError](typeparser.md#binaryninja.typeparser.TypeParserError "binaryninja.typeparser.TypeParserError")]][[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.parse_types_from_source)
    :   Parse an entire block of source into types, variables, and functions, with knowledge of
        the types in the Type Container.

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Source code to parse
            - **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the file containing the source (optional: exists on disk)
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional string arguments to pass as options, e.g.
              command line arguments
            - **include_dirs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of directories to include in the header
              search path
            - **auto_type_source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – Optional source of types if used for automatically generated types
            - **import_dependencies** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – If Type Library / Type Archive types should be imported during
              parsing

        Returns:
        :   A tuple of (result, errors) where the result is None if there was a fatal error

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*TypeParserResult*](typeparser.md#binaryninja.typeparser.TypeParserResult
            "binaryninja.typeparser.TypeParserResult") | *None*,
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeParserError*](typeparser.md#binaryninja.typeparser.TypeParserError
            "binaryninja.typeparser.TypeParserError")]]

    rename_type(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *new_name: _types.QualifiedNameType*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/typecontainer.html#TypeContainer.rename_type)
    :   Rename a type in the Type Container. All references to this type will be updated (by id)
        to use the new name.

        Parameters:
        :   - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of type to update
            - **new_name** (*_types.QualifiedNameType*) – New name for the type

        Returns:
        :   True if successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* container_type*: [TypeContainerType](enums.md#binaryninja.enums.TypeContainerType "binaryninja.enums.TypeContainerType")*
    :   Get the type of underlying model the Type Container is accessing. :return: Container
        type enum

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get an id string for the Type Container. This will be unique within a given analysis
        session, but may not be globally unique. :return: Identifier string

    *property* mutable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Test if the Type Container supports mutable operations (add, rename, delete) :return:
        True if mutable

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get a user-friendly name for the Type Container. :return: Display name

    *property* platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*
    :   Get the Platform object associated with this Type Container. All Type Containers have
        exactly one associated Platform (as opposed to, e.g. Type Libraries). :return:
        Associated Platform object

    *property* type_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Get the number of types in a Type Container. :return: Number of types in the container

    *property* type_ids*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get all type ids in a Type Container. :return: List of all type ids

    *property* type_names*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get all type names in a Type Container. :return: List of all type names

    *property* type_names_and_ids*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get a mapping of all type ids and type names in a Type Container. :return: Dict of type
        id -> type name

    *property* types*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get a mapping of all types in a Type Container. :return: All types in a dict of type id
        -> (type name, type definition)
