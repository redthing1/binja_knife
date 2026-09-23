# plugin module

| Class | Description |
| --- | --- |
| [`binaryninja.plugin.BackgroundTask`](#binaryninja.plugin.BackgroundTask "binaryninja.plugin.BackgroundTask") | The `BackgroundTask` class provides a mechanism for reporting progress of an optionally… |
| [`binaryninja.plugin.BackgroundTaskThread`](#binaryninja.plugin.BackgroundTaskThread "binaryninja.plugin.BackgroundTaskThread") | The `BackgroundTaskThread` class provides an all-in-one solution for executing a… |
| [`binaryninja.plugin.MainThreadAction`](#binaryninja.plugin.MainThreadAction "binaryninja.plugin.MainThreadAction") |  |
| [`binaryninja.plugin.MainThreadActionHandler`](#binaryninja.plugin.MainThreadActionHandler "binaryninja.plugin.MainThreadActionHandler") |  |
| [`binaryninja.plugin.PluginCommand`](#binaryninja.plugin.PluginCommand "binaryninja.plugin.PluginCommand") | The `class PluginCommand` contains all the plugin registration methods as class methods. |
| [`binaryninja.plugin.PluginCommandContext`](#binaryninja.plugin.PluginCommandContext "binaryninja.plugin.PluginCommandContext") | The `class PluginCommandContext` is used to access loaded plugins and their exposed methods… |

## BackgroundTask

*class* BackgroundTask[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTask)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `BackgroundTask` class provides a mechanism for reporting progress of an optionally
    cancelable task to the user via the status bar in the UI. If `can_cancel` is is True,
    then the task can be cancelled either programmatically (via
    [`cancel`](#binaryninja.plugin.BackgroundTask.cancel
    "binaryninja.plugin.BackgroundTask.cancel")) or by the user via the UI.

    Note this class does not provide a means to execute a task, which is available via the
    [`BackgroundTaskThread`](#binaryninja.plugin.BackgroundTaskThread
    "binaryninja.plugin.BackgroundTaskThread") class.

    Parameters:
    :   - **initial_progress_text** – text description of the task to display in the status bar in
          the UI, defaults to “”
        - **can_cancel** – whether to enable cancellation of the task, defaults to False

    __init__(*initial_progress_text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *can_cancel: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTask.__init__)
    :   Parameters:
        :   - **initial_progress_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)")) –
            - **can_cancel** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    cancel()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTask.cancel)

    finish()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTask.finish)

    *property* can_cancel
    :   Whether the task can be cancelled (read-only)

    *property* cancelled
    :   Whether the task has been cancelled

    *property* finished
    :   Whether the task has finished

    *property* progress
    :   Text description of the progress of the background task (displayed in status bar of the
        UI)

## BackgroundTaskThread

*class* BackgroundTaskThread[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTaskThread)
:   Bases: [`BackgroundTask`](#binaryninja.plugin.BackgroundTask
    "binaryninja.plugin.BackgroundTask")

    The `BackgroundTaskThread` class provides an all-in-one solution for executing a
    [`BackgroundTask`](#binaryninja.plugin.BackgroundTask
    "binaryninja.plugin.BackgroundTask") in a thread.

    See the [`BackgroundTask`](#binaryninja.plugin.BackgroundTask
    "binaryninja.plugin.BackgroundTask") for additional information.

    Parameters:
    :   - **initial_progress_text** – text description of the task to display in the status bar in
          the UI, defaults to “”
        - **can_cancel** – whether to enable cancellation of the task, defaults to False

    __init__(*initial_progress_text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *can_cancel: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTaskThread.__init__)
    :   Parameters:
        :   - **initial_progress_text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)")) –
            - **can_cancel** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    join(*timeout=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTaskThread.join)

    run()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTaskThread.run)

    start()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#BackgroundTaskThread.start)

## MainThreadAction

*class* MainThreadAction[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadAction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadAction.__init__)

    execute()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadAction.execute)

    wait()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadAction.wait)

    *property* done

## MainThreadActionHandler

*class* MainThreadActionHandler[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadActionHandler)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadActionHandler.__init__)

    add_action(*action*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadActionHandler.add_action)

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#MainThreadActionHandler.register)

## PluginCommand

*class* PluginCommand[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `class PluginCommand` contains all the plugin registration methods as class methods.

    You shouldn’t need to create an instance of this class, instead see register,
    register_for_address, register_for_function, and similar class methods for examples on
    how to register your plugin.

    __init__(*cmd*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.__init__)

    execute(*context: [PluginCommandContext](#binaryninja.plugin.PluginCommandContext "binaryninja.plugin.PluginCommandContext")*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.execute)
    :   `execute` Execute a plugin. See the example in
        [`PluginCommandContext`](#binaryninja.plugin.PluginCommandContext
        "binaryninja.plugin.PluginCommandContext")

        Parameters:
        :   **context** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – PluginCommandContext to pass the PluginCommand

        Return type:
        :   None

            ```
            >>> ctx = PluginCommandContext(bv);
            >>> PluginCommand.get_valid_list(ctx)[r'PDB\Load'].execute(ctx)
            ```

    *classmethod* get_valid_list(*context: [PluginCommandContext](#binaryninja.plugin.PluginCommandContext "binaryninja.plugin.PluginCommandContext")*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.get_valid_list)
    :   Dict of registered plugins

        Parameters:
        :   **context** ([*PluginCommandContext*](#binaryninja.plugin.PluginCommandContext
            "binaryninja.plugin.PluginCommandContext")) –

    is_valid(*context: [PluginCommandContext](#binaryninja.plugin.PluginCommandContext "binaryninja.plugin.PluginCommandContext")*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.is_valid)
    :   Parameters:
        :   **context** ([*PluginCommandContext*](#binaryninja.plugin.PluginCommandContext
            "binaryninja.plugin.PluginCommandContext")) –

    *classmethod* register(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register)
    :   `register` Register a plugin

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` as an argument
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` to
              determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView):
            >>>     log_info(f"My plugin was called on bv: `{bv}`")
            >>> PluginCommand.register("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView) -> bool:
            >>>     return False
            >>> PluginCommand.register("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register` with the same function name will replace the existing function but
        will leak the memory of the original plugin.

    *classmethod* register_for_address(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_address)
    :   `register_for_address` Register a plugin to be called with an address argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and address as
              arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              address to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, address: int):
            >>>     log_info(f"My plugin was called on bv: `{bv}` at address {hex(address)}")
            >>> PluginCommand.register_for_address("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, address: int) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_address("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_address` with the same function name will replace the existing
        function but will leak the memory of the original plugin.

    *classmethod* register_for_function(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_function)
    :   `register_for_function` Register a plugin to be called with a function argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a `Function` as
              arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `Function` to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, func: Function):
            >>>     log_info(f"My plugin was called on func {func} in bv `{bv}`")
            >>> PluginCommand.register_for_function("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, func: Function) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_function("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_function` with the same function name will replace the existing
        function but will leak the memory of the original plugin.

    *classmethod* register_for_high_level_il_function(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_high_level_il_function)
    :   `register_for_high_level_il_function` Register a plugin to be called with a high level
        IL function argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a
              `HighLevelILFunction` as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `HighLevelILFunction` to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, func: HighLevelILFunction):
            >>>     log_info(f"My plugin was called on func {func} in bv `{bv}`")
            >>> PluginCommand.register_for_high_level_il_function("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, func: HighLevelILFunction) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_high_level_il_function("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_high_level_il_function` with the same function name will replace
        the existing function but will leak the memory of the original plugin.

    *classmethod* register_for_high_level_il_instruction(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_high_level_il_instruction)
    :   `register_for_high_level_il_instruction` Register a plugin to be called with a high
        level IL instruction argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a
              `HighLevelILInstruction` as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `HighLevelILInstruction` to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, inst: HighLevelILInstruction):
            >>>     log_info(f"My plugin was called on inst {inst} in bv `{bv}`")
            >>> PluginCommand.register_for_high_level_il_instruction("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, inst: HighLevelILInstruction) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_high_level_il_instruction("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_high_level_il_instruction` with the same function name will
        replace the existing function but will leak the memory of the original plugin.

    *classmethod* register_for_low_level_il_function(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_low_level_il_function)
    :   `register_for_low_level_il_function` Register a plugin to be called with a low level IL
        function argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a
              `LowLevelILFunction` as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `LowLevelILFunction` to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, func: LowLevelILFunction):
            >>>     log_info(f"My plugin was called on func {func} in bv `{bv}`")
            >>> PluginCommand.register_for_low_level_il_function("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, func: LowLevelILFunction) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_low_level_il_function("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_low_level_il_function` with the same function name will replace
        the existing function but will leak the memory of the original plugin.

    *classmethod* register_for_low_level_il_instruction(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_low_level_il_instruction)
    :   `register_for_low_level_il_instruction` Register a plugin to be called with a low level
        IL instruction argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a
              `LowLevelILInstruction` as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `LowLevelILInstruction` to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, inst: LowLevelILInstruction):
            >>>     log_info(f"My plugin was called on inst {inst} in bv `{bv}`")
            >>> PluginCommand.register_for_low_level_il_instruction("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, inst: LowLevelILInstruction) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_low_level_il_instruction("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_low_level_il_instruction` with the same function name will replace
        the existing function but will leak the memory of the original plugin.

    *classmethod* register_for_medium_level_il_function(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_medium_level_il_function)
    :   `register_for_medium_level_il_function` Register a plugin to be called with a medium
        level IL function argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a
              `MediumLevelILFunction` as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `MediumLevelILFunction` to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, func: MediumLevelILFunction):
            >>>     log_info(f"My plugin was called on func {func} in bv `{bv}`")
            >>> PluginCommand.register_for_medium_level_il_function("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, func: MediumLevelILFunction) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_medium_level_il_function("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_medium_level_il_function` with the same function name will replace
        the existing function but will leak the memory of the original plugin.

    *classmethod* register_for_medium_level_il_instruction(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_medium_level_il_instruction)
    :   `register_for_medium_level_il_instruction` Register a plugin to be called with a medium
        level IL instruction argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView` and a
              `MediumLevelILInstruction` as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView` and
              `MediumLevelILInstruction` to determine whether the plugin should be enabled for that
              view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, inst: MediumLevelILInstruction):
            >>>     log_info(f"My plugin was called on inst {inst} in bv `{bv}`")
            >>> PluginCommand.register_for_medium_level_il_instruction("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, inst: MediumLevelILInstruction) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_medium_level_il_instruction("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_medium_level_il_instruction` with the same function name will
        replace the existing function but will leak the memory of the original plugin.

    *classmethod* register_for_project(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Project](project.md#binaryninja.project.Project "binaryninja.project.Project")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Project](project.md#binaryninja.project.Project "binaryninja.project.Project")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_project)
    :   `register_for_project` Register a plugin to be called with a project argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `Project` as an argument
            - **is_valid** (*callback*) – optional argument of a function passed a `Project` to
              determine whether the plugin should be enabled for that project

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(project: Project):
            >>>     log_info(f"My plugin was called on project: `{project}`")
            >>> PluginCommand.register_for_project("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(project: Project) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_project("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_project` with the same function name will replace the existing
        function but will leak the memory of the original plugin.

    *classmethod* register_for_range(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_for_range)
    :   `register_for_range` Register a plugin to be called with a range argument

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the plugin (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the plugin
            - **action** (*callback*) – function to call with the `BinaryView`, start address, and
              length as arguments
            - **is_valid** (*callback*) – optional argument of a function passed a `BinaryView`, start
              address, and length to determine whether the plugin should be enabled for that view

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_plugin(bv: BinaryView, start: int, length: int):
            >>>     log_info(f"My plugin was called on bv: `{bv}` at {hex(start)} of length {hex(length)}")
            >>> PluginCommand.register_for_range("My Plugin", "My plugin description (not used)", my_plugin)
            True
            >>> def is_valid(bv: BinaryView, start: int, length: int) -> bool:
            >>>     return False
            >>> PluginCommand.register_for_range("My Plugin (With Valid Function)", "My plugin description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_for_range` with the same function name will replace the existing
        function but will leak the memory of the original plugin.

    *classmethod* register_global(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *action: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *is_valid: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommand.register_global)
    :   `register_global` Register a command globally

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the command (use ‘Folder\Name’ to have the menu item nested in a
              folder)
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – description of the command
            - **action** (*callback*) – function to call
            - **is_valid** (*callback*) – optional argument of a function to determine whether the
              command should be enabled

        Return type:
        :   *None*

        Example:
        :   ```
            >>> def my_command():
            >>>     log_info(f"My command was called on bv")
            >>> PluginCommand.register_global("My Command", "My command description (not used)", my_command)
            True
            >>> def is_valid() -> bool:
            >>>     return False
            >>> PluginCommand.register_global("My Command (With Valid Function)", "My command description (not used)", my_plugin, is_valid)
            True
            ```

        Warning

        Calling `register_global` with the same function name will replace the existing function
        but will leak the memory of the original plugin.

    *property* command

    *property* description

    *property* name

    *property* type

## PluginCommandContext

*class* PluginCommandContext[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommandContext)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `class PluginCommandContext` is used to access loaded plugins and their exposed
    methods with the context of a specific Binary VIew.

    Example:
    :   ```
        >>> bv = load("/tmp/file1")
        >>> ctx = PluginCommandContext(bv);
        >>> binexport = PluginCommand.get_valid_list(ctx)["BinExport"]
        >>> binexport.execute(ctx)
        ```

    __init__(*view*)[[source]](https://api.binary.ninja/_modules/binaryninja/plugin.html#PluginCommandContext.__init__)

    *property* address

    *property* function

    *property* instruction

    *property* length

    *property* project

    *property* view
