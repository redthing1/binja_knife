# platform module

| Class | Description |
| --- | --- |
| [`binaryninja.platform.CorePlatform`](#binaryninja.platform.CorePlatform "binaryninja.platform.CorePlatform") | `class Platform` contains all information related to the execution environment of the binary,… |
| [`binaryninja.platform.Platform`](#binaryninja.platform.Platform "binaryninja.platform.Platform") | `class Platform` contains all information related to the execution environment of the binary,… |

## CorePlatform

*class* CorePlatform[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#CorePlatform)
:   Bases: [`Platform`](#binaryninja.platform.Platform "binaryninja.platform.Platform")

    __init__(*handle: BNPlatform*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#CorePlatform.__init__)
    :   Parameters:
        :   **handle** (*BNPlatform*) –

    adjust_type_parser_input(*parser: [TypeParser](typeparser.md#binaryninja.typeparser.TypeParser "binaryninja.typeparser.TypeParser")*, *arguments: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *source_files: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]][[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#CorePlatform.adjust_type_parser_input)
    :   Modify the arguments passed to the Type Parser with Platform-specific features.

        Parameters:
        :   - **parser** ([*TypeParser*](typeparser.md#binaryninja.typeparser.TypeParser
              "binaryninja.typeparser.TypeParser")) – Type Parser instance
            - **arguments** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – Default arguments passed to the parser
            - **source_files** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]**]*) – Source file names and contents

        Returns:
        :   A tuple of (modified arguments, modified source files)

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")], [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
            "(in Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]]]

## Platform

*class* Platform[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    > `class Platform` contains all information related to the execution environment of the
    > binary, mainly the calling conventions used, the operating system, and the architecture.

    The following example showing the live list of platforms may not match your list. Some
    platforms are included only with specific versions of Binary Ninja and others are
    installed by plugins. The bare architecture version of the platform does not include any
    default ABI/calling convention:

    ```
    >>> list(Platform)
    [<platform: Solana>, <platform: decree-x86>, <platform: efi-aarch64>, <platform: efi-windows-aarch64>,
    <platform: efi-x86>, <platform: efi-windows-x86>, <platform: efi-x86_64>, <platform: efi-windows-x86_64>,
    <platform: efi-armv7>, <platform: efi-thumb2>, <platform: freebsd-aarch64>, <platform: freebsd-x86>,
    <platform: freebsd-x86_64>, <platform: freebsd-armv7>, <platform: freebsd-thumb2>, <platform: ios-aarch64>,
    <platform: ios-armv7>, <platform: ios-thumb2>, <platform: ios-kernel-aarch64>, <platform: ios-kernel-armv7>,
    <platform: ios-kernel-thumb2>, <platform: linux-aarch64>, <platform: linux-mcore_le>,
    <platform: linux-mcore_be>, <platform: linux-csky_le_v1>, <platform: linux-csky_le>, <platform: linux-armv7eb>,
    <platform: linux-thumb2eb>, <platform: linux-mips>, <platform: linux-mipsel>, <platform: linux-mips3>,
    <platform: linux-mipsel3>, <platform: linux-mips64>, <platform: linux-cnmips64>, <platform: linux-ppc32>,
    <platform: linux-ppc64>, <platform: linux-ppc32_le>, <platform: linux-ppc64_le>, <platform: linux-rv32gc>,
    <platform: linux-rv64gc>, <platform: linux-x86>, <platform: linux-x86_64>, <platform: linux-armv7>,
    <platform: linux-thumb2>, <platform: mac-aarch64>, <platform: mac-x86>, <platform: mac-x86_64>,
    <platform: mac-armv7>, <platform: mac-thumb2>, <platform: mac-kernel-aarch64>, <platform: mac-kernel-x86>,
    <platform: mac-kernel-x86_64>, <platform: mac-kernel-armv7>, <platform: mac-kernel-thumb2>,
    <platform: vxworks-aarch64>, <platform: vxworks-mips32>, <platform: vxworks-mipsel32>,
    <platform: vxworks-mips64>, <platform: vxworks-cavium-mips64>, <platform: vxworks-ppc32>,
    <platform: vxworks-ppc64>, <platform: vxworks-rv32gc>, <platform: vxworks-rv64gc>, <platform: vxworks-x86>,
    <platform: vxworks-x86_64>, <platform: vxworks-armv7>, <platform: vxworks-thumb2>, <platform: windows-aarch64>,
    <platform: windows-x86>, <platform: windows-x86_64>, <platform: windows-armv7>, <platform: windows-thumb2>,
    <platform: windows-kernel-windows-aarch64>, <platform: windows-kernel-x86>, <platform: windows-kernel-x86_64>]
    >>> thumb2 = Platform["thumb2"]
    ```

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.__init__)
    :   Parameters:
        :   **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture") *|* *None*) –

    add_related_platform(*arch*, *platform*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.add_related_platform)

    adjust_type_parser_input(*parser: [TypeParser](typeparser.md#binaryninja.typeparser.TypeParser "binaryninja.typeparser.TypeParser")*, *arguments: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *source_files: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]][[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.adjust_type_parser_input)
    :   Modify the arguments passed to the Type Parser with Platform-specific features.

        Parameters:
        :   - **parser** ([*TypeParser*](typeparser.md#binaryninja.typeparser.TypeParser
              "binaryninja.typeparser.TypeParser")) – Type Parser instance
            - **arguments** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – Default arguments passed to the parser
            - **source_files** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]**]*) – Source file names and contents

        Returns:
        :   A tuple of (modified arguments, modified source files)

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")], [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
            "(in Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]]]

    generate_auto_platform_type_id(*name*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.generate_auto_platform_type_id)

    generate_auto_platform_type_ref(*type_class*, *name*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.generate_auto_platform_type_ref)

    get_associated_platform_by_address(*addr*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_associated_platform_by_address)

    get_auto_platform_type_id_source()[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_auto_platform_type_id_source)

    get_function_by_name(*name*, *exactMatch=False*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_function_by_name)

    get_global_register_type(*reg: architecture.RegisterType*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_global_register_type)
    :   Parameters:
        :   **reg** (*architecture.RegisterType*) –

    *classmethod* get_list(*os=None*, *arch=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_list)

    get_related_platform(*arch*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_related_platform)

    get_related_platforms() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Platform](#binaryninja.platform.Platform "binaryninja.platform.Platform")][[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_related_platforms)
    :   `get_related_platforms` returns a list of all related platforms for a given platform

        Returns:

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Platform*](#binaryninja.platform.Platform "binaryninja.platform.Platform")]

    get_system_call_name(*number*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_system_call_name)

    get_system_call_type(*number*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_system_call_type)

    get_type_by_name(*name*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_type_by_name)

    get_type_libraries_by_name(*name*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")][[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_type_libraries_by_name)
    :   Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")]

    get_variable_by_name(*name*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.get_variable_by_name)

    parse_types_from_source(*source*, *filename=None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto_type_source=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.parse_types_from_source)
    :   `parse_types_from_source` parses the source string and any needed headers searching for
        them in the optional list of directories provided in `include_dirs`. Note that this API
        does not allow the source to rely on existing types that only exist in a specific view.
        Use `BinaryView.parse_type_string` instead.

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – source string to be parsed
            - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – optional source filename
            - **include_dirs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*)*) – optional list of string filename include directories
            - **auto_type_source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – optional source of types if used for automatically generated types

        Returns:
        :   `BasicTypeParserResult` (a SyntaxError is thrown on parse error)

        Return type:
        :   [*BasicTypeParserResult*](typeparser.md#binaryninja.typeparser.BasicTypeParserResult
            "binaryninja.typeparser.BasicTypeParserResult")

        Example:
        :   ```
            >>> platform.parse_types_from_source('int foo;\nint bar(int x);\nstruct bas{int x,y;};\n')
            ({types: {'bas': <type: struct bas>}, variables: {'foo': <type: int32_t>}, functions:{'bar':
            <type: int32_t(int32_t x)>}}, '')
            >>>
            ```

    parse_types_from_source_file(*filename*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto_type_source=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.parse_types_from_source_file)
    :   `parse_types_from_source_file` parses the source file `filename` and any needed headers
        searching for them in the optional list of directories provided in `include_dirs`. Note
        that this API does not allow the source to rely on existing types that only exist in a
        specific view. Use `BinaryView.parse_type_string` instead.

        Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – filename of file to be parsed
            - **include_dirs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*)*) – optional list of string filename include directories
            - **auto_type_source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – optional source of types if used for automatically generated types

        Returns:
        :   `BasicTypeParserResult` (a SyntaxError is thrown on parse error)

        Return type:
        :   [*BasicTypeParserResult*](typeparser.md#binaryninja.typeparser.BasicTypeParserResult
            "binaryninja.typeparser.BasicTypeParserResult")

        Example:
        :   ```
            >>> file = "/Users/binja/tmp.c"
            >>> open(file).read()
            'int foo;\nint bar(int x);\nstruct bas{int x,y;};\n'
            >>> platform.parse_types_from_source_file(file)
            ({types: {'bas': <type: struct bas>}, variables: {'foo': <type: int32_t>}, functions:
            {'bar': <type: int32_t(int32_t x)>}}, '')
            >>>
            ```

    register(*os*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.register)
    :   `register` registers the platform for given OS name.

        Parameters:
        :   **os** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – OS name to register

        Return type:
        :   *None*

    register_calling_convention(*cc*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.register_calling_convention)
    :   `register_calling_convention` register a new calling convention.

        Parameters:
        :   **cc**
            ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention")) – a CallingConvention object to
            register

        Return type:
        :   *None*

    view_init(*view*)[[source]](https://api.binary.ninja/_modules/binaryninja/platform.html#Platform.view_init)

    *property* address_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* arch

    *property* calling_conventions
    :   List of platform CallingConvention objects (read-only)

        Getter:
        :   returns the list of supported CallingConvention objects

        Type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention"))

    *property* cdecl_calling_convention
    :   CallingConvention object for the cdecl calling convention

    *property* default_calling_convention
    :   Default calling convention.

        Getter:
        :   returns a CallingConvention object for the default calling convention.

        Setter:
        :   sets the default calling convention

        Type:
        :   [*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention")

    *property* fastcall_calling_convention
    :   CallingConvention object for the fastcall calling convention

    *property* functions
    :   List of platform-specific function definitions (read-only)

    global_reg_types *= {}*

    global_regs *= []*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *class property* os_list*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Built-in mutable sequence.

        If no argument is given, the constructor creates a new empty list. The argument must be
        an iterable if specified.

    *property* stdcall_calling_convention
    :   CallingConvention object for the stdcall calling convention

    *property* system_call_convention
    :   CallingConvention object for the system call convention

    *property* system_calls
    :   List of system calls for this platform (read-only)

    *property* type_container*: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*
    :   Type Container for all registered types in the Platform. :return: Platform types Type
        Container

    type_file_path *= None*

    type_include_dirs *= []*

    *property* type_libraries*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")]*

    *property* types
    :   List of platform-specific types (read-only)

    *property* variables
    :   List of platform-specific variable definitions (read-only)
