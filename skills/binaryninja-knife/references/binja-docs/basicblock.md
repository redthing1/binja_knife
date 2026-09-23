# basicblock module

| Class | Description |
| --- | --- |
| [`binaryninja.basicblock.BasicBlock`](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | The `class BasicBlock` object is returned during analysis and should not be directly instantiated. |
| [`binaryninja.basicblock.BasicBlockEdge`](#binaryninja.basicblock.BasicBlockEdge "binaryninja.basicblock.BasicBlockEdge") | `class BasicBlockEdge` represents the edges that connect basic blocks in graph view. |
| [`binaryninja.basicblock.PendingBasicBlockEdge`](#binaryninja.basicblock.PendingBasicBlockEdge "binaryninja.basicblock.PendingBasicBlockEdge") | `class PendingBasicBlockEdge` represents a pending edge that has not yet been resolved. |

## BasicBlock

*class* BasicBlock[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `class BasicBlock` object is returned during analysis and should not be directly
    instantiated.

    Basic blocks contain a sequence of instructions that must execute in-order with no
    branches. We include calls in basic blocks, which technically violates that assumption,
    but you can mark functions as func.can_return = False if a given function should
    terminate basic blocks. :Example:

    ```
    >>> for func in bv.functions:
    >>>   for bb in func:
    >>>     # Any block-based analysis could start here
    >>>     for inst in bb:
    >>>       pass # Optionally do something here with instructions
    ```

    __init__(*handle: LP_BNBasicBlock*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNBasicBlock*) –
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –

    add_instruction_data(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.add_instruction_data)
    :   Adds raw instruction data to the basic block.

        Note

        This method is intended for use by architecture plugins only.

        Parameters:
        :   **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
            v3.14)")) – Raw instruction data to add to the basic block.

        Return type:
        :   *None*

    add_pending_outgoing_edge(*typ: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *fallthrough: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.add_pending_outgoing_edge)
    :   Adds a pending outgoing edge to the basic block. This is used to add edges that are not
        yet resolved.

        Note

        This method is intended for use by architecture plugins only.

        Parameters:
        :   - **typ** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType")) – The type of the branch.
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The address of the target basic block.
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – The architecture of the target basic block.
            - **fallthrough** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether this edge is a fallthrough edge.

        Return type:
        :   *None*

    clear_pending_outgoing_edges() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.clear_pending_outgoing_edges)
    :   Clears all pending outgoing edges for the basic block. This is used to remove edges that
        have not yet been resolved.

        Note

        This method is intended for use by architecture plugins only.

        Return type:
        :   *None*

    get_disassembly_text(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.get_disassembly_text)
    :   `get_disassembly_text` returns a list of DisassemblyTextLine objects for the current
        basic block.

        Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings")) – (optional) DisassemblySettings object

        Example:
        :   ```
            >>> current_basic_block.get_disassembly_text()
            [<0x100000f30: _main:>, <0x100000f30: push    rbp>, ... ]
            ```

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    get_instruction_containing_address(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.get_instruction_containing_address)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)"), [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]

    get_instruction_data(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.get_instruction_data)
    :   Returns the raw instruction data for the basic block at the specified address.

        Note

        This method is intended for use by architecture plugins only.

        Returns:
        :   Raw instruction data as bytes.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")

    get_iterated_dominance_frontier(*blocks: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")][[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.get_iterated_dominance_frontier)
    :   Calculates the iterated dominance frontier of the given blocks (this is used to
        determine φ node placement)

        Parameters:
        :   **blocks** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*BasicBlock*](#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock")*]*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*BasicBlock*](#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock")]

    get_pending_outgoing_edges() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PendingBasicBlockEdge](#binaryninja.basicblock.PendingBasicBlockEdge "binaryninja.basicblock.PendingBasicBlockEdge")][[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.get_pending_outgoing_edges)
    :   Returns a list of pending outgoing edges for the basic block. These are edges that have
        not yet been resolved.

        Note

        This method is intended for use by architecture plugins only.

        Returns:
        :   List of PendingBasicBlockEdge objects.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")[[*PendingBasicBlockEdge*](#binaryninja.basicblock.PendingBasicBlockEdge
            "binaryninja.basicblock.PendingBasicBlockEdge")]

    mark_recent_use() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.mark_recent_use)
    :   Return type:
        :   *None*

    set_auto_highlight(*color: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.set_auto_highlight)
    :   `set_auto_highlight` highlights the current BasicBlock with the supplied color.

        Warning

        Use only in analysis plugins. Do not use in regular plugins, as colors won’t be saved to
        the database.

        Parameters:
        :   - **color** ([*HighlightColor*](highlight.md#binaryninja.highlight.HighlightColor
              "binaryninja.highlight.HighlightColor")) – Color value to use for highlighting
            - **color** –

        Return type:
        :   *None*

    set_user_highlight(*color: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlock.set_user_highlight)
    :   `set_user_highlight` highlights the current BasicBlock with the supplied color

        Parameters:
        :   - **color** ([*HighlightColor*](highlight.md#binaryninja.highlight.HighlightColor
              "binaryninja.highlight.HighlightColor")) – Color value to use for highlighting
            - **color** –

        Example:
        :   ```
            >>> current_basic_block.set_user_highlight(_highlight.HighlightColor(red=0xff, blue=0xff, green=0))
            >>> current_basic_block.set_user_highlight(HighlightStandardColor.BlueHighlightColor)
            ```

        Return type:
        :   *None*

    *property* annotations*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]]*
    :   List of automatic annotations for the start of this block (read-only)

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*
    :   Basic block architecture (read-only)

    *property* can_exit*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether basic block can return or is tagged as ‘No Return’ (read-only)

    *property* disassembly_text*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*
    :   `disassembly_text` property which returns a list of function.DisassemblyTextLine objects
        for the current basic block.

        Example:
        :   ```
            >>> current_basic_block.disassembly_text
            [<0x100000f30: _main:>, ...]
            ```

    *property* dominance_frontier*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   Dominance frontier for this basic block (read-only)

        The dominance frontier of a basic block B is the set of blocks that are not strictly
        dominated by B, but are immediately control-dependent on B. In other words, it contains
        the blocks where B’s dominance “stops” - the blocks that have at least one predecessor
        not dominated by B, while having another predecessor that is dominated by B.

    *property* dominator_tree_children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   List of child blocks in the dominator tree for this basic block (read-only)

        The dominator tree children of a basic block B are the blocks dominated by B. See
        [`BasicBlock.dominators`](#binaryninja.basicblock.BasicBlock.dominators
        "binaryninja.basicblock.BasicBlock.dominators") for the definition of a dominator.

    *property* dominators*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   List of dominators for this basic block (read-only).

        A dominator of a basic block B is a block that must be executed before B can be
        executed. In other words, every path from the entry block to B must go through the
        dominator. This includes B itself - every block dominates itself. See
        [`BasicBlock.strict_dominators`](#binaryninja.basicblock.BasicBlock.strict_dominators
        "binaryninja.basicblock.BasicBlock.strict_dominators") for dominators that don’t include
        B.

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Basic block end (read-only)

    *property* fallthrough_to_function*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the basic block has a fallthrough edge to a function.

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Basic block function (read-only)

    *property* function_graph_type*: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*
    :   Type of function graph from which this block represents instructions

    *property* has_invalid_instructions*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether basic block has any invalid instructions (read-only)

    *property* has_undetermined_outgoing_edges*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether basic block has undetermined outgoing edges (read-only)

    *property* highlight*: [HighlightColor](highlight.md#binaryninja.highlight.HighlightColor "binaryninja.highlight.HighlightColor")*
    :   Gets or sets the highlight color for basic block

        Example:
        :   ```
            >>> current_basic_block.highlight = HighlightStandardColor.BlueHighlightColor
            >>> current_basic_block.highlight
            <color: blue>
            ```

    *property* il_function*: _function.ILFunctionType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   IL Function of which this block is a part, if the block is part of an IL Function.

    *property* il_function_if_available*: _function.ILFunctionType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   IL Function of which this block is a part, if the block is part of an IL Function, and
        if the function has generated IL already.

    *property* immediate_dominator*: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Immediate dominator of this basic block (read-only)

        The immediate dominator of a basic block B is the dominator closest to B in the control
        flow graph. In other words, among all dominators of B, it is the dominator that doesn’t
        dominate any other dominator of B except itself. Each basic block except the entry block
        has a unique immediate dominator.

    *property* immediate_post_dominator*: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Immediate post-dominator of this basic block (read-only)

        The immediate post-dominator of a basic block B is the post-dominator closest to B in
        the control flow graph. In other words, among all post-dominators of B, it is the
        post-dominator that doesn’t post-dominate any other post-dominator of B except itself.
        If B has outgoing edges that can lead to different exit blocks, then this will not
        exist.

    *property* incoming_edges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlockEdge](#binaryninja.basicblock.BasicBlockEdge "binaryninja.basicblock.BasicBlockEdge")]*
    :   List of basic block incoming edges (read-only)

    *property* index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Basic block index in list of blocks for the function (read-only)

    *property* instruction_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* is_high_level_il*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the basic block contains High Level IL

    *property* is_il*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the basic block contains IL

    *property* is_low_level_il*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the basic block contains Low Level IL

    *property* is_medium_level_il*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the basic block contains Medium Level IL

    *property* length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Basic block length (read-only)

    *property* outgoing_edges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlockEdge](#binaryninja.basicblock.BasicBlockEdge "binaryninja.basicblock.BasicBlockEdge")]*
    :   List of basic block outgoing edges (read-only)

    *property* post_dominance_frontier*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   Post-dominance frontier for this basic block (read-only)

        The post-dominance frontier of a basic block B is the set of blocks that are not
        strictly post-dominated by B, but have at least one successor that is post-dominated by
        B. In other words, it contains the blocks where B’s post-dominance “stops” - the blocks
        that have at least one successor not post-dominated by B, while having another successor
        that is post-dominated by B.

    *property* post_dominator_tree_children*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   List of child blocks in the post-dominator tree for this basic block (read-only)

        The post-dominator tree children of a basic block B are the blocks post-dominated by B.
        See [`BasicBlock.post_dominators`](#binaryninja.basicblock.BasicBlock.post_dominators
        "binaryninja.basicblock.BasicBlock.post_dominators") for the definition of a
        post-dominator.

    *property* post_dominators*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   List of post-dominators for this basic block (read-only)

        A post-dominator of a basic block B is a block that must be executed after B is
        executed. In other words, every path from B to an exit block must go through the
        post-dominator. This includes B itself - every block post-dominates itself. See
        [`BasicBlock.strict_post_dominators`](#binaryninja.basicblock.BasicBlock.strict_post_dominators
        "binaryninja.basicblock.BasicBlock.strict_post_dominators") for post-dominators that
        don’t include B. If B has outgoing edges that can lead to different exit blocks, then
        this will only include B.

    *property* source_block*: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The corresponding assembly-level basic block for this basic block (read-only)

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Basic block start (read-only)

    *property* strict_dominators*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   List of strict dominators for this basic block (read-only)

        A strict dominator of a basic block B is a dominator of B that is not B itself. See
        [`BasicBlock.dominators`](#binaryninja.basicblock.BasicBlock.dominators
        "binaryninja.basicblock.BasicBlock.dominators") for the definition of a dominator.

    *property* strict_post_dominators*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")]*
    :   List of strict post-dominators for this basic block (read-only)

        A strict post-dominator of a basic block B is a post-dominator of B that is not B
        itself. See
        [`BasicBlock.post_dominators`](#binaryninja.basicblock.BasicBlock.post_dominators
        "binaryninja.basicblock.BasicBlock.post_dominators") for the definition of a
        post-dominator.

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   BinaryView that contains the basic block (read-only)

## BasicBlockEdge

*class* BasicBlockEdge[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#BasicBlockEdge)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BasicBlockEdge` represents the edges that connect basic blocks in graph view.

    Variables:
    :   - **type** – The `enums.BranchType` of the edge; Whether the edge is a true branch, false
          branch, unconditional, etc.
        - **source** – The basic block that the edge originates from.
        - **target** – The basic block that the edge is going to.
        - **backedge** – Whether this edge targets to a node whose control flow can eventually
          flow back through the source node of this edge.

    Example:

    ```
    >>> current_basic_block.outgoing_edges
    [<TrueBranch: x86_64@0x6>, <FalseBranch: x86_64@0x1f>]
    ```

    __init__(*type: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*, *source: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*, *target: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*, *back_edge: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *fall_through: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType")) –
            - **source** ([*BasicBlock*](#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock")) –
            - **target** ([*BasicBlock*](#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock")) –
            - **back_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **fall_through** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

        Return type:
        :   *None*

    back_edge*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    fall_through*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    source*: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*

    target*: [BasicBlock](#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*

    type*: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*

## PendingBasicBlockEdge

*class* PendingBasicBlockEdge[[source]](https://api.binary.ninja/_modules/binaryninja/basicblock.html#PendingBasicBlockEdge)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class PendingBasicBlockEdge` represents a pending edge that has not yet been resolved.

    Variables:
    :   - **type** – The edge branch type.
        - **arch** – The architecture of the target basic block.
        - **target** – The address of the target basic block.
        - **fall_through** – Whether this edge is a fallthrough edge.

    __init__(*type: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *target: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *fallthrough: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **target** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **fallthrough** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    fallthrough*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    target*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType")*
