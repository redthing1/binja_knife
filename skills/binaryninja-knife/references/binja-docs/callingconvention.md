# callingconvention module

| Class | Description |
| --- | --- |
| [`binaryninja.callingconvention.CallingConvention`](#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention") |  |

## CallingConvention

*class* CallingConvention[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 255*)[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) –
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    get_incoming_flag_value(*flag: architecture.FlagType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_incoming_flag_value)
    :   Parameters:
        :   - **flag** (*architecture.FlagType*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_incoming_reg_value(*reg: architecture.RegisterType*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_incoming_reg_value)
    :   Parameters:
        :   - **reg** (*architecture.RegisterType*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_incoming_var_for_parameter_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_incoming_var_for_parameter_var)
    :   Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_parameter_var_for_incoming_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.get_parameter_var_for_incoming_var)
    :   Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|*
              [*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|*
              [*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction") *|*
              [*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    perform_get_incoming_flag_value(*flag: FlagName*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_incoming_flag_value)
    :   Parameters:
        :   - **flag** (*FlagName*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    perform_get_incoming_reg_value(*reg: RegisterName*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_incoming_reg_value)
    :   Parameters:
        :   - **reg** (*RegisterName*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    perform_get_incoming_var_for_parameter_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_incoming_var_for_parameter_var)
    :   Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    perform_get_parameter_var_for_incoming_var(*in_var: [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreVariable](variable.md#binaryninja.variable.CoreVariable "binaryninja.variable.CoreVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.perform_get_parameter_var_for_incoming_var)
    :   Parameters:
        :   - **in_var** ([*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
              "binaryninja.variable.CoreVariable")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –

        Return type:
        :   [*CoreVariable*](variable.md#binaryninja.variable.CoreVariable
            "binaryninja.variable.CoreVariable")

    with_confidence(*confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [CallingConvention](#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention")[[source]](https://api.binary.ninja/_modules/binaryninja/callingconvention.html#CallingConvention.with_confidence)
    :   Parameters:
        :   **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*CallingConvention*](#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention")

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    arg_regs_for_varargs *= True*

    arg_regs_share_index *= False*

    callee_saved_regs *= []*

    caller_saved_regs *= []*

    eligible_for_heuristics *= True*

    float_arg_regs *= []*

    float_return_reg *= None*

    global_pointer_reg *= None*

    high_int_return_reg *= None*

    implicitly_defined_regs *= []*

    int_arg_regs *= []*

    int_return_reg *= None*

    name *= None*

    required_arg_regs *= []*

    required_clobbered_regs *= []*

    stack_adjusted_on_return *= False*

    stack_reserved_for_arg_regs *= False*
