# architecture module

| Class | Description |
| --- | --- |
| [`binaryninja.architecture.Architecture`](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | `class Architecture` is the parent class for all CPU architectures. Subclasses of Architecture… |
| [`binaryninja.architecture.ArchitectureHook`](#binaryninja.architecture.ArchitectureHook "binaryninja.architecture.ArchitectureHook") | `class Architecture` is the parent class for all CPU architectures. Subclasses of Architecture… |
| [`binaryninja.architecture.BasicBlockAnalysisContext`](#binaryninja.architecture.BasicBlockAnalysisContext "binaryninja.architecture.BasicBlockAnalysisContext") | Used by `analyze_basic_blocks` and contains analysis settings and other contextual information. |
| [`binaryninja.architecture.CoreArchitecture`](#binaryninja.architecture.CoreArchitecture "binaryninja.architecture.CoreArchitecture") | `class Architecture` is the parent class for all CPU architectures. Subclasses of Architecture… |
| [`binaryninja.architecture.FunctionLifterContext`](#binaryninja.architecture.FunctionLifterContext "binaryninja.architecture.FunctionLifterContext") | Used by `lift_function` and contains contextual information for function-level lifting |
| [`binaryninja.architecture.InstructionBranch`](#binaryninja.architecture.InstructionBranch "binaryninja.architecture.InstructionBranch") |  |
| [`binaryninja.architecture.InstructionInfo`](#binaryninja.architecture.InstructionInfo "binaryninja.architecture.InstructionInfo") |  |
| [`binaryninja.architecture.InstructionTextToken`](#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken") | `class InstructionTextToken` is used to tell the core about the various components in the… |
| [`binaryninja.architecture.IntrinsicInfo`](#binaryninja.architecture.IntrinsicInfo "binaryninja.architecture.IntrinsicInfo") |  |
| [`binaryninja.architecture.IntrinsicInput`](#binaryninja.architecture.IntrinsicInput "binaryninja.architecture.IntrinsicInput") |  |
| [`binaryninja.architecture.LifterInstructionData`](#binaryninja.architecture.LifterInstructionData "binaryninja.architecture.LifterInstructionData") | Per-function store of basic block instruction bytes, populated during basic block analysis and … |
| [`binaryninja.architecture.RegisterInfo`](#binaryninja.architecture.RegisterInfo "binaryninja.architecture.RegisterInfo") |  |
| [`binaryninja.architecture.RegisterStackInfo`](#binaryninja.architecture.RegisterStackInfo "binaryninja.architecture.RegisterStackInfo") |  |

## Architecture

*class* Architecture[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class Architecture` is the parent class for all CPU architectures. Subclasses of
    Architecture implement assembly, disassembly, IL lifting, and patching.

    `class Architecture` has a metaclass with the additional methods `register`, and
    supports iteration:

    ```
    >>> #List the architectures
    >>> list(Architecture)
    [<arch: aarch64>, <arch: armv7>, <arch: thumb2>, <arch: armv7eb>, <arch: thumb2eb>, <arch: mipsel32>, <arch: mips32>, <arch: ppc>, <arch: ppc64>, <arch: ppc_le>, <arch: ppc64_le>, <arch: x86_16>, <arch: x86>, <arch: x86_64>]
    >>> #Register a new Architecture
    >>> class MyArch(Architecture):
    ...  name = "MyArch"
    ...
    >>> MyArch.register()
    >>> list(Architecture)
    [<arch: aarch64>, <arch: armv7>, <arch: thumb2>, <arch: armv7eb>, <arch: thumb2eb>, <arch: mipsel32>, <arch: mips32>, <arch: ppc>, <arch: ppc64>, <arch: ppc_le>, <arch: ppc64_le>, <arch: x86_16>, <arch: x86>, <arch: x86_64>, <arch: MyArch>]
    >>>
    ```

    For the purposes of this documentation the variable `arch` will be used in the following
    context

    ```
    >>> from binaryninja import *
    >>> arch = Architecture['x86']
    ```

    Note

    The max_instr_length property of an architecture is not necessarily representative of
    the maximum instruction size of the associated CPU architecture. Rather, it represents
    the maximum size of a potential instruction that the architecture plugin can handle. So
    for example, the value for x86 is 16 despite the largest valid instruction being only 15
    bytes long, and the value for mips32 is currently 8 because multiple instructions are
    decoded looking for delay slots so they can be reordered.

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.__init__)

    always_branch(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.always_branch)
    :   `always_branch` reads the instruction(s) in `data` at virtual address `addr` and returns
        a string of bytes of the same length which always branches.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   string containing len(data) which always branches to the same location as the provided
            instruction

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> data = arch.always_branch(arch.assemble("je 10"), 0)
            >>> arch.get_instruction_text(data, 0)
            (['nop', '     '], 1)
            >>> arch.get_instruction_text(data[1:], 0)
            (['jmp', '     ', '0x9'], 5)
            >>>
            ```

    analyze_basic_blocks(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *context: [BasicBlockAnalysisContext](#binaryninja.architecture.BasicBlockAnalysisContext "binaryninja.architecture.BasicBlockAnalysisContext")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.analyze_basic_blocks)
    :   `analyze_basic_blocks` performs basic block recovery and commits the results to the
        function analysis

        Note

        Architecture subclasses should only implement this method if function-level analysis is
        required

        Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – the function to analyze
            - **context**
              ([*BasicBlockAnalysisContext*](#binaryninja.architecture.BasicBlockAnalysisContext
              "binaryninja.architecture.BasicBlockAnalysisContext")) – the analysis context

        Return type:
        :   *None*

    assemble(*code: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.assemble)
    :   `assemble` converts the string of assembly instructions `code` loaded at virtual address
        `addr` to the byte representation of those instructions.

        Note

        Architecture subclasses should implement this method.

        Architecture plugins can override this method to provide assembler functionality. This
        can be done by simply shelling out to an assembler like yasm or llvm-mc, since this
        method isn’t performance sensitive.

        Note

        It is important that the assembler used accepts a syntax identical to the one emitted by
        the disassembler. This will prevent confusing the user.

        If there is an error in the input assembly, this function should raise a ValueError
        (with a reasonable error message).

        Parameters:
        :   - **code** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – string representation of the instructions to be assembled
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address that the instructions will be loaded at

        Returns:
        :   the bytes for the assembled instructions

        Return type:
        :   Python3 - a ‘bytes’ object; Python2 - a ‘bytes’ object

        Example:
        :   ```
            >>> arch.assemble("je 10")
            b'\x0f\x84\x04\x00\x00\x00'
            >>>
            ```

    convert_to_nop(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.convert_to_nop)
    :   `convert_to_nop` reads the instruction(s) in `data` at virtual address `addr` and
        returns a string of nop instructions of the same length as data.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   string containing len(data) worth of no-operation instructions

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.convert_to_nop(b"\x00\x00", 0)
            b'\x90\x90'
            >>>
            ```

    get_associated_arch_by_address(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_associated_arch_by_address)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Architecture*](#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]

    get_default_flag_condition_low_level_il(*cond: [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")*, *sem_class: SemanticClassName | [ILSemanticFlagClass](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_default_flag_condition_low_level_il)
    :   Parameters:
        :   - **cond** ([*LowLevelILFlagCondition*](enums.md#binaryninja.enums.LowLevelILFlagCondition
              "binaryninja.enums.LowLevelILFlagCondition"))
            - **sem_class** (*SemanticClassType*)
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction"))

        Return type:
        :   ExpressionIndex

    get_default_flag_write_low_level_il(*op: lowlevelil.LowLevelILOperation*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *role: [FlagRole](enums.md#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole")*, *operands: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[lowlevelil.ILOperandType]*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → lowlevelil.ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_default_flag_write_low_level_il)
    :   Parameters:
        :   - **op** ([*LowLevelILOperation*](enums.md#binaryninja.enums.LowLevelILOperation
              "binaryninja.enums.LowLevelILOperation"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **role** ([*FlagRole*](enums.md#binaryninja.enums.FlagRole
              "binaryninja.enums.FlagRole"))
            - **operands** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*) or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*)*) – a list of either items that are either string register names or constant
              integer values
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction"))

        Return type:
        :   ExpressionIndex index

    get_flag_by_name(*flag: FlagName*) → FlagIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_by_name)
    :   `get_flag_by_name` get flag name for flag index.

        Parameters:
        :   **flag** (*FlagName*) – flag name

        Returns:
        :   flag index for flag name

        Return type:
        :   FlagIndex

    get_flag_condition_low_level_il(*cond: [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")*, *sem_class: SemanticClassName | [ILSemanticFlagClass](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_condition_low_level_il)
    :   Parameters:
        :   - **cond** ([*LowLevelILFlagCondition*](enums.md#binaryninja.enums.LowLevelILFlagCondition
              "binaryninja.enums.LowLevelILFlagCondition")) – Flag condition to be computed
            - **sem_class** (*SemanticClassType*) – Semantic class to be used (None for default
              semantics)
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – LowLevelILFunction object to append
              ExpressionIndex objects to

        Return type:
        :   ExpressionIndex

    get_flag_index(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → FlagIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_index)
    :   Parameters:
        :   **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
            "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*)

        Return type:
        :   *FlagIndex*

    get_flag_name(*flag: FlagIndex*) → FlagName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_name)
    :   `get_flag_name` gets a flag name from a flag index.

        Parameters:
        :   **flag** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – flag index

        Returns:
        :   the corresponding flag name string

        Return type:
        :   FlagName

    get_flag_role(*flag: FlagIndex*, *sem_class: SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [FlagRole](enums.md#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_role)
    :   `get_flag_role` gets the role of a given flag.

        Parameters:
        :   - **flag** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – flag
            - **sem_class** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional semantic flag class

        Returns:
        :   flag role

        Return type:
        :   [*FlagRole*](enums.md#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole")

    get_flag_write_low_level_il(*op: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *write_type: FlagWriteTypeName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*, *operands: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[lowlevelil.ILOperandType]*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → lowlevelil.ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_write_low_level_il)
    :   Parameters:
        :   - **op** ([*LowLevelILOperation*](enums.md#binaryninja.enums.LowLevelILOperation
              "binaryninja.enums.LowLevelILOperation"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **write_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **flag** (*FlagType*)
            - **operands** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*) or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*)*) – a list of either items that are either string registers, flags, or
              constant integer values
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction"))

        Return type:
        :   lowlevelil.ExpressionIndex

    get_flag_write_type_by_name(*write_type: FlagWriteTypeName*) → FlagWriteTypeIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_write_type_by_name)
    :   `get_flag_write_type_by_name` gets the flag write type name for the flag write type.

        Parameters:
        :   **write_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – flag write type

        Returns:
        :   flag write type

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_flag_write_type_name(*write_type: FlagWriteTypeIndex*) → FlagWriteTypeName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flag_write_type_name)
    :   `get_flag_write_type_name` gets the flag write type name for the given flag.

        Parameters:
        :   **write_type** (*FlagWriteTypeIndex*) – flag

        Returns:
        :   flag write type name

        Return type:
        :   FlagWriteTypeName

    get_flags_required_for_flag_condition(*cond: [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")*, *sem_class: SemanticClassName | [ILSemanticFlagClass](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_flags_required_for_flag_condition)
    :   Parameters:
        :   - **cond** ([*LowLevelILFlagCondition*](enums.md#binaryninja.enums.LowLevelILFlagCondition
              "binaryninja.enums.LowLevelILFlagCondition"))
            - **sem_class** (*SemanticClassName* *|*
              [*ILSemanticFlagClass*](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass
              "binaryninja.lowlevelil.ILSemanticFlagClass") *|* *SemanticClassIndex* *|* *None*)

    get_instruction_info(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [InstructionInfo](#binaryninja.architecture.InstructionInfo "binaryninja.architecture.InstructionInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_instruction_info)
    :   `get_instruction_info` returns an InstructionInfo object for the instruction at the
        given virtual address `addr` with data `data`.

        Note

        Architecture subclasses should implement this method.

        Note

        The instruction info object should always set the InstructionInfo.length to the
        instruction length, and the branches of the proper types should be added if the
        instruction is a branch.

        If the instruction is a branch instruction architecture plugins should add a branch of
        the proper type:

        > | BranchType | Description |
        > | --- | --- |
        > | UnconditionalBranch | Branch will always be taken |
        > | FalseBranch | False branch condition |
        > | TrueBranch | True branch condition |
        > | CallDestination | Branch is a call instruction (Branch with Link) |
        > | FunctionReturn | Branch returns from a function |
        > | SystemCall | System call instruction |
        > | IndirectBranch | Branch destination is a memory address or register |
        > | UnresolvedBranch | Branch destination is an unknown address |

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`

        Returns:
        :   the InstructionInfo for the current instruction

        Return type:
        :   [*InstructionInfo*](#binaryninja.architecture.InstructionInfo
            "binaryninja.architecture.InstructionInfo")

    get_instruction_low_level_il(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_instruction_low_level_il)
    :   `get_instruction_low_level_il` appends lowlevelil.ExpressionIndex objects to `il` for
        the instruction at the given virtual address `addr` with data `data`.

        This is used to analyze arbitrary data at an address, if you are working with an
        existing binary, you likely want to be using `Function.get_low_level_il_at`.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – The function the current instruction
              belongs to

        Returns:
        :   the length of the current instruction

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_instruction_low_level_il_instruction(*bv: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_instruction_low_level_il_instruction)
    :   Parameters:
        :   - **bv** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView"))
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")

    get_instruction_text(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_instruction_text)
    :   `get_instruction_text` returns a tuple containing a list of decoded InstructionTextToken
        objects and the bytes used at the given virtual address `addr` with data `data`.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`

        Returns:
        :   a tuple containing the InstructionTextToken list and length of bytes decoded

        Return type:
        :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*InstructionTextToken*](#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"))

    get_instruction_text_with_context(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *context: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_instruction_text_with_context)
    :   `get_instruction_text` returns a tuple containing a list of decoded InstructionTextToken
        objects and the bytes used at the given virtual address `addr` with data `data`.

        Note

        Architecture subclasses should implement this method if they require context from
        analyze_basic_blocks for instruction decoding.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`
            - **context** (*Any*) – function architecture context

        Returns:
        :   a tuple containing the InstructionTextToken list and length of bytes decoded

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*InstructionTextToken*](#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")],
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] |
            *None*

    get_intrinsic_class(*intrinsic: IntrinsicIndex*) → [IntrinsicClass](enums.md#binaryninja.enums.IntrinsicClass "binaryninja.enums.IntrinsicClass")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_intrinsic_class)
    :   `get_intrinsic_class` gets the intrinsic class from an intrinsic number.

        Parameters:
        :   **intrinsic** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – intrinsic number

        Returns:
        :   intrinsic class

        Return type:
        :   [*IntrinsicClass*](enums.md#binaryninja.enums.IntrinsicClass
            "binaryninja.enums.IntrinsicClass")

    get_intrinsic_index(*intrinsic: IntrinsicName | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | IntrinsicIndex*) → IntrinsicIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_intrinsic_index)
    :   `get_intrinsic_index` gets an intrinsic index given an IntrinsicType.

        Parameters:
        :   **intrinsic** (*IntrinsicType*) – intrinsic number

        Returns:
        :   the corresponding intrinsic string

        Return type:
        :   IntrinsicIndex

    get_intrinsic_name(*intrinsic: IntrinsicIndex*) → IntrinsicName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_intrinsic_name)
    :   `get_intrinsic_name` gets an intrinsic name from an intrinsic number.

        Parameters:
        :   **intrinsic** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – intrinsic number

        Returns:
        :   the corresponding intrinsic string

        Return type:
        :   IntrinsicName

    get_low_level_il_from_bytes(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_low_level_il_from_bytes)
    :   `get_low_level_il_from_bytes` converts the instruction in bytes to `il` at the given
        virtual address

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the bytes of the instruction
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`

        Returns:
        :   a list of low level il instructions

        Return type:
        :   [*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")

        Example:
        :   ```
            >>> list(arch.get_low_level_il_from_bytes(b'\xeb\xfe', 0x40DEAD))
            <il: jump(0x40dead)>
            >>>
            ```

    get_modified_regs_on_write(*reg: RegisterName*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName][[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_modified_regs_on_write)
    :   `get_modified_regs_on_write` returns a list of register names that are modified when
        `reg` is written.

        Parameters:
        :   **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – string register name

        Returns:
        :   list of register names

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

    get_reg_index(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*) → RegisterIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_reg_index)
    :   Parameters:
        :   **reg** (*RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*)

        Return type:
        :   *RegisterIndex*

    get_reg_name(*reg: RegisterIndex*) → RegisterName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_reg_name)
    :   `get_reg_name` gets a register name from a register index.

        Parameters:
        :   **reg** (*RegisterIndex*) – register index

        Returns:
        :   the corresponding register name

        Return type:
        :   RegisterName

    get_reg_stack_for_reg(*reg: RegisterName*) → RegisterStackName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_reg_stack_for_reg)
    :   Parameters:
        :   **reg** (*RegisterName*)

        Return type:
        :   *RegisterStackName* | *None*

    get_reg_stack_index(*reg_stack: RegisterStackName | [ILRegisterStack](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | RegisterStackIndex*) → RegisterStackIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_reg_stack_index)
    :   Parameters:
        :   **reg_stack** (*RegisterStackName* *|*
            [*ILRegisterStack*](lowlevelil.md#binaryninja.lowlevelil.ILRegisterStack
            "binaryninja.lowlevelil.ILRegisterStack") *|* *RegisterStackIndex*)

        Return type:
        :   *RegisterStackIndex*

    get_reg_stack_name(*reg_stack: RegisterStackIndex*) → RegisterStackName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_reg_stack_name)
    :   `get_reg_stack_name` gets a register stack name from a register stack number.

        Parameters:
        :   **reg_stack** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – register stack number

        Returns:
        :   the corresponding register string

        Return type:
        :   RegisterStackName

    get_semantic_flag_class_by_name(*sem_class: SemanticClassName*) → SemanticClassIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_class_by_name)
    :   `get_semantic_flag_class_by_name` gets the semantic flag class index by name.

        Parameters:
        :   **sem_class** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – semantic flag class

        Returns:
        :   semantic flag class index

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_semantic_flag_class_index(*sem_class: SemanticClassName | [ILSemanticFlagClass](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → SemanticClassIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_class_index)
    :   Parameters:
        :   **sem_class** (*SemanticClassName* *|*
            [*ILSemanticFlagClass*](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass
            "binaryninja.lowlevelil.ILSemanticFlagClass") *|* *SemanticClassIndex* *|* *None*)

        Return type:
        :   *SemanticClassIndex*

    get_semantic_flag_class_name(*class_index: SemanticClassIndex*) → SemanticClassName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_class_name)
    :   `get_semantic_flag_class_name` gets the name of a semantic flag class from the index.

        Parameters:
        :   **class_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) – class_index

        Returns:
        :   the name of the semantic flag class

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_semantic_flag_group_by_name(*sem_group: SemanticGroupName*) → SemanticGroupIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_group_by_name)
    :   `get_semantic_flag_group_by_name` gets the semantic flag group index by name.

        Parameters:
        :   **sem_group** (*SemanticGroupName*) – semantic flag group name

        Returns:
        :   semantic flag group index

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_semantic_flag_group_index(*sem_group: SemanticGroupName | [ILSemanticFlagGroup](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | SemanticGroupIndex*) → SemanticGroupIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_group_index)
    :   Parameters:
        :   **sem_group** (*SemanticGroupName* *|*
            [*ILSemanticFlagGroup*](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagGroup
            "binaryninja.lowlevelil.ILSemanticFlagGroup") *|* *SemanticGroupIndex*)

        Return type:
        :   *SemanticGroupIndex*

    get_semantic_flag_group_low_level_il(*sem_group: SemanticGroupName | [ILSemanticFlagGroup](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | SemanticGroupIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_group_low_level_il)
    :   Parameters:
        :   - **sem_group** (*Optional**[**SemanticGroupType**]*)
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction"))

        Return type:
        :   lowlevelil.ExpressionIndex

    get_semantic_flag_group_name(*group_index: SemanticGroupIndex*) → SemanticGroupName[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.get_semantic_flag_group_name)
    :   `get_semantic_flag_group_name` gets the name of a semantic flag group from the index.

        Parameters:
        :   **group_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) – group_index

        Returns:
        :   the name of the semantic flag group

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    invert_branch(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.invert_branch)
    :   `invert_branch` reads the instruction(s) in `data` at virtual address `addr` and returns
        a string of bytes of the same length which inverts the branch of provided instruction.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   string containing len(data) which always branches to the same location as the provided
            instruction

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.get_instruction_text(arch.invert_branch(arch.assemble("je 10"), 0), 0)
            (['jne', '     ', '0xa'], 6)
            >>> arch.get_instruction_text(arch.invert_branch(arch.assemble("jo 10"), 0), 0)
            (['jno', '     ', '0xa'], 6)
            >>> arch.get_instruction_text(arch.invert_branch(arch.assemble("jge 10"), 0), 0)
            (['jl', '      ', '0xa'], 6)
            >>>
            ```

    is_always_branch_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.is_always_branch_patch_available)
    :   `is_always_branch_patch_available` determines if the instruction `data` at `addr` can be
        made to **always branch**.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_always_branch_patch_available(arch.assemble("je 10"), 0)
            True
            >>> arch.is_always_branch_patch_available(arch.assemble("nop"), 0)
            False
            >>>
            ```

    is_invert_branch_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.is_invert_branch_patch_available)
    :   `is_always_branch_patch_available` determines if the instruction `data` at `addr` can be
        inverted.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_invert_branch_patch_available(arch.assemble("je 10"), 0)
            True
            >>> arch.is_invert_branch_patch_available(arch.assemble("nop"), 0)
            False
            >>>
            ```

    is_never_branch_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.is_never_branch_patch_available)
    :   `is_never_branch_patch_available` determines if the instruction `data` at `addr` can be
        made to **never branch**.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_never_branch_patch_available(arch.assemble("je 10"), 0)
            True
            >>> arch.is_never_branch_patch_available(arch.assemble("nop"), 0)
            False
            >>>
            ```

    is_skip_and_return_value_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.is_skip_and_return_value_patch_available)
    :   `is_skip_and_return_value_patch_available` determines if the instruction `data` at
        `addr` is a *call-like* instruction that can be made into an instruction *returns a
        value*.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_skip_and_return_value_patch_available(arch.assemble("call 0"), 0)
            True
            >>> arch.is_skip_and_return_value_patch_available(arch.assemble("jmp eax"), 0)
            False
            >>>
            ```

    is_skip_and_return_zero_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.is_skip_and_return_zero_patch_available)
    :   `is_skip_and_return_zero_patch_available` determines if the instruction `data` at `addr`
        is a *call-like* instruction that can be made into an instruction *returns zero*.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_skip_and_return_zero_patch_available(arch.assemble("call 0"), 0)
            True
            >>> arch.is_skip_and_return_zero_patch_available(arch.assemble("call eax"), 0)
            True
            >>> arch.is_skip_and_return_zero_patch_available(arch.assemble("jmp eax"), 0)
            False
            >>>
            ```

    lift_function(*func: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *context: [FunctionLifterContext](#binaryninja.architecture.FunctionLifterContext "binaryninja.architecture.FunctionLifterContext")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.lift_function)
    :   `lift_function` performs lifting of the function and commits the results to the function
        analysis

        Note

        Architecture subclasses should only implement this method if function-level analysis is
        required

        Parameters:
        :   - **func** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – the function to analyze
            - **context** ([*FunctionLifterContext*](#binaryninja.architecture.FunctionLifterContext
              "binaryninja.architecture.FunctionLifterContext")) – the lifting context

        Returns:
        :   True on success, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *classmethod* register() → [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.register)
    :   Return type:
        :   [*Architecture*](#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture")

    register_calling_convention(*cc: [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.register_calling_convention)
    :   `register_calling_convention` registers a new calling convention for the Architecture.

        Parameters:
        :   **cc**
            ([*CallingConvention*](callingconvention.md#binaryninja.callingconvention.CallingConvention
            "binaryninja.callingconvention.CallingConvention")) – CallingConvention object to be
            registered

        Return type:
        :   *None*

    skip_and_return_value(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#Architecture.skip_and_return_value)
    :   `skip_and_return_value` reads the instruction(s) in `data` at virtual address `addr` and
        returns a string of bytes of the same length which doesn’t call and instead *return a
        value*.

        Note

        Architecture subclasses should implement this method.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Returns:
        :   string containing len(data) which always branches to the same location as the provided
            instruction

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.get_instruction_text(arch.skip_and_return_value(arch.assemble("call 10"), 0, 0), 0)
            (['mov', '     ', 'eax', ', ', '0x0'], 5)
            >>>
            ```

    address_size *= 8*

    *property* calling_conventions*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [CallingConvention](callingconvention.md#binaryninja.callingconvention.CallingConvention "binaryninja.callingconvention.CallingConvention")]*
    :   Dict of CallingConvention objects (read-only)

    *property* can_assemble*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   returns if the architecture can assemble instructions (read-only)

    *property* cdecl_calling_convention
    :   Cdecl calling convention.

        Note

        Make sure the calling convention has been registered with
        Architecture.register_calling_convention.

        Getter:
        :   returns a CallingConvention object for the cdecl calling convention, if one exists.

        Setter:
        :   sets the cdecl calling convention

        Type:
        :   *Optional*[’callingconvention.CallingConvention’]

    *property* default_calling_convention
    :   Default calling convention.

        Note

        Make sure the calling convention has been registered with
        Architecture.register_calling_convention.

        Getter:
        :   returns a CallingConvention object for the default calling convention, if one exists.

        Setter:
        :   sets the default calling convention

        Type:
        :   *Optional*[’callingconvention.CallingConvention’]

    default_int_size *= 4*

    endianness *= 0*

    *property* fastcall_calling_convention
    :   Fastcall calling convention.

        Note

        Make sure the calling convention has been registered with
        Architecture.register_calling_convention.

        Getter:
        :   returns a CallingConvention object for the fastcall calling convention, if one exists.

        Setter:
        :   sets the fastcall calling convention

        Type:
        :   *Optional*[’callingconvention.CallingConvention’]

    flag_conditions_for_semantic_flag_group*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[SemanticGroupName, [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[SemanticClassName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")]]* *= {}*

    flag_roles*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[FlagName, [FlagRole](enums.md#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole")]* *= {}*

    flag_write_types*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagWriteTypeName]* *= []*

    flags*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName]* *= []*

    flags_required_for_flag_condition*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName]]* *= {}*

    flags_required_for_semantic_flag_group*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[SemanticGroupName, [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName]]* *= {}*

    flags_written_by_flag_write_type*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[FlagWriteTypeName, [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName]]* *= {}*

    *property* full_width_regs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*
    :   List of full width register strings (read-only)

    function_arch_contexts*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]* *= {}*

    global_regs *= []*

    instr_alignment *= 1*

    intrinsics *= {}*

    linear_sweep_analysis_capabilities *= 3*

    linear_sweep_initial_alignment*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    link_reg *= None*

    max_instr_length *= 16*

    name *= None*

    next_address *= 0*

    opcode_display_length *= 8*

    reg_stacks*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [RegisterStackInfo](#binaryninja.architecture.RegisterStackInfo "binaryninja.architecture.RegisterStackInfo")]* *= {}*

    regs*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterName, [RegisterInfo](#binaryninja.architecture.RegisterInfo "binaryninja.architecture.RegisterInfo")]* *= {}*

    semantic_class_for_flag_write_type*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[FlagWriteTypeName, SemanticClassName]* *= {}*

    semantic_flag_classes*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[SemanticClassName]* *= []*

    semantic_flag_groups*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[SemanticGroupName]* *= []*

    stack_pointer *= None*

    *property* standalone_platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*
    :   Architecture standalone platform (read-only)

    *property* stdcall_calling_convention
    :   Stdcall calling convention.

        Note

        Make sure the calling convention has been registered with
        Architecture.register_calling_convention.

        Getter:
        :   returns a CallingConvention object for the stdcall calling convention, if one exists.

        Setter:
        :   sets the stdcall calling convention

        Type:
        :   *Optional*[’callingconvention.CallingConvention’]

    system_regs *= []*

    *property* type_libraries*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")]*
    :   Architecture type libraries

## ArchitectureHook

*class* ArchitectureHook[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#ArchitectureHook)
:   Bases: [`CoreArchitecture`](#binaryninja.architecture.CoreArchitecture
    "binaryninja.architecture.CoreArchitecture")

    __init__(*base_arch: [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*)[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#ArchitectureHook.__init__)
    :   Parameters:
        :   **base_arch** ([*Architecture*](#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"))

    register() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#ArchitectureHook.register)
    :   Return type:
        :   *None*

    *property* base_arch*: [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

## BasicBlockAnalysisContext

*class* BasicBlockAnalysisContext[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Used by `analyze_basic_blocks` and contains analysis settings and other contextual
    information.

    Note

    This class is meant to be used by Architecture plugins only

    __init__(*_handle: BNBasicBlockAnalysisContext*, *_function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *_contextual_returns_dirty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *_indirect_branches: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IndirectBranchInfo](variable.md#binaryninja.variable.IndirectBranchInfo "binaryninja.variable.IndirectBranchInfo")]*, *_indirect_no_return_calls: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*, *_analysis_skip_override: [FunctionAnalysisSkipOverride](enums.md#binaryninja.enums.FunctionAnalysisSkipOverride "binaryninja.enums.FunctionAnalysisSkipOverride")*, *_guided_analysis_mode: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *_trigger_guided_on_invalid_instruction: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *_translate_tail_calls: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *_disallow_branch_to_string: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *_max_function_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *_max_size_reached: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *_contextual_returns: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *_direct_code_references: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*, *_direct_no_return_calls: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*, *_halted_disassembly_addresses: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **_handle** (*BNBasicBlockAnalysisContext*)
            - **_function** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function"))
            - **_contextual_returns_dirty**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"))
            - **_indirect_branches**
              ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*IndirectBranchInfo*](variable.md#binaryninja.variable.IndirectBranchInfo
              "binaryninja.variable.IndirectBranchInfo")*]*)
            - **_indirect_no_return_calls**
              ([*Set*](https://docs.python.org/3/library/typing.html#typing.Set "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]*)
            - **_analysis_skip_override**
              ([*FunctionAnalysisSkipOverride*](enums.md#binaryninja.enums.FunctionAnalysisSkipOverride
              "binaryninja.enums.FunctionAnalysisSkipOverride"))
            - **_guided_analysis_mode**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"))
            - **_trigger_guided_on_invalid_instruction**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"))
            - **_translate_tail_calls**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"))
            - **_disallow_branch_to_string**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"))
            - **_max_function_size** ([*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)"))
            - **_max_size_reached** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)"))
            - **_contextual_returns**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*,*
              [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*]*)
            - **_direct_code_references**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]*)
            - **_direct_no_return_calls**
              ([*Set*](https://docs.python.org/3/library/typing.html#typing.Set "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]*)
            - **_halted_disassembly_addresses**
              ([*Set*](https://docs.python.org/3/library/typing.html#typing.Set "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]*)

        Return type:
        :   *None*

    add_basic_block(*block: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.add_basic_block)
    :   `add_basic_block` adds a BasicBlock to the current function.

        Parameters:
        :   **block** ([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock")) – The BasicBlock to add

        Return type:
        :   *None*

    add_contextual_return(*loc: [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")*, *value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.add_contextual_return)
    :   `add_contextual_return` adds a contextual function return location and its value to the
        current function.

        Parameters:
        :   - **loc** ([*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")) – The location of the contextual function return
            - **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – The value of the contextual function return

        Return type:
        :   *None*

    add_direct_code_reference(*target: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source: [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.add_direct_code_reference)
    :   `add_direct_code_reference` adds a direct code reference to the current function.

        Parameters:
        :   - **target** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The target address of the direct code reference
            - **source** ([*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")) – The source location of the direct code reference

        Return type:
        :   *None*

    add_direct_no_return_call(*loc: [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.add_direct_no_return_call)
    :   `add_direct_no_return_call` adds a direct no-return call location to the current
        function.

        Parameters:
        :   **loc** ([*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
            "binaryninja.function.ArchAndAddr")) – The location of the direct no-return call

        Return type:
        :   *None*

    add_halted_disassembly_address(*loc: [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.add_halted_disassembly_address)
    :   `add_halted_disassembly_address` adds an address to the set of halted disassembly
        addresses.

        Parameters:
        :   **loc** ([*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
            "binaryninja.function.ArchAndAddr")) – The location of the halted disassembly address

        Return type:
        :   *None*

    add_temp_outgoing_reference(*target: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.add_temp_outgoing_reference)
    :   `add_temp_outgoing_reference` adds a temporary outgoing reference to the specified
        function.

        Parameters:
        :   **target** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) – The target function to add a temporary outgoing
            reference to

        Return type:
        :   *None*

    create_basic_block(*arch: [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.create_basic_block)
    :   `create_basic_block` creates a new BasicBlock at the specified address for the given
        Architecture.

        Parameters:
        :   - **arch** ([*Architecture*](#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture of the BasicBlock to create
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Address of the BasicBlock to create

        Return type:
        :   [*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock") | *None*

    finalize() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.finalize)
    :   `finalize` finalizes the function’s basic block analysis

        Return type:
        :   *None*

    *static* from_core_struct(*bn_bb_context: BNBasicBlockAnalysisContext*) → [BasicBlockAnalysisContext](#binaryninja.architecture.BasicBlockAnalysisContext "binaryninja.architecture.BasicBlockAnalysisContext")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#BasicBlockAnalysisContext.from_core_struct)
    :   Create a BasicBlockAnalysisContext from a core.BNBasicBlockAnalysisContext structure.

        Parameters:
        :   **bn_bb_context** (*BNBasicBlockAnalysisContext*)

        Return type:
        :   [*BasicBlockAnalysisContext*](#binaryninja.architecture.BasicBlockAnalysisContext
            "binaryninja.architecture.BasicBlockAnalysisContext")

    *property* analysis_skip_override*: [FunctionAnalysisSkipOverride](enums.md#binaryninja.enums.FunctionAnalysisSkipOverride "binaryninja.enums.FunctionAnalysisSkipOverride")*
    :   Get the analysis skip override setting for this context.

    *property* contextual_returns*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*
    :   Get the mapping of contextual function return locations to their values.

    *property* direct_code_references*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*
    :   Get the mapping of direct code reference targets to their source locations.

    *property* direct_no_return_calls*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*
    :   Get the set of direct no-return call locations in this context.

    *property* disallow_branch_to_string*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Get setting from context that determines if branches to string addresses should be
        disallowed.

    *property* function_arch_context*: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*
    :   Get the function architecture context

    *property* guided_analysis_mode*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Get the setting that determines if functions start in guided analysis mode.

    *property* halt_on_invalid_instruction*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Get the setting from context that determines if analysis should halt on invalid
        instructions.

    *property* halted_disassembly_addresses*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*
    :   Get the set of addresses where disassembly has been halted.

    *property* indirect_branches*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IndirectBranchInfo](variable.md#binaryninja.variable.IndirectBranchInfo "binaryninja.variable.IndirectBranchInfo")]*
    :   Get the list of indirect branches in this context.

    *property* indirect_no_return_calls*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*
    :   Get the set of indirect no-return calls in this context.

    *property* lifter_instruction_data*: [LifterInstructionData](#binaryninja.architecture.LifterInstructionData "binaryninja.architecture.LifterInstructionData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The per-function instruction byte store. Populate it during basic block analysis so that
        lifting can read instruction bytes without touching the view from the multi-threaded
        stage.

    *property* max_function_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Get the maximum function size setting for this context.

    *property* max_size_reached*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Get boolean that indicates if the maximum function size has been reached.

    *property* translate_tail_calls*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Get setting from context that determines if tail calls should be translated.

    *property* trigger_guided_on_invalid_instruction*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Get the setting that determines if guided mode should be triggered on invalid
        instructions.

## CoreArchitecture

*class* CoreArchitecture[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture)
:   Bases: [`Architecture`](#binaryninja.architecture.Architecture
    "binaryninja.architecture.Architecture")

    __init__(*handle: BNArchitecture*)[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.__init__)
    :   Parameters:
        :   **handle** (*BNArchitecture*)

    always_branch(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.always_branch)
    :   `always_branch` reads the instruction(s) in `data` at virtual address `addr` and returns
        a string of bytes of the same length which always branches.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   string containing len(data) which always branches to the same location as the provided
            instruction

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> data = arch.always_branch(arch.assemble("je 10"), 0)
            >>> arch.get_instruction_text(data, 0)
            (['nop', '     '], 1)
            >>> arch.get_instruction_text(bytes[1:], 0)
            (['jmp', '     ', '0x9'], 5)
            >>>
            ```

    assemble(*code: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.assemble)
    :   `assemble` converts the string of assembly instructions `code` loaded at virtual address
        `addr` to the byte representation of those instructions.

        Parameters:
        :   - **code** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – string representation of the instructions to be assembled
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address that the instructions will be loaded at

        Returns:
        :   the bytes for the assembled instructions

        Return type:
        :   Python3 - a ‘bytes’ object; Python2 - a ‘bytes’ object

        Example:
        :   ```
            >>> arch.assemble("je 10")
            b'\x0f\x84\x04\x00\x00\x00'
            >>>
            ```

    convert_to_nop(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.convert_to_nop)
    :   `convert_to_nop` reads the instruction(s) in `data` at virtual address `addr` and
        returns a string of nop instructions of the same length as data.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   string containing len(data) worth of no-operation instructions

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.convert_to_nop(b"\x00\x00", 0)
            b'\x90\x90'
            >>>
            ```

    get_associated_arch_by_address(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_associated_arch_by_address)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Architecture*](#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture"),
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]

    get_flag_condition_low_level_il(*cond: [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")*, *sem_class: SemanticClassName | [ILSemanticFlagClass](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | SemanticClassIndex*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_flag_condition_low_level_il)
    :   Parameters:
        :   - **cond** ([*LowLevelILFlagCondition*](enums.md#binaryninja.enums.LowLevelILFlagCondition
              "binaryninja.enums.LowLevelILFlagCondition")) – Flag condition to be computed
            - **sem_class** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Semantic class to be used (None for default semantics)
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – LowLevelILFunction object to append
              ExpressionIndex objects to

        Return type:
        :   ExpressionIndex

    get_flag_role(*flag: FlagIndex*, *sem_class: SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [FlagRole](enums.md#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_flag_role)
    :   `get_flag_role` gets the role of a given flag.

        Parameters:
        :   - **flag** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – flag
            - **sem_class** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional semantic flag class

        Returns:
        :   flag role

        Return type:
        :   [*FlagRole*](enums.md#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole")

    get_flag_write_low_level_il(*op: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *write_type: FlagWriteTypeName*, *flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*, *operands: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[lowlevelil.ILRegisterType]*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → lowlevelil.ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_flag_write_low_level_il)
    :   Parameters:
        :   - **op** ([*LowLevelILOperation*](enums.md#binaryninja.enums.LowLevelILOperation
              "binaryninja.enums.LowLevelILOperation"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **write_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **operands** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*) or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*)*) – a list of either items that are either string register names or constant
              integer values
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction"))
            - **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
              "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*)

        Return type:
        :   ExpressionIndex

    get_flags_required_for_flag_condition(*cond: [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")*, *sem_class: SemanticClassName | [ILSemanticFlagClass](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | SemanticClassIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[FlagName][[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_flags_required_for_flag_condition)
    :   Parameters:
        :   - **cond** ([*LowLevelILFlagCondition*](enums.md#binaryninja.enums.LowLevelILFlagCondition
              "binaryninja.enums.LowLevelILFlagCondition"))
            - **sem_class** (*SemanticClassName* *|*
              [*ILSemanticFlagClass*](lowlevelil.md#binaryninja.lowlevelil.ILSemanticFlagClass
              "binaryninja.lowlevelil.ILSemanticFlagClass") *|* *SemanticClassIndex* *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[*FlagName*]

    get_instruction_info(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [InstructionInfo](#binaryninja.architecture.InstructionInfo "binaryninja.architecture.InstructionInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_instruction_info)
    :   `get_instruction_info` returns an InstructionInfo object for the instruction at the
        given virtual address `addr` with data `data`.

        Note

        The instruction info object should always set the InstructionInfo.length to the
        instruction length, and the branches of the proper types should be added if the
        instruction is a branch.

        Parameters:
        :   - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`

        Returns:
        :   the InstructionInfo for the current instruction

        Return type:
        :   [*InstructionInfo*](#binaryninja.architecture.InstructionInfo
            "binaryninja.architecture.InstructionInfo")

    get_instruction_low_level_il(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_instruction_low_level_il)
    :   `get_instruction_low_level_il` appends lowlevelil.ExpressionIndex objects to `il` for
        the instruction at the given virtual address `addr` with data `data`.

        This is used to analyze arbitrary data at an address, if you are working with an
        existing binary, you likely want to be using `Function.get_low_level_il_at`.

        Parameters:
        :   - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – The function the current instruction
              belongs to

        Returns:
        :   the length of the current instruction

        Return type:
        :   *Optional*[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]

    get_instruction_text(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_instruction_text)
    :   `get_instruction_text` returns a list of InstructionTextToken objects for the
        instruction at the given virtual address `addr` with data `data`.

        Parameters:
        :   - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – a maximum of max_instruction_length bytes from the binary at virtual address
              `addr`
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of bytes in `data`

        Returns:
        :   an InstructionTextToken list for the current instruction

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*InstructionTextToken*](#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken"))

    get_semantic_flag_group_low_level_il(*sem_group: SemanticGroupName*, *il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.get_semantic_flag_group_low_level_il)
    :   Parameters:
        :   - **sem_group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **il** ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction"))

        Return type:
        :   ExpressionIndex

    invert_branch(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.invert_branch)
    :   `invert_branch` reads the instruction(s) in `data` at virtual address `addr` and returns
        a string of bytes of the same length which inverts the branch of provided instruction.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   string containing len(data) which always branches to the same location as the provided
            instruction

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.get_instruction_text(arch.invert_branch(arch.assemble("je 10"), 0), 0)
            (['jne', '     ', '0xa'], 6)
            >>> arch.get_instruction_text(arch.invert_branch(arch.assemble("jo 10"), 0), 0)
            (['jno', '     ', '0xa'], 6)
            >>> arch.get_instruction_text(arch.invert_branch(arch.assemble("jge 10"), 0), 0)
            (['jl', '      ', '0xa'], 6)
            >>>
            ```

    is_always_branch_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.is_always_branch_patch_available)
    :   `is_always_branch_patch_available` determines if the instruction `data` at `addr` can be
        made to **always branch**.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_always_branch_patch_available(arch.assemble("je 10"), 0)
            True
            >>> arch.is_always_branch_patch_available(arch.assemble("nop"), 0)
            False
            >>>
            ```

    is_invert_branch_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.is_invert_branch_patch_available)
    :   `is_always_branch_patch_available` determines if the instruction `data` at `addr` can be
        inverted.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_invert_branch_patch_available(arch.assemble("je 10"), 0)
            True
            >>> arch.is_invert_branch_patch_available(arch.assemble("nop"), 0)
            False
            >>>
            ```

    is_never_branch_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.is_never_branch_patch_available)
    :   `is_never_branch_patch_available` determines if the instruction `data` at `addr` can be
        made to **never branch**.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_never_branch_patch_available(arch.assemble("je 10"), 0)
            True
            >>> arch.is_never_branch_patch_available(arch.assemble("nop"), 0)
            False
            >>>
            ```

    is_skip_and_return_value_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.is_skip_and_return_value_patch_available)
    :   `is_skip_and_return_value_patch_available` determines if the instruction `data` at
        `addr` is a *call-like* instruction that can be made into an instruction *returns a
        value*.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_skip_and_return_value_patch_available(arch.assemble("call 0"), 0)
            True
            >>> arch.is_skip_and_return_value_patch_available(arch.assemble("jmp eax"), 0)
            False
            >>>
            ```

    is_skip_and_return_zero_patch_available(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.is_skip_and_return_zero_patch_available)
    :   `is_skip_and_return_zero_patch_available` determines if the instruction `data` at `addr`
        is a *call-like* instruction that can be made into an instruction *returns zero*.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be checked
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.is_skip_and_return_zero_patch_available(arch.assemble("call 0"), 0)
            True
            >>> arch.is_skip_and_return_zero_patch_available(arch.assemble("call eax"), 0)
            True
            >>> arch.is_skip_and_return_zero_patch_available(arch.assemble("jmp eax"), 0)
            False
            >>>
            ```

    skip_and_return_value(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#CoreArchitecture.skip_and_return_value)
    :   `skip_and_return_value` reads the instruction(s) in `data` at virtual address `addr` and
        returns a string of bytes of the same length which doesn’t call and instead *return a
        value*.

        Parameters:
        :   - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes for the instruction to be converted
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the value to return

        Returns:
        :   string containing len(data) which always branches to the same location as the provided
            instruction

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> arch.get_instruction_text(arch.skip_and_return_value(arch.assemble("call 10"), 0, 0), 0)
            (['mov', '     ', 'eax', ', ', '0x0'], 5)
            >>>
            ```

## FunctionLifterContext

*class* FunctionLifterContext[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#FunctionLifterContext)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Used by `lift_function` and contains contextual information for function-level lifting

    Note

    This class is meant to be used by Architecture plugins only

    __init__(*_handle: BNFunctionLifterContext*, *_function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *_platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*, *_logger: [Logger](log.md#binaryninja.log.Logger "binaryninja.log.Logger")*, *_blocks: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*, *_contextual_returns: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *_inline_remapping: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]*, *_user_indirect_branches: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]]*, *_auto_indirect_branches: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr"), [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")]]*, *_inlined_calls: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *_function_arch_context_token: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **_handle** (*BNFunctionLifterContext*)
            - **_function** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function"))
            - **_platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform"))
            - **_logger** ([*Logger*](log.md#binaryninja.log.Logger "binaryninja.log.Logger"))
            - **_blocks** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock")*]*)
            - **_contextual_returns**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*,*
              [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*]*)
            - **_inline_remapping**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*,*
              [*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]*)
            - **_user_indirect_branches**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*,*
              [*Set*](https://docs.python.org/3/library/typing.html#typing.Set "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]**]*)
            - **_auto_indirect_branches**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*,*
              [*Set*](https://docs.python.org/3/library/typing.html#typing.Set "(in Python
              v3.14)")*[*[*ArchAndAddr*](function.md#binaryninja.function.ArchAndAddr
              "binaryninja.function.ArchAndAddr")*]**]*)
            - **_inlined_calls** ([*Set*](https://docs.python.org/3/library/typing.html#typing.Set
              "(in Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]*)
            - **_function_arch_context_token**
              ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"))

        Return type:
        :   *None*

    *static* from_core_struct(*func: BNLowLevelILFunction*, *bn_fl_context: BNFunctionLifterContext*) → [FunctionLifterContext](#binaryninja.architecture.FunctionLifterContext "binaryninja.architecture.FunctionLifterContext")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#FunctionLifterContext.from_core_struct)
    :   Create a FunctionLifterContext from a core.BNFunctionLifterContext structure.

        Parameters:
        :   - **func** (*BNLowLevelILFunction*)
            - **bn_fl_context** (*BNFunctionLifterContext*)

        Return type:
        :   [*FunctionLifterContext*](#binaryninja.architecture.FunctionLifterContext
            "binaryninja.architecture.FunctionLifterContext")

    prepare_block_translation(*function*, *arch*, *address*)[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#FunctionLifterContext.prepare_block_translation)
    :   Prepare the basic block for translation

    *property* blocks*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   Get the list of basic blocks in this context

    *property* function_arch_context*: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*
    :   Get the function architecture context

    *property* lifter_instruction_data*: [LifterInstructionData](#binaryninja.architecture.LifterInstructionData "binaryninja.architecture.LifterInstructionData") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The per-function instruction byte store populated during basic block analysis.

## InstructionBranch

*class* InstructionBranch[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#InstructionBranch)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*type: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*, *target: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType"))
            - **target** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    arch*: [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    target*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*

## InstructionInfo

*class* InstructionInfo[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#InstructionInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*length: int = 0*, *arch_transition_by_target_addr: bool = False*, *branch_delay: int = 0*, *branches: ~typing.List[~binaryninja.architecture.InstructionBranch] = <factory>*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch_transition_by_target_addr**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"))
            - **branch_delay** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **branches** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*InstructionBranch*](#binaryninja.architecture.InstructionBranch
              "binaryninja.architecture.InstructionBranch")*]*)

        Return type:
        :   *None*

    add_branch(*branch_type: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*, *target: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *arch: [Architecture](#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#InstructionInfo.add_branch)
    :   Parameters:
        :   - **branch_type** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType"))
            - **target** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **arch** ([*Architecture*](#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*)

        Return type:
        :   *None*

    arch_transition_by_target_addr*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")* *= False*

    branch_delay*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    branches*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionBranch](#binaryninja.architecture.InstructionBranch "binaryninja.architecture.InstructionBranch")]*

    length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

## InstructionTextToken

*class* InstructionTextToken[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#InstructionTextToken)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class InstructionTextToken` is used to tell the core about the various components in
    the disassembly views.

    The below table is provided for documentation purposes but the complete list of
    TokenTypes is available at: `enums.InstructionTextTokenType`. Note that types marked as
    Not emitted by architectures are not intended to be used by Architectures during
    lifting. Rather, they are added by the core during analysis or display. UI plugins,
    however, may make use of them as appropriate.

    Uses of tokens include plugins that parse the output of an architecture (though parsing
    IL is recommended), or additionally, applying color schemes appropriately.

    > | InstructionTextTokenType | Description |
    > | --- | --- |
    > | AddressDisplayToken | **Not emitted by architectures** |
    > | AnnotationToken | **Not emitted by architectures** |
    > | ArgumentNameToken | **Not emitted by architectures** |
    > | BeginMemoryOperandToken | The start of memory operand |
    > | CharacterConstantToken | A printable character |
    > | CodeRelativeAddressToken | **Not emitted by architectures** |
    > | CodeSymbolToken | **Not emitted by architectures** |
    > | DataSymbolToken | **Not emitted by architectures** |
    > | EndMemoryOperandToken | The end of a memory operand |
    > | ExternalSymbolToken | **Not emitted by architectures** |
    > | FieldNameToken | **Not emitted by architectures** |
    > | FloatingPointToken | Floating point number |
    > | HexDumpByteValueToken | **Not emitted by architectures** |
    > | HexDumpInvalidByteToken | **Not emitted by architectures** |
    > | HexDumpSkippedByteToken | **Not emitted by architectures** |
    > | HexDumpTextToken | **Not emitted by architectures** |
    > | ImportToken | **Not emitted by architectures** |
    > | IndirectImportToken | **Not emitted by architectures** |
    > | InstructionToken | The instruction mnemonic |
    > | IntegerToken | Integers |
    > | KeywordToken | **Not emitted by architectures** |
    > | LocalVariableToken | **Not emitted by architectures** |
    > | StackVariableToken | **Not emitted by architectures** |
    > | NameSpaceSeparatorToken | **Not emitted by architectures** |
    > | NameSpaceToken | **Not emitted by architectures** |
    > | OpcodeToken | **Not emitted by architectures** |
    > | OperandSeparatorToken | The comma or delimiter that separates tokens |
    > | PossibleAddressToken | Integers that are likely addresses |
    > | RegisterToken | Registers |
    > | StringToken | **Not emitted by architectures** |
    > | StructOffsetToken | **Not emitted by architectures** |
    > | TagToken | **Not emitted by architectures** |
    > | TextToken | Used for anything not of another type. |
    > | CommentToken | Comments |
    > | TypeNameToken | **Not emitted by architectures** |
    > | AddressSeparatorToken | **Not emitted by architectures** |
    > | NewLineToken | New lines |

    __init__(*type: ~binaryninja.enums.InstructionTextTokenType | int*, *text: str*, *value: int = 0*, *size: int = 0*, *operand: int = 4294967295*, *context: ~binaryninja.enums.InstructionTextTokenContext = InstructionTextTokenContext.NoTokenContext*, *address: int = 0*, *confidence: int = 255*, *typeNames: ~typing.List[str] = <factory>*, *width: int = 0*, *il_expr_index: int = 18446744073709551615*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type**
              ([*InstructionTextTokenType*](enums.md#binaryninja.enums.InstructionTextTokenType
              "binaryninja.enums.InstructionTextTokenType") *|*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"))
            - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **context**
              ([*InstructionTextTokenContext*](enums.md#binaryninja.enums.InstructionTextTokenContext
              "binaryninja.enums.InstructionTextTokenContext"))
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **typeNames** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*)
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **il_expr_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))

        Return type:
        :   *None*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 255*

    context*: [InstructionTextTokenContext](enums.md#binaryninja.enums.InstructionTextTokenContext "binaryninja.enums.InstructionTextTokenContext")* *= 0*

    il_expr_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 18446744073709551615*

    operand*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 4294967295*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    text*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    type*: [InstructionTextTokenType](enums.md#binaryninja.enums.InstructionTextTokenType "binaryninja.enums.InstructionTextTokenType") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    typeNames*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

    value*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

## IntrinsicInfo

*class* IntrinsicInfo[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#IntrinsicInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*inputs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IntrinsicInput](#binaryninja.architecture.IntrinsicInput "binaryninja.architecture.IntrinsicInput")]*, *outputs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **inputs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*IntrinsicInput*](#binaryninja.architecture.IntrinsicInput
              "binaryninja.architecture.IntrinsicInput")*]*)
            - **outputs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")*]*)
            - **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

    index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    inputs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IntrinsicInput](#binaryninja.architecture.IntrinsicInput "binaryninja.architecture.IntrinsicInput")]*

    outputs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*

## IntrinsicInput

*class* IntrinsicInput[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#IntrinsicInput)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")* *= ''*

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

## LifterInstructionData

*class* LifterInstructionData[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#LifterInstructionData)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Per-function store of basic block instruction bytes, populated during basic block analysis and
    :   read during lifting.

    Note

    This class is meant to be used by Architecture plugins only

    __init__(*handle: LP_BNLifterInstructionData*)[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#LifterInstructionData.__init__)
    :   Parameters:
        :   **handle** (*LP_BNLifterInstructionData*)

    append(*block: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#LifterInstructionData.append)
    :   Append decoded bytes for a block. Call during basic block analysis only.

        Parameters:
        :   - **block** ([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock"))
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)"))

        Return type:
        :   *None*

    get(*block: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#LifterInstructionData.get)
    :   Returns the bytes from `addr` to the end of its block, or `b''` when the block has no
        stored data. Read-only, call during lifting.

        Parameters:
        :   - **block** ([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock"))
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")

## RegisterInfo

*class* RegisterInfo[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#RegisterInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*full_width_reg: RegisterName*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *extend: [ImplicitRegisterExtend](enums.md#binaryninja.enums.ImplicitRegisterExtend "binaryninja.enums.ImplicitRegisterExtend") = ImplicitRegisterExtend.NoExtend*, *index: RegisterIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **full_width_reg** (*RegisterName*)
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **extend** ([*ImplicitRegisterExtend*](enums.md#binaryninja.enums.ImplicitRegisterExtend
              "binaryninja.enums.ImplicitRegisterExtend"))
            - **index** (*RegisterIndex* *|* *None*)

        Return type:
        :   *None*

    extend*: [ImplicitRegisterExtend](enums.md#binaryninja.enums.ImplicitRegisterExtend "binaryninja.enums.ImplicitRegisterExtend")* *= 0*

    full_width_reg*: RegisterName*

    index*: RegisterIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")* *= 0*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## RegisterStackInfo

*class* RegisterStackInfo[[source]](https://api.binary.ninja/_modules/binaryninja/architecture.html#RegisterStackInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*storage_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*, *top_relative_regs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*, *stack_top_reg: RegisterName*, *index: RegisterStackIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **storage_regs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[**RegisterName**]*)
            - **top_relative_regs**
              ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**RegisterName**]*)
            - **stack_top_reg** (*RegisterName*)
            - **index** (*RegisterStackIndex* *|* *None*)

        Return type:
        :   *None*

    index*: RegisterStackIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    stack_top_reg*: RegisterName*

    storage_regs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*

    top_relative_regs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[RegisterName]*
