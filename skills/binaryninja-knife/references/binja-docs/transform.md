# transform module

| Class | Description |
| --- | --- |
| [`binaryninja.transform.Transform`](#binaryninja.transform.Transform "binaryninja.transform.Transform") | `class Transform` allows users to implement custom transformations. New transformations may be… |
| [`binaryninja.transform.TransformContext`](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext") | `TransformContext` represents a node in the container extraction tree, containing the input… |
| [`binaryninja.transform.TransformParameter`](#binaryninja.transform.TransformParameter "binaryninja.transform.TransformParameter") |  |
| [`binaryninja.transform.TransformSession`](#binaryninja.transform.TransformSession "binaryninja.transform.TransformSession") | `TransformSession` manages the extraction workflow for container files (ZIP, TAR, IMG4, etc.),… |
| [`binaryninja.transform.ZipPython`](#binaryninja.transform.ZipPython "binaryninja.transform.ZipPython") | Reference implementation of a ZIP container transform using Python’s zipfile module. |

## Transform

*class* Transform[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class Transform` allows users to implement custom transformations. New transformations
    may be added at runtime, so an instance of a transform is created like:

    ```
    >>> list(Transform)
    [<transform: Zlib>, <transform: StringEscape>, <transform: RawHex>, <transform: HexDump>, <transform: Base64>, <transform: Reverse>, <transform: CArray08>, <transform: CArrayA16>, <transform: CArrayA32>, <transform: CArrayA64>, <transform: CArrayB16>, <transform: CArrayB32>, <transform: CArrayB64>, <transform: IntList08>, <transform: IntListA16>, <transform: IntListA32>, <transform: IntListA64>, <transform: IntListB16>, <transform: IntListB32>, <transform: IntListB64>, <transform: MD4>, <transform: MD5>, <transform: SHA1>, <transform: SHA224>, <transform: SHA256>, <transform: SHA384>, <transform: SHA512>, <transform: AES-128 ECB>, <transform: AES-128 CBC>, <transform: AES-256 ECB>, <transform: AES-256 CBC>, <transform: DES ECB>, <transform: DES CBC>, <transform: Triple DES ECB>, <transform: Triple DES CBC>, <transform: RC2 ECB>, <transform: RC2 CBC>, <transform: Blowfish ECB>, <transform: Blowfish CBC>, <transform: CAST ECB>, <transform: CAST CBC>, <transform: RC4>, <transform: XOR>]
    >>> sha512=Transform['SHA512']
    >>> rawhex=Transform['RawHex']
    >>> rawhex.encode(sha512.encode("test string"))
    '10e6d647af44624442f388c2c14a787ff8b17e6165b83d767ec047768d8cbcb71a1a3226e7cc7816bc79c0427d94a9da688c41a3992c7bf5e4d7cc3e0be5dbac'
    ```

    Note that some transformations take additional parameters (most notably encryption ones
    that require a ‘key’ parameter passed via a dict):

    ```
    >>> xor=Transform['XOR']
    >>> rawhex=Transform['RawHex']
    >>> xor.encode("Original Data", {'key':'XORKEY'})
    >>> rawhex.encode(xor.encode("Original Data", {'key':'XORKEY'}))
    b'173d3b2c2c373923720f242d39'
    ```

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.__init__)

    can_decode(*input*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.can_decode)
    :   `can_decode` checks if this transform can decode the given input.

        Parameters:
        :   **input** – can be a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes
            "(in Python v3.14)"),
            [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python
            v3.14)"), `DataBuffer`, or `BinaryView`

        Returns:
        :   [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
            indicating whether the transform can decode the input

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    decode(*input_buf*, *params={}*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.decode)

    decode_with_context(*context*, *params={}*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.decode_with_context)
    :   `decode_with_context` performs context-aware transformation for container formats,
        enabling multi-file extraction

        **Processing Protocol:**

        Container transforms typically operate in two phases:

        1. **Discovery Phase**: Transform enumerates available files and populates
           `context.available_files`. Returns `False` to indicate user file selection is required.
        2. **Extraction Phase**: Transform processes `context.requested_files` and creates child
           contexts for each file with extraction results. Returns `True` when extraction is
           complete.

        **Return Value Semantics:**

        - `True`: Processing complete, no more user interaction needed
        - `False`: Processing incomplete, requires user input or session management (e.g., file
          selection after discovery)

        **Error Reporting:**

        Extraction results and messages are accessible via context properties:

        - **Context-level** (transformation/extraction status): - `context.extraction_result`:
          Result of parent producing input - `context.extraction_message`: Human-readable
          extraction message - `context.transform_result`: Result of applying transform to input

        Common error scenarios:

        > - Archive encrypted, password required
        > - Corrupt archive structure
        > - Unsupported archive format
        > - Individual file extraction failures

        **Usage Examples:**

        ```
        from binaryninja import TransformSession

        # Full mode - automatically extracts all files
        session = TransformSession("archive.zip")
        if session.process(): # All extraction complete, no interaction needed
                # Select the intended context(s) for loading
                session.set_selected_contexts(session.current_context)
                # Load the resulting BinaryView(s)
                loaded_view = load(session.current_view)
        else:
                # Extraction incomplete - user input required
                print("Extraction requires user input")

        # Interactive mode - requires manual processing for each step
        session = TransformSession("nested.zip")
        while not session.process():
                # Process returned False - user input needed
                ctx = session.current_context

                # Check if parent has available files for selection
                if ctx.parent and ctx.parent.has_available_files:
                        # Show files to user and let them select
                        available = ctx.parent.available_files
                        print(f"Available files: {available}")

                        # Select files to extract (or all)
                        ctx.parent.set_requested_files(available)

                        # Continue processing from parent
                        session.process_from(ctx.parent)

        # Extraction complete - select and load the final context
        session.set_selected_contexts(session.current_context)
        final_view = session.current_view
        ```

        Parameters:
        :   - **context** ([*TransformContext*](#binaryninja.transform.TransformContext
              "binaryninja.transform.TransformContext")) – Transform context containing input data and
              state
            - **params** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
              v3.14)")) – Optional transform parameters (e.g., passwords, settings)

        Returns:
        :   True if processing complete, False if user input required

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    encode(*input_buf*, *params={}*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.encode)

    *abstract* perform_decode(*data*, *params*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.perform_decode)

    perform_decode_with_context(*context*, *params*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.perform_decode_with_context)

    *abstract* perform_encode(*data*, *params*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.perform_encode)

    *classmethod* register()[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#Transform.register)

    capabilities *= 0*

    group *= None*

    long_name *= None*

    name *= None*

    parameters *= []*

    supports_detection *= False*

    transform_type *= None*

## TransformContext

*class* TransformContext[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `TransformContext` represents a node in the container extraction tree, containing the
    input data, transformation state, and relationships to parent/child contexts.

    Each context can have:

    > - Input data (BinaryView)
    > - Transform information (name, parameters, results)
    > - File selection state (available_files, requested_files)
    > - Parent/child relationships for nested containers
    > - Extraction status and error messages

    Contexts are typically accessed through a `TransformSession` rather than created
    directly.

    **Example:**

    ```
    session = TransformSession("archive.zip")
    session.process()

    # Access context properties
    ctx = session.current_context
    print(f"Filename: {ctx.filename}")
    print(f"Transform: {ctx.transform_name}")
    print(f"Size: {ctx.input.length}")

    # Navigate the tree
    if ctx.parent:
            print(f"Parent files: {ctx.parent.available_files}")

    # Check extraction status
    if ctx.extraction_result != 0:
            print(f"Error: {ctx.extraction_message}")
    ```

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.__init__)

    clear_transform_parameter(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.clear_transform_parameter)
    :   Clear a transform parameter

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    create_child(*data: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*, *filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *result: [TransformResult](enums.md#binaryninja.enums.TransformResult "binaryninja.enums.TransformResult") = TransformResult.TransformSuccess*, *message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *filename_is_descriptor: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.create_child)
    :   Create a new child context with the given data, filename, result status, and message

        Parameters:
        :   - **data** ([*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer")) – The data for the child context
            - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The filename for the child context (default: “”)
            - **result** ([*TransformResult*](enums.md#binaryninja.enums.TransformResult
              "binaryninja.enums.TransformResult")) – Transform result for the child (default:
              TransformResult.TransformSuccess)
            - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Extraction message for the child (default: “”)
            - **filename_is_descriptor**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –
              Whether the filename is a descriptor that should be combined with parent (default:
              False)

        Return type:
        :   [*TransformContext*](#binaryninja.transform.TransformContext
            "binaryninja.transform.TransformContext")

    get_child(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.get_child)
    :   Get a child context by filename

        Parameters:
        :   **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*TransformContext*](#binaryninja.transform.TransformContext
            "binaryninja.transform.TransformContext") | *None*

    has_transform_parameter(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.has_transform_parameter)
    :   Check if a transform parameter exists

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_available_files(*files: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.set_available_files)
    :   Populate the list of files available for extraction (Discovery Phase).

        Container transforms call this during the **Discovery Phase** to enumerate files without
        extracting them. After calling this, the transform should return `False` to indicate
        user selection is needed.

        **Session Mode Handling:**

        - **Full Mode**: Session automatically calls `set_requested_files(available_files)` and
          re-invokes the transform for extraction, so all files are extracted in one pass.
        - **Interactive Mode**: Transform returns `False`, user must call `set_requested_files()`
          manually, then call `process_from()` to continue.

        Parameters:
        :   **files** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – List of filenames that can be extracted from this container

    set_requested_files(*files: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.set_requested_files)
    :   Specify which files to extract from this container (Extraction Phase).

        Call this after `available_files` has been populated to indicate which files should be
        extracted. After setting this, call `session.process_from(context)` to perform the
        extraction.

        **Mode Behavior:**

        - **Full Mode**: Called automatically by the session with all available files, you rarely
          need to call this.
        - **Interactive Mode**: You must call this manually to select which files to extract.

        Parameters:
        :   **files** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – List of filenames to extract (must be subset of `available_files`)

    set_transform_name(*transform_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.set_transform_name)
    :   Manually specify which transform to apply to this context.

        Use this when auto-detection is not possible or when you want to override the detected
        transform. This is commonly needed for formats without magic bytes (like Base64) or when
        forcing a specific decoder.

        After setting the transform name, call `session.process_from(context)` to apply the
        transform.

        Parameters:
        :   **transform_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")) – Name of the transform to apply (e.g., “Base64”, “Gzip”, “XOR”)

        **Example:**

        ```
        # Base64 has no magic bytes, so it's not auto-detected
        session = TransformSession("data.zip")
        session.process()

        ctx = session.current_context
        ctx.set_transform_name("Base64") # Manually specify Base64

        # Now apply the Base64 transform
        if session.process_from(ctx):
                print("Base64 decoded successfully")
        ```

    set_transform_parameter(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *data: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformContext.set_transform_parameter)
    :   Set a parameter for the transform (e.g., password, encryption key).

        Transform parameters provide additional input required for decoding, such as passwords
        for encrypted archives or keys for encryption transforms. Parameters are passed to the
        transform’s decode operation.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Parameter name (e.g., “password”, “key”)
            - **data** ([*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer")) – Parameter value as a DataBuffer

        **Example:**

        ```
        # Create session and attempt extraction
        session = TransformSession("encrypted.zip")
        session.process() # Returns False - processing incomplete

        # Check why extraction failed
        if session.current_context.extraction_result == TransformResult.TransformRequiresPassword:
                # Password is set on the parent context (the one doing extraction)
                parent = session.current_context.parent
                parent.set_transform_parameter("password", DataBuffer("secret_password"))

                # Retry extraction from parent
                if session.process_from(parent):
                        # Verify successful extraction
                        assert parent.children[0].extraction_result == TransformResult.TransformSuccess
                        print("Archive decrypted successfully")
        ```

    *property* available_files*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get the list of files available for extraction from this container.

        This property is populated during the **Discovery Phase** of container extraction, when
        a transform enumerates the contents of an archive without extracting them.

        **Mode Behavior:**

        - **Full Mode (default)**: Discovery and extraction happen automatically in one pass.
          After `process()`, `available_files` will be populated on the container context (the one
          with the archive transform), and all files will already be extracted.
        - **Interactive Mode**: Discovery pauses for user selection. After first `process()`,
          `available_files` is populated on the parent context (the container), and you must call
          `set_requested_files()` before extraction proceeds.

        Returns:
        :   List of filenames that can be extracted from this container

        Return type:
        :   *List*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]

        **Example (Full Mode - Automatic):**

        ```
        # Full mode (default) - all files extracted automatically
        session = TransformSession("archive.zip")
        session.process() # Discovery + extraction in one pass

        # After processing, available_files shows what was discovered on the container
        # For a root-level archive, this is the root context
        container = session.root_context
        print(f"Extracted {len(container.available_files)} files")
        print(f"Files: {container.available_files[:5]}...")
        ```

        **Example (Interactive Mode - User Selection):**

        ```
        # Interactive mode - user selects files
        session = TransformSession("archive.zip", mode=TransformSessionMode.TransformSessionModeInteractive)
        session.process() # Discovery phase only - returns False

        # available_files is on the parent (the container doing extraction)
        container = session.current_context.parent
        if container.has_available_files:
                print(f"Archive contains {len(container.available_files)} files")
                print(f"Files: {container.available_files[:5]}...")

                # User selects which files to extract
                container.set_requested_files(["important.bin", "config.txt"])

                # Extract selected files
                session.process_from(container)
        ```

    *property* available_transforms*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get the list of transforms that can decode this context’s input.

        Binary Ninja auto-detects which transforms can handle the current data by checking each
        transform’s `can_decode()` method. This property returns the names of all transforms
        that reported they can decode this context’s input.

        Returns:
        :   List of transform names that can decode this data

        Return type:
        :   *List*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]

    *property* child_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Get the number of child contexts

    *property* children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext")]*
    :   Get all child contexts

    *property* extraction_message*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the extraction message

    *property* extraction_result*: [TransformResult](enums.md#binaryninja.enums.TransformResult "binaryninja.enums.TransformResult")*
    :   Get the extraction result

    *property* filename*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the filename for this context

    *property* has_available_files*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this context has available files for selection

    *property* has_requested_files*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this context has requested files

    *property* input*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the input BinaryView for this context

    *property* is_database*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this context represents a database file

    *property* is_interactive*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this context is in interactive mode.

        This flag indicates whether the transform session is operating in interactive mode
        (e.g., UI with user dialogs) or non-interactive mode (e.g., headless/auto-open).
        Transforms can use this to adjust their behavior. For example, filtering children in
        non-interactive mode while showing all children in interactive mode.

        Returns:
        :   True if in interactive mode, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* is_leaf*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this context is a leaf (has no children)

    *property* is_root*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this context is the root (has no parent)

    *property* metadata_obj*: [Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the metadata associated with this extraction context.

        Container transforms can store format-specific metadata during extraction (e.g.,
        timestamps, permissions, compression ratios, archive structure). This metadata is
        preserved in the context tree and can be accessed for analysis or debugging.

        Returns:
        :   Metadata object containing transform-specific key-value pairs, or None if no metadata

        Return type:
        :   [*Metadata*](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata")
            or *None*

    *property* parent*: [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the parent context

    *property* requested_files*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Get the list of files requested for extraction from this container.

        This property contains the filenames that have been selected for extraction during the
        **Extraction Phase**. Container transforms read this property to determine which files
        to extract and create child contexts for.

        Returns:
        :   List of filenames requested for extraction

        Return type:
        :   *List*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]

    *property* settings*: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*
    :   Get the settings object for this transform context.

        This provides access to session-time settings overrides passed via the
        `TransformSession` `options` parameter. These ephemeral settings override global
        settings for this session only. Transforms should use this Settings object instead of
        `Settings()` to read settings values that may have been overridden for the session.

        Returns:
        :   Settings object

        Return type:
        :   [*Settings*](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")

    *property* transform_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the name of the transform that created this context

    *property* transform_result*: [TransformResult](enums.md#binaryninja.enums.TransformResult "binaryninja.enums.TransformResult")*
    :   Get the transform result

## TransformParameter

*class* TransformParameter[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformParameter)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*name*, *long_name=None*, *fixed_length=0*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformParameter.__init__)

    *property* fixed_length
    :   (read-only)

    *property* long_name
    :   (read-only)

    *property* name
    :   (read-only)

## TransformSession

*class* TransformSession[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformSession)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `TransformSession` manages the extraction workflow for container files (ZIP, TAR, IMG4,
    etc.), handling multi-stage extraction, file selection, and transform application.

    Sessions automatically detect and apply appropriate transforms to navigate through
    nested containers, maintaining a tree of `TransformContext` objects representing each
    extraction stage.

    Parameters:
    :   - **filename_or_view**
          (*Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")*,* *'binaryview.BinaryView'**]*) – Path to the file to process, or an existing
          BinaryView to start from.
        - **mode** ([*TransformSessionMode*](enums.md#binaryninja.enums.TransformSessionMode
          "binaryninja.enums.TransformSessionMode")) – Session mode controlling extraction
          behavior. Can be `TransformSessionMode.Full` (automatic),
          `TransformSessionMode.Interactive` (requires user selection), or None to use the default
          mode from settings. Defaults to None.
        - **options** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
          v3.14)")) – Dictionary of session-time settings overrides that apply only to this
          session. These ephemeral settings override global settings and are accessible to
          transforms via `TransformContext.settings`. For example,
          `{'files.universal.architecturePreference': ['x86_64']}` to prefer x86_64 when opening
          universal binaries. Defaults to empty dict.

    **Modes:**

    - **Full Mode** (default): Automatically extracts all files through nested containers
    - **Interactive Mode**: Requires user file selection at each stage

    **Basic Usage:**

    ```
    from binaryninja import TransformSession

    # Full automatic extraction
    session = TransformSession("archive.zip")
    if session.process():
            final_data = session.current_view
            load(final_data)
    ```

    **Interactive Extraction:**

    ```
    session = TransformSession("nested_archive.zip")
    while not session.process():
            # User input needed
            ctx = session.current_context
            if ctx.parent and ctx.parent.has_available_files:
                    # Show file choices to user
                    print(f"Available: {ctx.parent.available_files}")

                    # User selects files
                    ctx.parent.set_requested_files(["important_file.bin"])

                    # Continue extraction
                    session.process_from(ctx.parent)

    # Access final extracted data
    session.set_selected_contexts(session.current_context)
    final_view = session.current_view
    ```

    **Key Methods:**

    - `process()`: Process the next extraction stage
    - `process_from(context)`: Resume processing from a specific context
    - `set_selected_contexts(contexts)`: Mark contexts for final access

    **Key Properties:**

    - `current_context`: The current point in the extraction tree
    - `current_view`: The current BinaryView (after processing)
    - `root_context`: The root of the extraction tree

    __init__(*filename_or_view: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *mode=None*, *options: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] = {}*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformSession.__init__)
    :   Parameters:
        :   - **filename_or_view** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **options** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) –

    process() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformSession.process)
    :   Process the transform session from the root context.

        Returns:
        :   `True` if processing completed successfully (all transforms applied and no user input
            required). `False` if processing is incomplete and requires user input (file selection,
            password), additional parameters, or if an error occurred during transformation.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        In **Full Mode** (default), automatically processes the entire container tree. In
        **Interactive Mode**, processes one stage at a time, returning `False` when user input
        is needed. In **Disabled Mode**, immediately returns `True` without processing.

        Common reasons for returning `False`:

        - Container has multiple files and user must select which to extract
        - Archive is password-protected and no valid password was provided
        - Transform requires additional parameters
        - Transform encountered an error during processing

    process_from(*context: [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformSession.process_from)
    :   Process the transform session starting from a specific context.

        Returns:
        :   `True` if processing completed successfully (all transforms applied and no user input
            required). `False` if processing is incomplete and requires user input (file selection,
            password), additional parameters, or if an error occurred during transformation.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Parameters:
        :   **context** ([*TransformContext*](#binaryninja.transform.TransformContext
            "binaryninja.transform.TransformContext")) –

        In **Interactive Mode**, this returns `False` when user selection is needed at the
        current stage. In **Full Mode**, this recursively processes all child contexts and
        returns `False` if any stage is incomplete.

    set_interactive(*interactive: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformSession.set_interactive)
    :   Set whether this session is running in interactive mode.

        This flag allows transforms to adjust their behavior: in interactive mode, transforms
        typically expose all available children and options. In non-interactive mode, transforms
        may filter children based on settings preferences or apply automatic selections.

        Call this before `process()` to establish the session’s mode.

        Parameters:
        :   **interactive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
            Python v3.14)")) – True for interactive mode (UI), False for non-interactive
            (headless/scripting)

    set_selected_contexts(*contexts: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext")] | [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext")*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#TransformSession.set_selected_contexts)
    :   Mark contexts as selected for analysis and resource management. This allows Binary Ninja
        to release resources for unselected branches of the extraction tree.

        Parameters:
        :   **contexts** ([*TransformContext*](#binaryninja.transform.TransformContext
            "binaryninja.transform.TransformContext") *or*
            *List**[*[*TransformContext*](#binaryninja.transform.TransformContext
            "binaryninja.transform.TransformContext")*]*) – Single context or list of contexts to
            mark as selected. All other contexts will be unselected.

        **Example:**

        ```
        session = TransformSession("archive.tar.gz")
        if session.process():
                # Mark the final extracted file for loading
                session.set_selected_contexts(session.current_context)

                # Now load it
                with load(session.current_view) as bv:
                        print(f"Loaded: {bv.file.virtual_path}")
        ```

    *property* current_context*: [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the current transform context

    *property* current_view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the current BinaryView for this session

    *property* has_any_stages*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this session has any processing stages

    *property* has_single_path*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this session has a single processing path

    *property* root_context*: [TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the root transform context

    *property* selected_contexts*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TransformContext](#binaryninja.transform.TransformContext "binaryninja.transform.TransformContext")]*
    :   Get the currently selected contexts.

        Selected contexts are the extraction outputs that will be loaded into Binary Ninja for
        analysis. Use `set_selected_contexts()` to mark which contexts should be kept active.

## ZipPython

*class* ZipPython[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#ZipPython)
:   Bases: [`Transform`](#binaryninja.transform.Transform "binaryninja.transform.Transform")

    Reference implementation of a ZIP container transform using Python’s zipfile module.

    This transform demonstrates the Container Transform API including two-phase extraction
    (discovery and extraction), multi-file support, password handling, and result reporting.

    ```
    >>> from binaryninja.transform import ZipPython
    >>> ZipPython.register()
    >>> session = TransformSession("Archive.zip")
    >>> session.root_context.available_transforms
    >>> ['Zip', 'ZipPython']
    ```

    can_decode(*input*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#ZipPython.can_decode)
    :   Detect ZIP archives by checking for “PK” magic bytes and valid ZIP signature.

        Checks the first 4 bytes for ZIP file signatures (local file header, central directory,
        etc.).

        Parameters:
        :   **input** – BinaryView to check

        Returns:
        :   True if valid ZIP archive

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_decode(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *params: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#ZipPython.perform_decode)
    :   Extract a single file from a ZIP archive.

        Extracts the file specified in params[‘filename’], or the first file if not specified.
        For multi-file extraction and password handling, use `perform_decode_with_context()`.

        Parameters:
        :   - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – Raw ZIP archive bytes
            - **params** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
              v3.14)")) – May contain ‘filename’ key

        Returns:
        :   Extracted file data, or None on failure

        Return type:
        :   [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") |
            *None*

    perform_decode_with_context(*context*, *params*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#ZipPython.perform_decode_with_context)
    :   Extract files from a ZIP archive using two-phase container extraction.

        **Phase 1 (Discovery):** Enumerates files and populates `context.available_files`.
        Returns False for user file selection.

        **Phase 2 (Extraction):** Extracts files from `context.requested_files`, trying
        passwords from params[‘password’] and `files.container.defaultPasswords` setting.
        Creates child contexts for each file with appropriate result codes.

        Parameters:
        :   - **context** – Transform context with input data and file selection state
            - **params** – May contain ‘password’ key for encrypted archives

        Returns:
        :   True if all extractions succeeded, False if user input needed or extraction failed

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_encode(*data*, *params*)[[source]](https://api.binary.ninja/_modules/binaryninja/transform.html#ZipPython.perform_encode)

    capabilities *= 3*

    group *= 'Container'*

    long_name *= 'Zip (Python)'*

    name *= 'ZipPython'*

    transform_type *= 3*
