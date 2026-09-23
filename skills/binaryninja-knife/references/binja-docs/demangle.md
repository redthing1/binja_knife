# demangle module

| Class | Description |
| --- | --- |
| [`binaryninja.demangle.CoreDemangler`](#binaryninja.demangle.CoreDemangler "binaryninja.demangle.CoreDemangler") | Pluggable name demangling interface. See `register` and `demangle` for details… |
| [`binaryninja.demangle.DemangleResult`](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | Tuple-compatible demangle result. A successful result always has a QualifiedName; the type may… |
| [`binaryninja.demangle.Demangler`](#binaryninja.demangle.Demangler "binaryninja.demangle.Demangler") | Pluggable name demangling interface. See `register` and `demangle` for details… |
| [`binaryninja.demangle.DemanglerConfig`](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig") | Platform, view, and simplification options used by demangler APIs. |

| Function | Description |
| --- | --- |
| [`binaryninja.demangle.demangle_any`](#binaryninja.demangle.demangle_any "binaryninja.demangle.demangle_any") | Attempt to demangle a mangled name, trying all relevant demanglers and using whichever one… |
| [`binaryninja.demangle.demangle_generic`](#binaryninja.demangle.demangle_generic "binaryninja.demangle.demangle_generic") | Compatibility wrapper for the legacy generic demangler API. |
| [`binaryninja.demangle.demangle_gnu3`](#binaryninja.demangle.demangle_gnu3 "binaryninja.demangle.demangle_gnu3") | `demangle_gnu3` demangles a mangled name to a Type object. |
| [`binaryninja.demangle.demangle_llvm`](#binaryninja.demangle.demangle_llvm "binaryninja.demangle.demangle_llvm") | `demangle_llvm` demangles a mangled name using the LLVM demangler. |
| [`binaryninja.demangle.demangle_ms`](#binaryninja.demangle.demangle_ms "binaryninja.demangle.demangle_ms") | `demangle_ms` demangles a mangled Microsoft Visual Studio C++ name to a Type object. |
| [`binaryninja.demangle.simplify_demangled_template_name`](#binaryninja.demangle.simplify_demangled_template_name "binaryninja.demangle.simplify_demangled_template_name") | `simplify_demangled_template_name` simplifies standard-library template spelling in an already… |

## CoreDemangler

*class* CoreDemangler[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#CoreDemangler)
:   Bases: [`Demangler`](#binaryninja.demangle.Demangler "binaryninja.demangle.Demangler")

    demangle(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *config: [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#CoreDemangler.demangle)
    :   Demangle a raw name into a Type and QualifiedName.

        The result of this function is a DemangleResult with Type and QualifiedName fields for
        the demangled name’s details. DemangleResult can be unpacked as (type, name).

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
        [`demangle_any`](#binaryninja.demangle.demangle_any
        "binaryninja.demangle.demangle_any"). If this call returns None, the next most recently
        used demangler(s) will be tried instead.

        If the mangled name has no type information, but a name is still possible to extract,
        this function may return a successful DemangleResult(None, <name>), which will be
        accepted.

        Custom demanglers using the legacy `demangle(arch, name, view)` signature remain
        supported for one deprecation cycle.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Raw mangled name
            - **config** ([*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
              "binaryninja.demangle.DemanglerConfig")) – Platform/view/options used while demangling

        Returns:
        :   DemangleResult with type and name fields if successful, None if not. Type may be None if
            only a demangled name can be recovered from the raw name.

        Return type:
        :   [*DemangleResult*](#binaryninja.demangle.DemangleResult
            "binaryninja.demangle.DemangleResult") | *None*

    is_mangled_string(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#CoreDemangler.is_mangled_string)
    :   Determine if a given name is mangled and this demangler can process it

        The most recently registered demangler that claims a name is a mangled string (returns
        true from this function), and then returns a value from
        [`demangle`](#binaryninja.demangle.CoreDemangler.demangle
        "binaryninja.demangle.CoreDemangler.demangle") will determine the result of a call to
        [`demangle_any`](#binaryninja.demangle.demangle_any
        "binaryninja.demangle.demangle_any"). Returning True from this does not require the
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

## DemangleResult

*class* DemangleResult[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#DemangleResult)
:   Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple
    "(in Python v3.14)")

    Tuple-compatible demangle result. A successful result always has a QualifiedName; the
    type may be None when the demangler can recover only a name.

    *static* __new__(*_cls*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*)
    :   Create new instance of DemangleResult(type, name)

        Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|* *None*)
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName"))

    name*: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*
    :   Alias for field number 1

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for field number 0

## Demangler

*class* Demangler[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Pluggable name demangling interface. See
    [`register`](#binaryninja.demangle.Demangler.register
    "binaryninja.demangle.Demangler.register") and
    [`demangle`](#binaryninja.demangle.Demangler.demangle
    "binaryninja.demangle.Demangler.demangle") for details on the process of this interface.

    Custom Demangler subclasses can be registered and promoted at runtime.

    The list of Demanglers can be queried:

    ```
    >>> list(Demangler)
    [<Demangler: MS>, <Demangler: GNU3>, <Demangler: LLVM>]
    ```

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.__init__)

    demangle(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *config: [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.demangle)
    :   Demangle a raw name into a Type and QualifiedName.

        The result of this function is a DemangleResult with Type and QualifiedName fields for
        the demangled name’s details. DemangleResult can be unpacked as (type, name).

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
        [`demangle_any`](#binaryninja.demangle.demangle_any
        "binaryninja.demangle.demangle_any"). If this call returns None, the next most recently
        used demangler(s) will be tried instead.

        If the mangled name has no type information, but a name is still possible to extract,
        this function may return a successful DemangleResult(None, <name>), which will be
        accepted.

        Custom demanglers using the legacy `demangle(arch, name, view)` signature remain
        supported for one deprecation cycle.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Raw mangled name
            - **config** ([*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
              "binaryninja.demangle.DemanglerConfig")) – Platform/view/options used while demangling

        Returns:
        :   DemangleResult with type and name fields if successful, None if not. Type may be None if
            only a demangled name can be recovered from the raw name.

        Return type:
        :   [*DemangleResult*](#binaryninja.demangle.DemangleResult
            "binaryninja.demangle.DemangleResult") | *None*

    *static* demangle_any(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *config: [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.demangle_any)
    :   Demangle a raw name using an optional prebuilt DemanglerConfig.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **config** ([*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
              "binaryninja.demangle.DemanglerConfig") *|* *None*)

        Return type:
        :   [*DemangleResult*](#binaryninja.demangle.DemangleResult
            "binaryninja.demangle.DemangleResult") | *None*

    is_mangled_string(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.is_mangled_string)
    :   Determine if a given name is mangled and this demangler can process it

        The most recently registered demangler that claims a name is a mangled string (returns
        true from this function), and then returns a value from
        [`demangle`](#binaryninja.demangle.Demangler.demangle
        "binaryninja.demangle.Demangler.demangle") will determine the result of a call to
        [`demangle_any`](#binaryninja.demangle.demangle_any
        "binaryninja.demangle.demangle_any"). Returning True from this does not require the
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
        [<Demangler: MS>, <Demangler: GNU3>, <Demangler: LLVM>]
        >>> Demangler.promote(list(Demangler)[0])
        True
        >>> list(Demangler)
        [<Demangler: GNU3>, <Demangler: LLVM>, <Demangler: MS>]
        ```

        Parameters:
        :   **demangler** – Demangler to promote

        Returns:
        :   True if promotion succeeded; False if the demangler was invalid or not registered.

    *classmethod* register()[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#Demangler.register)
    :   Register a custom Demangler. Newly registered demanglers will get priority over
        previously registered demanglers and built-in demanglers.

        Returns:
        :   True if registration succeeded; False if the demangler was invalid.

    name *= None*

## DemanglerConfig

*class* DemanglerConfig[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#DemanglerConfig)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Platform, view, and simplification options used by demangler APIs.

    Use `default`, `for_platform`, or `for_binary_view` when the configuration should
    inherit the corresponding core defaults.

    __init__(*arch_or_platform: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *simplify: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#DemanglerConfig.__init__)
    :   Parameters:
        :   - **arch_or_platform**
              ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|*
              [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")
              *|* *None*)
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)
            - **simplify** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)"))

    *classmethod* default() → [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#DemanglerConfig.default)
    :   Create the core default demangler configuration.

        Return type:
        :   [*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
            "binaryninja.demangle.DemanglerConfig")

    *classmethod* for_binary_view(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#DemanglerConfig.for_binary_view)
    :   Create a configuration using a view’s platform and template-simplifier setting.

        Parameters:
        :   **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView"))

        Return type:
        :   [*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
            "binaryninja.demangle.DemanglerConfig")

    *classmethod* for_platform(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *simplify: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#DemanglerConfig.for_platform)
    :   Create a configuration for a platform.

        Parameters:
        :   - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform"))
            - **simplify** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)"))

        Return type:
        :   [*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
            "binaryninja.demangle.DemanglerConfig")

## demangle_any

demangle_any(*mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *config: [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_any)
:   Attempt to demangle a mangled name, trying all relevant demanglers and using whichever
    one accepts it.

    Parameters:
    :   - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled symbol name
        - **config** (*Optional**[*[*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
          "binaryninja.demangle.DemanglerConfig")*]*) – Platform/view/options used while
          demangling. If omitted, the core default standalone platform is used.

    Returns:
    :   returns a DemangleResult with type and name fields, or None on error. DemangleResult can
        be unpacked as (type, name).

    Return type:
    :   *Optional*[[*DemangleResult*](#binaryninja.demangle.DemangleResult
        "binaryninja.demangle.DemangleResult")]

    Example:
    :   ```
        >>> result = demangle_any("?testf@Foobar@@SA?AW4foo@1@W421@@Z")
        >>> result.type
        <type: immutable:FunctionTypeClass 'enum Foobar::foo __cdecl(enum Foobar::foo)'>
        >>> result.name
        'Foobar::testf'
        ```

## demangle_generic

demangle_generic(*archOrPlatform: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *simplify: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_generic)
:   Compatibility wrapper for the legacy generic demangler API.

    Deprecated since version 5.4: Use demangle_any with a DemanglerConfig instead.

    Parameters:
    :   - **archOrPlatform**
          ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
          "binaryninja.architecture.Architecture") *|*
          [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform"))
        - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)"))
        - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
          "binaryninja.binaryview.BinaryView") *|* *None*)
        - **simplify** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)"))

    Return type:
    :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
        v3.14)")[[*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*,
        [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
        v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")]] | *None*

## demangle_gnu3

demangle_gnu3(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")*, *mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options=None*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_gnu3)
:   `demangle_gnu3` demangles a mangled name to a Type object.

    Warning

    Passing a BinaryView through the legacy `options` compatibility path queries its
    template-simplifier setting on every call. This is very slow and should not be used in
    an inner loop. Create one `DemanglerConfig` with `DemanglerConfig.for_binary_view(view)`
    and pass it to `demangle_any` instead.

    Parameters:
    :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
          "binaryninja.architecture.Architecture") *|*
          [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")
          *|* [*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
          "binaryninja.demangle.DemanglerConfig")) – A prebuilt configuration, or an Architecture
          or Platform for the symbol
        - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled GNU3 name
        - **arch**

    Returns:
    :   returns a DemangleResult with type and name fields, or None on error

    Return type:
    :   *Optional*[[*DemangleResult*](#binaryninja.demangle.DemangleResult
        "binaryninja.demangle.DemangleResult")]

## demangle_llvm

demangle_llvm(*mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options: [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_llvm)
:   `demangle_llvm` demangles a mangled name using the LLVM demangler.

    Warning

    Passing a BinaryView through the legacy `options` compatibility path queries its
    template-simplifier setting on every call. This is very slow and should not be used in
    an inner loop. Create one `DemanglerConfig` with `DemanglerConfig.for_binary_view(view)`
    and pass it to `demangle_any` instead.

    Parameters:
    :   - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled (msvc/gnu3/rust/dlang) name
        - **options** (*Optional**[*[*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
          "binaryninja.demangle.DemanglerConfig")*]*) – a prebuilt demangler configuration

    Returns:
    :   returns a DemangleResult with type and name fields, or None on error

    Return type:
    :   *Optional*[[*DemangleResult*](#binaryninja.demangle.DemangleResult
        "binaryninja.demangle.DemangleResult")]

    Example:
    :   ```
        >>> config = DemanglerConfig.default()
        >>> demangle_llvm("?testf@Foobar@@SA?AW4foo@1@W421@@Z", config)
        DemangleResult(type=None, name='public: static enum Foobar::foo __cdecl Foobar::testf(enum Foobar::foo)')
        >>>
        ```

## demangle_ms

demangle_ms(*archOrPlatform: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [DemanglerConfig](#binaryninja.demangle.DemanglerConfig "binaryninja.demangle.DemanglerConfig")*, *mangled_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options=False*) → [DemangleResult](#binaryninja.demangle.DemangleResult "binaryninja.demangle.DemangleResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#demangle_ms)
:   `demangle_ms` demangles a mangled Microsoft Visual Studio C++ name to a Type object.

    Warning

    Passing a BinaryView through the legacy `options` compatibility path queries its
    template-simplifier setting on every call. This is very slow and should not be used in
    an inner loop. Create one `DemanglerConfig` with `DemanglerConfig.for_binary_view(view)`
    and pass it to `demangle_any` instead.

    Parameters:
    :   - **archOrPlatform**
          ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
          "binaryninja.architecture.Architecture") *|*
          [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")
          *|* [*DemanglerConfig*](#binaryninja.demangle.DemanglerConfig
          "binaryninja.demangle.DemanglerConfig")) – A prebuilt configuration, or an Architecture
          or Platform for the symbol
        - **mangled_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – a mangled Microsoft Visual Studio C++ name
        - **archOrPlatform**

    Returns:
    :   returns a DemangleResult with type and name fields, or None on error

    Return type:
    :   *Optional*[[*DemangleResult*](#binaryninja.demangle.DemangleResult
        "binaryninja.demangle.DemangleResult")]

    Example:
    :   ```
        >>> config = DemanglerConfig.for_platform(Architecture["x86_64"].standalone_platform)
        >>> demangle_ms(config, "?testf@Foobar@@SA?AW4foo@1@W421@@Z")
        DemangleResult(type=<type: immutable:FunctionTypeClass 'enum Foobar::foo __cdecl(enum Foobar::foo)'>, name='Foobar::testf')
        >>>
        ```

## simplify_demangled_template_name

simplify_demangled_template_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")[[source]](https://api.binary.ninja/_modules/binaryninja/demangle.html#simplify_demangled_template_name)
:   `simplify_demangled_template_name` simplifies standard-library template spelling in an
    already demangled qualified name.

    Parameters:
    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)") *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable
        "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
        Python v3.14)")*]* *|* [*QualifiedName*](types.md#binaryninja.types.QualifiedName
        "binaryninja.types.QualifiedName"))

    Return type:
    :   [*QualifiedName*](types.md#binaryninja.types.QualifiedName
        "binaryninja.types.QualifiedName")
