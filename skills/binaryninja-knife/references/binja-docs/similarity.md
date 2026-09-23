# similarity module

Binary similarity providers, session graphs, result resolution, and rendering. (Ultimate
Only)

| Class | Description |
| --- | --- |
| [`binaryninja.similarity.CoreSimilarityProvider`](#binaryninja.similarity.CoreSimilarityProvider "binaryninja.similarity.CoreSimilarityProvider") | A similarity provider implemented by the core or a native plugin. |
| [`binaryninja.similarity.CoreSimilarityProviderType`](#binaryninja.similarity.CoreSimilarityProviderType "binaryninja.similarity.CoreSimilarityProviderType") | A similarity provider type implemented by the core or a native plugin. |
| [`binaryninja.similarity.CoreSimilaritySessionGraphReceiver`](#binaryninja.similarity.CoreSimilaritySessionGraphReceiver "binaryninja.similarity.CoreSimilaritySessionGraphReceiver") | A session graph receiver implemented by the core or a native plugin. |
| [`binaryninja.similarity.CoreSimilaritySessionReceiver`](#binaryninja.similarity.CoreSimilaritySessionReceiver "binaryninja.similarity.CoreSimilaritySessionReceiver") | A session receiver implemented by the core or a native plugin. |
| [`binaryninja.similarity.CoreSimilaritySessionResolver`](#binaryninja.similarity.CoreSimilaritySessionResolver "binaryninja.similarity.CoreSimilaritySessionResolver") | A resolver implemented by the core or a native plugin. |
| [`binaryninja.similarity.CoreSimilaritySessionResolverType`](#binaryninja.similarity.CoreSimilaritySessionResolverType "binaryninja.similarity.CoreSimilaritySessionResolverType") | A resolver type implemented by the core or a native plugin. |
| [`binaryninja.similarity.DiffRenderer`](#binaryninja.similarity.DiffRenderer "binaryninja.similarity.DiffRenderer") | Renders functions with similarity range annotations. |
| [`binaryninja.similarity.SimilarityEntityInfo`](#binaryninja.similarity.SimilarityEntityInfo "binaryninja.similarity.SimilarityEntityInfo") | The type, address, and display name of a session entity. |
| [`binaryninja.similarity.SimilarityEntityRef`](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | Identifies an entity within a session node. |
| [`binaryninja.similarity.SimilarityProvider`](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider") | Visits session nodes and produces similarity results. |
| [`binaryninja.similarity.SimilarityProviderResults`](#binaryninja.similarity.SimilarityProviderResults "binaryninja.similarity.SimilarityProviderResults") | Writes results for one provider visit. |
| [`binaryninja.similarity.SimilarityProviderType`](#binaryninja.similarity.SimilarityProviderType "binaryninja.similarity.SimilarityProviderType") | Creates similarity providers with the given settings. |
| [`binaryninja.similarity.SimilarityRangeAnnotation`](#binaryninja.similarity.SimilarityRangeAnnotation "binaryninja.similarity.SimilarityRangeAnnotation") | An added, removed, or changed address range `[start, end)`. |
| [`binaryninja.similarity.SimilarityRenderContext`](#binaryninja.similarity.SimilarityRenderContext "binaryninja.similarity.SimilarityRenderContext") | Holds views used to display a similarity result. |
| [`binaryninja.similarity.SimilarityResult`](#binaryninja.similarity.SimilarityResult "binaryninja.similarity.SimilarityResult") | A match produced by a provider. |
| [`binaryninja.similarity.SimilaritySession`](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession") | Runs similarity providers and resolvers over a graph of binaries. |
| [`binaryninja.similarity.SimilaritySessionCompletion`](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion") | Tracks stop requests, progress, and timing for a session run. |
| [`binaryninja.similarity.SimilaritySessionCompletionQuery`](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery") | Chooses which session completion data to read or update. |
| [`binaryninja.similarity.SimilaritySessionGraph`](#binaryninja.similarity.SimilaritySessionGraph "binaryninja.similarity.SimilaritySessionGraph") | A graph that controls node processing order and cannot contain cycles. |
| [`binaryninja.similarity.SimilaritySessionGraphReceiver`](#binaryninja.similarity.SimilaritySessionGraphReceiver "binaryninja.similarity.SimilaritySessionGraphReceiver") | Receives notifications after nodes or edges are added to or removed from a session graph. |
| [`binaryninja.similarity.SimilaritySessionNode`](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode") | The main unit of similarity processing. |
| [`binaryninja.similarity.SimilaritySessionReceiver`](#binaryninja.similarity.SimilaritySessionReceiver "binaryninja.similarity.SimilaritySessionReceiver") | Receives session-start and entity-update notifications. |
| [`binaryninja.similarity.SimilaritySessionResolver`](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver") | Selects provider results to apply to session entities. |
| [`binaryninja.similarity.SimilaritySessionResolverType`](#binaryninja.similarity.SimilaritySessionResolverType "binaryninja.similarity.SimilaritySessionResolverType") | Creates resolvers with the given settings. |
| [`binaryninja.similarity.SimilarityView`](#binaryninja.similarity.SimilarityView "binaryninja.similarity.SimilarityView") | A graph or linear view produced for a similarity result. |

## CoreSimilarityProvider

*class* CoreSimilarityProvider[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilarityProvider)
:   Bases: [`SimilarityProvider`](#binaryninja.similarity.SimilarityProvider
    "binaryninja.similarity.SimilarityProvider")

    A similarity provider implemented by the core or a native plugin.

## CoreSimilarityProviderType

*class* CoreSimilarityProviderType[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilarityProviderType)
:   Bases: [`SimilarityProviderType`](#binaryninja.similarity.SimilarityProviderType
    "binaryninja.similarity.SimilarityProviderType")

    A similarity provider type implemented by the core or a native plugin.

    create(*settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilarityProviderType.create)
    :   Create a provider using `settings_obj`, or return `None`. Returns `None` outside
        Ultimate.

        Parameters:
        :   **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
            "binaryninja.settings.Settings"))

        Return type:
        :   [*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
            "binaryninja.similarity.SimilarityProvider") | *None*

    get_default_settings() → [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilarityProviderType.get_default_settings)
    :   Return settings used to configure new providers.

        Return type:
        :   [*Settings*](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")
            | *None*

## CoreSimilaritySessionGraphReceiver

*class* CoreSimilaritySessionGraphReceiver[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilaritySessionGraphReceiver)
:   Bases:
    [`SimilaritySessionGraphReceiver`](#binaryninja.similarity.SimilaritySessionGraphReceiver
    "binaryninja.similarity.SimilaritySessionGraphReceiver")

    A session graph receiver implemented by the core or a native plugin.

## CoreSimilaritySessionReceiver

*class* CoreSimilaritySessionReceiver[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilaritySessionReceiver)
:   Bases: [`SimilaritySessionReceiver`](#binaryninja.similarity.SimilaritySessionReceiver
    "binaryninja.similarity.SimilaritySessionReceiver")

    A session receiver implemented by the core or a native plugin.

## CoreSimilaritySessionResolver

*class* CoreSimilaritySessionResolver[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilaritySessionResolver)
:   Bases: [`SimilaritySessionResolver`](#binaryninja.similarity.SimilaritySessionResolver
    "binaryninja.similarity.SimilaritySessionResolver")

    A resolver implemented by the core or a native plugin.

## CoreSimilaritySessionResolverType

*class* CoreSimilaritySessionResolverType[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilaritySessionResolverType)
:   Bases:
    [`SimilaritySessionResolverType`](#binaryninja.similarity.SimilaritySessionResolverType
    "binaryninja.similarity.SimilaritySessionResolverType")

    A resolver type implemented by the core or a native plugin.

    create(*session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession")*, *settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilaritySessionResolverType.create)
    :   Create a resolver for `session` using `settings_obj`, or return `None`.

        Parameters:
        :   - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession"))
            - **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
              "binaryninja.settings.Settings"))

        Return type:
        :   [*SimilaritySessionResolver*](#binaryninja.similarity.SimilaritySessionResolver
            "binaryninja.similarity.SimilaritySessionResolver") | *None*

    get_default_settings() → [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#CoreSimilaritySessionResolverType.get_default_settings)
    :   Return settings used to configure new resolvers.

        Return type:
        :   [*Settings*](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")
            | *None*

## DiffRenderer

*class* DiffRenderer[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#DiffRenderer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Renders functions with similarity range annotations.

    __init__(*handle: LP_BNDiffRenderer | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#DiffRenderer.__init__)
    :   Parameters:
        :   **handle** (*LP_BNDiffRenderer* *|* *None*)

    add_range_annotation(*annotation: [SimilarityRangeAnnotation](#binaryninja.similarity.SimilarityRangeAnnotation "binaryninja.similarity.SimilarityRangeAnnotation")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#DiffRenderer.add_range_annotation)
    :   Add an annotation to subsequent renders.

        Note

        Empty ranges are ignored.

        Parameters:
        :   **annotation**
            ([*SimilarityRangeAnnotation*](#binaryninja.similarity.SimilarityRangeAnnotation
            "binaryninja.similarity.SimilarityRangeAnnotation"))

        Return type:
        :   *None*

    render(*context: [SimilarityRenderContext](#binaryninja.similarity.SimilarityRenderContext "binaryninja.similarity.SimilarityRenderContext")*, *source: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *entity: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#DiffRenderer.render)
    :   Render graph and linear views for `source`.

        Parameters:
        :   - **context** ([*SimilarityRenderContext*](#binaryninja.similarity.SimilarityRenderContext
              "binaryninja.similarity.SimilarityRenderContext"))
            - **source** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function"))
            - **entity** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef") *|* *None*)

        Return type:
        :   *None*

    render_flow_graph(*context: [SimilarityRenderContext](#binaryninja.similarity.SimilarityRenderContext "binaryninja.similarity.SimilarityRenderContext")*, *group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *entity: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#DiffRenderer.render_flow_graph)
    :   Render an annotated flow graph into `context`.

        Parameters:
        :   - **context** ([*SimilarityRenderContext*](#binaryninja.similarity.SimilarityRenderContext
              "binaryninja.similarity.SimilarityRenderContext"))
            - **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
              "binaryninja.flowgraph.FlowGraph"))
            - **entity** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef") *|* *None*)

        Return type:
        :   *None*

    render_linear_view(*context: [SimilarityRenderContext](#binaryninja.similarity.SimilarityRenderContext "binaryninja.similarity.SimilarityRenderContext")*, *group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *data: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *linear_view: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")*, *entity: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#DiffRenderer.render_linear_view)
    :   Render an annotated linear view into `context`.

        Parameters:
        :   - **context** ([*SimilarityRenderContext*](#binaryninja.similarity.SimilarityRenderContext
              "binaryninja.similarity.SimilarityRenderContext"))
            - **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **data** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView"))
            - **linear_view**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject"))
            - **entity** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef") *|* *None*)

        Return type:
        :   *None*

## SimilarityEntityInfo

*class* SimilarityEntityInfo[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityEntityInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The type, address, and display name of a session entity.

    __init__(*type: [SimilarityEntityType](enums.md#binaryninja.enums.SimilarityEntityType "binaryninja.enums.SimilarityEntityType")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*SimilarityEntityType*](enums.md#binaryninja.enums.SimilarityEntityType
              "binaryninja.enums.SimilarityEntityType"))
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")* *= ''*

    type*: [SimilarityEntityType](enums.md#binaryninja.enums.SimilarityEntityType "binaryninja.enums.SimilarityEntityType")*

## SimilarityEntityRef

*class* SimilarityEntityRef[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityEntityRef)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Identifies an entity within a session node.

    __init__(*node_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *entity_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **node_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **entity_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    entity_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    node_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## SimilarityProvider

*class* SimilarityProvider[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Visits session nodes and produces similarity results.

    Implementations must be thread-safe. Callbacks may overlap across nodes and sessions.
    Visits made by a session keep the visited node and both edge endpoints active. Direct
    calls must provide active views.

    __init__(*provider_type: [SimilarityProviderType](#binaryninja.similarity.SimilarityProviderType "binaryninja.similarity.SimilarityProviderType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: LP_BNSimilarityProvider | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.__init__)
    :   Parameters:
        :   - **provider_type**
              ([*SimilarityProviderType*](#binaryninja.similarity.SimilarityProviderType
              "binaryninja.similarity.SimilarityProviderType") *|* *None*)
            - **handle** (*LP_BNSimilarityProvider* *|* *None*)

    apply(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilarityApplyStatus](enums.md#binaryninja.enums.SimilarityApplyStatus "binaryninja.enums.SimilarityApplyStatus")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.apply)
    :   Call the provider’s apply hook for `result`.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*SimilarityApplyStatus*](enums.md#binaryninja.enums.SimilarityApplyStatus
            "binaryninja.enums.SimilarityApplyStatus")

    get_name(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.get_name)
    :   Return the display name of `result`.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    perform_apply(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilarityApplyStatus](enums.md#binaryninja.enums.SimilarityApplyStatus "binaryninja.enums.SimilarityApplyStatus")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.perform_apply)
    :   Transfer typical metadata from the result target. Overrides can call this before adding
        provider metadata.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*SimilarityApplyStatus*](enums.md#binaryninja.enums.SimilarityApplyStatus
            "binaryninja.enums.SimilarityApplyStatus")

    perform_get_name(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.perform_get_name)
    :   Return a display name for `result`.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    perform_render(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *context: [SimilarityRenderContext](#binaryninja.similarity.SimilarityRenderContext "binaryninja.similarity.SimilarityRenderContext")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.perform_render)
    :   Add views for `result` to `context`.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **context** ([*SimilarityRenderContext*](#binaryninja.similarity.SimilarityRenderContext
              "binaryninja.similarity.SimilarityRenderContext"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    perform_update_settings(*settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.perform_update_settings)
    :   Replace this provider’s settings only if they are valid.

        Return `False` without changing the current settings when the new settings are invalid
        or updates are not supported. Use
        [`SimilaritySession.update_provider_settings`](#binaryninja.similarity.SimilaritySession.update_provider_settings
        "binaryninja.similarity.SimilaritySession.update_provider_settings") so affected
        entities are scheduled again.

        Parameters:
        :   **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
            "binaryninja.settings.Settings"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_visit_node(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *results: [SimilarityProviderResults](#binaryninja.similarity.SimilarityProviderResults "binaryninja.similarity.SimilarityProviderResults")*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.perform_visit_node)
    :   Visit a node and write results for it, returning `False` to discard the visit.

        Process `node.scheduled_entities`. Omitted results are removed for those entities only.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **results**
              ([*SimilarityProviderResults*](#binaryninja.similarity.SimilarityProviderResults
              "binaryninja.similarity.SimilarityProviderResults"))
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") |
            *None*

    perform_visit_node_edge(*from_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *to_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *results: [SimilarityProviderResults](#binaryninja.similarity.SimilarityProviderResults "binaryninja.similarity.SimilarityProviderResults")*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.perform_visit_node_edge)
    :   Visit an edge and write results for it, returning `False` to discard the visit.

        Parameters:
        :   - **from_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **to_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **results**
              ([*SimilarityProviderResults*](#binaryninja.similarity.SimilarityProviderResults
              "binaryninja.similarity.SimilarityProviderResults"))
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") |
            *None*

    render(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *context: [SimilarityRenderContext](#binaryninja.similarity.SimilarityRenderContext "binaryninja.similarity.SimilarityRenderContext")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.render)
    :   Add views for `result` to `context`.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **context** ([*SimilarityRenderContext*](#binaryninja.similarity.SimilarityRenderContext
              "binaryninja.similarity.SimilarityRenderContext"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   *None*

    visit_node(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.visit_node)
    :   Perform a complete visit of `node`. The core manages the result updates.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    visit_node_edge(*from_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *to_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProvider.visit_node_edge)
    :   Perform a complete visit of the edge from `from_node` to `to_node`.

        Parameters:
        :   - **from_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **to_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    *property* id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   This provider’s ID.

    *property* type*: [SimilarityProviderType](#binaryninja.similarity.SimilarityProviderType "binaryninja.similarity.SimilarityProviderType")*
    :   The type that created this provider.

## SimilarityProviderResults

*class* SimilarityProviderResults[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderResults)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Writes results for one provider visit.

    Only use an instance during the provider callback that received it. A successful visit
    replaces earlier results for the same provider and node or edge. Results for unscheduled
    entities remain unchanged.

    __init__(*handle: LP_BNSimilarityProviderResults*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderResults.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilarityProviderResults*)

    add_result(*source: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef")*, *target: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef")*, *similarity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderResults.add_result)
    :   Add a result for a scheduled entity and return its ID, or zero on failure.

        The ID is unique within the node. A later visit replaces the result and gives it a new
        ID.

        Parameters:
        :   - **source** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef"))
            - **target** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef"))
            - **similarity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    *property* handle

## SimilarityProviderType

*class* SimilarityProviderType[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Creates similarity providers with the given settings.

    __init__(*handle: LP_BNSimilarityProviderType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderType.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilarityProviderType* *|* *None*)

    create(*settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderType.create)
    :   Create a provider using `settings_obj`, or return `None`. Custom types must override
        this method.

        Parameters:
        :   **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
            "binaryninja.settings.Settings"))

        Return type:
        :   [*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
            "binaryninja.similarity.SimilarityProvider") | *None*

    get_default_settings() → [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderType.get_default_settings)
    :   Return settings used to configure new providers.

        Return type:
        :   [*Settings*](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")
            | *None*

    register() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityProviderType.register)
    :   Register this provider type for the process lifetime.

        Return type:
        :   *None*

    description *= None*

    name *= None*

## SimilarityRangeAnnotation

*class* SimilarityRangeAnnotation[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityRangeAnnotation)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    An added, removed, or changed address range `[start, end)`.

    __init__(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [SimilarityAnnotationType](enums.md#binaryninja.enums.SimilarityAnnotationType "binaryninja.enums.SimilarityAnnotationType")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **type**
              ([*SimilarityAnnotationType*](enums.md#binaryninja.enums.SimilarityAnnotationType
              "binaryninja.enums.SimilarityAnnotationType"))

        Return type:
        :   *None*

    end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [SimilarityAnnotationType](enums.md#binaryninja.enums.SimilarityAnnotationType "binaryninja.enums.SimilarityAnnotationType")*

## SimilarityRenderContext

*class* SimilarityRenderContext[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityRenderContext)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Holds views used to display a similarity result.

    __init__(*handle: LP_BNSimilarityRenderContext | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityRenderContext.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilarityRenderContext* *|* *None*)

    add_flow_graph(*group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *entity: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityRenderContext.add_flow_graph)
    :   Add a flow graph to `group`.

        Parameters:
        :   - **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
              "binaryninja.flowgraph.FlowGraph"))
            - **entity** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef") *|* *None*)

        Return type:
        :   *None*

    add_linear_view(*group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *data: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *linear_view: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject")*, *entity: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityRenderContext.add_linear_view)
    :   Add a linear view backed by `data` to `group`.

        Parameters:
        :   - **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **data** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView"))
            - **linear_view**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject"))
            - **entity** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef") *|* *None*)

        Return type:
        :   *None*

    *property* preferred_view_type*: [FunctionViewType](function.md#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType")*
    :   Function representation preferred by renderers writing to this context.

    *property* views*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilarityView](#binaryninja.similarity.SimilarityView "binaryninja.similarity.SimilarityView")]*
    :   Views in the order they were added.

## SimilarityResult

*class* SimilarityResult[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityResult)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    A match produced by a provider.

    Similarity and confidence range from 0 to 255, where 255 is strongest. Automatic
    metadata transfer requires `target` to identify an active function.

    __init__(*provider_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *similarity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *target: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **provider_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **similarity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **target** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef"))

        Return type:
        :   *None*

    confidence*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The provider’s confidence in the match.

    provider_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The provider which produced the match.

    similarity*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The similarity of the two entities.

    target*: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef")*
    :   The matched entity, which may be used as the source for metadata transfer.

## SimilaritySession

*class* SimilaritySession[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Runs similarity providers and resolvers over a graph of binaries.

    __init__(*handle: LP_BNSimilaritySession | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilaritySession* *|* *None*)

    add_provider(*provider: [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.add_provider)
    :   Add a provider and schedule entities processed by earlier runs for the next run.

        Note

        Ignored while a run is active.

        Parameters:
        :   **provider** ([*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
            "binaryninja.similarity.SimilarityProvider"))

        Return type:
        :   *None*

    add_receiver(*receiver: [SimilaritySessionReceiver](#binaryninja.similarity.SimilaritySessionReceiver "binaryninja.similarity.SimilaritySessionReceiver")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.add_receiver)
    :   Add a receiver. A running session keeps using the receiver list it started with.

        Parameters:
        :   **receiver**
            ([*SimilaritySessionReceiver*](#binaryninja.similarity.SimilaritySessionReceiver
            "binaryninja.similarity.SimilaritySessionReceiver"))

        Return type:
        :   *None*

    add_resolver(*resolver: [SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.add_resolver)
    :   Add a resolver and mark entities processed by earlier runs for resolution.

        Note

        Returns `False` during a run, for a duplicate, or for a resolver from another session.

        Parameters:
        :   **resolver**
            ([*SimilaritySessionResolver*](#binaryninja.similarity.SimilaritySessionResolver
            "binaryninja.similarity.SimilaritySessionResolver"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_provider(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.get_provider)
    :   Return the provider with `id`.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
            "binaryninja.similarity.SimilarityProvider") | *None*

    get_resolver(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.get_resolver)
    :   Return the resolver with `id`, if present.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*SimilaritySessionResolver*](#binaryninja.similarity.SimilaritySessionResolver
            "binaryninja.similarity.SimilaritySessionResolver") | *None*

    remove_provider(*provider: [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.remove_provider)
    :   Remove a provider, clear its results, and mark affected entities for resolution.

        Note

        Ignored while a run is active.

        Parameters:
        :   **provider** ([*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
            "binaryninja.similarity.SimilarityProvider"))

        Return type:
        :   *None*

    remove_receiver(*receiver: [SimilaritySessionReceiver](#binaryninja.similarity.SimilaritySessionReceiver "binaryninja.similarity.SimilaritySessionReceiver")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.remove_receiver)
    :   Remove a receiver. A running session keeps using the receiver list it started with.

        Parameters:
        :   **receiver**
            ([*SimilaritySessionReceiver*](#binaryninja.similarity.SimilaritySessionReceiver
            "binaryninja.similarity.SimilaritySessionReceiver"))

        Return type:
        :   *None*

    remove_resolver(*resolver: [SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.remove_resolver)
    :   Remove a resolver.

        Note

        Returns `False` during a run, or if it is absent or belongs to another session.

        Parameters:
        :   **resolver**
            ([*SimilaritySessionResolver*](#binaryninja.similarity.SimilaritySessionResolver
            "binaryninja.similarity.SimilaritySessionResolver"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    run() → [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.run)
    :   Start a background run with the current graph, providers, and resolvers.

        Changes to them are ignored until the run finishes.

        Note

        Returns the active run’s completion state when already running.

        Return type:
        :   [*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
            "binaryninja.similarity.SimilaritySessionCompletion")

    update_provider_settings(*provider: [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider")*, *settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.update_provider_settings)
    :   Update a provider already in the session and schedule previously processed entities
        again.

        Returns `False` during a run, when the provider is absent, or when it rejects the
        settings.

        Parameters:
        :   - **provider** ([*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
              "binaryninja.similarity.SimilarityProvider"))
            - **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
              "binaryninja.settings.Settings"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    update_resolver_settings(*resolver: [SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver")*, *settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySession.update_resolver_settings)
    :   Update a resolver already in the session and mark previously processed entities for
        resolution.

        Returns `False` during a run, when the resolver is absent or belongs to another session,
        or when it rejects the settings.

        Parameters:
        :   - **resolver**
              ([*SimilaritySessionResolver*](#binaryninja.similarity.SimilaritySessionResolver
              "binaryninja.similarity.SimilaritySessionResolver"))
            - **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
              "binaryninja.settings.Settings"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* graph*: [SimilaritySessionGraph](#binaryninja.similarity.SimilaritySessionGraph "binaryninja.similarity.SimilaritySessionGraph")*
    :   The session’s dependency graph.

    *property* id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   This session’s ID.

    *property* providers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider")]*
    :   Providers in this session.

    *property* receivers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionReceiver](#binaryninja.similarity.SimilaritySessionReceiver "binaryninja.similarity.SimilaritySessionReceiver")]*
    :   Receivers in this session.

    *property* resolvers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver")]*
    :   Resolvers in this session.

## SimilaritySessionCompletion

*class* SimilaritySessionCompletion[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletion)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Tracks stop requests, progress, and timing for a session run.

    __init__(*handle: LP_BNSimilaritySessionCompletion | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletion.__init__)
    :   Create an independent completion state, or wrap `handle` when provided.

        Independent states are normally only needed when calling providers or resolvers
        directly.

        Parameters:
        :   **handle** (*LP_BNSimilaritySessionCompletion* *|* *None*)

    get_progress(*query: [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletion.get_progress)
    :   Return progress matching `query` from 0.0 to 1.0.

        Parameters:
        :   **query**
            ([*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery"))

        Return type:
        :   [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")

    get_timing(*query: [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")*) → [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletion.get_timing)
    :   Return elapsed time matching `query`.

        Parameters:
        :   **query**
            ([*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery"))

        Return type:
        :   [*timedelta*](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in
            Python v3.14)")

    request_stop() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletion.request_stop)
    :   Ask the active run to stop.

        Return type:
        :   *None*

    set_progress(*query: [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")*, *progress: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletion.set_progress)
    :   Increase provider or resolver progress for a node. Progress cannot decrease.

        Note

        Call this only from the provider or resolver selected by `query`.

        Parameters:
        :   - **query**
              ([*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
              "binaryninja.similarity.SimilaritySessionCompletionQuery"))
            - **progress** ([*float*](https://docs.python.org/3/library/functions.html#float "(in
              Python v3.14)"))

        Return type:
        :   *None*

    *property* is_finished*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the run has finished.

    *property* is_stop_requested*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the run has been asked to stop.

    *property* progress*: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*
    :   Overall progress from 0.0 to 1.0.

## SimilaritySessionCompletionQuery

*class* SimilaritySessionCompletionQuery[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Chooses which session completion data to read or update.

    A query cannot select both a provider and a resolver. Omitting all IDs selects the whole
    session.

    __init__(*node_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *provider_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *resolver_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **node_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)
            - **provider_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*)
            - **resolver_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*)

        Return type:
        :   *None*

    *classmethod* for_node(*node_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery.for_node)
    :   Select a node.

        Parameters:
        :   **node_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery")

    *classmethod* for_provider(*provider_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery.for_provider)
    :   Select a provider across the session.

        Parameters:
        :   **provider_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)"))

        Return type:
        :   [*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery")

    *classmethod* for_resolver(*resolver_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery.for_resolver)
    :   Select a resolver across the session.

        Parameters:
        :   **resolver_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)"))

        Return type:
        :   [*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery")

    *classmethod* for_session() → [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery.for_session)
    :   Select the whole session.

        Return type:
        :   [*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery")

    with_provider(*provider_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery.with_provider)
    :   Select a provider within the current selection.

        Parameters:
        :   **provider_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)"))

        Return type:
        :   [*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery")

    with_resolver(*resolver_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionCompletionQuery](#binaryninja.similarity.SimilaritySessionCompletionQuery "binaryninja.similarity.SimilaritySessionCompletionQuery")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionCompletionQuery.with_resolver)
    :   Select a resolver within the current selection.

        Parameters:
        :   **resolver_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)"))

        Return type:
        :   [*SimilaritySessionCompletionQuery*](#binaryninja.similarity.SimilaritySessionCompletionQuery
            "binaryninja.similarity.SimilaritySessionCompletionQuery")

    node_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    provider_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    resolver_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

## SimilaritySessionGraph

*class* SimilaritySessionGraph[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    A graph that controls node processing order and cannot contain cycles.

    Nodes and edges cannot be changed during a run. Methods with no return value ignore
    changes, while methods that return `bool` return `False`.

    __init__(*handle: LP_BNSimilaritySessionGraph*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilaritySessionGraph*)

    add_edge(*from_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *to_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.add_edge)
    :   Make `to_node` run after `from_node`.

        Parameters:
        :   - **from_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **to_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    add_node(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.add_node)
    :   Add `node`, moving it unless either graph is currently running.

        Parameters:
        :   **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
            "binaryninja.similarity.SimilaritySessionNode"))

        Return type:
        :   *None*

    add_receiver(*receiver: [SimilaritySessionGraphReceiver](#binaryninja.similarity.SimilaritySessionGraphReceiver "binaryninja.similarity.SimilaritySessionGraphReceiver")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.add_receiver)
    :   Add a graph-change receiver.

        Parameters:
        :   **receiver**
            ([*SimilaritySessionGraphReceiver*](#binaryninja.similarity.SimilaritySessionGraphReceiver
            "binaryninja.similarity.SimilaritySessionGraphReceiver"))

        Return type:
        :   *None*

    get_node(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.get_node)
    :   Return the node with `id`.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
            "binaryninja.similarity.SimilaritySessionNode") | *None*

    get_schedule() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")]][[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.get_schedule)
    :   Return groups of nodes in processing order. Nodes in the same group may run in parallel.

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
            "binaryninja.similarity.SimilaritySessionNode")]]

    is_valid_edge(*from_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *to_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.is_valid_edge)
    :   Return whether an edge can be added without duplicating an edge or creating a cycle.

        Parameters:
        :   - **from_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **to_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_edge(*from_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *to_node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.remove_edge)
    :   Remove the edge from `from_node` to `to_node`.

        Parameters:
        :   - **from_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **to_node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_node(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.remove_node)
    :   Remove `node` and its edges from this graph.

        Parameters:
        :   **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
            "binaryninja.similarity.SimilaritySessionNode"))

        Return type:
        :   *None*

    remove_receiver(*receiver: [SimilaritySessionGraphReceiver](#binaryninja.similarity.SimilaritySessionGraphReceiver "binaryninja.similarity.SimilaritySessionGraphReceiver")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraph.remove_receiver)
    :   Remove a graph-change receiver.

        Parameters:
        :   **receiver**
            ([*SimilaritySessionGraphReceiver*](#binaryninja.similarity.SimilaritySessionGraphReceiver
            "binaryninja.similarity.SimilaritySessionGraphReceiver"))

        Return type:
        :   *None*

    *property* nodes*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")]*
    :   Nodes in this graph.

    *property* receivers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionGraphReceiver](#binaryninja.similarity.SimilaritySessionGraphReceiver "binaryninja.similarity.SimilaritySessionGraphReceiver")]*
    :   Graph-change receivers currently registered with this graph.

## SimilaritySessionGraphReceiver

*class* SimilaritySessionGraphReceiver[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraphReceiver)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Receives notifications after nodes or edges are added to or removed from a session
    graph.

    __init__(*handle: LP_BNSimilaritySessionGraphReceiver | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraphReceiver.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilaritySessionGraphReceiver* *|* *None*)

    perform_on_graph_changed() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionGraphReceiver.perform_on_graph_changed)
    :   Handle a node or edge being added to or removed from the graph.

        Return type:
        :   *None*

## SimilaritySessionNode

*class* SimilaritySessionNode[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The main unit of similarity processing.

    __init__(*view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *file: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: LP_BNSimilaritySessionNode | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)
            - **file** ([*FileMetadata*](filemetadata.md#binaryninja.filemetadata.FileMetadata
              "binaryninja.filemetadata.FileMetadata") *|* *None*)
            - **handle** (*LP_BNSimilaritySessionNode* *|* *None*)

    add_scheduled_entity(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.add_scheduled_entity)
    :   Schedule an entity for the next provider round.

        Nodes initially schedule all available entities. The session consumes each scheduled
        batch before resolution; resolvers can call this method to request another round.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    clear_resolved_result(*entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.clear_resolved_result)
    :   Clear the selected result for `entity`.

        Parameters:
        :   **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    create_entity(*info: [SimilarityEntityInfo](#binaryninja.similarity.SimilarityEntityInfo "binaryninja.similarity.SimilarityEntityInfo")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.create_entity)
    :   Add an entity without scheduling it.

        An existing entity with the same type and address is reused. A non-empty name refreshes
        its display name.

        Parameters:
        :   **info** ([*SimilarityEntityInfo*](#binaryninja.similarity.SimilarityEntityInfo
            "binaryninja.similarity.SimilarityEntityInfo"))

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_entity(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilarityEntityInfo](#binaryninja.similarity.SimilarityEntityInfo "binaryninja.similarity.SimilarityEntityInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.get_entity)
    :   Return information about an entity.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*SimilarityEntityInfo*](#binaryninja.similarity.SimilarityEntityInfo
            "binaryninja.similarity.SimilarityEntityInfo") | *None*

    get_entity_function(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.get_entity_function)
    :   Return the function represented by an entity, if available.

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
            | *None*

    get_resolved_result(*entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.get_resolved_result)
    :   Return the selected result for `entity`.

        Parameters:
        :   **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    get_result(*result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SimilarityResult](#binaryninja.similarity.SimilarityResult "binaryninja.similarity.SimilarityResult") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.get_result)
    :   Return a stored result by its ID, which is unique within the node.

        Parameters:
        :   **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*SimilarityResult*](#binaryninja.similarity.SimilarityResult
            "binaryninja.similarity.SimilarityResult") | *None*

    get_results(*entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.get_results)
    :   Return the result IDs for `entity`.

        Parameters:
        :   **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]

    remove_entity(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.remove_entity)
    :   Remove an entity, its schedule, its provider results, and its selected result.

        To only unschedule it, use
        [`remove_scheduled_entity`](#binaryninja.similarity.SimilaritySessionNode.remove_scheduled_entity
        "binaryninja.similarity.SimilaritySessionNode.remove_scheduled_entity").

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_scheduled_entity(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.remove_scheduled_entity)
    :   Unschedule an entity without removing it.

        To remove it, use
        [`remove_entity`](#binaryninja.similarity.SimilaritySessionNode.remove_entity
        "binaryninja.similarity.SimilaritySessionNode.remove_entity").

        Parameters:
        :   **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_resolved_result(*entity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *result: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionNode.set_resolved_result)
    :   Select one of `entity`’s results.

        Parameters:
        :   - **entity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **result** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* entities*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*
    :   All entities, including entities used only as match targets.

    *property* file*: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata")*
    :   The file backing this node.

    *property* id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   This node’s ID.

    *property* incoming_edges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*
    :   IDs of nodes that must run before this node, in ascending order.

    *property* incoming_nodes*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")]*
    :   Nodes that must run before this node, ordered by ID.

    *property* load_options*: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*
    :   Options used when opening this node’s view. Modify them before running the session.

    *property* outgoing_edges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*
    :   IDs of nodes that depend on this node, in ascending order.

    *property* outgoing_nodes*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")]*
    :   Nodes that depend on this node, ordered by ID.

    *property* scheduled_entities*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*
    :   Entities waiting for provider processing.

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The open view, if one is available.

        A file-backed node’s view may be unavailable outside a session run. The session closes
        it when the run no longer needs it.

## SimilaritySessionReceiver

*class* SimilaritySessionReceiver[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionReceiver)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Receives session-start and entity-update notifications.

    `perform_on_start` is called before
    [`SimilaritySession.run`](#binaryninja.similarity.SimilaritySession.run
    "binaryninja.similarity.SimilaritySession.run") returns. Update callbacks run on workers
    and may overlap across nodes and sessions.

    __init__(*handle: LP_BNSimilaritySessionReceiver | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionReceiver.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilaritySessionReceiver* *|* *None*)

    perform_on_start(*completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionReceiver.perform_on_start)
    :   Handle the start of a session run.

        This is mainly used to get the completion state for the run.

        Parameters:
        :   **completion**
            ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
            "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    perform_on_update(*node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *provider: [SimilarityProvider](#binaryninja.similarity.SimilarityProvider "binaryninja.similarity.SimilarityProvider")*, *entities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionReceiver.perform_on_update)
    :   Handle entities whose provider results, resolution state, or applied metadata changed.

        Custom receivers must override this method.

        Parameters:
        :   - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **provider** ([*SimilarityProvider*](#binaryninja.similarity.SimilarityProvider
              "binaryninja.similarity.SimilarityProvider"))
            - **entities** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]*)

        Return type:
        :   *None*

## SimilaritySessionResolver

*class* SimilaritySessionResolver[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Selects provider results to apply to session entities.

    Calls for nodes in the same processing group may run at the same time. Do not keep the
    session after a callback returns.

    __init__(*resolver_type: [SimilaritySessionResolverType](#binaryninja.similarity.SimilaritySessionResolverType "binaryninja.similarity.SimilaritySessionResolverType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: LP_BNSimilaritySessionResolver | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver.__init__)
    :   Parameters:
        :   - **resolver_type**
              ([*SimilaritySessionResolverType*](#binaryninja.similarity.SimilaritySessionResolverType
              "binaryninja.similarity.SimilaritySessionResolverType") *|* *None*)
            - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession") *|* *None*)
            - **handle** (*LP_BNSimilaritySessionResolver* *|* *None*)

    perform_prepare_for_node(*session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession")*, *node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver.perform_prepare_for_node)
    :   Prepare `node` before its providers are visited.

        This is useful for large graphs where views may be unavailable, but the resolver needs
        to change the scheduled entities or add entities itself.

        Parameters:
        :   - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession"))
            - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    perform_resolve_for_node(*session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession")*, *node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver.perform_resolve_for_node)
    :   Select results for `node` after its providers have run.

        Call
        [`SimilaritySessionNode.set_resolved_result`](#binaryninja.similarity.SimilaritySessionNode.set_resolved_result
        "binaryninja.similarity.SimilaritySessionNode.set_resolved_result") to select a result.
        Custom resolvers must override this method. Call
        [`SimilaritySessionNode.add_scheduled_entity`](#binaryninja.similarity.SimilaritySessionNode.add_scheduled_entity
        "binaryninja.similarity.SimilaritySessionNode.add_scheduled_entity") to request another
        round.

        Parameters:
        :   - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession"))
            - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entities** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]*)
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    perform_update_settings(*settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver.perform_update_settings)
    :   Replace this resolver’s settings only if they are valid.

        Return `False` without changing the current settings when the new settings are invalid
        or updates are not supported. Use
        [`SimilaritySession.update_resolver_settings`](#binaryninja.similarity.SimilaritySession.update_resolver_settings
        "binaryninja.similarity.SimilaritySession.update_resolver_settings") so affected
        entities are resolved again.

        Parameters:
        :   **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
            "binaryninja.settings.Settings"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    prepare_for_node(*session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession")*, *node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver.prepare_for_node)
    :   Prepare `node` in `session` before its providers are visited.

        Parameters:
        :   - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession"))
            - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    resolve_for_node(*session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession")*, *node: [SimilaritySessionNode](#binaryninja.similarity.SimilaritySessionNode "binaryninja.similarity.SimilaritySessionNode")*, *entities: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *completion: [SimilaritySessionCompletion](#binaryninja.similarity.SimilaritySessionCompletion "binaryninja.similarity.SimilaritySessionCompletion")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolver.resolve_for_node)
    :   Select results for `node` in `session`.

        Parameters:
        :   - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession"))
            - **node** ([*SimilaritySessionNode*](#binaryninja.similarity.SimilaritySessionNode
              "binaryninja.similarity.SimilaritySessionNode"))
            - **entities** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*]*)
            - **completion**
              ([*SimilaritySessionCompletion*](#binaryninja.similarity.SimilaritySessionCompletion
              "binaryninja.similarity.SimilaritySessionCompletion"))

        Return type:
        :   *None*

    *property* id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   This resolver’s ID.

    *property* type*: [SimilaritySessionResolverType](#binaryninja.similarity.SimilaritySessionResolverType "binaryninja.similarity.SimilaritySessionResolverType")*
    :   The type that created this resolver.

## SimilaritySessionResolverType

*class* SimilaritySessionResolverType[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolverType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Creates resolvers with the given settings.

    __init__(*handle: LP_BNSimilaritySessionResolverType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolverType.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSimilaritySessionResolverType* *|* *None*)

    create(*session: [SimilaritySession](#binaryninja.similarity.SimilaritySession "binaryninja.similarity.SimilaritySession")*, *settings_obj: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")*) → [SimilaritySessionResolver](#binaryninja.similarity.SimilaritySessionResolver "binaryninja.similarity.SimilaritySessionResolver") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolverType.create)
    :   Create a resolver for `session`, or return `None`. Custom types must override this
        method.

        Parameters:
        :   - **session** ([*SimilaritySession*](#binaryninja.similarity.SimilaritySession
              "binaryninja.similarity.SimilaritySession"))
            - **settings_obj** ([*Settings*](settings.md#binaryninja.settings.Settings
              "binaryninja.settings.Settings"))

        Return type:
        :   [*SimilaritySessionResolver*](#binaryninja.similarity.SimilaritySessionResolver
            "binaryninja.similarity.SimilaritySessionResolver") | *None*

    get_default_settings() → [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolverType.get_default_settings)
    :   Return settings used to configure new resolvers.

        Return type:
        :   [*Settings*](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")
            | *None*

    register() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilaritySessionResolverType.register)
    :   Register this resolver type for the process lifetime.

        Return type:
        :   *None*

    description *= None*

    name *= None*

## SimilarityView

*class* SimilarityView[[source]](https://api.binary.ninja/_modules/binaryninja/similarity.html#SimilarityView)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    A graph or linear view produced for a similarity result.

    __init__(*group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *type: [SimilarityViewType](enums.md#binaryninja.enums.SimilarityViewType "binaryninja.enums.SimilarityViewType")*, *graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *data: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *linear_view: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *entity: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **type** ([*SimilarityViewType*](enums.md#binaryninja.enums.SimilarityViewType
              "binaryninja.enums.SimilarityViewType"))
            - **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
              "binaryninja.flowgraph.FlowGraph") *|* *None*)
            - **data** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)
            - **linear_view**
              ([*LinearViewObject*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject
              "binaryninja.lineardisassembly.LinearViewObject") *|* *None*)
            - **entity** ([*SimilarityEntityRef*](#binaryninja.similarity.SimilarityEntityRef
              "binaryninja.similarity.SimilarityEntityRef") *|* *None*)

        Return type:
        :   *None*

    data*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    entity*: [SimilarityEntityRef](#binaryninja.similarity.SimilarityEntityRef "binaryninja.similarity.SimilarityEntityRef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    graph*: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    group*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    linear_view*: [LinearViewObject](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewObject "binaryninja.lineardisassembly.LinearViewObject") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    type*: [SimilarityViewType](enums.md#binaryninja.enums.SimilarityViewType "binaryninja.enums.SimilarityViewType")*
