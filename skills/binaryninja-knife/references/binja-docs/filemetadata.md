# filemetadata module

| Class | Description |
| --- | --- |
| [`binaryninja.filemetadata.FileMetadata`](#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata") | `class FileMetadata` represents the file being analyzed by Binary Ninja. It is responsible for… |
| [`binaryninja.filemetadata.NavigationHandler`](#binaryninja.filemetadata.NavigationHandler "binaryninja.filemetadata.NavigationHandler") |  |
| [`binaryninja.filemetadata.SaveSettings`](#binaryninja.filemetadata.SaveSettings "binaryninja.filemetadata.SaveSettings") | `class SaveSettings` is used to specify actions and options that apply to saving a database… |

## FileMetadata

*class* FileMetadata[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FileMetadata` represents the file being analyzed by Binary Ninja. It is
    responsible for opening, closing, creating the database (.bndb) files, and is used to
    keep track of undoable actions.

    Parameters:
    :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – The string path to the file to be opened. Defaults to None.
        - **handle** – A handle to the underlying C FileMetadata object. Defaults to None.
          (Internal use only.)

    __init__(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: LP_BNFileMetadata | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.__init__)
    :   Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)
            - **handle** (*LP_BNFileMetadata* *|* *None*)

    begin_undo_actions(*anonymous_allowed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.begin_undo_actions)
    :   `begin_undo_actions` starts recording actions taken so they can be undone at some point.

        Parameters:
        :   **anonymous_allowed** ([*bool*](https://docs.python.org/3/library/functions.html#bool
            "(in Python v3.14)")) – Legacy interop: prevent empty calls to
            [`commit_undo_actions`](#binaryninja.filemetadata.FileMetadata.commit_undo_actions
            "binaryninja.filemetadata.FileMetadata.commit_undo_actions") from affecting this undo
            state. Specifically for
            [`undoable_transaction`](#binaryninja.filemetadata.FileMetadata.undoable_transaction
            "binaryninja.filemetadata.FileMetadata.undoable_transaction")

        Returns:
        :   Id of undo state, for passing to
            [`commit_undo_actions`](#binaryninja.filemetadata.FileMetadata.commit_undo_actions
            "binaryninja.filemetadata.FileMetadata.commit_undo_actions") or
            [`revert_undo_actions`](#binaryninja.filemetadata.FileMetadata.revert_undo_actions
            "binaryninja.filemetadata.FileMetadata.revert_undo_actions").

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.commit_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>>
            ```

    close() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.close)
    :   Closes the underlying file handle. It is recommended that this is done in a finally
        clause to avoid handle leaks.

        Return type:
        :   *None*

    commit_undo_actions(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.commit_undo_actions)
    :   `commit_undo_actions` commits the actions taken since a call to
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions") Pass as id the value
        returned by
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions"). Empty values of id will
        commit all changes since the last call to
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions").

        Parameters:
        :   **id** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – id of undo state, from
            [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
            "binaryninja.filemetadata.FileMetadata.begin_undo_actions")

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.commit_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>>
            ```

    create_database(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *settings: [SaveSettings](#binaryninja.filemetadata.SaveSettings "binaryninja.filemetadata.SaveSettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.create_database)
    :   `create_database` writes the current database (.bndb) out to the specified file.

        Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – path and filename to write the bndb to, this string should have “.bndb”
              appended to it.
            - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count.
            - **settings** ([*SaveSettings*](#binaryninja.filemetadata.SaveSettings
              "binaryninja.filemetadata.SaveSettings")) – optional argument for special save options.

        Returns:
        :   true on success, false on failure

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Note

        The progress_func callback **must** return True to continue the save operation, False
        will abort the save operation.

        Warning

        The calling thread must not hold a lock on the BinaryView instance as this action is run
        on the main thread which requires the lock.

        Example:
        :   ```
            >>> settings = SaveSettings()
            >>> bv.file.create_database(f"{bv.file.filename}.bndb", None, settings)
            True
            ```

        Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*)
            - **settings** ([*SaveSettings*](#binaryninja.filemetadata.SaveSettings
              "binaryninja.filemetadata.SaveSettings") *|* *None*)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    forget_undo_actions(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.forget_undo_actions)
    :   `forget_undo_actions` removes the actions taken since a call to
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions") Pass as id the value
        returned by
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions"). Empty values of id will
        remove all changes since the last call to
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions").

        Parameters:
        :   **id** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – id of undo state, from
            [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
            "binaryninja.filemetadata.FileMetadata.begin_undo_actions")

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.forget_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>>
            ```

    get_view_of_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.get_view_of_type)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView") | *None*

    navigate(*view: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.navigate)
    :   `navigate` navigates the UI to the specified virtual address

        Note

        Despite the confusing name, `view` in this context is not a BinaryView but rather a
        string describing the different UI Views. Check
        [`view`](#binaryninja.filemetadata.FileMetadata.view
        "binaryninja.filemetadata.FileMetadata.view") while in different views to see examples
        such as `Linear:ELF`, `Graph:PE`.

        Parameters:
        :   - **view** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – view name
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address to navigate to

        Returns:
        :   whether or not navigation succeeded

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> import random
            >>> bv.navigate(bv.view, random.choice(list(bv.functions)).start)
            True
            ```

    redo() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.redo)
    :   `redo` redo the last committed transaction in the undo database.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)
            True
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> bv.redo()
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>>
            ```

    reopen_moved_database(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.reopen_moved_database)
    :   `reopen_moved_database` reopens the database backing this file metadata from a new path.

        Parameters:
        :   **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – path and filename to the moved bndb.

        Returns:
        :   true on success, false on failure

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    revert_undo_actions(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.revert_undo_actions)
    :   `revert_undo_actions` reverts the actions taken since a call to
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions") Pass as id the value
        returned by
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions"). Empty values of id will
        revert all changes since the last call to
        [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
        "binaryninja.filemetadata.FileMetadata.begin_undo_actions").

        Parameters:
        :   **id** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – id of undo state, from
            [`begin_undo_actions`](#binaryninja.filemetadata.FileMetadata.begin_undo_actions
            "binaryninja.filemetadata.FileMetadata.begin_undo_actions")

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.revert_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>>
            ```

    save_auto_snapshot(*progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *settings: [SaveSettings](#binaryninja.filemetadata.SaveSettings "binaryninja.filemetadata.SaveSettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.save_auto_snapshot)
    :   Parameters:
        :   - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*)
            - **settings** ([*SaveSettings*](#binaryninja.filemetadata.SaveSettings
              "binaryninja.filemetadata.SaveSettings") *|* *None*)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *static* set_default_session_data(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.set_default_session_data)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **value** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)"))

        Return type:
        :   *None*

    undo() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.undo)
    :   `undo` undo the last committed transaction in the undo database.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)
            True
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> bv.redo()
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>>
            ```

    undoable_transaction() → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#FileMetadata.undoable_transaction)
    :   `undoable_transaction` gives you a context in which you can make changes to analysis,
        and creates an Undo state containing those actions. If an exception is thrown, any
        changes made to the analysis inside the transaction are reverted.

        Returns:
        :   Transaction context manager, which will commit/revert actions depending on if an
            exception is thrown when it goes out of scope.

        Return type:
        :   *Generator*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> # Actions inside the transaction will be committed to the undo state upon exit
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)
            True
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> # A thrown exception inside the transaction will undo all changes made inside it
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)  # Reverted on thrown exception
            >>>     raise RuntimeError("oh no")
            RuntimeError: oh no
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            ```

    *property* analysis_changed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean result of whether the auto-analysis results have changed (read-only)

    *property* database*: [Database](database.md#binaryninja.database.Database "binaryninja.database.Database") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets the backing Database of the file

    *property* display_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   `display_name` is a leaf-shaped human-readable name for UI presentation. It never
        contains a directory path. Resolution order:

        - An explicitly set display name (project-assigned, transform-synthesized for container
          entries, or set by a plugin or user).
        - Otherwise the leaf of `filename`.

        Use this for tab titles, save-dialog default leaf names, logs, and any UI surface where
        you’d refer to the file by name. Use `filename` for the physical path that can be
        reopened.

    *property* existing_views*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

    *property* filename*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   The name of the open bndb or binary filename (read/write)

    *property* has_database*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the FileMetadata is backed by a database, or if specified, a specific
        BinaryViewType (read-only)

    *property* is_container_entry*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   `True` if this file was produced by the container transform system (e.g. an entry
        extracted from a Zip archive). `False` for plain files, databases, and FileMetadata that
        has not yet been processed by the transform system.

    *property* modified*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean result of whether the file is modified (Inverse of ‘saved’ property)
        (read/write)

    *property* nav*: [NavigationHandler](#binaryninja.filemetadata.NavigationHandler "binaryninja.filemetadata.NavigationHandler") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Navigation handler for this FileMetadata (read/write)

    *property* navigation*: [NavigationHandler](#binaryninja.filemetadata.NavigationHandler "binaryninja.filemetadata.NavigationHandler") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for nav

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The current offset into the file (read/write)

    *property* original_filename*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   The original name of the binary opened if a bndb, otherwise reads or sets the current
        filename (read/write)

        Note

        With projects, `bv.file.original_filename` queries the path of the binary as staged in
        the project directory. Use `bv.project_file.name` to query the original name of the
        opened binary.

    *property* project*: [Project](project.md#binaryninja.project.Project "binaryninja.project.Project") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* project_file*: [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* raw*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets the “Raw” BinaryView of the file

    *property* redo_entries*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[UndoEntry](undo.md#binaryninja.undo.UndoEntry "binaryninja.undo.UndoEntry")]*

    *property* saved*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean result of whether the file has been saved (Inverse of ‘modified’ property)
        (read/write)

    *property* session_data*: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*
    :   Dictionary object where plugins can store arbitrary data associated with the file

    *property* session_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* snapshot_data_applied_without_error*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* undo_entries*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[UndoEntry](undo.md#binaryninja.undo.UndoEntry "binaryninja.undo.UndoEntry")]*

    *property* view*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* virtual_path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   `virtual_path` is a logical (non-filesystem) path describing how this file was derived
        from the container transform system in the current session. There are three meaningful
        states:

        - Empty - not yet processed by the transform system.
        - Equal to `filename` - processed, no transform chain applied (plain file, database, or
          container system disabled via `files.container.mode`).
        - Non-empty and different from `filename` - derived container entry.

        Session-scoped: save-as does not persist the chain. Reopening the saved artifact yields
        whatever chain that session’s access path produces.

        Use this for cache keys or identity-sensitive operations. Use `filename` for the
        physical path and `display_name` for UI display.

## NavigationHandler

*class* NavigationHandler[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#NavigationHandler)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    get_current_offset() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#NavigationHandler.get_current_offset)
    :   Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_current_view() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#NavigationHandler.get_current_view)
    :   Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    navigate(*view: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#NavigationHandler.navigate)
    :   Parameters:
        :   - **view** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## SaveSettings

*class* SaveSettings[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#SaveSettings)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class SaveSettings` is used to specify actions and options that apply to saving a
    database (.bndb).

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#SaveSettings.__init__)

    is_option_set(*option: [SaveOption](enums.md#binaryninja.enums.SaveOption "binaryninja.enums.SaveOption")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#SaveSettings.is_option_set)
    :   Parameters:
        :   **option** ([*SaveOption*](enums.md#binaryninja.enums.SaveOption
            "binaryninja.enums.SaveOption"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_option(*option: [SaveOption](enums.md#binaryninja.enums.SaveOption "binaryninja.enums.SaveOption")*, *state: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/filemetadata.html#SaveSettings.set_option)
    :   Set a SaveOption in this instance.

        Parameters:
        :   - **option** ([*SaveOption*](enums.md#binaryninja.enums.SaveOption
              "binaryninja.enums.SaveOption")) – Option to set.
            - **state** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – State to assign. Defaults to True.

        Example:
        :   ```
            >>> settings = SaveSettings()
            >>> settings.set_option(SaveOption.TrimSnapshots)
            ```
