# commonil module

| Class | Description |
| --- | --- |
| [`binaryninja.commonil.AliasedVariableInstruction`](#binaryninja.commonil.AliasedVariableInstruction "binaryninja.commonil.AliasedVariableInstruction") |  |
| [`binaryninja.commonil.Arithmetic`](#binaryninja.commonil.Arithmetic "binaryninja.commonil.Arithmetic") |  |
| [`binaryninja.commonil.BaseILInstruction`](#binaryninja.commonil.BaseILInstruction "binaryninja.commonil.BaseILInstruction") |  |
| [`binaryninja.commonil.BinaryOperation`](#binaryninja.commonil.BinaryOperation "binaryninja.commonil.BinaryOperation") |  |
| [`binaryninja.commonil.Call`](#binaryninja.commonil.Call "binaryninja.commonil.Call") |  |
| [`binaryninja.commonil.Carry`](#binaryninja.commonil.Carry "binaryninja.commonil.Carry") |  |
| [`binaryninja.commonil.Comparison`](#binaryninja.commonil.Comparison "binaryninja.commonil.Comparison") |  |
| [`binaryninja.commonil.Constant`](#binaryninja.commonil.Constant "binaryninja.commonil.Constant") |  |
| [`binaryninja.commonil.ControlFlow`](#binaryninja.commonil.ControlFlow "binaryninja.commonil.ControlFlow") |  |
| [`binaryninja.commonil.DoublePrecision`](#binaryninja.commonil.DoublePrecision "binaryninja.commonil.DoublePrecision") |  |
| [`binaryninja.commonil.FloatingPoint`](#binaryninja.commonil.FloatingPoint "binaryninja.commonil.FloatingPoint") |  |
| [`binaryninja.commonil.ILSourceLocation`](#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | ILSourceLocation is used to indicate where expressions were defined during the lifting process… |
| [`binaryninja.commonil.Intrinsic`](#binaryninja.commonil.Intrinsic "binaryninja.commonil.Intrinsic") |  |
| [`binaryninja.commonil.Load`](#binaryninja.commonil.Load "binaryninja.commonil.Load") |  |
| [`binaryninja.commonil.Localcall`](#binaryninja.commonil.Localcall "binaryninja.commonil.Localcall") |  |
| [`binaryninja.commonil.Loop`](#binaryninja.commonil.Loop "binaryninja.commonil.Loop") |  |
| [`binaryninja.commonil.Memory`](#binaryninja.commonil.Memory "binaryninja.commonil.Memory") |  |
| [`binaryninja.commonil.Phi`](#binaryninja.commonil.Phi "binaryninja.commonil.Phi") |  |
| [`binaryninja.commonil.RegisterStack`](#binaryninja.commonil.RegisterStack "binaryninja.commonil.RegisterStack") |  |
| [`binaryninja.commonil.Return`](#binaryninja.commonil.Return "binaryninja.commonil.Return") |  |
| [`binaryninja.commonil.SSA`](#binaryninja.commonil.SSA "binaryninja.commonil.SSA") |  |
| [`binaryninja.commonil.SSAVariableInstruction`](#binaryninja.commonil.SSAVariableInstruction "binaryninja.commonil.SSAVariableInstruction") |  |
| [`binaryninja.commonil.SetReg`](#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg") |  |
| [`binaryninja.commonil.SetVar`](#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar") |  |
| [`binaryninja.commonil.Signed`](#binaryninja.commonil.Signed "binaryninja.commonil.Signed") |  |
| [`binaryninja.commonil.StackOperation`](#binaryninja.commonil.StackOperation "binaryninja.commonil.StackOperation") |  |
| [`binaryninja.commonil.Store`](#binaryninja.commonil.Store "binaryninja.commonil.Store") |  |
| [`binaryninja.commonil.Syscall`](#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall") |  |
| [`binaryninja.commonil.Tailcall`](#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall") |  |
| [`binaryninja.commonil.Terminal`](#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal") |  |
| [`binaryninja.commonil.UnaryOperation`](#binaryninja.commonil.UnaryOperation "binaryninja.commonil.UnaryOperation") |  |
| [`binaryninja.commonil.VariableInstruction`](#binaryninja.commonil.VariableInstruction "binaryninja.commonil.VariableInstruction") |  |

## AliasedVariableInstruction

*class* AliasedVariableInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#AliasedVariableInstruction)
:   Bases: [`VariableInstruction`](#binaryninja.commonil.VariableInstruction
    "binaryninja.commonil.VariableInstruction")

    AliasedVariableInstruction()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Arithmetic

*class* Arithmetic[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Arithmetic)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Arithmetic()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## BaseILInstruction

*class* BaseILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#BaseILInstruction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    BaseILInstruction()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

    *classmethod* add_subgraph(*graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *nodes*) → [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#BaseILInstruction.add_subgraph)
    :   Parameters:
        :   **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph")) –

        Return type:
        :   [*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph")

    *classmethod* prepend_parent(*graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *node: [FlowGraphNode](flowgraph.md#binaryninja.flowgraph.FlowGraphNode "binaryninja.flowgraph.FlowGraphNode")*, *nodes={}*)[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#BaseILInstruction.prepend_parent)
    :   Parameters:
        :   - **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
              "binaryninja.flowgraph.FlowGraph")) –
            - **node** ([*FlowGraphNode*](flowgraph.md#binaryninja.flowgraph.FlowGraphNode
              "binaryninja.flowgraph.FlowGraphNode")) –

    *classmethod* show_hierarchy_graph()[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#BaseILInstruction.show_hierarchy_graph)

## BinaryOperation

*class* BinaryOperation[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#BinaryOperation)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    BinaryOperation()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Call

*class* Call[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Call)
:   Bases: [`ControlFlow`](#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    Call()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Carry

*class* Carry[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Carry)
:   Bases: [`Arithmetic`](#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    Carry()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Comparison

*class* Comparison[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Comparison)
:   Bases: [`BinaryOperation`](#binaryninja.commonil.BinaryOperation
    "binaryninja.commonil.BinaryOperation")

    Comparison()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Constant

*class* Constant[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Constant)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Constant()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## ControlFlow

*class* ControlFlow[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#ControlFlow)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    ControlFlow()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## DoublePrecision

*class* DoublePrecision[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#DoublePrecision)
:   Bases: [`Arithmetic`](#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    DoublePrecision()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## FloatingPoint

*class* FloatingPoint[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#FloatingPoint)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    FloatingPoint()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## ILSourceLocation

*class* ILSourceLocation[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#ILSourceLocation)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILSourceLocation is used to indicate where expressions were defined during the lifting
    process and gets propagated through the lifting process as an instruction’s
    address/source_operand properties. These are used for, for example, integer display
    types and expression addresses.

    __init__(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source_operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#ILSourceLocation.__init__)
    :   Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **source_operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –

    *classmethod* from_instruction(*instr: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*, *il_direct: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [ILSourceLocation](#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation")[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#ILSourceLocation.from_instruction)
    :   Get the source location of a given instruction :param instr: Instruction, Low, Medium,
        or High level :return: Its location

        Parameters:
        :   - **instr**
              ([*LowLevelILInstruction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction") *|*
              [*MediumLevelILInstruction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction") *|*
              [*HighLevelILInstruction*](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")) –
            - **il_direct** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

        Return type:
        :   [*ILSourceLocation*](#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    il_direct*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")* *= True*

    source_hlil_instruction*: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    source_llil_instruction*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    source_mlil_instruction*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    source_operand*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## Intrinsic

*class* Intrinsic[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Intrinsic)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Intrinsic()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Load

*class* Load[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Load)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Load()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Localcall

*class* Localcall[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Localcall)
:   Bases: [`Call`](#binaryninja.commonil.Call "binaryninja.commonil.Call")

    Localcall()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Loop

*class* Loop[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Loop)
:   Bases: [`ControlFlow`](#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    Loop()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Memory

*class* Memory[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Memory)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Memory()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Phi

*class* Phi[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Phi)
:   Bases: [`SSA`](#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    Phi()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## RegisterStack

*class* RegisterStack[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#RegisterStack)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    RegisterStack()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Return

*class* Return[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Return)
:   Bases: [`Terminal`](#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    Return()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## SSA

*class* SSA[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#SSA)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    SSA()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## SSAVariableInstruction

*class* SSAVariableInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#SSAVariableInstruction)
:   Bases: [`SSA`](#binaryninja.commonil.SSA "binaryninja.commonil.SSA"),
    [`VariableInstruction`](#binaryninja.commonil.VariableInstruction
    "binaryninja.commonil.VariableInstruction")

    SSAVariableInstruction()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## SetReg

*class* SetReg[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#SetReg)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SetReg()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## SetVar

*class* SetVar[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#SetVar)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    SetVar()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Signed

*class* Signed[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Signed)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Signed()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## StackOperation

*class* StackOperation[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#StackOperation)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    StackOperation()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Store

*class* Store[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Store)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    Store()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Syscall

*class* Syscall[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Syscall)
:   Bases: [`Call`](#binaryninja.commonil.Call "binaryninja.commonil.Call")

    Syscall()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Tailcall

*class* Tailcall[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Tailcall)
:   Bases: [`Localcall`](#binaryninja.commonil.Localcall "binaryninja.commonil.Localcall")

    Tailcall()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## Terminal

*class* Terminal[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#Terminal)
:   Bases: [`ControlFlow`](#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    Terminal()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## UnaryOperation

*class* UnaryOperation[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#UnaryOperation)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    UnaryOperation()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*

## VariableInstruction

*class* VariableInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/commonil.html#VariableInstruction)
:   Bases: [`BaseILInstruction`](#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    VariableInstruction()

    __init__() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return type:
        :   *None*
