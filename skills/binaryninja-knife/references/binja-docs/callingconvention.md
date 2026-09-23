# callingconvention module

| Class | Description |
| --- | --- |
| [`binaryninja.callingconvention.CallLayout`](#binaryninja.callingconvention.CallLayout "binaryninja.callingconvention.CallLayout") |  |
| [`binaryninja.callingconvention.CallingConvention`](#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") | `class CallingConvention` describes how parameters, return values, and the stack are handled… |
| [`binaryninja.callingconvention.CoreCallingConvention`](#binaryninja.callingconvention.CoreCallingConvention "binaryninja.callingconvention.CoreCallingConvention") | `class CallingConvention` describes how parameters, return values, and the stack are handled… |

## CallLayout

*class* CallLayout[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallLayout)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*parameters: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *stack_adjustment: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack_adjustments: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterIndex, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **parameters** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*]*)
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*)
            - **stack_adjustment** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **reg_stack_adjustments**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[**RegisterIndex**,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]*)

        Return type:
        :   *None*

    parameters*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*

    reg_stack_adjustments*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterIndex, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

    return_value*: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    stack_adjustment*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## CallingConvention

*class* CallingConvention[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class CallingConvention` describes how parameters, return values, and the stack are
    handled when a function is called. Subclasses of `CallingConvention` define the behavior
    of a calling convention by setting the class attributes below and, where necessary,
    overriding the methods.

    Variables:
    :   - **name** – The name of this calling convention.
        - **caller_saved_regs** – The list of registers that are not preserved across a call
          (caller-saved / volatile registers).
        - **callee_saved_regs** – The list of registers that a callee must preserve across a call
          (callee-saved / non-volatile registers).
        - **int_arg_regs** – The registers used to pass integer and pointer arguments, in the
          order they are used.
        - **float_arg_regs** – The registers used to pass floating point arguments, in the order
          they are used.
        - **required_arg_regs** – The set of registers that must be arguments for heuristic
          calling convention detection to consider this calling convention as a valid option.
        - **required_clobbered_regs** – The set of registers that must be clobbered for heuristic
          calling convention detection to consider this calling convention as a valid option.
        - **arg_regs_share_index** – Whether the integer and floating point argument registers
          share a single argument index. When `True`, the Nth argument consumes the Nth slot of
          both the integer and float register lists regardless of its type. When `False`, integer
          and float arguments are assigned from their respective register lists independently.
        - **arg_regs_for_varargs** – Whether argument registers are used to pass variadic
          arguments.
        - **stack_reserved_for_arg_regs** – Whether stack space is reserved by the caller for the
          register arguments (for example, the shadow/home space used by the Windows x64 calling
          convention).
        - **stack_adjusted_on_return** – Whether the callee adjusts the stack to remove the
          arguments before returning (as in stdcall), rather than leaving the caller to clean up
          the stack (as in cdecl).
        - **eligible_for_heuristics** – Whether this calling convention may be selected by
          heuristic calling convention detection.
        - **int_return_reg** – The register that holds the integer return value.
        - **high_int_return_reg** – The register that holds the high part of an integer return
          value that is too large to fit in a single register, or `None` if there is none.
        - **float_return_reg** – The register that holds the floating point return value, or
          `None` if there is none.
        - **global_pointer_reg** – Deprecated. Use `global_pointer_regs` instead. The register
          that holds the global pointer, if the calling convention defines one, or `None` if there
          is none.
        - **global_pointer_regs** – The registers that hold global pointers, if the calling
          convention defines any.
        - **implicitly_defined_regs** – The registers that are implicitly given a known value on
          function entry by this calling convention.
        - **stack_args_naturally_aligned** – Whether arguments passed on the stack are aligned to
          their natural alignment. If `False`, arguments are aligned to the address size.
        - **stack_args_pushed_left_to_right** – Whether arguments passed on the stack are pushed
          left-to-right, as opposed to the more common right-to-left order.

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

    default_is_arg_type_reg_compatible(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.default_is_arg_type_reg_compatible)
    :   `default_is_arg_type_reg_compatible` is the default implementation of
        [`is_arg_type_reg_compatible`](#binaryninja.callingconvention.CallingConvention.is_arg_type_reg_compatible
        "binaryninja.callingconvention.CallingConvention.is_arg_type_reg_compatible"). The
        default implementation allows register arguments for types that fit in a single
        register, or are a floating point type when `float_arg_regs` has valid registers.

        Parameters:
        :   **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – argument
            type to check

        Returns:
        :   whether the argument type is register compatible

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    default_is_return_type_reg_compatible(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.default_is_return_type_reg_compatible)
    :   `default_is_return_type_reg_compatible` is the default implementation of
        [`is_return_type_reg_compatible`](#binaryninja.callingconvention.CallingConvention.is_return_type_reg_compatible
        "binaryninja.callingconvention.CallingConvention.is_return_type_reg_compatible"). The
        default implementation allows register returns for types that fit in a single register,
        have a size equal to two registers when `high_int_return_reg` is set, or are a floating
        point type when `float_return_reg` is set.

        Parameters:
        :   **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – return
            type to check

        Returns:
        :   whether the return type is register compatible

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_call_layout(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: types.ReturnValueOrType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: types.ParamsType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *permitted_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CallLayout](#binaryninja.callingconvention.CallLayout "binaryninja.callingconvention.CallLayout")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_call_layout)
    :   `get_call_layout` computes the complete call layout (parameter locations, return value
        location, and stack adjustments) for a call with the given return value and parameters.
        It is recommended to only override this method if the calling convention behavior cannot
        be modeled with
        [`get_return_value_location`](#binaryninja.callingconvention.CallingConvention.get_return_value_location
        "binaryninja.callingconvention.CallingConvention.get_return_value_location") and/or
        [`get_parameter_locations`](#binaryninja.callingconvention.CallingConvention.get_parameter_locations
        "binaryninja.callingconvention.CallingConvention.get_parameter_locations").

        The default implementation calls
        [`get_default_call_layout`](#binaryninja.callingconvention.CallingConvention.get_default_call_layout
        "binaryninja.callingconvention.CallingConvention.get_default_call_layout").

        When calling this method to query the layout of a function, the return value and
        parameters should have their named type references dereferenced before passing them to
        this method. Calling the methods `BinaryView.deref_return_value_named_type_references`
        and `BinaryView.deref_parameter_named_type_references` will perform this dereferencing.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** (*types.ReturnValueOrType* *|* *None*) – return value of the call
            - **params** (*types.ParamsType*) – parameters of the call
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function used to resolve the architecture of the
              resulting locations
            - **permitted_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**architecture.RegisterIndex**]* *|* *None*) – optional set of
              register indices that argument passing is restricted to; if not provided, the calling
              convention’s default registers are used

        Returns:
        :   the computed call layout

        Return type:
        :   [*CallLayout*](#binaryninja.callingconvention.CallLayout
            "binaryninja.callingconvention.CallLayout")

    get_default_call_layout(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: types.ReturnValueOrType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: types.ParamsType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *permitted_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CallLayout](#binaryninja.callingconvention.CallLayout "binaryninja.callingconvention.CallLayout")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_call_layout)
    :   `get_default_call_layout` is the default implementation of
        [`get_call_layout`](#binaryninja.callingconvention.CallingConvention.get_call_layout
        "binaryninja.callingconvention.CallingConvention.get_call_layout"). The default
        implementation uses
        [`get_return_value_location`](#binaryninja.callingconvention.CallingConvention.get_return_value_location
        "binaryninja.callingconvention.CallingConvention.get_return_value_location"),
        [`get_parameter_locations`](#binaryninja.callingconvention.CallingConvention.get_parameter_locations
        "binaryninja.callingconvention.CallingConvention.get_parameter_locations"),
        [`get_stack_adjustment_for_locations`](#binaryninja.callingconvention.CallingConvention.get_stack_adjustment_for_locations
        "binaryninja.callingconvention.CallingConvention.get_stack_adjustment_for_locations"),
        and
        [`get_register_stack_adjustments`](#binaryninja.callingconvention.CallingConvention.get_register_stack_adjustments
        "binaryninja.callingconvention.CallingConvention.get_register_stack_adjustments") to
        compute the layout.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** (*types.ReturnValueOrType* *|* *None*) – return value of the call
            - **params** (*types.ParamsType*) – parameters of the call
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function used to resolve the architecture of the
              resulting locations
            - **permitted_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**architecture.RegisterIndex**]* *|* *None*) – optional set of
              register indices that argument passing is restricted to; if not provided, the calling
              convention’s default registers are used

        Returns:
        :   the computed call layout

        Return type:
        :   [*CallLayout*](#binaryninja.callingconvention.CallLayout
            "binaryninja.callingconvention.CallLayout")

    get_default_indirect_return_value_location() → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_indirect_return_value_location)
    :   `get_default_indirect_return_value_location` is the default implementation of
        [`get_indirect_return_value_location`](#binaryninja.callingconvention.CallingConvention.get_indirect_return_value_location
        "binaryninja.callingconvention.CallingConvention.get_indirect_return_value_location").
        The default location is the first integer argument register, or the first stack slot if
        there are no integer argument registers.

        Returns:
        :   the location of the indirect return value pointer

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_default_parameter_locations(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: types.ParamsType*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *permitted_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_parameter_locations)
    :   `get_default_parameter_locations` is the default implementation of
        [`get_parameter_locations`](#binaryninja.callingconvention.CallingConvention.get_parameter_locations
        "binaryninja.callingconvention.CallingConvention.get_parameter_locations"). The default
        implementation uses `int_arg_regs`, `float_arg_regs`, `arg_regs_share_index`,
        `stack_reserved_for_arg_regs`,
        [`is_arg_type_reg_compatible`](#binaryninja.callingconvention.CallingConvention.is_arg_type_reg_compatible
        "binaryninja.callingconvention.CallingConvention.is_arg_type_reg_compatible"),
        [`is_non_reg_arg_indirect`](#binaryninja.callingconvention.CallingConvention.is_non_reg_arg_indirect
        "binaryninja.callingconvention.CallingConvention.is_non_reg_arg_indirect"),
        `stack_args_naturally_aligned`, and `stack_args_pushed_left_to_right` to compute the
        parameter layout.

        This function is usually sufficient unless the calling convention has unusual parameter
        passing behavior. Most calling conventions can be defined per-argument using the
        attributes and methods listed above.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** (*types.ParamsType*) – parameters of the call
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – architecture used to resolve the resulting
              locations
            - **permitted_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**architecture.RegisterIndex**]* *|* *None*) – optional set of
              register indices that argument passing is restricted to; if not provided, the calling
              convention’s default registers are used

        Returns:
        :   the locations of the parameters, in order

        Return type:
        :   *List*[[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation")]

    get_default_parameter_ordering_for_variables(*params: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_parameter_ordering_for_variables)
    :   `get_default_parameter_ordering_for_variables` is the default implementation of
        [`get_parameter_ordering_for_variables`](#binaryninja.callingconvention.CallingConvention.get_parameter_ordering_for_variables
        "binaryninja.callingconvention.CallingConvention.get_parameter_ordering_for_variables").
        The default implementation first checks `arg_regs_share_index` to see if the parameter
        ordering is well defined. If the arguments do not share an index, it places all integer
        arguments before the floating point arguments. Arguments that are not passed in a normal
        location are placed last.

        Parameters:
        :   **params** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
            Python v3.14)")*[*[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")*,* [*Type*](types.md#binaryninja.types.Type
            "binaryninja.types.Type")*]*) – map of parameter variables to their types

        Returns:
        :   the parameter variables in the order they are passed

        Return type:
        :   *List*[[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")]

    get_default_register_stack_adjustments(*return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterIndex, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_register_stack_adjustments)
    :   `get_default_register_stack_adjustments` is the default implementation of
        [`get_register_stack_adjustments`](#binaryninja.callingconvention.CallingConvention.get_register_stack_adjustments
        "binaryninja.callingconvention.CallingConvention.get_register_stack_adjustments"). The
        default implementation compares the register stack slots used by the parameters and the
        return value to compute the adjustments.

        Parameters:
        :   - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*]*) – locations of the parameters

        Returns:
        :   a map from register stack index to its adjustment

        Return type:
        :   *Dict*[RegisterIndex, [*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")]

    get_default_return_value_location(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: types.ReturnValueOrType*) → [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_return_value_location)
    :   `get_default_return_value_location` is the default implementation of
        [`get_return_value_location`](#binaryninja.callingconvention.CallingConvention.get_return_value_location
        "binaryninja.callingconvention.CallingConvention.get_return_value_location"). The
        default implementation checks
        [`is_return_type_reg_compatible`](#binaryninja.callingconvention.CallingConvention.is_return_type_reg_compatible
        "binaryninja.callingconvention.CallingConvention.is_return_type_reg_compatible") and
        places the return value in registers if it can, or uses an indirect return by pointer if
        not. If an indirect return is required, then
        [`get_indirect_return_value_location`](#binaryninja.callingconvention.CallingConvention.get_indirect_return_value_location
        "binaryninja.callingconvention.CallingConvention.get_indirect_return_value_location")
        and
        [`get_returned_indirect_return_value_pointer`](#binaryninja.callingconvention.CallingConvention.get_returned_indirect_return_value_pointer
        "binaryninja.callingconvention.CallingConvention.get_returned_indirect_return_value_pointer")
        are used to provide the location of the indirect return value.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** (*types.ReturnValueOrType*) – return value to compute the location for

        Returns:
        :   the location of the return value

        Return type:
        :   *Optional*[[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation")]

    get_default_stack_adjustment_for_locations(*return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*)[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_default_stack_adjustment_for_locations)
    :   `get_default_stack_adjustment_for_locations` is the default implementation of
        [`get_stack_adjustment_for_locations`](#binaryninja.callingconvention.CallingConvention.get_stack_adjustment_for_locations
        "binaryninja.callingconvention.CallingConvention.get_stack_adjustment_for_locations").
        The default implementation first checks `stack_adjusted_on_return`, and returns zero if
        that is `False`. Otherwise, it checks the stack parameter locations and
        `stack_args_naturally_aligned` to compute the stack adjustment necessary to cover all
        parameters.

        Parameters:
        :   - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]**]*) – list of `(location, type)` tuples for the parameters

        Returns:
        :   the stack adjustment in bytes

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_incoming_flag_value(*reg: RegisterName*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_incoming_flag_value)
    :   `get_incoming_flag_value` gets the known value of a flag on entry to a function.

        Parameters:
        :   - **reg** (*RegisterName*) – flag to query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the incoming value of the flag

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_incoming_reg_value(*reg: RegisterName*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_incoming_reg_value)
    :   `get_incoming_reg_value` gets the known value of a register on entry to a function.

        Parameters:
        :   - **reg** (*RegisterName*) – register to query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the incoming value of the register

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_incoming_var_for_parameter_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_incoming_var_for_parameter_var)
    :   `get_incoming_var_for_parameter_var` gets the incoming variable that corresponds to the
        given parameter variable. This is the inverse of
        [`get_parameter_var_for_incoming_var`](#binaryninja.callingconvention.CallingConvention.get_parameter_var_for_incoming_var
        "binaryninja.callingconvention.CallingConvention.get_parameter_var_for_incoming_var").

        Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) – parameter variable
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the incoming variable corresponding to the parameter variable

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_indirect_return_value_location() → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_indirect_return_value_location)
    :   `get_indirect_return_value_location` gets the location used to pass the hidden pointer
        argument for return values that are returned indirectly through memory.

        Returns:
        :   the location of the indirect return value pointer

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_parameter_locations(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: types.ParamsType*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *permitted_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_parameter_locations)
    :   `get_parameter_locations` computes the locations of the parameters for a call with the
        given return value and parameters.

        The default implementation calls
        [`get_default_parameter_locations`](#binaryninja.callingconvention.CallingConvention.get_default_parameter_locations
        "binaryninja.callingconvention.CallingConvention.get_default_parameter_locations").

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value,
              which may affect parameter placement (for example, when an indirect return pointer
              consumes an argument register)
            - **params** (*types.ParamsType*) – parameters of the call
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – architecture used to resolve the resulting
              locations
            - **permitted_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**architecture.RegisterIndex**]* *|* *None*) – optional set of
              register indices that argument passing is restricted to; if not provided, the calling
              convention’s default registers are used

        Returns:
        :   the locations of the parameters, in order

        Return type:
        :   *List*[[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation")]

    get_parameter_ordering_for_variables(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_parameter_ordering_for_variables)
    :   `get_parameter_ordering_for_variables` computes the order in which the given parameter
        variables are passed. Used by the heuristic calling convention detection to create a
        function type from a list of parameter variables.

        The default implementation calls
        [`get_default_parameter_ordering_for_variables`](#binaryninja.callingconvention.CallingConvention.get_default_parameter_ordering_for_variables
        "binaryninja.callingconvention.CallingConvention.get_default_parameter_ordering_for_variables").

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **params** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]*) – map of parameter variables to their types

        Returns:
        :   the parameter variables in the order they are passed

        Return type:
        :   *List*[[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")]

    get_parameter_var_for_incoming_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_parameter_var_for_incoming_var)
    :   `get_parameter_var_for_incoming_var` gets the parameter variable that corresponds to the
        given incoming variable. This is the inverse of
        [`get_incoming_var_for_parameter_var`](#binaryninja.callingconvention.CallingConvention.get_incoming_var_for_parameter_var
        "binaryninja.callingconvention.CallingConvention.get_incoming_var_for_parameter_var").

        Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) – incoming variable
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the parameter variable corresponding to the incoming variable

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_register_stack_adjustments(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterIndex, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_register_stack_adjustments)
    :   `get_register_stack_adjustments` computes the per-register-stack adjustments (for
        architectures with register stacks, such as the x87 floating point stack) for a call
        with the given return value and parameter locations.

        The default implementation calls
        [`get_default_register_stack_adjustments`](#binaryninja.callingconvention.CallingConvention.get_default_register_stack_adjustments
        "binaryninja.callingconvention.CallingConvention.get_default_register_stack_adjustments").

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*]*) – locations of the parameters

        Returns:
        :   a map from register stack index to its adjustment

        Return type:
        :   *Dict*[RegisterIndex, [*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")]

    get_return_value_location(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: types.ReturnValueOrType*) → [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_return_value_location)
    :   `get_return_value_location` computes the location of the return value for the given
        return value type and location structure.

        The default implementation calls
        [`get_default_return_value_location`](#binaryninja.callingconvention.CallingConvention.get_default_return_value_location
        "binaryninja.callingconvention.CallingConvention.get_default_return_value_location").

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** (*types.ReturnValueOrType*) – return value to compute the location for

        Returns:
        :   the location of the return value

        Return type:
        :   *Optional*[[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation")]

    get_returned_indirect_return_value_pointer() → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_returned_indirect_return_value_pointer)
    :   `get_returned_indirect_return_value_pointer` gets the location in which the hidden
        indirect return value pointer is returned to the caller, for calling conventions that
        return it.

        Returns:
        :   the location the indirect return value pointer is returned in, or `None` if it is not
            returned

        Return type:
        :   *Optional*[[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")]

    get_stack_adjustment_for_locations(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*)[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_stack_adjustment_for_locations)
    :   `get_stack_adjustment_for_locations` computes the stack adjustment applied on return for
        a call with the given return value and parameter locations.

        The default implementation calls
        [`get_default_stack_adjustment_for_locations`](#binaryninja.callingconvention.CallingConvention.get_default_stack_adjustment_for_locations
        "binaryninja.callingconvention.CallingConvention.get_default_stack_adjustment_for_locations").

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]**]*) – list of `(location, type)` tuples for the parameters

        Returns:
        :   the stack adjustment in bytes

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    is_arg_type_reg_compatible(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.is_arg_type_reg_compatible)
    :   `is_arg_type_reg_compatible` determines whether a value of the given type can be passed
        as an argument in registers.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – argument
              type to check

        Returns:
        :   whether the argument type is register compatible

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_non_reg_arg_indirect(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.is_non_reg_arg_indirect)
    :   `is_non_reg_arg_indirect` determines whether an argument that cannot be passed in
        registers is passed indirectly by pointer as opposed to being passed directly on the
        stack.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – argument
              type to check

        Returns:
        :   whether the non-register argument is passed indirectly by pointer

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_return_type_reg_compatible(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.is_return_type_reg_compatible)
    :   `is_return_type_reg_compatible` determines whether a value of the given type can be
        returned in registers, as opposed to being returned indirectly through memory.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – return
              type to check

        Returns:
        :   whether the return type is register compatible

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_get_incoming_flag_value(*flag: FlagName*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_incoming_flag_value)
    :   Deprecated, override get_incoming_flag_value instead.

        Parameters:
        :   - **flag** (*FlagName*)
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function"))

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    perform_get_incoming_reg_value(*reg: RegisterName*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_incoming_reg_value)
    :   Deprecated, override get_incoming_reg_value instead.

        Parameters:
        :   - **reg** (*RegisterName*)
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function"))

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    perform_get_incoming_var_for_parameter_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_incoming_var_for_parameter_var)
    :   Deprecated, override get_incoming_var_for_parameter_var instead.

        Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable"))
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*)

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    perform_get_parameter_var_for_incoming_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_parameter_var_for_incoming_var)
    :   Deprecated, override get_parameter_var_for_incoming_var instead.

        Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable"))
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*)

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    with_confidence(*confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [CallingConvention](#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.with_confidence)
    :   Parameters:
        :   **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*CallingConvention*](#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention")

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*
    :   The architecture this calling convention applies to.

        Getter:
        :   returns the architecture this calling convention applies to

        Setter:
        :   sets the architecture this calling convention applies to

        Type:
        :   [*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture")

    arg_regs_for_varargs *= True*

    arg_regs_share_index *= False*

    callee_saved_regs *= []*

    caller_saved_regs *= []*

    eligible_for_heuristics *= True*

    float_arg_regs *= []*

    float_return_reg *= None*

    global_pointer_reg *= None*

    global_pointer_regs *= []*

    high_int_return_reg *= None*

    implicitly_defined_regs *= []*

    int_arg_regs *= []*

    int_return_reg *= None*

    name *= None*

    required_arg_regs *= []*

    required_clobbered_regs *= []*

    stack_adjusted_on_return *= False*

    stack_args_naturally_aligned *= False*

    stack_args_pushed_left_to_right *= False*

    stack_reserved_for_arg_regs *= False*

## CoreCallingConvention

*class* CoreCallingConvention[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention)
:   Bases: [`CallingConvention`](#binaryninja.callingconvention.CallingConvention
    "binaryninja.callingconvention.CallingConvention")

    __init__(*handle*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.__init__)
    :   Parameters:
        :   **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

    get_call_layout(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: types.ReturnValueOrType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: types.ParamsType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *permitted_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CallLayout](#binaryninja.callingconvention.CallLayout "binaryninja.callingconvention.CallLayout")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_call_layout)
    :   `get_call_layout` computes the complete call layout (parameter locations, return value
        location, and stack adjustments) for a call with the given return value and parameters.
        It is recommended to only override this method if the calling convention behavior cannot
        be modeled with
        [`get_return_value_location`](#binaryninja.callingconvention.CoreCallingConvention.get_return_value_location
        "binaryninja.callingconvention.CoreCallingConvention.get_return_value_location") and/or
        [`get_parameter_locations`](#binaryninja.callingconvention.CoreCallingConvention.get_parameter_locations
        "binaryninja.callingconvention.CoreCallingConvention.get_parameter_locations").

        The default implementation calls `get_default_call_layout`.

        When calling this method to query the layout of a function, the return value and
        parameters should have their named type references dereferenced before passing them to
        this method. Calling the methods `BinaryView.deref_return_value_named_type_references`
        and `BinaryView.deref_parameter_named_type_references` will perform this dereferencing.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** (*types.ReturnValueOrType* *|* *None*) – return value of the call
            - **params** (*types.ParamsType*) – parameters of the call
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function used to resolve the architecture of the
              resulting locations
            - **permitted_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**architecture.RegisterIndex**]* *|* *None*) – optional set of
              register indices that argument passing is restricted to; if not provided, the calling
              convention’s default registers are used

        Returns:
        :   the computed call layout

        Return type:
        :   [*CallLayout*](#binaryninja.callingconvention.CallLayout
            "binaryninja.callingconvention.CallLayout")

    get_incoming_flag_value(*flag: architecture.FlagType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_incoming_flag_value)
    :   `get_incoming_flag_value` gets the known value of a flag on entry to a function.

        Parameters:
        :   - **reg** – flag to query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed
            - **flag** (*architecture.FlagType*)

        Returns:
        :   the incoming value of the flag

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_incoming_reg_value(*reg: architecture.RegisterType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_incoming_reg_value)
    :   `get_incoming_reg_value` gets the known value of a register on entry to a function.

        Parameters:
        :   - **reg** (*RegisterName*) – register to query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the incoming value of the register

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_incoming_var_for_parameter_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") = None*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_incoming_var_for_parameter_var)
    :   `get_incoming_var_for_parameter_var` gets the incoming variable that corresponds to the
        given parameter variable. This is the inverse of
        [`get_parameter_var_for_incoming_var`](#binaryninja.callingconvention.CoreCallingConvention.get_parameter_var_for_incoming_var
        "binaryninja.callingconvention.CoreCallingConvention.get_parameter_var_for_incoming_var").

        Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) – parameter variable
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the incoming variable corresponding to the parameter variable

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_indirect_return_value_location() → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_indirect_return_value_location)
    :   `get_indirect_return_value_location` gets the location used to pass the hidden pointer
        argument for return values that are returned indirectly through memory.

        Returns:
        :   the location of the indirect return value pointer

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_parameter_locations(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: types.ParamsType*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *permitted_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[architecture.RegisterIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_parameter_locations)
    :   `get_parameter_locations` computes the locations of the parameters for a call with the
        given return value and parameters.

        The default implementation calls `get_default_parameter_locations`.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value,
              which may affect parameter placement (for example, when an indirect return pointer
              consumes an argument register)
            - **params** (*types.ParamsType*) – parameters of the call
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – architecture used to resolve the resulting
              locations
            - **permitted_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**architecture.RegisterIndex**]* *|* *None*) – optional set of
              register indices that argument passing is restricted to; if not provided, the calling
              convention’s default registers are used

        Returns:
        :   the locations of the parameters, in order

        Return type:
        :   *List*[[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation")]

    get_parameter_ordering_for_variables(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_parameter_ordering_for_variables)
    :   `get_parameter_ordering_for_variables` computes the order in which the given parameter
        variables are passed. Used by the heuristic calling convention detection to create a
        function type from a list of parameter variables.

        The default implementation calls `get_default_parameter_ordering_for_variables`.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **params** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]*) – map of parameter variables to their types

        Returns:
        :   the parameter variables in the order they are passed

        Return type:
        :   *List*[[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")]

    get_parameter_var_for_incoming_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") = None*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_parameter_var_for_incoming_var)
    :   `get_parameter_var_for_incoming_var` gets the parameter variable that corresponds to the
        given incoming variable. This is the inverse of
        [`get_incoming_var_for_parameter_var`](#binaryninja.callingconvention.CoreCallingConvention.get_incoming_var_for_parameter_var
        "binaryninja.callingconvention.CoreCallingConvention.get_incoming_var_for_parameter_var").

        Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) – incoming variable
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – function being analyzed

        Returns:
        :   the parameter variable corresponding to the incoming variable

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    get_register_stack_adjustments(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation")]*) → [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterIndex, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_register_stack_adjustments)
    :   `get_register_stack_adjustments` computes the per-register-stack adjustments (for
        architectures with register stacks, such as the x87 floating point stack) for a call
        with the given return value and parameter locations.

        The default implementation calls `get_default_register_stack_adjustments`.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*]*) – locations of the parameters

        Returns:
        :   a map from register stack index to its adjustment

        Return type:
        :   *Dict*[RegisterIndex, [*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")]

    get_return_value_location(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: types.ReturnValueOrType*) → [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_return_value_location)
    :   `get_return_value_location` computes the location of the return value for the given
        return value type and location structure.

        The default implementation calls `get_default_return_value_location`.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** (*types.ReturnValueOrType*) – return value to compute the location for

        Returns:
        :   the location of the return value

        Return type:
        :   *Optional*[[*ValueLocation*](types.md#binaryninja.types.ValueLocation
            "binaryninja.types.ValueLocation")]

    get_returned_indirect_return_value_pointer() → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_returned_indirect_return_value_pointer)
    :   `get_returned_indirect_return_value_pointer` gets the location in which the hidden
        indirect return value pointer is returned to the caller, for calling conventions that
        return it.

        Returns:
        :   the location the indirect return value pointer is returned in, or `None` if it is not
            returned

        Return type:
        :   *Optional*[[*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")]

    get_stack_adjustment_for_locations(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *return_value: [ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[ValueLocation](types.md#binaryninja.types.ValueLocation "binaryninja.types.ValueLocation"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]]*)[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.get_stack_adjustment_for_locations)
    :   `get_stack_adjustment_for_locations` computes the stack adjustment applied on return for
        a call with the given return value and parameter locations.

        The default implementation calls `get_default_stack_adjustment_for_locations`.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **return_value** ([*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation") *|* *None*) – optional location of the return value
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*ValueLocation*](types.md#binaryninja.types.ValueLocation
              "binaryninja.types.ValueLocation")*,* [*Type*](types.md#binaryninja.types.Type
              "binaryninja.types.Type")*]**]*) – list of `(location, type)` tuples for the parameters

        Returns:
        :   the stack adjustment in bytes

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    is_arg_type_reg_compatible(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.is_arg_type_reg_compatible)
    :   `is_arg_type_reg_compatible` determines whether a value of the given type can be passed
        as an argument in registers.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – argument
              type to check

        Returns:
        :   whether the argument type is register compatible

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_non_reg_arg_indirect(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.is_non_reg_arg_indirect)
    :   `is_non_reg_arg_indirect` determines whether an argument that cannot be passed in
        registers is passed indirectly by pointer as opposed to being passed directly on the
        stack.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – argument
              type to check

        Returns:
        :   whether the non-register argument is passed indirectly by pointer

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_return_type_reg_compatible(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CoreCallingConvention.is_return_type_reg_compatible)
    :   `is_return_type_reg_compatible` determines whether a value of the given type can be
        returned in registers, as opposed to being returned indirectly through memory.

        Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) – binary view providing type information
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) – return
              type to check

        Returns:
        :   whether the return type is register compatible

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
