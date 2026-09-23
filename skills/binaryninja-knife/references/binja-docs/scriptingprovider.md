# scriptingprovider module

| Class | Description |
| --- | --- |
| [`binaryninja.scriptingprovider.BlacklistedDict`](#binaryninja.scriptingprovider.BlacklistedDict "binaryninja.scriptingprovider.BlacklistedDict") | dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping… |
| [`binaryninja.scriptingprovider.PythonScriptingInstance`](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance") |  |
| [`binaryninja.scriptingprovider.PythonScriptingProvider`](#binaryninja.scriptingprovider.PythonScriptingProvider "binaryninja.scriptingprovider.PythonScriptingProvider") |  |
| [`binaryninja.scriptingprovider.ScriptingInstance`](#binaryninja.scriptingprovider.ScriptingInstance "binaryninja.scriptingprovider.ScriptingInstance") |  |
| [`binaryninja.scriptingprovider.ScriptingOutputListener`](#binaryninja.scriptingprovider.ScriptingOutputListener "binaryninja.scriptingprovider.ScriptingOutputListener") |  |
| [`binaryninja.scriptingprovider.ScriptingProvider`](#binaryninja.scriptingprovider.ScriptingProvider "binaryninja.scriptingprovider.ScriptingProvider") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.scriptingprovider.bninspect`](#binaryninja.scriptingprovider.bninspect "binaryninja.scriptingprovider.bninspect") | `bninspect` prints documentation about a command that is about to be run The interpreter will… |
| [`binaryninja.scriptingprovider.redirect_stdio`](#binaryninja.scriptingprovider.redirect_stdio "binaryninja.scriptingprovider.redirect_stdio") |  |

## BlacklistedDict

*class* BlacklistedDict[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#BlacklistedDict)
:   Bases: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
    v3.14)")

    __init__(*blacklist*, **args*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#BlacklistedDict.__init__)

    add_blacklist_item(*item*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#BlacklistedDict.add_blacklist_item)

    enable_blacklist(*enabled*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#BlacklistedDict.enable_blacklist)

    is_blacklisted_item(*item*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#BlacklistedDict.is_blacklisted_item)

    remove_blacklist_item(*item*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#BlacklistedDict.remove_blacklist_item)

    *property* blacklist_enabled

## PythonScriptingInstance

*class* PythonScriptingInstance[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance)
:   Bases: [`ScriptingInstance`](#binaryninja.scriptingprovider.ScriptingInstance
    "binaryninja.scriptingprovider.ScriptingInstance")

    *class* InterpreterThread[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread)
    :   Bases: [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "(in
        Python v3.14)")

        __init__(*instance*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.__init__)
        :   This constructor should always be called with keyword arguments. Arguments are:

            *group* should be None; reserved for future extension when a ThreadGroup class is
            implemented.

            *target* is the callable object to be invoked by the run() method. Defaults to None,
            meaning nothing is called.

            *name* is the thread name. By default, a unique name is constructed of the form
            “Thread-N” where N is a small decimal number.

            *args* is the argument tuple for the target invocation. Defaults to ().

            *kwargs* is a dictionary of keyword arguments for the target invocation. Defaults to {}.

            If a subclass overrides the constructor, it must make sure to invoke the base class
            constructor (Thread.__init__()) before doing anything else to the thread.

        add_input(*data*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.add_input)

        apply_locals()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.apply_locals)

        end()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.end)

        execute(*_code*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.execute)

        get_selected_data()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.get_selected_data)

        read(*size*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.read)

        run()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.run)
        :   Method representing the thread’s activity.

            You may override this method in a subclass. The standard run() method invokes the
            callable object passed to the object’s constructor as the target argument, if any, with
            sequential and keyword arguments taken from the args and kwargs arguments, respectively.

        update_locals()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.update_locals)

        update_magic_variables()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.update_magic_variables)

        write_at_cursor(*data*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.InterpreterThread.write_at_cursor)

    __init__(*provider*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.__init__)

    *abstract* perform_cancel_script_input()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_cancel_script_input)

    *abstract* perform_complete_input(*text*, *state*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_complete_input)

    *abstract* perform_execute_script_input(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_execute_script_input)

    *abstract* perform_execute_script_input_from_filename(*filename*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_execute_script_input_from_filename)

    *abstract* perform_set_current_address(*addr*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_set_current_address)

    *abstract* perform_set_current_basic_block(*block*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_set_current_basic_block)

    *abstract* perform_set_current_binary_view(*view*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_set_current_binary_view)

    *abstract* perform_set_current_function(*func*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_set_current_function)

    *abstract* perform_set_current_selection(*begin*, *end*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_set_current_selection)

    *abstract* perform_stop()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingInstance.perform_stop)

## PythonScriptingProvider

*class* PythonScriptingProvider[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingProvider)
:   Bases: [`ScriptingProvider`](#binaryninja.scriptingprovider.ScriptingProvider
    "binaryninja.scriptingprovider.ScriptingProvider")

    *class* MagicVariable[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingProvider.MagicVariable)
    :   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
        v3.14)")

        Represents an automatically-populated (magic) variable in the python scripting console

        __init__(*get_value: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[PythonScriptingInstance](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *set_value: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[PythonScriptingInstance](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *depends_on: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
        :   Parameters:
            :   - **get_value**
                  ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable
                  "(in Python
                  v3.14)")*[**[*[*PythonScriptingInstance*](#binaryninja.scriptingprovider.PythonScriptingInstance
                  "binaryninja.scriptingprovider.PythonScriptingInstance")*]**,*
                  [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
                  v3.14)")*]*) –
                - **set_value**
                  ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable
                  "(in Python
                  v3.14)")*[**[*[*PythonScriptingInstance*](#binaryninja.scriptingprovider.PythonScriptingInstance
                  "binaryninja.scriptingprovider.PythonScriptingInstance")*,*
                  [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*,*
                  [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
                  v3.14)")*]**,* *None**]* *|* *None*) –
                - **depends_on** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
                  Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
                  Python v3.14)")*]*) –

            Return type:
            :   *None*

        depends_on*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
        :   List of other variables whose values on which this variable’s value depends

        get_value*: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[PythonScriptingInstance](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*
        :   Function to call, before every time a script is evaluated, to get the value of the
            variable

        set_value*: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[PythonScriptingInstance](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
        :   (Optional) function to call after a script is evaluated, if the value of the variable
            has changed during the course of the script. If None, a warning will be printed stating
            that the variable is read-only. Signature: (instance: PythonScriptingInstance,
            old_value: any, new_value: any) -> None

    instance_class
    :   alias of
        [`PythonScriptingInstance`](#binaryninja.scriptingprovider.PythonScriptingInstance
        "binaryninja.scriptingprovider.PythonScriptingInstance")

    *classmethod* register_magic_variable(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *get_value: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[PythonScriptingInstance](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *set_value: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[PythonScriptingInstance](#binaryninja.scriptingprovider.PythonScriptingInstance "binaryninja.scriptingprovider.PythonScriptingInstance"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *depends_on: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingProvider.register_magic_variable)
    :   Add a magic variable to all scripting instances created by the scripting provider :param
        name: Variable name identifier to be used in the interpreter :param get_value: Function
        to call, before every time a script is evaluated, to get the value of the variable
        :param set_value: (Optional) Function to call after a script is evaluated, if the value
        of the variable has changed during the course of the script. If None, a warning will be
        printed stating that the variable is read-only. Signature: (instance:
        PythonScriptingInstance, old_value: any, new_value: any) -> None :param depends_on: List
        of other variables whose values on which this variable’s value depends

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **get_value**
              ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable
              "(in Python
              v3.14)")*[**[*[*PythonScriptingInstance*](#binaryninja.scriptingprovider.PythonScriptingInstance
              "binaryninja.scriptingprovider.PythonScriptingInstance")*]**,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]*) –
            - **set_value**
              ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable
              "(in Python
              v3.14)")*[**[*[*PythonScriptingInstance*](#binaryninja.scriptingprovider.PythonScriptingInstance
              "binaryninja.scriptingprovider.PythonScriptingInstance")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* *None**]* *|* *None*) –
            - **depends_on** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) –

    *classmethod* unregister_magic_variable(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#PythonScriptingProvider.unregister_magic_variable)
    :   Remove a magic variable by name :param name: Variable name

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

    apiName *= 'python3'*

    magic_variables*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MagicVariable](#binaryninja.scriptingprovider.PythonScriptingProvider.MagicVariable "binaryninja.scriptingprovider.PythonScriptingProvider.MagicVariable")]* *= {'bv': PythonScriptingProvider.MagicVariable(get_value=<function <lambda>>, set_value=None, depends_on=[]), 'current_address': PythonScriptingProvider.MagicVariable(get_value=<function _get_here>, set_value=<function _set_here>, depends_on=['current_ui_context']), 'current_basic_block': PythonScriptingProvider.MagicVariable(get_value=<function <lambda>>, set_value=None, depends_on=[]), 'current_comment': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_comment>, set_value=<function _set_current_comment>, depends_on=[]), 'current_data_var': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_data_var>, set_value=None, depends_on=[]), 'current_function': PythonScriptingProvider.MagicVariable(get_value=<function <lambda>>, set_value=None, depends_on=[]), 'current_hlil': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_hlil>, set_value=None, depends_on=[]), 'current_hlil_ssa': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_hlil_ssa>, set_value=None, depends_on=['current_hlil']), 'current_il_basic_block': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_basic_block>, set_value=None, depends_on=['current_il_instruction']), 'current_il_expr': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_expr>, set_value=None, depends_on=['current_il_expr_index', 'current_il_function']), 'current_il_expr_index': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_expr_index>, set_value=None, depends_on=['current_token']), 'current_il_function': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_function>, set_value=None, depends_on=['current_ui_view_location', 'current_llil', 'current_lifted_il', 'current_llil_ssa', 'current_mapped_mlil', 'current_mapped_mlil_ssa', 'current_mlil', 'current_mlil_ssa', 'current_hlil', 'current_hlil_ssa']), 'current_il_index': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_index>, set_value=None, depends_on=['current_ui_view_location']), 'current_il_instruction': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_instruction>, set_value=None, depends_on=['current_il_index', 'current_il_function']), 'current_il_instructions': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_il_instructions>, set_value=None, depends_on=['current_il_index', 'current_il_function', 'current_ui_view']), 'current_lifted_il': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_lifted_il>, set_value=None, depends_on=[]), 'current_llil': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_llil>, set_value=None, depends_on=[]), 'current_llil_ssa': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_llil_ssa>, set_value=None, depends_on=['current_llil']), 'current_mapped_mlil': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_mapped_mlil>, set_value=None, depends_on=[]), 'current_mapped_mlil_ssa': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_mapped_mlil_ssa>, set_value=None, depends_on=['current_mapped_mlil']), 'current_mlil': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_mlil>, set_value=None, depends_on=[]), 'current_mlil_ssa': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_mlil_ssa>, set_value=None, depends_on=['current_mlil']), 'current_project': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_project>, set_value=None, depends_on=['current_ui_context', 'current_view']), 'current_raw_offset': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_raw_offset>, set_value=<function _set_current_raw_offset>, depends_on=['current_ui_context']), 'current_sections': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_sections>, set_value=None, depends_on=[]), 'current_segment': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_segment>, set_value=None, depends_on=[]), 'current_selection': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_selection>, set_value=<function _set_current_selection>, depends_on=['current_ui_view']), 'current_symbol': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_symbol>, set_value=None, depends_on=[]), 'current_symbols': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_symbols>, set_value=None, depends_on=[]), 'current_thread': PythonScriptingProvider.MagicVariable(get_value=<function <lambda>>, set_value=None, depends_on=[]), 'current_token': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_token>, set_value=None, depends_on=['current_ui_token_state']), 'current_ui_action_context': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_action_context>, set_value=None, depends_on=['current_ui_view', 'current_ui_action_handler']), 'current_ui_action_handler': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_action_handler>, set_value=None, depends_on=['current_ui_context']), 'current_ui_context': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_context>, set_value=None, depends_on=[]), 'current_ui_token_state': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_token_state>, set_value=None, depends_on=['current_ui_action_context']), 'current_ui_view': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_view>, set_value=None, depends_on=['current_ui_context']), 'current_ui_view_frame': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_view_frame>, set_value=None, depends_on=['current_ui_context']), 'current_ui_view_location': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_ui_view_location>, set_value=None, depends_on=['current_ui_view_frame']), 'current_variable': PythonScriptingProvider.MagicVariable(get_value=<function _get_current_variable>, set_value=None, depends_on=['current_ui_token_state']), 'current_view': PythonScriptingProvider.MagicVariable(get_value=<function <lambda>>, set_value=None, depends_on=[]), 'dbg': PythonScriptingProvider.MagicVariable(get_value=<function _get_debugger>, set_value=None, depends_on=[]), 'dsc': PythonScriptingProvider.MagicVariable(get_value=<function _get_shared_cache>, set_value=None, depends_on=[]), 'here': PythonScriptingProvider.MagicVariable(get_value=<function _get_here>, set_value=<function _set_here>, depends_on=['current_ui_context']), 'kc': PythonScriptingProvider.MagicVariable(get_value=<function _get_kernel_cache>, set_value=None, depends_on=[]), 'kernel_cache': PythonScriptingProvider.MagicVariable(get_value=<function _get_kernel_cache>, set_value=None, depends_on=[]), 'shared_cache': PythonScriptingProvider.MagicVariable(get_value=<function _get_shared_cache>, set_value=None, depends_on=[])}*

    name *= 'Python'*

## ScriptingInstance

*class* ScriptingInstance[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*provider*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.__init__)

    cancel_script_input(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.cancel_script_input)

    complete_input(*text*, *state*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.complete_input)

    error(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.error)

    execute_script_input(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.execute_script_input)

    execute_script_input_from_filename(*filename*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.execute_script_input_from_filename)

    output(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.output)

    *abstract* perform_cancel_script_input()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_cancel_script_input)

    *abstract* perform_complete_input(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *state*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_complete_input)
    :   Parameters:
        :   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *abstract* perform_execute_script_input(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_execute_script_input)

    *abstract* perform_execute_script_input_from_filename(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_execute_script_input_from_filename)

    *abstract* perform_set_current_address(*addr*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_set_current_address)

    *abstract* perform_set_current_basic_block(*block*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_set_current_basic_block)

    *abstract* perform_set_current_binary_view(*view*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_set_current_binary_view)

    *abstract* perform_set_current_function(*func*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_set_current_function)

    *abstract* perform_set_current_selection(*begin*, *end*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_set_current_selection)

    *abstract* perform_stop()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.perform_stop)

    register_output_listener(*listener*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.register_output_listener)

    set_current_address(*addr*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.set_current_address)

    set_current_basic_block(*block*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.set_current_basic_block)

    set_current_binary_view(*view*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.set_current_binary_view)

    set_current_function(*func*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.set_current_function)

    set_current_selection(*begin*, *end*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.set_current_selection)

    stop()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.stop)

    unregister_output_listener(*listener*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.unregister_output_listener)

    warning(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingInstance.warning)

    *property* delimiters

    *property* input_ready_state

## ScriptingOutputListener

*class* ScriptingOutputListener[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingOutputListener)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    notify_error(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingOutputListener.notify_error)

    notify_input_ready_state_changed(*state*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingOutputListener.notify_input_ready_state_changed)

    notify_output(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingOutputListener.notify_output)

    notify_warning(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingOutputListener.notify_warning)

## ScriptingProvider

*class* ScriptingProvider[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingProvider)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingProvider.__init__)

    create_instance() → [ScriptingInstance](#binaryninja.scriptingprovider.ScriptingInstance "binaryninja.scriptingprovider.ScriptingInstance") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingProvider.create_instance)
    :   Return type:
        :   [*ScriptingInstance*](#binaryninja.scriptingprovider.ScriptingInstance
            "binaryninja.scriptingprovider.ScriptingInstance") | *None*

    register() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#ScriptingProvider.register)
    :   Return type:
        :   *None*

    apiName *= ''*

    instance_class*: [Type](https://docs.python.org/3/library/typing.html#typing.Type "(in Python v3.14)")[[ScriptingInstance](#binaryninja.scriptingprovider.ScriptingInstance "binaryninja.scriptingprovider.ScriptingInstance")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    name *= ''*

## bninspect

bninspect(*code_*, *globals_*, *locals_*)[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#bninspect)
:   `bninspect` prints documentation about a command that is about to be run The interpreter
    will invoke this function if you input a line ending in ? e.g. bv?

    Parameters:
    :   - **code** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Python code to be evaluated
        - **globals** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
          v3.14)")) – globals() from callsite
        - **locals** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
          v3.14)")) – locals() from callsite

## redirect_stdio

redirect_stdio()[[source]](https://api.binary.ninja/_modules/binaryninja/scriptingprovider.html#redirect_stdio)
