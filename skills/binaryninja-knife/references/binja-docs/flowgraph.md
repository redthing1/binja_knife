# flowgraph module

| Class | Description |
| --- | --- |
| [`binaryninja.flowgraph.CoreFlowGraph`](#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph") | `class FlowGraph` implements a directed flow graph to be shown in the UI. This class allows… |
| [`binaryninja.flowgraph.EdgeStyle`](#binaryninja.flowgraph.EdgeStyle "binaryninja.flowgraph.EdgeStyle") |  |
| [`binaryninja.flowgraph.FlowGraph`](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph") | `class FlowGraph` implements a directed flow graph to be shown in the UI. This class allows… |
| [`binaryninja.flowgraph.FlowGraphEdge`](#binaryninja.flowgraph.FlowGraphEdge "binaryninja.flowgraph.FlowGraphEdge") |  |
| [`binaryninja.flowgraph.FlowGraphLayout`](#binaryninja.flowgraph.FlowGraphLayout "binaryninja.flowgraph.FlowGraphLayout") |  |
| [`binaryninja.flowgraph.FlowGraphLayoutRequest`](#binaryninja.flowgraph.FlowGraphLayoutRequest "binaryninja.flowgraph.FlowGraphLayoutRequest") |  |
| [`binaryninja.flowgraph.FlowGraphNode`](#binaryninja.flowgraph.FlowGraphNode "binaryninja.flowgraph.FlowGraphNode") |  |

## CoreFlowGraph

*class* CoreFlowGraph[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#CoreFlowGraph)
:   Bases: [`FlowGraph`](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#CoreFlowGraph.__init__)

    update()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#CoreFlowGraph.update)
    :   `update` can be overridden by subclasses to allow a graph to be updated after it has
        been presented in the UI. This will automatically occur if the function referenced by
        the `function` property has been updated.

        Return a new [`FlowGraph`](#binaryninja.flowgraph.FlowGraph
        "binaryninja.flowgraph.FlowGraph") object with the new information if updates are
        desired. If the graph does not need updating, `None` can be returned to leave the graph
        in its current state.

        Returns:
        :   Updated graph, or `None`

        Return type:
        :   [*FlowGraph*](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")

## EdgeStyle

*class* EdgeStyle[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#EdgeStyle)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*style: [EdgePenStyle](enums.md#binaryninja.enums.EdgePenStyle "binaryninja.enums.EdgePenStyle") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *theme_color: [ThemeColor](enums.md#binaryninja.enums.ThemeColor "binaryninja.enums.ThemeColor") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#EdgeStyle.__init__)
    :   Parameters:
        :   - **style** ([*EdgePenStyle*](enums.md#binaryninja.enums.EdgePenStyle
              "binaryninja.enums.EdgePenStyle") *|* *None*) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –
            - **theme_color** ([*ThemeColor*](enums.md#binaryninja.enums.ThemeColor
              "binaryninja.enums.ThemeColor") *|* *None*) –

    *static* from_core_struct(*edge_style*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#EdgeStyle.from_core_struct)

## FlowGraph

*class* FlowGraph[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class FlowGraph` implements a directed flow graph to be shown in the UI. This class
    allows plugins to create custom flow graphs and render them in the UI using the flow
    graph report API.

    An example of creating a flow graph and presenting it in the UI:

    ```
    >>> graph = FlowGraph()
    >>> node_a = FlowGraphNode(graph)
    >>> node_a.lines = ["Node A"]
    >>> node_b = FlowGraphNode(graph)
    >>> node_b.lines = ["Node B"]
    >>> node_c = FlowGraphNode(graph)
    >>> node_c.lines = ["Node C"]
    >>> graph.append(node_a)
    0
    >>> graph.append(node_b)
    1
    >>> graph.append(node_c)
    2
    >>> edge = EdgeStyle(EdgePenStyle.DashDotDotLine, 2, ThemeColor.AddressColor)
    >>> node_a.add_outgoing_edge(BranchType.UserDefinedBranch, node_b, edge)
    >>> node_a.add_outgoing_edge(BranchType.UnconditionalBranch, node_c)
    >>> show_graph_report("Custom Graph", graph)
    ```

    Note

    In the current implementation, only graphs that have a single start node where all other
    nodes are reachable from outgoing edges can be rendered correctly. This describes the
    natural limitations of a control flow graph, which is what the rendering logic was
    designed for. Graphs that have nodes that are only reachable from incoming edges, or
    graphs that have disjoint subgraphs will not render correctly. This will be fixed in a
    future version.

    __init__(*handle: LP_BNCustomFlowGraph | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.__init__)
    :   Parameters:
        :   **handle** (*LP_BNCustomFlowGraph* *|* *None*) –

    add_render_layer(*layer: [RenderLayer](renderlayer.md#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.add_render_layer)
    :   Add a Render Layer to be applied to this Flow Graph. Note that layers will be applied in
        the order in which they are added.

        Parameters:
        :   **layer** ([*RenderLayer*](renderlayer.md#binaryninja.renderlayer.RenderLayer
            "binaryninja.renderlayer.RenderLayer")) – Render Layer to add

    append(*node*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.append)
    :   `append` adds a node to a flow graph.

        Note

        After the graph has completed layout, this function has no effect.

        Parameters:
        :   **node** ([*FlowGraphNode*](#binaryninja.flowgraph.FlowGraphNode
            "binaryninja.flowgraph.FlowGraphNode")) – Node to add

        Returns:
        :   Index of node

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    clear()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.clear)
    :   `clear` clears all the nodes in the graph

        Note

        After the graph has completed layout, this function has no effect.

    complete_layout()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.complete_layout)
    :   `complete_layout` can be overridden by subclasses and is called when a graph layout is
        completed.

    finish_prepare_for_layout()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.finish_prepare_for_layout)
    :   `finish_prepare_for_layout` signals that preparations for rendering a graph are
        complete. This method should only be called by a
        [`prepare_for_layout`](#binaryninja.flowgraph.FlowGraph.prepare_for_layout
        "binaryninja.flowgraph.FlowGraph.prepare_for_layout") reimplementation.

    get_nodes_in_region(*left*, *top*, *right*, *bottom*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.get_nodes_in_region)

    is_option_set(*option*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.is_option_set)

    layout(*callback=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.layout)
    :   `layout` starts rendering a graph for display. Once a layout is complete, each node will
        contain coordinates and extents that can be used to render a graph with minimum
        additional computation. This function does not wait for the graph to be ready to
        display, but a callback can be provided to signal when the graph is ready.

        Parameters:
        :   **callback** (*callback*) – Function to be called when the graph is ready to display

        Returns:
        :   Pending flow graph layout request object

        Return type:
        :   [*FlowGraphLayoutRequest*](#binaryninja.flowgraph.FlowGraphLayoutRequest
            "binaryninja.flowgraph.FlowGraphLayoutRequest")

    layout_and_wait()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.layout_and_wait)
    :   `layout_and_wait` starts rendering a graph for display, and waits for the graph to be
        ready to display. After this function returns, each node will contain coordinates and
        extents that can be used to render a graph with minimum additional computation.

        Do not use this API on the UI thread (use
        [`layout`](#binaryninja.flowgraph.FlowGraph.layout
        "binaryninja.flowgraph.FlowGraph.layout") with a callback instead).

    populate_nodes()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.populate_nodes)
    :   `populate_nodes` can be overridden by subclasses to create nodes in a graph when a flow
        graph needs to be rendered. This will happen on a worker thread and will not block the
        UI.

    prepare_for_layout()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.prepare_for_layout)
    :   `prepare_for_layout` can be overridden by subclasses to handling preparations that must
        take place before a flow graph is rendered, such as waiting for a function to finish
        analysis. If this function is overridden, the
        [`finish_prepare_for_layout`](#binaryninja.flowgraph.FlowGraph.finish_prepare_for_layout
        "binaryninja.flowgraph.FlowGraph.finish_prepare_for_layout") method must be called once
        preparations are completed.

    remove_render_layer(*layer: [RenderLayer](renderlayer.md#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer")*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.remove_render_layer)
    :   Remove a Render Layer from being applied to this Flow Graph

        Parameters:
        :   **layer** ([*RenderLayer*](renderlayer.md#binaryninja.renderlayer.RenderLayer
            "binaryninja.renderlayer.RenderLayer")) – Render Layer to remove

    replace(*index*, *node*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.replace)
    :   `replace` replaces an existing node in the graph with a new node. Any existing edges
        referencing the old node will be updated to point to the new node.

        Note

        After the graph has completed layout, this function has no effect.

        Parameters:
        :   - **index** – Index of the node to replace
            - **node** – New node with which to replace the old node

    set_option(*option*, *value=True*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.set_option)

    show(*title*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.show)
    :   `show` displays the graph in a new tab in the UI.

        Parameters:
        :   **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Title to show in the new tab

    update()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraph.update)
    :   `update` can be overridden by subclasses to allow a graph to be updated after it has
        been presented in the UI. This will automatically occur if the function referenced by
        the [`function`](#binaryninja.flowgraph.FlowGraph.function
        "binaryninja.flowgraph.FlowGraph.function") property has been updated.

        Return a new [`FlowGraph`](#binaryninja.flowgraph.FlowGraph
        "binaryninja.flowgraph.FlowGraph") object with the new information if updates are
        desired. If the graph does not need updating, `None` can be returned to leave the graph
        in its current state.

        Returns:
        :   Updated graph, or `None`

        Return type:
        :   [*FlowGraph*](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")

    *property* allows_inline_instruction_editing
    :   Set if flow graph should allow inline instruction editing (assembly only)

    *property* allows_patching
    :   Set if flow graph should allow modification of code from within the graph view

    *property* complete
    :   Whether flow graph layout is complete (read-only)

    *property* function
    :   Function for a flow graph

    *property* has_nodes
    :   Whether the flow graph has at least one node (read-only)

    *property* height
    :   Flow graph height

    *property* horizontal_block_margin

    *property* il_function

    *property* includes_user_comments
    :   Set if flow graph includes comments made by the user

    *property* is_addressable
    :   Set if flow graph should make use of address information

    *property* is_high_level_il

    *property* is_il

    *property* is_low_level_il

    *property* is_medium_level_il

    *property* is_workflow_graph
    :   Set if flow graph should be treated as a workflow graph

    *property* node_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Number of nodes in graph (read-only)

    *property* nodes
    :   List of nodes in graph (read-only)

    *property* render_layers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[RenderLayer](renderlayer.md#binaryninja.renderlayer.RenderLayer "binaryninja.renderlayer.RenderLayer")]*
    :   Get the list of Render Layers which will be applied to this Flow Graph, after it calls
        populate_nodes. :return: List of Render Layers

    *property* shows_secondary_reg_highlighting
    :   Set if flow graph should highlight associated registers in the UI

    *property* uses_block_highlights
    :   Set if flow graph uses the standard basic block highlighting settings

    *property* uses_instruction_highlights
    :   Set if flow graph uses the standard instruction highlighting settings

    *property* vertical_block_margin

    *property* view
    :   Binary view for a flow graph

    *property* width
    :   Flow graph width

## FlowGraphEdge

*class* FlowGraphEdge[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphEdge)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*branch_type: [BranchType](enums.md#binaryninja.enums.BranchType "binaryninja.enums.BranchType") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source: [FlowGraphNode](#binaryninja.flowgraph.FlowGraphNode "binaryninja.flowgraph.FlowGraphNode")*, *target: [FlowGraphNode](#binaryninja.flowgraph.FlowGraphNode "binaryninja.flowgraph.FlowGraphNode")*, *points: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *back_edge: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *style: [EdgeStyle](#binaryninja.flowgraph.EdgeStyle "binaryninja.flowgraph.EdgeStyle")*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphEdge.__init__)
    :   Parameters:
        :   - **branch_type** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType") *|*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) –
            - **source** ([*FlowGraphNode*](#binaryninja.flowgraph.FlowGraphNode
              "binaryninja.flowgraph.FlowGraphNode")) –
            - **target** ([*FlowGraphNode*](#binaryninja.flowgraph.FlowGraphNode
              "binaryninja.flowgraph.FlowGraphNode")) –
            - **points** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*float*](https://docs.python.org/3/library/functions.html#float
              "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float
              "(in Python v3.14)")*]**]*) –
            - **back_edge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **style** ([*EdgeStyle*](#binaryninja.flowgraph.EdgeStyle
              "binaryninja.flowgraph.EdgeStyle")) –

## FlowGraphLayout

*class* FlowGraphLayout[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayout)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: BNCustomFlowGraphLayout | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayout.__init__)
    :   Parameters:
        :   **handle** (*BNCustomFlowGraphLayout* *|* *None*) –

    layout(*graph: [FlowGraph](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *nodes: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FlowGraphNode](#binaryninja.flowgraph.FlowGraphNode "binaryninja.flowgraph.FlowGraphNode")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayout.layout)
    :   Parameters:
        :   - **graph** ([*FlowGraph*](#binaryninja.flowgraph.FlowGraph
              "binaryninja.flowgraph.FlowGraph")) –
            - **nodes** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*FlowGraphNode*](#binaryninja.flowgraph.FlowGraphNode
              "binaryninja.flowgraph.FlowGraphNode")*]*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    register(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayout.register)
    :   Register a custom layout with the API

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

## FlowGraphLayoutRequest

*class* FlowGraphLayoutRequest[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayoutRequest)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*graph: [FlowGraph](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *callback=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayoutRequest.__init__)
    :   Parameters:
        :   **graph** ([*FlowGraph*](#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph")) –

    abort()[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphLayoutRequest.abort)

    *property* complete
    :   Whether flow graph layout is complete (read-only)

    *property* graph
    :   Flow graph that is being processed (read-only)

## FlowGraphNode

*class* FlowGraphNode[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphNode)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*graph: [FlowGraph](#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphNode.__init__)
    :   Parameters:
        :   **graph** ([*FlowGraph*](#binaryninja.flowgraph.FlowGraph
            "binaryninja.flowgraph.FlowGraph") *|* *None*) –

    add_outgoing_edge(*edge_type*, *target*, *style=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphNode.add_outgoing_edge)
    :   `add_outgoing_edge` connects two flow graph nodes with an edge.

        Parameters:
        :   - **edge_type** ([*BranchType*](enums.md#binaryninja.enums.BranchType
              "binaryninja.enums.BranchType")) – Type of edge to add
            - **target** ([*FlowGraphNode*](#binaryninja.flowgraph.FlowGraphNode
              "binaryninja.flowgraph.FlowGraphNode")) – Target node object
            - **style** ([*EdgeStyle*](#binaryninja.flowgraph.EdgeStyle
              "binaryninja.flowgraph.EdgeStyle")) – (optional) Styling for graph edge Branch Type must
              be set to UserDefinedBranch

    is_valid_for_graph(*graph*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphNode.is_valid_for_graph)

    set_outgoing_edge_points(*edge_num: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *points: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphNode.set_outgoing_edge_points)
    :   Parameters:
        :   - **edge_num** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **points** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
              "(in Python v3.14)")*[*[*float*](https://docs.python.org/3/library/functions.html#float
              "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float
              "(in Python v3.14)")*]**]*) –

    set_visibility_region(*x: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *y: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *w: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *h: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/flowgraph.html#FlowGraphNode.set_visibility_region)
    :   Parameters:
        :   - **x** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **y** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **w** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **h** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *property* basic_block
    :   Basic block associated with this part of the flow graph (well not automatically cause
        the node to render as a native basic block)

    *property* graph

    *property* height
    :   Flow graph block height (read-only)

    *property* highlight
    :   Gets or sets the highlight color for the node

        Example:
        :   ```
            >>> g = FlowGraph()
            >>> node = FlowGraphNode(g)
            >>> node.highlight = HighlightStandardColor.BlueHighlightColor
            >>> node.highlight
            <color: blue>
            ```

    *property* incoming_edges
    :   Flow graph block list of incoming edges (read-only)

    *property* lines
    :   Flow graph block list of text lines

    *property* outgoing_edges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[FlowGraphEdge](#binaryninja.flowgraph.FlowGraphEdge "binaryninja.flowgraph.FlowGraphEdge")]*
    :   Flow graph block list of outgoing edges (read-only)

    *property* width
    :   Flow graph block width (read-only)

    *property* x
    :   Flow graph block X

    *property* y
    :   Flow graph block Y
