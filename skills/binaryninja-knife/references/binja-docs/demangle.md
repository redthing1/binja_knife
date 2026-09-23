# demangle module

| Class | Description |
| --- | --- |
| [`binaryninja.demangle.CoreDemangler`](#binaryninja.demangle.CoreDemangler "binaryninja.demangle.CoreDemangler") | Pluggable name demangling interface. See `register` and `demangle` for details… |
| [`binaryninja.demangle.Demangler`](#binaryninja.demangle.Demangler "binaryninja.demangle.Demangler") | Pluggable name demangling interface. See `register` and `demangle` for details… |

| Function | Description |
| --- | --- |
| [`binaryninja.demangle.demangle_generic`](#binaryninja.demangle.demangle_generic "binaryninja.demangle.demangle_generic") | `demangle_generic` demangles a mangled symbol name to a Type object. |
| [`binaryninja.demangle.demangle_gnu3`](#binaryninja.demangle.demangle_gnu3 "binaryninja.demangle.demangle_gnu3") | `demangle_gnu3` demangles a mangled name to a Type object. |
| [`binaryninja.demangle.demangle_llvm`](#binaryninja.demangle.demangle_llvm "binaryninja.demangle.demangle_llvm") | `demangle_llvm` demangles a mangled name using the LLVM demangler. |
| [`binaryninja.demangle.demangle_ms`](#binaryninja.demangle.demangle_ms "binaryninja.demangle.demangle_ms") | `demangle_ms` demangles a mangled Microsoft Visual Studio C++ name to a Type object. |
| [`binaryninja.demangle.get_qualified_name`](#binaryninja.demangle.get_qualified_name "binaryninja.demangle.get_qualified_name") | `get_qualified_name` gets a qualified name for the provided name list. |
| [`binaryninja.demangle.simplify_name_to_qualified_name`](#binaryninja.demangle.simplify_name_to_qualified_name "binaryninja.demangle.simplify_name_to_qualified_name") | `simplify_name_to_qualified_name` simplifies a templated C++ name with default arguments and… |
| [`binaryninja.demangle.simplify_name_to_string`](#binaryninja.demangle.simplify_name_to_string "binaryninja.demangle.simplify_name_to_string") | `simplify_name_to_string` simplifies a templated C++ name with default arguments and returns a… |

## CoreDemangler

*class* CoreDemangler[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#CoreDemangler)
:   Bases: [`Demangler`](#binaryninja.demangle.Demangler "binaryninja.demangle.Demangler")

    demangle(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#CoreDemangler.demangle)
    :   Demangle a raw name into a Type and QualifiedName.

        The result of this function is a (Type, QualifiedName) tuple for the demangled name’s
        details.

        Any unresolved named types referenced by the resulting Type will be created as empty
        structures or void typedefs in the view, if the result is used on a data structure in
        the view. Given this, the call to
        [`demangle`](#binaryninja.demangle.CoreDemangler.demangle
        "binaryninja.demangle.CoreDemangler.demangle") should NOT cause any side-effects
        creating types in the view trying to resolve this and instead just return a type with
        unresolved named type references.

        The most recently registered demangler that claims a name is a mangled string (returns
        true from [`is_mangled_string`](#binaryninja.demangle.CoreDemangler.is_mangled_string
        "binaryninja.demangle.CoreDemangler.is_mangled_string")), and then returns a value from
        this function will determine the result of a call to
        [`demangle_generic`](#binaryninja.demangle.demangle_generic
        "binaryninja.demangle.demangle_generic"). If this call returns None, the next most
        recently used demangler(s) will be tried instead.

        If the mangled name has no type information, but a name is still possible to extract,
        this function may return a successful (None, <name>) result, which will be accepted.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for context in which the name
              exists, eg for pointer sizes
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Raw mangled name
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) – (Optional) BinaryView context in
              which the name exists, eg for type lookup

        Returns:
        :   Tuple of (Type, Name) if successful, None if not. Type may be None if only a demangled
            name can be recovered from the raw name.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*,
            [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")] | *None*

    is_mangled_string(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#CoreDemangler.is_mangled_string)
    :   Determine if a given name is mangled and this demangler can process it

        The most recently registered demangler that claims a name is a mangled string (returns
        true from this function), and then returns a value from
        [`demangle`](#binaryninja.demangle.CoreDemangler.demangle
        "binaryninja.demangle.CoreDemangler.demangle") will determine the result of a call to
        [`demangle_generic`](#binaryninja.demangle.demangle_generic
        "binaryninja.demangle.demangle_generic"). Returning True from this does not require the
        demangler to succeed the call to
        [`demangle`](#binaryninja.demangle.CoreDemangler.demangle
        "binaryninja.demangle.CoreDemangler.demangle"), but simply implies that it may succeed.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Raw mangled name string

        Returns:
        :   True if the demangler thinks it can handle the name

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## Demangler

*class* Demangler[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Pluggable name demangling interface. See
    [`register`](#binaryninja.demangle.Demangler.register
    "binaryninja.demangle.Demangler.register") and
    [`demangle`](#binaryninja.demangle.Demangler.demangle
    "binaryninja.demangle.Demangler.demangle") for details on the process of this interface.

    The list of Demanglers can be queried:

    ```
    >>> list(Demangler)
    [<Demangler: MS>, <Demangler: GNU3>]
    ```

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.__init__)

    demangle(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.demangle)
    :   Demangle a raw name into a Type and QualifiedName.

        The result of this function is a (Type, QualifiedName) tuple for the demangled name’s
        details.

        Any unresolved named types referenced by the resulting Type will be created as empty
        structures or void typedefs in the view, if the result is used on a data structure in
        the view. Given this, the call to [`demangle`](#binaryninja.demangle.Demangler.demangle
        "binaryninja.demangle.Demangler.demangle") should NOT cause any side-effects creating
        types in the view trying to resolve this and instead just return a type with unresolved
        named type references.

        The most recently registered demangler that claims a name is a mangled string (returns
        true from [`is_mangled_string`](#binaryninja.demangle.Demangler.is_mangled_string
        "binaryninja.demangle.Demangler.is_mangled_string")), and then returns a value from this
        function will determine the result of a call to
        [`demangle_generic`](#binaryninja.demangle.demangle_generic
        "binaryninja.demangle.demangle_generic"). If this call returns None, the next most
        recently used demangler(s) will be tried instead.

        If the mangled name has no type information, but a name is still possible to extract,
        this function may return a successful (None, <name>) result, which will be accepted.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture for context in which the name
              exists, eg for pointer sizes
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Raw mangled name
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) – (Optional) BinaryView context in
              which the name exists, eg for type lookup

        Returns:
        :   Tuple of (Type, Name) if successful, None if not. Type may be None if only a demangled
            name can be recovered from the raw name.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"),
            [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")] | *None*

    is_mangled_string(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.is_mangled_string)
    :   Determine if a given name is mangled and this demangler can process it

        The most recently registered demangler that claims a name is a mangled string (returns
        true from this function), and then returns a value from
        [`demangle`](#binaryninja.demangle.Demangler.demangle
        "binaryninja.demangle.Demangler.demangle") will determine the result of a call to
        [`demangle_generic`](#binaryninja.demangle.demangle_generic
        "binaryninja.demangle.demangle_generic"). Returning True from this does not require the
        demangler to succeed the call to [`demangle`](#binaryninja.demangle.Demangler.demangle
        "binaryninja.demangle.Demangler.demangle"), but simply implies that it may succeed.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Raw mangled name string

        Returns:
        :   True if the demangler thinks it can handle the name

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *classmethod* promote(*demangler*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.promote)
    :   Promote a demangler to the highest-priority position.

        ```
        >>> list(Demangler)
        [<Demangler: MS>, <Demangler: GNU3>]
        >>> Demangler.promote(list(Demangler)[0])
        >>> list(Demangler)
        [<Demangler: GNU3>, <Demangler: MS>]
        ```

        Parameters:
        :   **demangler** – Demangler to promote

    *classmethod* register()[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.register)
    :   Register a custom Demangler. Newly registered demanglers will get priority over
        previously registered demanglers and built-in demanglers.

    name *= None*

## demangle_generic

demangle_generic(*archOrPlatform: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *simplify: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_generic)
:   `demangle_generic` demangles a mangled symbol name to a Type object.

    Parameters:
    :   - **archOrPlatform**
          ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
          "binaryninja.architecture.Architecture") *|*
          [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform"))
          – Architecture or Platform for the symbol. Required for pointer/integer sizes and
          calling conventions.
        - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled symbol name
        - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
          "binaryninja.binaryview.BinaryView") *|* *None*) – (optional) view of the binary
          containing the mangled name
        - **simplify** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – (optional) Whether to simplify demangled names
        - **archOrPlatform** –

    Returns:
    :   returns tuple of (Optional[Type], demangled_name) or None on error

    Return type:
    :   *Tuple*

    Example:
    :   ```
        >>> demangle_generic(Architecture["x86_64"], "?testf@Foobar@@SA?AW4foo@1@W421@@Z")
        (<type: public: static enum Foobar::foo __cdecl (enum Foobar::foo)>, ['Foobar', 'testf'])
        >>> demangle_generic(Architecture["x86_64"], "__ZN20ArmCallingConvention27GetIntegerArgumentRegistersEv")
        (<type: immutable:FunctionTypeClass 'int64_t()'>, ['ArmCallingConvention', 'GetIntegerArgumentRegisters'])
        >>>
        ```

## demangle_gnu3

demangle_gnu3(*arch*, *mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_gnu3)
:   `demangle_gnu3` demangles a mangled name to a Type object.

    Parameters:
    :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
          "binaryninja.architecture.Architecture")) – Architecture for the symbol. Required for
          pointer and integer sizes.
        - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled GNU3 name
        - **options**
          (*Optional**[**Union**[*[*bool*](https://docs.python.org/3/library/functions.html#bool
          "(in Python v3.14)")*,* [*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
          "binaryninja.binaryview.BinaryView")*]**]*) – (optional) Whether to simplify demangled
          names : None falls back to user settings, a BinaryView uses that BinaryView’s settings,
          or a boolean to set it directly

    Returns:
    :   returns tuple of (Type, demangled_name) or (None, mangled_name) on error

    Return type:
    :   *Tuple*[*Optional*[[*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")],
        *Union*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)"), *List*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")]]]

## demangle_llvm

demangle_llvm(*mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_llvm)
:   `demangle_llvm` demangles a mangled name using the LLVM demangler.

    Parameters:
    :   - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled (msvc/itanium/rust/dlang) name
        - **options**
          (*Optional**[**Union**[*[*bool*](https://docs.python.org/3/library/functions.html#bool
          "(in Python v3.14)")*,* [*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
          "binaryninja.binaryview.BinaryView")*]**]*) – (optional) Whether to simplify demangled
          names : None falls back to user settings, a BinaryView uses that BinaryView’s settings,
          or a boolean to set it directly

    Returns:
    :   returns demangled name or None on error

    Return type:
    :   *Optional*[*List*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
        Python v3.14)")]]

    Example:
    :   ```
        >>> demangle_llvm("?testf@Foobar@@SA?AW4foo@1@W421@@Z")
        ['public: static enum Foobar::foo __cdecl Foobar::testf(enum Foobar::foo)']
        >>>
        ```

## demangle_ms

demangle_ms(*archOrPlatform: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_ms)
:   `demangle_ms` demangles a mangled Microsoft Visual Studio C++ name to a Type object.

    Parameters:
    :   - **archOrPlatform**
          ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
          "binaryninja.architecture.Architecture") *|*
          [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform"))
          – Architecture or Platform for the symbol. Required for pointer/integer sizes and
          calling conventions.
        - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled Microsoft Visual Studio C++ name
        - **options**
          (*Optional**[**Union**[*[*bool*](https://docs.python.org/3/library/functions.html#bool
          "(in Python v3.14)")*,* [*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
          "binaryninja.binaryview.BinaryView")*]**]*) – (optional) Whether to simplify demangled
          names : None falls back to user settings, a BinaryView uses that BinaryView’s settings,
          or a boolean to set it directly
        - **archOrPlatform** –

    Returns:
    :   returns tuple of (Type, demangled_name) or (None, mangled_name) on error

    Return type:
    :   *Tuple*[*Optional*[[*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")],
        *Union*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)"), *List*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")]]]

    Example:
    :   ```
        >>> demangle_ms(Platform["x86_64"], "?testf@Foobar@@SA?AW4foo@1@W421@@Z")
        (<type: public: static enum Foobar::foo __cdecl (enum Foobar::foo)>, ['Foobar', 'testf'])
        >>>
        ```

## get_qualified_name

get_qualified_name(*names: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#get_qualified_name)
:   `get_qualified_name` gets a qualified name for the provided name list.

    Parameters:
    :   **names** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
        v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")*)*) – name list to qualify

    Returns:
    :   a qualified name

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    Example:
    :   ```
        >>> type, name = demangle_ms(Architecture["x86_64"], "?testf@Foobar@@SA?AW4foo@1@W421@@Z")
        >>> get_qualified_name(name)
        'Foobar::testf'
        >>>
        ```

## simplify_name_to_qualified_name

simplify_name_to_qualified_name(*input_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *simplify: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#simplify_name_to_qualified_name)
:   `simplify_name_to_qualified_name` simplifies a templated C++ name with default arguments
    and returns a qualified name. This can also tokenize a string to a qualified name
    with/without simplifying it

    Parameters:
    :   - **input_name** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str
          "(in Python v3.14)")*,* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
          "binaryninja.types.QualifiedName")*]*) – String or qualified name to be simplified
        - **simplify** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – (optional) Whether to simplify input string (no effect if given a qualified
          name; will always simplify)

    Returns:
    :   simplified name (or one-element array containing the input if simplifier fails/cannot
        simplify)

    Return type:
    :   [*QualifiedName*](types.md#binaryninja.types.QualifiedName
        "binaryninja.types.QualifiedName")

    Example:
    :   ```
        >>> demangle.simplify_name_to_qualified_name(QualifiedName(["std", "__cxx11", "basic_string<wchar, std::char_traits<wchar>, std::allocator<wchar> >"]), True)
        'std::wstring'
        >>>
        ```

## simplify_name_to_string

simplify_name_to_string(*input_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#simplify_name_to_string)
:   `simplify_name_to_string` simplifies a templated C++ name with default arguments and
    returns a string

    Parameters:
    :   **input_name** (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str
        "(in Python v3.14)")*,* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
        "binaryninja.types.QualifiedName")*]*) – String or qualified name to be simplified

    Returns:
    :   simplified name (or original name if simplifier fails/cannot simplify)

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    Example:
    :   ```
        >>> demangle.simplify_name_to_string("std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >")
        'std::string'
        >>>
        ```
