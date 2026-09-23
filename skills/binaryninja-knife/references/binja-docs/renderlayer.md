# renderlayer module

| Class | Description |
| --- | --- |
| [`binaryninja.renderlayer.CoreRenderLayer`](#binaryninja.renderlayer.CoreRenderLayer "binaryninja.renderlayer.CoreRenderLayer") | RenderLayer is a plugin class that allows you to customize the presentation of Linear and Graph… |
| [`binaryninja.renderlayer.RenderLayer`](#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer") | RenderLayer is a plugin class that allows you to customize the presentation of Linear and Graph… |

## CoreRenderLayer

*class* CoreRenderLayer[[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#CoreRenderLayer)
:   Bases: [`RenderLayer`](#binaryninja.renderlayer.RenderLayer
    "binaryninja.renderlayer.RenderLayer")

    apply_to_flow_graph(*graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#CoreRenderLayer.apply_to_flow_graph)
    :   Apply this Render Layer to a Flow Graph, potentially modifying its nodes, their edges,
        their lines, and their lines’ content.

        Note

        If you override this function, you will need to call the `super()` implementation if you
        want to use the higher level `apply_to_X_level_il_block` functionality.

        Parameters:
        :   **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph")) – Graph to modify

        Return type:
        :   *None*

    apply_to_linear_view_object(*obj: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")*, *prev: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *next: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#CoreRenderLayer.apply_to_linear_view_object)
    :   Apply this Render Layer to the lines produced by a LinearViewObject for rendering in
        Linear View, potentially modifying the lines and their contents.

        Note

        If you override this function, you will need to call the `super()` implementation if you
        want to use the higher level `apply_to_X_level_il_block` functionality.

        Parameters:
        :   - **obj**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject")) – Linear View Object being rendered
            - **prev**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) – Linear View Object
              located directly above this one
            - **next**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) – Linear View Object
              located directly below this one
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
              "binaryninja.lineardisassembly.LinearDisassemblyLine")*]*) – Original lines rendered by
              the Linear View Object

        Returns:
        :   Modified list of lines to display in Linear View

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine")]

## RenderLayer

*class* RenderLayer[[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    RenderLayer is a plugin class that allows you to customize the presentation of Linear
    and Graph view output, adding, changing, or removing lines before they are presented in
    the UI.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.__init__)

    apply_to_block(*block: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_block)
    :   Apply to lines generated by a Basic Block, of any type. If not overridden, this function
        will call the appropriate `apply_to_X_level_il_block` function. Subclasses should return
        a modified list of lines to be rendered in the UI.

        Parameters:
        :   - **block** ([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock")) – Basic Block containing those lines
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*) – Original lines of text for the block

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    apply_to_disassembly_block(*block: [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_disassembly_block)
    :   Apply this Render Layer to a single Basic Block of Disassembly lines. Subclasses should
        return a modified list of lines to be rendered in the UI.

        Note

        This function will only handle Disassembly lines, and not any ILs.

        Parameters:
        :   - **block** ([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
              "binaryninja.basicblock.BasicBlock")) – Basic Block containing those lines
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*) – Original lines of text for the block

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    apply_to_flow_graph(*graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_flow_graph)
    :   Apply this Render Layer to a Flow Graph, potentially modifying its nodes, their edges,
        their lines, and their lines’ content.

        Note

        If you override this function, you will need to call the `super()` implementation if you
        want to use the higher level `apply_to_X_level_il_block` functionality.

        Parameters:
        :   **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph")) – Graph to modify

        Return type:
        :   *None*

    apply_to_high_level_il_block(*block: [HighLevelILBasicBlock](highlevelil.md#binaryninja.highlevelil.HighLevelILBasicBlock "binaryninja.highlevelil.HighLevelILBasicBlock")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_high_level_il_block)
    :   Apply this Render Layer to a single Basic Block of High Level IL lines. Subclasses
        should return a modified list of lines to be rendered in the UI.

        Note

        This function will only handle HLIL/HLIL(SSA)/Language Representation lines. You can use
        the block’s `function_graph_type` property to determine which is being handled.

        Warning

        This function will NOT apply to High Level IL bodies as displayed in Linear View! Those
        are handled by `apply_to_high_level_il_body` instead as they do not have a Basic Block
        associated with them.

        Parameters:
        :   - **block**
              ([*HighLevelILBasicBlock*](highlevelil.md#binaryninja.highlevelil.HighLevelILBasicBlock
              "binaryninja.highlevelil.HighLevelILBasicBlock")) – Basic Block containing those lines
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*) – Original lines of text for the block

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    apply_to_high_level_il_body(*function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_high_level_il_body)
    :   Apply this Render Layer to the entire body of a High Level IL function. Subclasses
        should return a modified list of lines to be rendered in the UI.

        Warning

        This function only applies to Linear View, and not to Graph View! If you want to handle
        Graph View too, you will need to use `apply_to_high_level_il_block` and handle the lines
        one block at a time.

        Parameters:
        :   - **function** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – Function containing those lines
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
              "binaryninja.lineardisassembly.LinearDisassemblyLine")*]*) – Original lines of text for
              the function

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine")]

    apply_to_linear_view_object(*obj: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")*, *prev: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *next: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_linear_view_object)
    :   Apply this Render Layer to the lines produced by a LinearViewObject for rendering in
        Linear View, potentially modifying the lines and their contents.

        Note

        If you override this function, you will need to call the `super()` implementation if you
        want to use the higher level `apply_to_X_level_il_block` functionality.

        Parameters:
        :   - **obj**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject")) – Linear View Object being rendered
            - **prev**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) – Linear View Object
              located directly above this one
            - **next**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) – Linear View Object
              located directly below this one
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
              "binaryninja.lineardisassembly.LinearDisassemblyLine")*]*) – Original lines rendered by
              the Linear View Object

        Returns:
        :   Modified list of lines to display in Linear View

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine")]

    apply_to_low_level_il_block(*block: [LowLevelILBasicBlock](lowlevelil.md#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_low_level_il_block)
    :   Apply this Render Layer to a single Basic Block of Low Level IL lines. Subclasses should
        return a modified list of lines to be rendered in the UI.

        Note

        This function will only handle Lifted IL/LLIL/LLIL(SSA) lines. You can use the block’s
        `function_graph_type` property to determine which is being handled.

        Parameters:
        :   - **block**
              ([*LowLevelILBasicBlock*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILBasicBlock
              "binaryninja.lowlevelil.LowLevelILBasicBlock")) – Basic Block containing those lines
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*) – Original lines of text for the block

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    apply_to_medium_level_il_block(*block: [MediumLevelILBasicBlock](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_medium_level_il_block)
    :   Apply this Render Layer to a single Basic Block of Medium Level IL lines. Subclasses
        should return a modified list of lines to be rendered in the UI.

        Note

        This function will only handle MLIL/MLIL(SSA)/Mapped MLIL/Mapped MLIL(SSA) lines. You
        can use the block’s `function_graph_type` property to determine which is being handled.

        Parameters:
        :   - **block**
              ([*MediumLevelILBasicBlock*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILBasicBlock
              "binaryninja.mediumlevelil.MediumLevelILBasicBlock")) – Basic Block containing those
              lines
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
              "binaryninja.function.DisassemblyTextLine")*]*) – Original lines of text for the block

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    apply_to_misc_linear_lines(*obj: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")*, *prev: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *next: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *lines: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine")][[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.apply_to_misc_linear_lines)
    :   Apply to lines generated by Linear View that are not part of a function. It is up to
        your implementation to figure out which type of Linear View Object lines these are, and
        what to do with them. Subclasses should return a modified list of lines to be rendered
        in the UI.

        Parameters:
        :   - **obj**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject")) – Linear View Object being rendered
            - **prev**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) – Linear View Object
              located directly above this one
            - **next**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*) – Linear View Object
              located directly below this one
            - **lines** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
              "binaryninja.lineardisassembly.LinearDisassemblyLine")*]*) – Original lines rendered by
              obj

        Returns:
        :   Modified list of lines

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine")]

    *classmethod* register()[[source]](https://api.binary.ninja/_modules/binaryninja/renderlayer.html#RenderLayer.register)
    :   Register a custom Render Layer.

    default_enable_state *= 0*
    :   Whether the Render Layer is enabled by default in the UI. If set to AlwaysEnabled, the
        Render Layer will always be enabled and will not be displayed in the UI.

    name *= None*
    :   Name of the Render Layer, to be displayed in the UI.
