# binaryview module

| Class | Description |
| --- | --- |
| [`binaryninja.binaryview.ActiveAnalysisInfo`](#binaryninja.binaryview.ActiveAnalysisInfo "binaryninja.binaryview.ActiveAnalysisInfo") |  |
| [`binaryninja.binaryview.AdvancedILFunctionList`](#binaryninja.binaryview.AdvancedILFunctionList "binaryninja.binaryview.AdvancedILFunctionList") | The purpose of this class is to generate IL functions IL function in the background improving… |
| [`binaryninja.binaryview.AnalysisCompletionEvent`](#binaryninja.binaryview.AnalysisCompletionEvent "binaryninja.binaryview.AnalysisCompletionEvent") | The `AnalysisCompletionEvent` object provides an asynchronous mechanism for receiving… |
| [`binaryninja.binaryview.AnalysisInfo`](#binaryninja.binaryview.AnalysisInfo "binaryninja.binaryview.AnalysisInfo") |  |
| [`binaryninja.binaryview.AnalysisProgress`](#binaryninja.binaryview.AnalysisProgress "binaryninja.binaryview.AnalysisProgress") |  |
| [`binaryninja.binaryview.BinaryDataNotification`](#binaryninja.binaryview.BinaryDataNotification "binaryninja.binaryview.BinaryDataNotification") | `class BinaryDataNotification` provides an interface for receiving event notifications. |
| [`binaryninja.binaryview.BinaryDataNotificationCallbacks`](#binaryninja.binaryview.BinaryDataNotificationCallbacks "binaryninja.binaryview.BinaryDataNotificationCallbacks") |  |
| [`binaryninja.binaryview.BinaryReader`](#binaryninja.binaryview.BinaryReader "binaryninja.binaryview.BinaryReader") | `class BinaryReader` is a convenience class for reading binary data. |
| [`binaryninja.binaryview.BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | `class BinaryView` implements a view on binary data, and presents a queryable interface of a… |
| [`binaryninja.binaryview.BinaryViewEvent`](#binaryninja.binaryview.BinaryViewEvent "binaryninja.binaryview.BinaryViewEvent") | The `BinaryViewEvent` object provides a mechanism for receiving callbacks when a… |
| [`binaryninja.binaryview.BinaryViewType`](#binaryninja.binaryview.BinaryViewType "binaryninja.binaryview.BinaryViewType") | The `BinaryViewType` object is used internally and should not be directly instantiated. |
| [`binaryninja.binaryview.BinaryWriter`](#binaryninja.binaryview.BinaryWriter "binaryninja.binaryview.BinaryWriter") | `class BinaryWriter` is a convenience class for writing binary data. |
| [`binaryninja.binaryview.CoreDataVariable`](#binaryninja.binaryview.CoreDataVariable "binaryninja.binaryview.CoreDataVariable") |  |
| [`binaryninja.binaryview.DataVariable`](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | CoreDataVariable(_address: int, _type: ‘_types.Type’, _auto_discovered: bool) |
| [`binaryninja.binaryview.DataVariableAndName`](#binaryninja.binaryview.DataVariableAndName "binaryninja.binaryview.DataVariableAndName") | CoreDataVariable(_address: int, _type: ‘_types.Type’, _auto_discovered: bool) |
| [`binaryninja.binaryview.DerivedString`](#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | Contains a string derived from code or data. The string does not need to be directly present in… |
| [`binaryninja.binaryview.DerivedStringLocation`](#binaryninja.binaryview.DerivedStringLocation "binaryninja.binaryview.DerivedStringLocation") | Location associated with a derived string. Locations are optional. |
| [`binaryninja.binaryview.FunctionList`](#binaryninja.binaryview.FunctionList "binaryninja.binaryview.FunctionList") |  |
| [`binaryninja.binaryview.MemoryMap`](#binaryninja.binaryview.MemoryMap "binaryninja.binaryview.MemoryMap") | Live proxy to the memory map of a BinaryView. |
| [`binaryninja.binaryview.MemoryRegionInfo`](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo") | Snapshot of a memory region’s properties at the time of query. |
| [`binaryninja.binaryview.ReferenceSource`](#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource") |  |
| [`binaryninja.binaryview.Relocation`](#binaryninja.binaryview.Relocation "binaryninja.binaryview.Relocation") |  |
| [`binaryninja.binaryview.RelocationInfo`](#binaryninja.binaryview.RelocationInfo "binaryninja.binaryview.RelocationInfo") |  |
| [`binaryninja.binaryview.ResolvedRange`](#binaryninja.binaryview.ResolvedRange "binaryninja.binaryview.ResolvedRange") | A computed, non-overlapping interval in the resolved address space. |
| [`binaryninja.binaryview.Section`](#binaryninja.binaryview.Section "binaryninja.binaryview.Section") | The `Section` object is returned during BinaryView creation and should not be directly… |
| [`binaryninja.binaryview.SectionDescriptorList`](#binaryninja.binaryview.SectionDescriptorList "binaryninja.binaryview.SectionDescriptorList") | Built-in mutable sequence. |
| [`binaryninja.binaryview.SectionInfo`](#binaryninja.binaryview.SectionInfo "binaryninja.binaryview.SectionInfo") | SectionInfo is a helper class for describing sections to be added to a BinaryView. |
| [`binaryninja.binaryview.Segment`](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment") | The `Segment` object is returned during BinaryView creation and should not be directly… |
| [`binaryninja.binaryview.SegmentDescriptorList`](#binaryninja.binaryview.SegmentDescriptorList "binaryninja.binaryview.SegmentDescriptorList") | Built-in mutable sequence. |
| [`binaryninja.binaryview.SegmentInfo`](#binaryninja.binaryview.SegmentInfo "binaryninja.binaryview.SegmentInfo") | This class helper class holds Segment information used to describe segments when creating a… |
| [`binaryninja.binaryview.StringRef`](#binaryninja.binaryview.StringRef "binaryninja.binaryview.StringRef") | Deduplicated reference to a string owned by the Binary Ninja core. Use str or bytes to… |
| [`binaryninja.binaryview.StringReference`](#binaryninja.binaryview.StringReference "binaryninja.binaryview.StringReference") |  |
| [`binaryninja.binaryview.StructuredDataValue`](#binaryninja.binaryview.StructuredDataValue "binaryninja.binaryview.StructuredDataValue") |  |
| [`binaryninja.binaryview.SymbolMapping`](#binaryninja.binaryview.SymbolMapping "binaryninja.binaryview.SymbolMapping") | SymbolMapping object is used to improve performance of the bv.symbols API. This allows… |
| [`binaryninja.binaryview.Tag`](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag") | The `Tag` object is created by other APIs (create_*_tag) and should not be directly instantiated. |
| [`binaryninja.binaryview.TagType`](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType") | The `TagType` object is created by the create_tag_type API and should not be directly… |
| [`binaryninja.binaryview.TypeMapping`](#binaryninja.binaryview.TypeMapping "binaryninja.binaryview.TypeMapping") | TypeMapping object is used to improve performance of the bv.types API. This allows pythonic… |
| [`binaryninja.binaryview.TypedDataAccessor`](#binaryninja.binaryview.TypedDataAccessor "binaryninja.binaryview.TypedDataAccessor") |  |
| [`binaryninja.binaryview.TypedDataReader`](#binaryninja.binaryview.TypedDataReader "binaryninja.binaryview.TypedDataReader") | TypedDataAccessor(type: ‘_types.Type’, address: int, view: ‘BinaryView’, endian: binaryninja.enum… |

## ActiveAnalysisInfo

*class* ActiveAnalysisInfo[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#ActiveAnalysisInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ActiveAnalysisInfo(func: ‘_function.Function’, analysis_time: int, update_count: int,
    submit_count: int)

    __init__(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *analysis_time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *update_count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *submit_count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –
            - **analysis_time** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **update_count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **submit_count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –

        Return type:
        :   *None*

    analysis_time*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    func*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*

    submit_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    update_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## AdvancedILFunctionList

*class* AdvancedILFunctionList[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AdvancedILFunctionList)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The purpose of this class is to generate IL functions IL function in the background
    improving the performance of iterating MediumLevelIL and HighLevelILFunctions.

    Using this class or the associated helper methods BinaryView.mlil_functions /
    BinaryView.hlil_functions can improve the performance of ILFunction iteration
    significantly

    The prefetch_limit property is configurable and should be modified based upon your
    machines hardware and RAM limitations.

    Warning

    Setting the prefetch_limit excessively high can result in high memory utilization.

    Example:
    :   ```
        >>> import timeit
        >>> len(bv.functions)
        4817
        >>> # Calculate the average time to generate hlil for all functions withing 'bv':
        >>> timeit.timeit(lambda:[f.hlil for f in bv.functions], number=1)
        21.761621682000168
        >>> t1 = _
        >>> # Now try again with the advanced analysis iterator
        >>> timeit.timeit(lambda:[f for f in bv.hlil_functions(128)], number=1)
        6.3147709989998475
        >>> t1/_
        3.4461458199270947
        >>> # This particular binary can iterate hlil functions 3.4x faster
        >>> # If you don't need IL then its still much faster to just use `bv.functions`
        >>> timeit.timeit(lambda:[f for f in bv.functions], number=1)
        0.02230275600004461
        ```

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *preload_limit: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 11*, *functions: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AdvancedILFunctionList.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **preload_limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **functions**
              ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python
              v3.14)") *|* *None*) –

## AnalysisCompletionEvent

*class* AnalysisCompletionEvent[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AnalysisCompletionEvent)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `AnalysisCompletionEvent` object provides an asynchronous mechanism for receiving
    callbacks when analysis is complete. The callback runs once. A completion event must be
    added for each new analysis in order to be notified of each analysis completion. The
    AnalysisCompletionEvent class takes responsibility for keeping track of the object’s
    lifetime.

    Example:
    :   ```
        >>> def on_complete(self):
        ...     print("Analysis Complete", self._view)
        ...
        >>> evt = AnalysisCompletionEvent(bv, on_complete)
        >>>
        ```

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[AnalysisCompletionEvent](#binaryninja.binaryview.AnalysisCompletionEvent "binaryninja.binaryview.AnalysisCompletionEvent")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AnalysisCompletionEvent.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **callback** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
              "(in Python
              v3.14)")*[**[*[*AnalysisCompletionEvent*](#binaryninja.binaryview.AnalysisCompletionEvent
              "binaryninja.binaryview.AnalysisCompletionEvent")*]**,* *None**]* *|*
              [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[**]**,* *None**]*) –

    cancel() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AnalysisCompletionEvent.cancel)
    :   The `cancel` method will cancel analysis for an
        [`AnalysisCompletionEvent`](#binaryninja.binaryview.AnalysisCompletionEvent
        "binaryninja.binaryview.AnalysisCompletionEvent").

        Warning

        This method should only be used when the system is being shut down and no further
        analysis should be done afterward.

        Return type:
        :   *None*

    *property* view*: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*

## AnalysisInfo

*class* AnalysisInfo[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AnalysisInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    AnalysisInfo(state: binaryninja.enums.AnalysisState, analysis_time: int, active_info:
    List[binaryninja.binaryview.ActiveAnalysisInfo])

    __init__(*state: [AnalysisState](enums.md#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState")*, *analysis_time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *active_info: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ActiveAnalysisInfo](#binaryninja.binaryview.ActiveAnalysisInfo "binaryninja.binaryview.ActiveAnalysisInfo")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **state** ([*AnalysisState*](enums.md#binaryninja.enums.AnalysisState
              "binaryninja.enums.AnalysisState")) –
            - **analysis_time** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **active_info** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*ActiveAnalysisInfo*](#binaryninja.binaryview.ActiveAnalysisInfo
              "binaryninja.binaryview.ActiveAnalysisInfo")*]*) –

        Return type:
        :   *None*

    active_info*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ActiveAnalysisInfo](#binaryninja.binaryview.ActiveAnalysisInfo "binaryninja.binaryview.ActiveAnalysisInfo")]*

    analysis_time*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    state*: [AnalysisState](enums.md#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState")*

## AnalysisProgress

*class* AnalysisProgress[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#AnalysisProgress)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    AnalysisProgress(state: binaryninja.enums.AnalysisState, count: int, total: int)

    __init__(*state: [AnalysisState](enums.md#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState")*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *total: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **state** ([*AnalysisState*](enums.md#binaryninja.enums.AnalysisState
              "binaryninja.enums.AnalysisState")) –
            - **count** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **total** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    state*: [AnalysisState](enums.md#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState")*

    total*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## BinaryDataNotification

*class* BinaryDataNotification[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BinaryDataNotification` provides an interface for receiving event notifications.
    Usage requires inheriting from this interface, overriding the relevant event handlers,
    and registering the BinaryDataNotification instance with a BinaryView using the
    register_notification method.

    By default, a BinaryDataNotification instance receives notifications for all available
    notification types. It is recommended for users of this interface to initialize the
    BinaryDataNotification base class with specific callbacks of interest by passing the
    appropriate NotificationType flags into the __init__ constructor.

    Handlers provided by the user should aim to limit the amount of processing within the
    callback. The callback context holds a global lock, preventing other threads from making
    progress during the callback phase. While most of the API can be used safely during this
    time, care must be taken when issuing a call that can block, as waiting for a thread
    requiring the global lock can result in deadlock.

    The NotificationBarrier is a special NotificationType that is disabled by default. To
    enable it, the NotificationBarrier flag must be passed to __init__. This notification is
    designed to facilitate efficient batch processing of other notification types. The idea
    is to collect other notifications of interest into a cache, which can be very efficient
    as it doesn’t require additional locks. After some time, the core generates a
    NotificationBarrier event, providing a safe context to move the cache for processing by
    a different thread.

    To control the time of the next NotificationBarrier event, return the desired number of
    milliseconds until the next event from the NotificationBarrier callback. Returning zero
    quiesces future NotificationBarrier events. If the NotificationBarrier is quiesced, the
    reception of a new callback of interest automatically generates a new
    NotificationBarrier call after that notification is delivered. This mechanism
    effectively allows throttling and quiescing when necessary.

    Note

    Note that the core generates a NotificationBarrier as part of the BinaryDataNotification
    registration process. Registering the same BinaryDataNotification instance again results
    in a gratuitous NotificationBarrier event, which can be useful in situations requiring a
    safe context for processing due to some other asynchronous event (e.g., user
    interaction).

    Example:

    ```
    >>> class NotifyTest(binaryninja.BinaryDataNotification):
    ...     def __init__(self):
    ...             super(NotifyTest, self).__init__(binaryninja.NotificationType.NotificationBarrier | binaryninja.NotificationType.FunctionLifetime | binaryninja.NotificationType.FunctionUpdated)
    ...             self.received_event = False
    ...     def notification_barrier(self, view: 'BinaryView') -> int:
    ...             has_events = self.received_event
    ...             self.received_event = False
    ...             log_info("notification_barrier")
    ...             if has_events:
    ...                     return 250
    ...             else:
    ...                     return 0
    ...     def function_added(self, view: 'BinaryView', func: '_function.Function') -> None:
    ...             self.received_event = True
    ...             log_info("function_added")
    ...     def function_removed(self, view: 'BinaryView', func: '_function.Function') -> None:
    ...             self.received_event = True
    ...             log_info("function_removed")
    ...     def function_updated(self, view: 'BinaryView', func: '_function.Function') -> None:
    ...             self.received_event = True
    ...             log_info("function_updated")
    ...
    >>>
    >>> bv.register_notification(NotifyTest())
    >>>
    ```

    __init__(*notifications: NotificationType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.__init__)
    :   Parameters:
        :   **notifications** (*NotificationType* *|* *None*) –

    component_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –

        Return type:
        :   *None*

    component_data_var_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *var: [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_data_var_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **var** ([*DataVariable*](#binaryninja.binaryview.DataVariable
              "binaryninja.binaryview.DataVariable")) –

    component_data_var_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *var: [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_data_var_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **var** ([*DataVariable*](#binaryninja.binaryview.DataVariable
              "binaryninja.binaryview.DataVariable")) –

    component_function_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_function_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

    component_function_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_function_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

    component_moved(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *formerParent: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *newParent: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_moved)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **formerParent** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **newParent** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –

        Return type:
        :   *None*

    component_name_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *previous_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_name_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **previous_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –

        Return type:
        :   *None*

    component_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *formerParent: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*, *_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.component_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **formerParent** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –
            - **_component** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component")) –

        Return type:
        :   *None*

    data_inserted(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_inserted)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    data_metadata_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_metadata_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    data_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    data_var_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *var: [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_var_added)
    :   Note

        data_var_updated will be triggered instead when a user data variable is added over an
        auto data variable.

        Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **var** ([*DataVariable*](#binaryninja.binaryview.DataVariable
              "binaryninja.binaryview.DataVariable")) –

        Return type:
        :   *None*

    data_var_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *var: [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_var_removed)
    :   Note

        data_var_updated will be triggered instead when a user data variable is removed over an
        auto data variable.

        Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **var** ([*DataVariable*](#binaryninja.binaryview.DataVariable
              "binaryninja.binaryview.DataVariable")) –

        Return type:
        :   *None*

    data_var_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *var: [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_var_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **var** ([*DataVariable*](#binaryninja.binaryview.DataVariable
              "binaryninja.binaryview.DataVariable")) –

        Return type:
        :   *None*

    data_written(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.data_written)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    derived_string_found(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *string: [DerivedString](#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.derived_string_found)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **string** ([*DerivedString*](#binaryninja.binaryview.DerivedString
              "binaryninja.binaryview.DerivedString")) –

        Return type:
        :   *None*

    derived_string_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *string: [DerivedString](#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.derived_string_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **string** ([*DerivedString*](#binaryninja.binaryview.DerivedString
              "binaryninja.binaryview.DerivedString")) –

        Return type:
        :   *None*

    function_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.function_added)
    :   Note

        function_updated will be triggered instead when a user function is added over an auto
        function.

        Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   *None*

    function_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.function_removed)
    :   Note

        function_updated will be triggered instead when a user function is removed over an auto
        function.

        Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   *None*

    function_update_requested(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.function_update_requested)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   *None*

    function_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.function_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) –

        Return type:
        :   *None*

    notification_barrier(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.notification_barrier)
    :   Parameters:
        :   **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    rebased(*old_view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *new_view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.rebased)
    :   Parameters:
        :   - **old_view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **new_view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –

    redo_entry_taken(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *entry: [UndoEntry](undo.md#binaryninja.undo.UndoEntry "binaryninja.undo.UndoEntry")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.redo_entry_taken)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **entry** ([*UndoEntry*](undo.md#binaryninja.undo.UndoEntry
              "binaryninja.undo.UndoEntry")) –

    section_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *section: [Section](#binaryninja.binaryview.Section "binaryninja.binaryview.Section")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.section_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **section** ([*Section*](#binaryninja.binaryview.Section
              "binaryninja.binaryview.Section")) –

        Return type:
        :   *None*

    section_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *section: [Section](#binaryninja.binaryview.Section "binaryninja.binaryview.Section")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.section_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **section** ([*Section*](#binaryninja.binaryview.Section
              "binaryninja.binaryview.Section")) –

        Return type:
        :   *None*

    section_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *section: [Section](#binaryninja.binaryview.Section "binaryninja.binaryview.Section")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.section_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **section** ([*Section*](#binaryninja.binaryview.Section
              "binaryninja.binaryview.Section")) –

        Return type:
        :   *None*

    segment_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *segment: [Segment](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.segment_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **segment** ([*Segment*](#binaryninja.binaryview.Segment
              "binaryninja.binaryview.Segment")) –

        Return type:
        :   *None*

    segment_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *segment: [Segment](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.segment_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **segment** ([*Segment*](#binaryninja.binaryview.Segment
              "binaryninja.binaryview.Segment")) –

        Return type:
        :   *None*

    segment_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *segment: [Segment](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.segment_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **segment** ([*Segment*](#binaryninja.binaryview.Segment
              "binaryninja.binaryview.Segment")) –

        Return type:
        :   *None*

    string_found(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *string_type: [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.string_found)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **string_type** ([*StringType*](enums.md#binaryninja.enums.StringType
              "binaryninja.enums.StringType")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    string_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *string_type: [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.string_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **string_type** ([*StringType*](enums.md#binaryninja.enums.StringType
              "binaryninja.enums.StringType")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    symbol_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.symbol_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")) –

        Return type:
        :   *None*

    symbol_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.symbol_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")) –

        Return type:
        :   *None*

    symbol_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.symbol_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")) –

        Return type:
        :   *None*

    tag_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *tag: [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*, *ref_type: [TagReferenceType](enums.md#binaryninja.enums.TagReferenceType "binaryninja.enums.TagReferenceType")*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.tag_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **tag** ([*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) –
            - **ref_type** ([*TagReferenceType*](enums.md#binaryninja.enums.TagReferenceType
              "binaryninja.enums.TagReferenceType")) –
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    tag_removed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *tag: [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*, *ref_type: [TagReferenceType](enums.md#binaryninja.enums.TagReferenceType "binaryninja.enums.TagReferenceType")*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.tag_removed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **tag** ([*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) –
            - **ref_type** ([*TagReferenceType*](enums.md#binaryninja.enums.TagReferenceType
              "binaryninja.enums.TagReferenceType")) –
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    tag_type_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *tag_type*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.tag_type_updated)
    :   Parameters:
        :   **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   *None*

    tag_updated(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *tag: [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*, *ref_type: [TagReferenceType](enums.md#binaryninja.enums.TagReferenceType "binaryninja.enums.TagReferenceType")*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.tag_updated)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **tag** ([*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) –
            - **ref_type** ([*TagReferenceType*](enums.md#binaryninja.enums.TagReferenceType
              "binaryninja.enums.TagReferenceType")) –
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    type_archive_attached(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_archive_attached)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

    type_archive_connected(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_archive_connected)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) –

    type_archive_detached(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_archive_detached)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

    type_archive_disconnected(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_archive_disconnected)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) –

    type_defined(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_defined)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   *None*

    type_field_ref_changed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_field_ref_changed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    type_ref_changed(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_ref_changed)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   *None*

    type_undefined(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.type_undefined)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   *None*

    undo_entry_added(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *entry: [UndoEntry](undo.md#binaryninja.undo.UndoEntry "binaryninja.undo.UndoEntry")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.undo_entry_added)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **entry** ([*UndoEntry*](undo.md#binaryninja.undo.UndoEntry
              "binaryninja.undo.UndoEntry")) –

    undo_entry_taken(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *entry: [UndoEntry](undo.md#binaryninja.undo.UndoEntry "binaryninja.undo.UndoEntry")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotification.undo_entry_taken)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **entry** ([*UndoEntry*](undo.md#binaryninja.undo.UndoEntry
              "binaryninja.undo.UndoEntry")) –

## BinaryDataNotificationCallbacks

*class* BinaryDataNotificationCallbacks[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotificationCallbacks)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *notify: [BinaryDataNotification](#binaryninja.binaryview.BinaryDataNotification "binaryninja.binaryview.BinaryDataNotification")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryDataNotificationCallbacks.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **notify** ([*BinaryDataNotification*](#binaryninja.binaryview.BinaryDataNotification
              "binaryninja.binaryview.BinaryDataNotification")) –

    *property* notify*: [BinaryDataNotification](#binaryninja.binaryview.BinaryDataNotification "binaryninja.binaryview.BinaryDataNotification")*

    *property* view*: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*

## BinaryReader

*class* BinaryReader[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BinaryReader` is a convenience class for reading binary data.

    BinaryReader can be instantiated as follows and the rest of the document will start from
    this context

    ```
    >>> from binaryninja import *
    >>> bv = load("/bin/ls")
    >>> br = BinaryReader(bv)
    >>> hex(br.read32())
    '0xfeedfacfL'
    >>>
    ```

    Or using the optional endian parameter

    ```
    >>> from binaryninja import *
    >>> br = BinaryReader(bv, Endianness.BigEndian)
    >>> hex(br.read32())
    '0xcffaedfeL'
    >>>
    ```

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness") *|* *None*) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

    read(*length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read)
    :   `read` returns `length` bytes read from the current offset, adding `length` to offset.

        Parameters:
        :   - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to read.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   `length` bytes from current offset

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.read(8)
            '\xcf\xfa\xed\xfe\x07\x00\x00\x01'
            >>>
            ```

    read16(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read16)
    :   `read16` returns a two byte integer from offset incrementing the offset by two, using
        specified endianness.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a two byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read16())
            '0xfacf'
            >>>
            ```

    read16be(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read16be)
    :   `read16be` returns a two byte big endian integer from offset incrementing the offset by
        two.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a two byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read16be())
            '0xcffa'
            >>>
            ```

    read16le(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read16le)
    :   `read16le` returns a two byte little endian integer from offset incrementing the offset
        by two.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a two byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read16le())
            '0xfacf'
            >>>
            ```

    read32(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read32)
    :   `read32` returns a four byte integer from offset incrementing the offset by four, using
        specified endianness.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a four byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read32())
            '0xfeedfacfL'
            >>>
            ```

    read32be(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read32be)
    :   `read32be` returns a four byte big endian integer from offset incrementing the offset by
        four.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a four byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read32be())
            '0xcffaedfe'
            ```

    read32le(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read32le)
    :   `read32le` returns a four byte little endian integer from offset incrementing the offset
        by four.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a four byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read32le())
            '0xfeedfacf'
            >>>
            ```

    read64(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read64)
    :   `read64` returns an eight byte integer from offset incrementing the offset by eight,
        using specified endianness.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   an eight byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read64())
            '0x1000007feedfacfL'
            >>>
            ```

    read64be(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read64be)
    :   `read64be` returns an eight byte big endian integer from offset incrementing the offset
        by eight.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a eight byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read64be())
            '0xcffaedfe07000001L'
            ```

    read64le(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read64le)
    :   `read64le` returns an eight byte little endian integer from offset incrementing the
        offset by eight.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   a eight byte integer at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> hex(br.read64le())
            '0x1000007feedfacf'
            >>>
            ```

    read8(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.read8)
    :   `read8` returns a one byte integer from offset incrementing the offset.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset before reading

        Returns:
        :   byte at offset.

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), or
            None on failure

        Example:
        :   ```
            >>> br.seek(0x100000000)
            >>> br.read8()
            207
            >>>
            ```

    seek(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *whence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.seek)
    :   `seek` update internal offset to `offset`.

        Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset to
            - **whence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional, defaults to 0 for absolute file positioning, or 1 for relative to
              current location

        Return type:
        :   *None*

        Example:
        :   ```
            >>> hex(br.offset)
            '0x100000008L'
            >>> br.seek(0x100000000)
            >>> hex(br.offset)
            '0x100000000L'
            >>>
            ```

    seek_relative(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryReader.seek_relative)
    :   `seek_relative` updates the internal offset by `offset`.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to add to the internal offset

        Return type:
        :   *None*

        Example:
        :   ```
            >>> hex(br.offset)
            '0x100000008L'
            >>> br.seek_relative(-8)
            >>> hex(br.offset)
            '0x100000000L'
            >>>
            ```

    *property* endianness*: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*
    :   The Endianness to read data. (read/write)

        Getter:
        :   returns the endianness of the reader

        Setter:
        :   sets the endianness of the reader (BigEndian or LittleEndian)

        Type:
        :   [*Endianness*](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")

    *property* eof*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Is end of file (read-only)

        Getter:
        :   returns boolean, true if end of file, false otherwise

        Type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The current read offset (read/write).

        Getter:
        :   returns the current internal offset

        Setter:
        :   sets the internal offset

        Type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    *property* virtual_base*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The current virtual base offset for the stream (read/write).

        Getter:
        :   returns the current virtual base

        Setter:
        :   sets the virtual base

        Type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## BinaryView

*class* BinaryView[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BinaryView` implements a view on binary data, and presents a queryable interface
    of a binary file. One key job of BinaryView is file format parsing which allows Binary
    Ninja to read, write, insert, remove portions of the file given a virtual address. For
    the purposes of this documentation we define a virtual address as the memory address
    that the various pieces of the physical file will be loaded at.

    A binary file does not have to have just one BinaryView, thus much of the interface to
    manipulate disassembly exists within or is accessed through a BinaryView. All files are
    guaranteed to have at least the `Raw` BinaryView. The `Raw` BinaryView is simply a hex
    editor, but is helpful for manipulating binary files via their absolute addresses.

    BinaryViews are plugins and thus registered with Binary Ninja at startup, and thus
    should **never** be instantiated directly as this is already done. The list of available
    BinaryViews can be seen in the BinaryViewType class which provides an iterator and map
    of the various installed BinaryViews:

    ```
    >>> list(BinaryViewType)
    [<view type: 'Raw'>, <view type: 'ELF'>, <view type: 'Mach-O'>, <view type: 'PE'>]
    >>> BinaryViewType['ELF']
    <view type: 'ELF'>
    ```

    To open a file with a given BinaryView the following code is recommended:

    ```
    >>> with load("/bin/ls") as bv:
    ...   bv
    <BinaryView: '/bin/ls', start 0x100000000, len 0x142c8>
    ```

    By convention in the rest of this document we will use bv to mean an open and, analyzed,
    BinaryView of an executable file. When a BinaryView is open on an executable view
    analysis is automatically run unless specific named parameters are used to disable
    updates. If such a parameter is used, updates can be triggered using the
    [`update_analysis_and_wait`](#binaryninja.binaryview.BinaryView.update_analysis_and_wait
    "binaryninja.binaryview.BinaryView.update_analysis_and_wait") method which disassembles
    the executable and returns when all disassembly and analysis is complete:

    ```
    >>> bv.update_analysis_and_wait()
    >>>
    ```

    Since BinaryNinja’s analysis is multi-threaded (depending on version) this can also be
    done in the background by using the
    [`update_analysis`](#binaryninja.binaryview.BinaryView.update_analysis
    "binaryninja.binaryview.BinaryView.update_analysis") method instead.

    By standard python convention methods which start with ‘_’ should be considered private
    and should not be called externally. Additionally, methods which begin with `perform_`
    should not be called directly either and are used explicitly for subclassing a
    BinaryView.

    Note

    An important note on the `*_user_*()` methods. Binary Ninja makes a distinction between
    edits performed by the user and actions performed by auto analysis. Auto analysis
    actions that can quickly be recalculated are not saved to the database. Auto analysis
    actions that take a long time and all user edits are stored in the database (e.g.
    [`remove_user_function`](#binaryninja.binaryview.BinaryView.remove_user_function
    "binaryninja.binaryview.BinaryView.remove_user_function") rather than
    [`remove_function`](#binaryninja.binaryview.BinaryView.remove_function
    "binaryninja.binaryview.BinaryView.remove_function")). Thus use `_user_` methods if
    saving to the database is desired.

    *class* QueueGenerator[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.QueueGenerator)
    :   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
        v3.14)")

        __init__(*t: [Thread](https://docs.python.org/3/library/threading.html#threading.Thread "(in Python v3.14)")*, *results: [Queue](https://docs.python.org/3/library/queue.html#queue.Queue "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.QueueGenerator.__init__)
        :   Parameters:
            :   - **t** ([*Thread*](https://docs.python.org/3/library/threading.html#threading.Thread "(in
                  Python v3.14)")) –
                - **results** ([*Queue*](https://docs.python.org/3/library/queue.html#queue.Queue "(in
                  Python v3.14)")) –

    __init__(*file_metadata: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parent_view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: LP_BNBinaryView | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.__init__)
    :   Parameters:
        :   - **file_metadata**
              ([*FileMetadata*](filemetadata.md#binaryninja.filemetadata.FileMetadata
              "binaryninja.filemetadata.FileMetadata") *|* *None*) –
            - **parent_view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –
            - **handle** (*LP_BNBinaryView* *|* *None*) –

    *static* __new__(*cls*, *file_metadata=None*, *parent_view=None*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.__new__)

    abort_analysis() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.abort_analysis)
    :   `abort_analysis` aborts analysis and suspends the workflow machine. This operation is
        recoverable, and the workflow machine can be re-enabled via the `enable` API on
        WorkflowMachine.

        Return type:
        :   *None*

    add_analysis_completion_event(*callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [AnalysisCompletionEvent](#binaryninja.binaryview.AnalysisCompletionEvent "binaryninja.binaryview.AnalysisCompletionEvent")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_analysis_completion_event)
    :   `add_analysis_completion_event` sets up a call back function to be called when analysis
        has been completed. This is helpful when using
        [`update_analysis`](#binaryninja.binaryview.BinaryView.update_analysis
        "binaryninja.binaryview.BinaryView.update_analysis") which does not wait for analysis
        completion before returning.

        The callee of this function is not responsible for maintaining the lifetime of the
        returned AnalysisCompletionEvent object.

        Note

        The lock held by the callback thread on the BinaryView instance ensures that other
        BinaryView actions can be safely performed in the callback thread.

        Warning

        The built-in python console automatically updates analysis after every command is run,
        which means this call back may not behave as expected if entered interactively.

        Parameters:
        :   **callback** (*callback*) – A function to be called with no parameters when analysis has
            completed.

        Returns:
        :   An initialized AnalysisCompletionEvent object

        Return type:
        :   [*AnalysisCompletionEvent*](#binaryninja.binaryview.AnalysisCompletionEvent
            "binaryninja.binaryview.AnalysisCompletionEvent")

        Example:
        :   ```
            >>> def completionEvent():
            ...   print("done")
            ...
            >>> bv.add_analysis_completion_event(completionEvent)
            <binaryninja.AnalysisCompletionEvent object at 0x10a2c9f10>
            >>> bv.update_analysis()
            done
            >>>
            ```

    add_analysis_option(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_analysis_option)
    :   `add_analysis_option` adds an analysis option. Analysis options elaborate the analysis
        phase. The user must start analysis by calling either
        [`update_analysis`](#binaryninja.binaryview.BinaryView.update_analysis
        "binaryninja.binaryview.BinaryView.update_analysis") or
        [`update_analysis_and_wait`](#binaryninja.binaryview.BinaryView.update_analysis_and_wait
        "binaryninja.binaryview.BinaryView.update_analysis_and_wait").

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – name of the analysis option. Available options are: “linearsweep”, and
            “signaturematcher”.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.add_analysis_option("linearsweep")
            >>> bv.update_analysis_and_wait()
            ```

    add_auto_section(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *semantics: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics") = SectionSemantics.DefaultSectionSemantics*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *entry_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *linked_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_data: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_auto_section)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **semantics** ([*SectionSemantics*](enums.md#binaryninja.enums.SectionSemantics
              "binaryninja.enums.SectionSemantics")) –
            - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **entry_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **linked_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **info_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **info_data** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    add_auto_sections(*sections: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SectionInfo](#binaryninja.binaryview.SectionInfo "binaryninja.binaryview.SectionInfo")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[BNSectionInfo]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_auto_sections)
    :   `add_auto_sections` Adds analysis sections that specify semantic information about
        regions of the binary

        Parameters:
        :   - **sections** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*SectionInfo*](#binaryninja.binaryview.SectionInfo
              "binaryninja.binaryview.SectionInfo")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**BNSectionInfo**]*) – list of sections to add
            - **sections** –

        Return type:
        :   *None*

    add_auto_segment(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_auto_segment)
    :   `add_auto_segment` Adds an analysis segment that specifies how data from the raw file is
        mapped into a virtual address space

        Note that the segments added may have different size attributes than requested

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **data_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **data_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) –

        Return type:
        :   *None*

    add_auto_segments(*segments: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SegmentInfo](#binaryninja.binaryview.SegmentInfo "binaryninja.binaryview.SegmentInfo")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[BNSegmentInfo]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_auto_segments)
    :   `add_auto_segments` Adds analysis segments that specify how data from the raw file is
        mapped into a virtual address space

        Parameters:
        :   **segments** (*List**[**core.BNSegmentInfo**]*) – list of segments to add

        Return type:
        :   *None*

    add_data_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *to_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_data_ref)
    :   `add_data_ref` adds an auto data cross-reference (xref) from the address `from_addr` to
        the address `to_addr`.

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s source virtual address.
            - **to_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s destination virtual address.

        Return type:
        :   *None*

        Note

        It is intended to be used from within workflows or binary view initialization.

    add_entry_point(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_entry_point)
    :   `add_entry_point` adds a virtual address to start analysis from for a given plat.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start analysis from
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform for the entry point analysis

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.add_entry_point(0xdeadbeef)
            >>>
            ```

    add_expression_parser_magic_value(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_expression_parser_magic_value)
    :   Add a magic value to the expression parser.

        If the magic value already exists, its value gets updated. The magic value can be used
        in the expression by a $ followed by its name, e.g., $foobar. It is optional to include
        the $ when calling this function, i.e., calling with foobar and $foobar has the same
        effect.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name for the magic value to add or update
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – value for the magic value

        Returns:

        Return type:
        :   *None*

    add_expression_parser_magic_values(*names: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *values: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_expression_parser_magic_values)
    :   Add a list of magic value to the expression parser.

        The list names and values must have the same size. The ith name in the names will
        correspond to the ith value in the values.

        If a magic value already exists, its value gets updated. The magic value can be used in
        the expression by a $ followed by its name, e.g., $foobar. It is optional to include the
        $ when calling this function, i.e., calling with foobar and $foobar has the same effect.

        Parameters:
        :   - **names** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*)*) – names for the magic values to add or update
            - **values** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
              v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*)*) – value for the magic values

        Returns:

        Return type:
        :   *None*

    add_external_library(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *backing_file: [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [ExternalLibrary](externallibrary.md#binaryninja.externallibrary.ExternalLibrary "binaryninja.externallibrary.ExternalLibrary")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_external_library)
    :   Add an ExternalLibrary to this BinaryView

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the external library
            - **backing_file** ([*ProjectFile*](project.md#binaryninja.project.ProjectFile
              "binaryninja.project.ProjectFile") *|* *None*) – Optional ProjectFile that backs the
              external library
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether or not this action is the result of automated analysis

        Returns:
        :   The created ExternalLibrary

        Return type:
        :   [*ExternalLibrary*](externallibrary.md#binaryninja.externallibrary.ExternalLibrary
            "binaryninja.externallibrary.ExternalLibrary")

    add_external_location(*source_symbol: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*, *library: [ExternalLibrary](externallibrary.md#binaryninja.externallibrary.ExternalLibrary "binaryninja.externallibrary.ExternalLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *target_symbol: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *target_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [ExternalLocation](externallibrary.md#binaryninja.externallibrary.ExternalLocation "binaryninja.externallibrary.ExternalLocation")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_external_location)
    :   Add an ExternalLocation with its source in this BinaryView. ExternalLocations must have
        a target address and/or symbol.

        Parameters:
        :   - **source_symbol** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")) – Symbol that the association is from
            - **library**
              ([*ExternalLibrary*](externallibrary.md#binaryninja.externallibrary.ExternalLibrary
              "binaryninja.externallibrary.ExternalLibrary") *|* *None*) – Library that the
              ExternalLocation belongs to
            - **target_symbol** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* *None*) – Symbol that the ExternalLocation points to
            - **target_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*) – Address that the ExternalLocation points to
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether or not this action is the result of automated analysis

        Returns:
        :   The created ExternalLocation

        Return type:
        :   [*ExternalLocation*](externallibrary.md#binaryninja.externallibrary.ExternalLocation
            "binaryninja.externallibrary.ExternalLocation")

    add_function(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *auto_discovered: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *func_type: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_function)
    :   `add_function` add a new function of the given `plat` at the virtual address `addr`

        Warning

        This function is used to create auto functions, often used when writing loaders, etc.
        Most users will want to use
        [`create_user_function`](#binaryninja.binaryview.BinaryView.create_user_function
        "binaryninja.binaryview.BinaryView.create_user_function") in their scripts.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the function to be added
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform for the function to be added
            - **auto_discovered** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – True if function was automatically discovered, False if created by
              user
            - **func_type** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) – optional function type

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.add_function(1)
            >>> bv.functions
            [<func: x86_64@0x1>]
            ```

    add_tag(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag_type_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *data: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *user: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_tag)
    :   `add_tag` creates and adds a [`Tag`](#binaryninja.binaryview.Tag
        "binaryninja.binaryview.Tag") object at a data address.

        This API is appropriate for generic data tags. For functions, consider using
        [`add_tag`](function.md#binaryninja.function.Function.add_tag
        "binaryninja.function.Function.add_tag").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to add the tag
            - **tag_type_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – The name of the tag type for this Tag
            - **data** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – additional data for the Tag
            - **user** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether or not a user tag

        Example:
        :   ```
            >>> bv.add_tag(here, "Crashes", "Null pointer dereference")
            >>>
            ```

    add_to_entry_functions(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_to_entry_functions)
    :   `add_to_entry_functions` adds a function to the entry_functions list.

        Parameters:
        :   **func** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) – a Function object

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.entry_functions
            [<func: x86@0x4014c8>, <func: x86@0x401618>]
            >>> bv.add_to_entry_functions(bv.get_function_at(0x4014da))
            >>> bv.entry_functions
            [<func: x86@0x4014c8>, <func: x86@0x401618>, <func: x86@0x4014da>]
            ```

    add_type_library(*lib: [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_type_library)
    :   `add_type_library` make the contents of a type library available for type/import
        resolution

        Parameters:
        :   **lib** ([*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary")) – library to register with the view

        Return type:
        :   *None*

    add_user_data_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *to_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_user_data_ref)
    :   `add_user_data_ref` adds a user-specified data cross-reference (xref) from the address
        `from_addr` to the address `to_addr`. If the reference already exists, no action is
        performed. To remove the reference, use
        [`remove_user_data_ref`](#binaryninja.binaryview.BinaryView.remove_user_data_ref
        "binaryninja.binaryview.BinaryView.remove_user_data_ref").

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s source virtual address.
            - **to_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s destination virtual address.

        Return type:
        :   *None*

    add_user_section(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *semantics: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics") = SectionSemantics.DefaultSectionSemantics*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *entry_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *linked_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_data: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_user_section)
    :   `add_user_section` creates a user-defined section that can help inform analysis by
        clarifying what types of data exist in what ranges. Note that all data specified must
        already be mapped by an existing segment.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the section
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the start of the section
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – length of the section
            - **semantics** ([*SectionSemantics*](enums.md#binaryninja.enums.SectionSemantics
              "binaryninja.enums.SectionSemantics")) – SectionSemantics of the section
            - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – optional type
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional byte alignment
            - **entry_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional entry size
            - **linked_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – optional name of a linked section
            - **info_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – optional name of an associated informational section
            - **info_data** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional info data

        Return type:
        :   *None*

    add_user_sections(*sections: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SectionInfo](#binaryninja.binaryview.SectionInfo "binaryninja.binaryview.SectionInfo")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[BNSectionInfo]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_user_sections)
    :   `add_user_sections` Adds user-defined sections that specify semantic information about
        regions of the binary

        Parameters:
        :   - **sections** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*SectionInfo*](#binaryninja.binaryview.SectionInfo
              "binaryninja.binaryview.SectionInfo")*]* *|*
              [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[**BNSectionInfo**]*) – list of sections to add
            - **sections** –

        Return type:
        :   *None*

    add_user_segment(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_user_segment)
    :   `add_user_segment` creates a user-defined segment that specifies how data from the raw
        file is mapped into a virtual address space.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the start of the segment
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – length of the segment (may be larger than the source data)
            - **data_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – offset from the parent view
            - **data_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – length of the data from the parent view
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) – SegmentFlags

        Return type:
        :   *None*

    add_user_segments(*segments: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SegmentInfo](#binaryninja.binaryview.SegmentInfo "binaryninja.binaryview.SegmentInfo")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[BNSegmentInfo]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.add_user_segments)
    :   `add_user_segments` Adds user-defined segments that specify how data from the raw file
        is mapped into a virtual address space

        Parameters:
        :   **segments** (*List**[**core.BNSegmentInfo**]*) – list of segments to add

        Return type:
        :   *None*

    always_branch(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.always_branch)
    :   `always_branch` convert the instruction of architecture `arch` at the virtual address
        `addr` to an unconditional branch.

        Note

        This API performs a binary patch, analysis may need to be updated afterward.
        Additionally the binary file must be saved in order to preserve the changes made.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be modified
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012ef)
            'jg      0x100012f5'
            >>> bv.always_branch(0x100012ef)
            True
            >>> bv.get_disassembly(0x100012ef)
            'jmp     0x100012f5'
            >>>
            ```

    apply_debug_info(*value: [DebugInfo](debuginfo.md#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.apply_debug_info)
    :   Sets the debug info and applies its contents to the current binary view

        Parameters:
        :   **value** ([*DebugInfo*](debuginfo.md#binaryninja.debuginfo.DebugInfo
            "binaryninja.debuginfo.DebugInfo")) –

        Return type:
        :   *None*

    attach_type_archive(*archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.attach_type_archive)
    :   Attach a given type archive to the analysis and try to connect to it. If attaching was
        successful, names from that archive will become available to pull, but no types will
        actually be associated by calling this.

        Parameters:
        :   **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive")) – New archive

    attach_type_archive_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.attach_type_archive_by_id)
    :   Attach a type archive to the owned analysis and try to connect to it. If attaching was
        successful, names from that archive will become available to pull, but no types will
        actually be associated by calling this.

        The behavior of this function is rather complicated, in an attempt to enable the ability
        to have attached, but disconnected Type Archives.

        Normal operation:

        If there was no previously connected Type Archive whose id matches id, and the file at
        path contains a Type Archive whose id matches id, it will be attached and connected.

        Edge-cases:

        If there was a previously connected Type Archive whose id matches id, nothing will
        happen, and it will simply be returned. If the file at path does not exist, nothing will
        happen and None will be returned. If the file at path exists but does not contain a Type
        Archive whose id matches id, nothing will happen and None will be returned. If there was
        a previously attached but disconnected Type Archive whose id matches id, and the file at
        path contains a Type Archive whose id matches id, the previously attached Type Archive
        will have its saved path updated to point to path. The Type Archive at path will be
        connected and returned.

        Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of Type Archive to attach
            - **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Path to file of Type Archive to attach

        Returns:
        :   Attached archive object, if it could be connected.

        Return type:
        :   [*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive") | *None*

    begin_bulk_add_segments() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.begin_bulk_add_segments)
    :   `begin_bulk_add_segments` Begins a bulk segment addition operation.

        This function prepares the BinaryView for bulk addition of both auto and user-defined
        segments. During the bulk operation, segments can be added using add_auto_segment or
        similar functions without immediately triggering the MemoryMap update process. The
        queued segments will not take effect until end_bulk_add_segments is called.

        Return type:
        :   *None*

    begin_undo_actions(*anonymous_allowed: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.begin_undo_actions)
    :   `begin_undo_actions` starts recording actions taken so they can be undone at some point.

        Parameters:
        :   **anonymous_allowed** ([*bool*](https://docs.python.org/3/library/functions.html#bool
            "(in Python v3.14)")) – Legacy interop: prevent empty calls to `` commit_undo_actions`
            `` from affecting this undo state. Specifically for `` undoable_transaction` ``

        Returns:
        :   Id of undo state, for passing to `` commit_undo_actions` `` or
            [`revert_undo_actions`](#binaryninja.binaryview.BinaryView.revert_undo_actions
            "binaryninja.binaryview.BinaryView.revert_undo_actions").

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.commit_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>>
            ```

    bulk_modify_symbols()[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.bulk_modify_symbols)
    :   `bulk_modify_symbols` returns a context manager that improves performance when adding or
        removing a large number of symbols. Symbols added within the Python with keyword will
        defer processing until the end of the block. Many symbol getter APIs will return stale
        results inside the with block, so this function should only be used when symbol queries
        are not needed at the same time as the modifications.

    can_assemble(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.can_assemble)
    :   `can_assemble` queries the architecture plugin to determine if the architecture can
        assemble instructions.

        Returns:
        :   True if the architecture can assemble, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.can_assemble()
            True
            >>>
            ```

        Parameters:
        :   **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture") *|* *None*) –

    cancel_bulk_add_segments() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.cancel_bulk_add_segments)
    :   `cancel_bulk_add_segments` Cancels a bulk segment addition operation.

        This function discards all auto and user segments that were queued since the last call
        to begin_bulk_add_segments without applying them. It allows you to abandon the changes
        in case they are no longer needed.

        Note: If no bulk operation is in progress, calling this function has no effect.

        Return type:
        :   *None*

    check_for_string_annotation_type(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *allow_short_strings: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *allow_large_strings: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *child_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.check_for_string_annotation_type)
    :   Check for string annotation at a given address. This returns the string (and type of the
        string) as annotated in the UI at a given address. If there’s no annotation, this
        function returns None.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to check for string annotation
            - **allow_short_strings** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – Allow string shorter than the analysis.limits.minStringLength
              setting
            - **allow_large_strings** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – Allow strings longer than the
              rendering.strings.maxAnnotationLength setting (up to analysis.limits.maxStringLength)
            - **child_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – What width of strings to look for, 1 for ASCII/UTF8, 2 for UTF16, 4
              for UTF32, 0 to check for all

        Return type:
        :   *None*

    clear_user_global_pointer_value()[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.clear_user_global_pointer_value)
    :   Clear a previously set user global pointer value, so the auto-analysis can calculate a
        new value

    commit_undo_actions(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.commit_undo_actions)
    :   `commit_undo_actions` commits the actions taken since a call to
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions") Pass as id the value returned by
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions"). Empty values of id will commit
        all changes since the last call to
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions").

        Parameters:
        :   **id** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – id of undo state, from
            [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
            "binaryninja.binaryview.BinaryView.begin_undo_actions")

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.commit_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>>
            ```

    convert_to_nop(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.convert_to_nop)
    :   `convert_to_nop` converts the instruction at virtual address `addr` to a nop of the
        provided architecture.

        Note

        This API performs a binary patch, analysis may need to be updated afterward.
        Additionally the binary file must be saved in order to preserve the changes made.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to convert to nops
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012fb)
            'call    0x10001629'
            >>> bv.convert_to_nop(0x100012fb)
            True
            >>> #The above 'call' instruction is 5 bytes, a nop in x86 is 1 byte,
            >>> # thus 5 nops are used:
            >>> bv.get_disassembly(0x100012fb)
            'nop'
            >>> bv.get_disassembly(0x100012fb + 1)
            'nop'
            >>> bv.get_disassembly(0x100012fb + 2)
            'nop'
            >>> bv.get_disassembly(0x100012fb + 3)
            'nop'
            >>> bv.get_disassembly(0x100012fb + 4)
            'nop'
            >>> bv.get_disassembly(0x100012fb + 5)
            'mov     byte [ebp-0x1c], al'
            ```

    create_component(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parent: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_component)
    :   Create a new component with an optional name and parent.

        The parent argument can be either a Component or the Guid of a component to which the
        created component will be added as a child

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*) – Optional name to create the component with
            - **parent** ([*Component*](component.md#binaryninja.component.Component
              "binaryninja.component.Component") *|*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              *None*) – Optional parent to which the component will be added

        Returns:
        :   The created component

        Return type:
        :   [*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component")

    create_database(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *settings: [SaveSettings](filemetadata.md#binaryninja.filemetadata.SaveSettings "binaryninja.filemetadata.SaveSettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_database)
    :   `create_database` writes the current database (.bndb) out to the specified file.

        Warning

        This API will only save a database, NOT the original file from a view. To save the
        original file, use [`save`](#binaryninja.binaryview.BinaryView.save
        "binaryninja.binaryview.BinaryView.save"). To update a database, use
        [`save_auto_snapshot`](#binaryninja.binaryview.BinaryView.save_auto_snapshot
        "binaryninja.binaryview.BinaryView.save_auto_snapshot")

        Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – path and filename to write the bndb to, this string should have “.bndb”
              appended to it.
            - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count.
            - **settings** ([*SaveSettings*](filemetadata.md#binaryninja.filemetadata.SaveSettings
              "binaryninja.filemetadata.SaveSettings")) – optional argument for special save options.

        Returns:
        :   True on success, False on failure

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Warning

        The calling thread must not hold a lock on the BinaryView instance as this action is run
        on the main thread which requires the lock.

        Example:
        :   ```
            >>> settings = SaveSettings()
            >>> bv.create_database(f"{bv.file.filename}.bndb", None, settings)
            True
            ```

        Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*) –
            - **settings** ([*SaveSettings*](filemetadata.md#binaryninja.filemetadata.SaveSettings
              "binaryninja.filemetadata.SaveSettings") *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    create_logger(*logger_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Logger](log.md#binaryninja.log.Logger "binaryninja.log.Logger")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_logger)
    :   Parameters:
        :   **logger_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*Logger*](log.md#binaryninja.log.Logger "binaryninja.log.Logger")

    create_structure_from_offset_access(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*) → [StructureType](types.md#binaryninja.types.StructureType "binaryninja.types.StructureType")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_structure_from_offset_access)
    :   Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) –

        Return type:
        :   [*StructureType*](types.md#binaryninja.types.StructureType
            "binaryninja.types.StructureType")

    create_structure_member_from_access(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_structure_member_from_access)
    :   Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")

    create_tag_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *icon: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_tag_type)
    :   `create_tag_type` creates a new [`TagType`](#binaryninja.binaryview.TagType
        "binaryninja.binaryview.TagType") and adds it to the view

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The name for the tag
            - **icon** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The icon (recommended 1 emoji or 2 chars) for the tag

        Returns:
        :   The created tag type

        Return type:
        :   [*TagType*](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")

        Example:
        :   ```
            >>> bv.create_tag_type("Crabby Functions", "🦀")
            >>>
            ```

    create_user_function(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.create_user_function)
    :   `create_user_function` add a new *user* function of the given `plat` at the virtual
        address `addr`

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the *user* function to be added
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – Platform for the function to be added

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.create_user_function(1)
            >>> bv.functions
            [<func: x86_64@0x1>]
            ```

    define_auto_symbol(*sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_auto_symbol)
    :   `define_auto_symbol` adds a symbol to the internal list of automatically discovered
        Symbol objects in a given namespace.

        Warning

        If multiple symbols for the same address are defined, the symbol with the highest
        confidence and lowest SymbolType value will be used. Ties are broken by symbol name.

        Parameters:
        :   **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")) – the symbol to define

        Return type:
        :   *None*

    define_auto_symbol_and_var_or_function(*sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *type_confidence: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 0*) → [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_auto_symbol_and_var_or_function)
    :   `define_auto_symbol_and_var_or_function` Defines an “Auto” symbol, and a
        Variable/Function alongside it.

        Warning

        If multiple symbols for the same address are defined, the symbol with the highest
        confidence and lowest SymbolType value will be used. Ties are broken by symbol name.

        Parameters:
        :   - **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")) – Symbol to define
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|* *None*)
              – Type for the function/variable being defined (can be None)
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform (optional)
            - **type_confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*) – Optional confidence value for the type

        Return type:
        :   *Optional*[[*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")]

    define_data_var(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *var_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_data_var)
    :   `define_data_var` defines a non-user data variable `var_type` at the virtual address
        `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to define the given data variable
            - **var_type** (*StringOrType*) – type to be defined at the given virtual address
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol") *|* *None*) – Optionally additionally define a symbol at
              this location
            - **name** –

        Return type:
        :   *None*

        Example:
        :   ```
            >>> t = bv.parse_type_string("int foo")
            >>> t
            (<type: int32_t>, 'foo')
            >>> bv.define_data_var(bv.entry_point, t[0])
            >>> bv.define_data_var(bv.entry_point + 4, "int", "foo")
            >>> bv.get_symbol_at(bv.entry_point + 4)
            <DataSymbol: "foo" @ 0x23950>
            >>> bv.get_data_var_at(bv.entry_point + 4)
            <var 0x23950: int32_t>
            ```

    define_imported_function(*import_addr_sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_imported_function)
    :   `define_imported_function` defines an imported Function `func` with a
        ImportedFunctionSymbol type.

        Parameters:
        :   - **import_addr_sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")) – A Symbol object with type ImportedFunctionSymbol
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – A Function object to define as an imported function
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|* *None*)
              – Optional type for the function

        Return type:
        :   *None*

    define_type(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default_name: _types.QualifiedNameType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type_obj: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | _types.Type | _types.TypeBuilder*) → _types.QualifiedName[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_type)
    :   `define_type` registers a `Type` `type_obj` of the given `name` in the global list of
        types for the current [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView"). This method should only be used for automatically
        generated types.

        Parameters:
        :   - **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Unique identifier for the automatically generated type
            - **default_name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the type to be registered
            - **type_obj** (*StringOrType*) – Type object to be registered

        Returns:
        :   Registered name of the type. May not be the same as the requested name if the user has
            renamed types.

        Return type:
        :   [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> registered_name = bv.define_type(Type.generate_auto_type_id("source", name), name, type)
            >>> bv.get_type_by_name(registered_name)
            <type: int32_t>
            >>> registered_name = bv.define_type("mytypeid", None, "int bar")
            >>> bv.get_type_by_name(registered_name)
            <type: int32_t>
            ```

    define_types(*types: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), _types.QualifiedNameType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | _types.Type | _types.TypeBuilder]]*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), _types.QualifiedName][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_types)
    :   `define_types` registers multiple types as though calling
        [`define_type`](#binaryninja.binaryview.BinaryView.define_type
        "binaryninja.binaryview.BinaryView.define_type") multiple times. The difference with
        this plural version is that it is optimized for adding many types at the same time,
        using knowledge of all types at add-time to improve runtime. There is an optional
        `progress_func` callback function in case you want updates for a long-running call.

        Warning

        This method should only be used for automatically generated types, see
        [`define_user_types`](#binaryninja.binaryview.BinaryView.define_user_types
        "binaryninja.binaryview.BinaryView.define_user_types") for interactive plugin uses.

        The return values of this function provide a map of each type id and which name was
        chosen for that type (which may be different from the requested name).

        Parameters:
        :   - **types** ([*Sequence*](https://docs.python.org/3/library/typing.html#typing.Sequence
              "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*,* *_types.QualifiedNameType* *|* *None**,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              *_types.Type* *|* *_types.TypeBuilder**]**]*) – List of type ids/names/definitions for
              the new types. Check [`define_type`](#binaryninja.binaryview.BinaryView.define_type
              "binaryninja.binaryview.BinaryView.define_type") for more details.
            - **progress** – Function to call for progress updates
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*) –

        Returns:
        :   A map of all the chosen names for the defined types with their ids.

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), _types.QualifiedName]

    define_user_data_var(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *var_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_user_data_var)
    :   `define_user_data_var` defines a user data variable `var_type` at the virtual address
        `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to define the given data variable
            - **var_type** (*binaryninja.Type*) – type to be defined at the given virtual address
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol") *|* *None*) – Optionally, additionally define a symbol
              at this same address
            - **name** –

        Return type:
        :   *Optional*[[*DataVariable*](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")]

        Example:
        :   ```
            >>> t = bv.parse_type_string("int foo")
            >>> t
            (<type: int32_t>, 'foo')
            >>> bv.define_user_data_var(bv.entry_point, t[0])
            <var 0x2394c: int32_t>
            >>> bv.define_user_data_var(bv.entry_point + 4, "int", "foo")
            <var 0x23950: int32_t>
            >>> bv.get_symbol_at(bv.entry_point + 4)
            <DataSymbol: "foo" @ 0x23950>
            >>> bv.get_data_var_at(bv.entry_point + 4)
            <var 0x23950: int32_t>
            ```

    define_user_symbol(*sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_user_symbol)
    :   `define_user_symbol` adds a symbol to the internal list of user added Symbol objects.

        Warning

        If multiple symbols for the same address are defined, the symbol with the highest
        confidence and lowest SymbolType value will be used. Ties are broken by symbol name.

        Parameters:
        :   **sym** ([*Symbol*](types.md#binaryninja.types.Symbol "binaryninja.types.Symbol")) – the
            symbol to define

        Return type:
        :   *None*

    define_user_type(*name: _types.QualifiedNameType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type_obj: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | _types.Type | _types.TypeBuilder*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_user_type)
    :   `define_user_type` registers a `Type` `type_obj` of the given `name` in the global list
        of user types for the current [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView").

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Name of the user type to be registered
            - **type_obj** (*StringOrType*) – Type object to be registered

        Return type:
        :   *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> bv.define_user_type(name, type)
            >>> bv.get_type_by_name(name)
            <type: int32_t>
            >>> bv.define_user_type(None, "int bas")
            >>> bv.get_type_by_name("bas")
            <type: int32_t>
            ```

    define_user_types(*types: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[_types.QualifiedNameType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | _types.Type | _types.TypeBuilder]]*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.define_user_types)
    :   `define_user_types` registers multiple types as though calling
        [`define_user_type`](#binaryninja.binaryview.BinaryView.define_user_type
        "binaryninja.binaryview.BinaryView.define_user_type") multiple times. The difference
        with this plural version is that it is optimized for adding many types at the same time,
        using knowledge of all types at add-time to improve runtime. There is an optional
        `progress_func` callback function in case you want updates for a long-running call.

        Parameters:
        :   - **types** ([*Sequence*](https://docs.python.org/3/library/typing.html#typing.Sequence
              "(in Python
              v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[**_types.QualifiedNameType* *|* *None**,*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              *_types.Type* *|* *_types.TypeBuilder**]**]*) – List of type names/definitions for the
              new types. Check
              [`define_user_type`](#binaryninja.binaryview.BinaryView.define_user_type
              "binaryninja.binaryview.BinaryView.define_user_type") for more details.
            - **progress** – Function to call for progress updates
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*) –

    detach_type_archive(*archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.detach_type_archive)
    :   Detach from a type archive, breaking all associations to types within the archive

        Parameters:
        :   **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive")) – Type archive to detach

    detach_type_archive_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.detach_type_archive_by_id)
    :   Detach from a type archive, breaking all associations to types within the archive

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of archive to detach

    *static* detect_search_mode(*pattern: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *raw: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.detect_search_mode)
    :   Detects the search mode that would be used by
        [`search`](#binaryninja.binaryview.BinaryView.search
        "binaryninja.binaryview.BinaryView.search") for the given pattern.

        Parameters:
        :   - **pattern** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The search pattern to analyze.
            - **raw** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether to interpret the pattern as a raw string (default: False).

        Returns:
        :   The detected search mode: `"FlexHex"`, `"Regex"`, or `"Raw String"`.

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    disassembly_text(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.disassembly_text)
    :   `disassembly_text` helper function for getting disassembly of a given address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of instruction
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – optional Architecture, `self.arch` is used
              if this parameter is None

        Returns:
        :   a str representation of the instruction at virtual address `addr` or None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") or
            *None*

        Example:
        :   ```
            >>> next(bv.disassembly_text(bv.entry_point))
            'push    ebp', 1
            >>>
            ```

    disassembly_tokens(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.disassembly_tokens)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python
            v3.14)")[[*InstructionTextToken*](architecture.md#binaryninja.architecture.InstructionTextToken
            "binaryninja.architecture.InstructionTextToken")],
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")],
            *None*, *None*]

    disassociate_type_archive_type(*type: _types.QualifiedNameType*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.disassociate_type_archive_type)
    :   Disassociate an associated type, so that it will no longer receive updates from its
        connected type archive

        Parameters:
        :   **type** (*_types.QualifiedNameType*) – Name of type in analysis

        Returns:
        :   True if successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    disassociate_type_archive_type_by_id(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.disassociate_type_archive_type_by_id)
    :   Disassociate an associated type id, so that it will no longer receive updates from its
        connected type archive

        Parameters:
        :   **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of type in analysis

        Returns:
        :   True if successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    end_bulk_add_segments() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.end_bulk_add_segments)
    :   `end_bulk_add_segments` Finalizes and applies all queued segments (auto and user) added
        during a bulk segment addition operation.

        This function commits all segments that were queued since the last call to
        begin_bulk_add_segments. The MemoryMap update process is executed at this point,
        applying all changes in one batch for improved performance.

        Note: This function must be called after begin_bulk_add_segments to apply the queued
        segments.

        Return type:
        :   *None*

    eval(*expression: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *here: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.eval)
    :   Evaluates a string expression to an integer value. This is a more concise alias for the
        [`parse_expression`](#binaryninja.binaryview.BinaryView.parse_expression
        "binaryninja.binaryview.BinaryView.parse_expression") API

        Parameters:
        :   - **expression** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **here** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    export_object_to_library(*lib: [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type_obj: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.export_object_to_library)
    :   Recursively exports `type_obj` into `lib` as an object with a `name`.

        This should be used to store definitions for functions, variables, and other things that
        are named symbols. For example, MessageBoxA might be the name of a function with the
        type int ()(HWND, LPCSTR, LPCSTR, UINT). If you just want to store a type definition,
        you probably want
        [`export_type_to_library`](#binaryninja.binaryview.BinaryView.export_type_to_library
        "binaryninja.binaryview.BinaryView.export_type_to_library").

        As other referenced types are encountered, they are either copied into the destination
        type library or else the type library that provided the referenced type is added as a
        dependency for the destination library.

        Parameters:
        :   - **lib** ([*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) –
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type_obj** (*StringOrType*) –

        Return type:
        :   *None*

    export_type_to_library(*lib: [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *type_obj: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.export_type_to_library)
    :   Recursively exports `type_obj` into `lib` as a type with a `name`.

        This should be used to store type definitions with no symbol information. For example,
        color might be a type of enum {RED=0, ORANGE=1, YELLOW=2, …} used by this library. If
        you have a function, variable, or other object that is exported, you probably want
        [`export_object_to_library`](#binaryninja.binaryview.BinaryView.export_object_to_library
        "binaryninja.binaryview.BinaryView.export_object_to_library") instead.

        As other referenced types are encountered, they are either copied into the destination
        type library or else the type library that provided the referenced type is added as a
        dependency for the destination library.

        Parameters:
        :   - **lib** ([*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) –
            - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **type_obj** (*StringOrType*) –

        Return type:
        :   *None*

    *static* external_namespace() → [NameSpace](types.md#binaryninja.types.NameSpace "binaryninja.types.NameSpace")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.external_namespace)
    :   External namespace for the current BinaryView

        Return type:
        :   [*NameSpace*](types.md#binaryninja.types.NameSpace "binaryninja.types.NameSpace")

    finalize_new_segments() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.finalize_new_segments)
    :   Performs “finalization” on segments added after initial Finalization (performed after an
        Init() has completed).

        Finalizing a segment involves optimizing the relocation info stored in that segment, so
        if a segment is added and relocations are defined for that segment by some automated
        process, this function should be called afterwards.

        An example of this can be seen in the KernelCache plugin, in
        KernelCache::LoadImageWithInstallName. After we load an image, map new segments, and
        define relocations for all of them, we call this function to let core know it is now
        safe to finalize the new segments

        Returns:
        :   Whether finalization was successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    find_all_constant(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *constant: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *graph_type: _function.FunctionViewTypeOrName = FunctionGraphType.NormalFunctionGraph*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *match_callback: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [QueueGenerator](#binaryninja.binaryview.BinaryView.QueueGenerator "binaryninja.binaryview.BinaryView.QueueGenerator")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.find_all_constant)

    find_all_constant(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *constant: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *graph_type: _function.FunctionViewTypeOrName = FunctionGraphType.NormalFunctionGraph*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *match_callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   `find_all_constant` searches for the integer constant `constant` starting at the virtual
        address `start` until the virtual address `end`. Once a match is found, the
        `match_callback` is called.

        Note

        A `constant` is considered used if a line in the linear view expansion of the given
        function graph type contains a token with a value that matches that constant. This does
        not search for raw bytes/data in the binary, for that you want to use
        [`find_all_data`](#binaryninja.binaryview.BinaryView.find_all_data
        "binaryninja.binaryview.BinaryView.find_all_data").

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start searching from.
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to end the search.
            - **constant** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – constant to search for
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings")) – DisassemblySettings object used to render
              the text to be searched
            - **graph_type** ([*FunctionViewType*](function.md#binaryninja.function.FunctionViewType
              "binaryninja.function.FunctionViewType")) – the IL to search within
            - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count. This function should return a boolean value that decides
              whether the search should continue or stop
            - **match_callback** (*callback*) – function that gets called when a match is found. The
              callback takes two parameters, i.e., the address of the match, and the
              LinearDisassemblyLine that contains the matching line. If this parameter is None, this
              function becomes a generator and yields the matching address and the matching
              LinearDisassemblyLine. This function can return a boolean value that decides whether the
              search should continue or stop

        Rtype QueueGenerator:
        :   A generator object that will yield all the found results

    find_all_data(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *flags: [FindFlag](enums.md#binaryninja.enums.FindFlag "binaryninja.enums.FindFlag") = FindFlag.FindCaseSensitive*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *match_callback: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [QueueGenerator](#binaryninja.binaryview.BinaryView.QueueGenerator "binaryninja.binaryview.BinaryView.QueueGenerator")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.find_all_data)

    find_all_data(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *flags: [FindFlag](enums.md#binaryninja.enums.FindFlag "binaryninja.enums.FindFlag") = FindFlag.FindCaseSensitive*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *match_callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   `find_all_data` searches for the bytes `data` starting at the virtual address `start`
        until the virtual address `end`. Once a match is found, the `match_callback` is called.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start searching from.
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to end the search.
            - **data** (*Union**[*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*,*
              [*bytearray*](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python
              v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*]*) – data to search for
            - **flags** ([*FindFlag*](enums.md#binaryninja.enums.FindFlag
              "binaryninja.enums.FindFlag")) –

              (optional) defaults to case-insensitive data search

              | FindFlag | Description |
              | --- | --- |
              | FindCaseSensitive | Case-sensitive search |
              | FindCaseInsensitive | Case-insensitive search |
            - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count. This function should return a boolean value that decides
              whether the search should continue or stop
            - **match_callback** (*callback*) – function that gets called when a match is found. The
              callback takes two parameters, i.e., the address of the match, and the actual DataBuffer
              that satisfies the search. If this parameter is None, this function becomes a generator
              and yields a tuple of the matching address and the matched DataBuffer. This function can
              return a boolean value that decides whether the search should continue or stop.

        Rtype QueueGenerator:
        :   A generator object that will yield all the found results

    find_all_text(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *flags=FindFlag.FindCaseSensitive*, *graph_type: _function.FunctionViewTypeOrName = FunctionGraphType.NormalFunctionGraph*, *progress_func=None*, *match_callback: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [QueueGenerator](#binaryninja.binaryview.BinaryView.QueueGenerator "binaryninja.binaryview.BinaryView.QueueGenerator")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.find_all_text)

    find_all_text(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *flags=FindFlag.FindCaseSensitive*, *graph_type: _function.FunctionViewTypeOrName = FunctionGraphType.NormalFunctionGraph*, *progress_func=None*, *match_callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   `find_all_text` searches for string `text` occurring in the linear view output starting
        at the virtual address `start` until the virtual address `end`. Once a match is found,
        the `match_callback` is called.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start searching from.
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to end the search.
            - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – text to search for
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings")) – DisassemblySettings object used to render
              the text to be searched
            - **flags** ([*FindFlag*](enums.md#binaryninja.enums.FindFlag
              "binaryninja.enums.FindFlag")) –

              (optional) bit-flags list of options, defaults to case-insensitive data search

              | FindFlag | Description |
              | --- | --- |
              | FindCaseSensitive | Case-sensitive search |
              | FindCaseInsensitive | Case-insensitive search |
              | FindIgnoreWhitespace | Ignore whitespace characters |
            - **graph_type** ([*FunctionViewType*](function.md#binaryninja.function.FunctionViewType
              "binaryninja.function.FunctionViewType")) – the IL to search within
            - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count. This function should return a boolean value that decides
              whether the search should continue or stop
            - **match_callback** (*callback*) – function that gets called when a match is found. The
              callback takes three parameters, i.e., the address of the match, and the actual string
              that satisfies the search, and the LinearDisassemblyLine that contains the matching
              line. If this parameter is None, this function becomes a generator and yields a tuple of
              the matching address, the matched string, and the matching LinearDisassemblyLine. This
              function can return a boolean value that decides whether the search should continue or
              stop

        Rtype QueueGenerator:
        :   A generator object that will yield all the found results

    find_next_constant(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *constant: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *graph_type: [FunctionViewType](function.md#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType") | [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = FunctionGraphType.NormalFunctionGraph*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.find_next_constant)
    :   `find_next_constant` searches for integer constant `constant` occurring in the linear
        view output starting at the virtual address `start` until the end of the BinaryView.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start searching from.
            - **constant** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – constant to search for
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings")) – disassembly settings
            - **graph_type** ([*FunctionViewType*](function.md#binaryninja.function.FunctionViewType
              "binaryninja.function.FunctionViewType")) – the IL to search within

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    find_next_data(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *flags: [FindFlag](enums.md#binaryninja.enums.FindFlag "binaryninja.enums.FindFlag") = FindFlag.FindCaseSensitive*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.find_next_data)
    :   `find_next_data` searches for the bytes `data` starting at the virtual address `start`
        until the end of the BinaryView.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start searching from.
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – data to search for
            - **flags** ([*FindFlag*](enums.md#binaryninja.enums.FindFlag
              "binaryninja.enums.FindFlag")) –

              (optional) defaults to case-insensitive data search

              | FindFlag | Description |
              | --- | --- |
              | FindCaseSensitive | Case-sensitive search |
              | FindCaseInsensitive | Case-insensitive search |
            - **data** –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    find_next_text(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *flags: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = FindFlag.FindCaseSensitive*, *graph_type: [FunctionViewType](function.md#binaryninja.function.FunctionViewType "binaryninja.function.FunctionViewType") | [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = FunctionGraphType.NormalFunctionGraph*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.find_next_text)
    :   `find_next_text` searches for string `text` occurring in the linear view output starting
        at the virtual address `start` until the end of the BinaryView.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start searching from.
            - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – text to search for
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings")) – disassembly settings
            - **flags** ([*FindFlag*](enums.md#binaryninja.enums.FindFlag
              "binaryninja.enums.FindFlag")) –

              (optional) bit-flags list of options, defaults to case-insensitive data search

              | FindFlag | Description |
              | --- | --- |
              | FindCaseSensitive | Case-sensitive search |
              | FindCaseInsensitive | Case-insensitive search |
              | FindIgnoreWhitespace | Ignore whitespace characters |
            - **graph_type** ([*FunctionViewType*](function.md#binaryninja.function.FunctionViewType
              "binaryninja.function.FunctionViewType")) – the IL to search within

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    forget_undo_actions(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.forget_undo_actions)
    :   `forget_undo_actions` removes the actions taken since a call to
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions") Pass as id the value returned by
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions"). Empty values of id will remove
        all changes since the last call to
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions").

        Parameters:
        :   **id** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – id of undo state, from
            [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
            "binaryninja.binaryview.BinaryView.begin_undo_actions")

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.forget_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>>
            ```

    get_address_for_data_offset(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_address_for_data_offset)
    :   `get_address_for_data_offset` returns the virtual address that maps to the specific file
        offset.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – file offset

        Returns:
        :   the virtual address of the first segment that contains that file location

        Return type:
        :   Int

    get_address_input(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *current_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_address_input)
    :   `get_address_input` Gets a virtual address via a prompt displayed to the user

        Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Prompt for the dialog
            - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Window title, if used in the UI
            - **current_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*) – Optional current address, for relative inputs

        Returns:
        :   The value entered by the user, if one was entered

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    get_all_fields_referenced(*name: _types.QualifiedNameType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_all_fields_referenced)
    :   `get_all_fields_referenced` returns a list of offsets in the QualifiedName specified by
        name, which are referenced by code.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – name of type to query for references

        Returns:
        :   List of offsets

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

        Example:
        :   ```
            >>> bv.get_all_fields_referenced('A')
            [0, 8, 16, 24, 32, 40]
            >>>
            ```

    get_all_sizes_referenced(*name: _types.QualifiedNameType*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_all_sizes_referenced)
    :   `get_all_sizes_referenced` returns a map from field offset to a list of sizes of the
        accesses to it.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – name of type to query for references

        Returns:
        :   A map from field offset to the size of the code accesses to it

        Return type:
        :   *map*

        Example:
        :   ```
            >>> bv.get_all_sizes_referenced('B')
            {0: [1, 8], 8: [8], 16: [1, 8]}
            >>>
            ```

    get_all_types_referenced(*name: _types.QualifiedNameType*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.Type]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_all_types_referenced)
    :   `get_all_types_referenced` returns a map from field offset to a list of incoming types
        written to the specified type.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – name of type to query for references

        Returns:
        :   A map from field offset to a list of incoming types written to it

        Return type:
        :   *map*

        Example:
        :   ```
            >>> bv.get_all_types_referenced('B')
            {0: [<type: char, 0% confidence>], 8: [<type: int64_t, 0% confidence>],
            16: [<type: char, 0% confidence>, <type: bool>]}
            >>>
            ```

    get_ascii_string_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *min_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 4*, *max_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *require_cstring: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [StringReference](#binaryninja.binaryview.StringReference "binaryninja.binaryview.StringReference") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_ascii_string_at)
    :   `get_ascii_string_at` returns an ascii string found at `addr`.

        Note

        This returns an ascii string irrespective of whether the core analysis identified a
        string at that location. For an alternative API that uses existing identified strings,
        use [`get_string_at`](#binaryninja.binaryview.BinaryView.get_string_at
        "binaryninja.binaryview.BinaryView.get_string_at").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to start the string
            - **min_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – minimum length to define a string
            - **max_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – max length string to return
            - **require_cstring** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – only return 0x0-terminated strings

        Returns:
        :   the string found at `addr` or None if a string does not exist

        Return type:
        :   [*StringReference*](#binaryninja.binaryview.StringReference
            "binaryninja.binaryview.StringReference") or *None*

        Example:
        :   ```
            >>> s1 = bv.get_ascii_string_at(0x70d0)
            >>> s1
            <AsciiString: 0x70d0, len 0xb>
            >>> s1.value
            'AWAVAUATUSH'
            >>> s2 = bv.get_ascii_string_at(0x70d1)
            >>> s2
            <AsciiString: 0x70d1, len 0xa>
            >>> s2.value
            'WAVAUATUSH'
            ```

    get_associated_type_archive_type_source(*archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *archive_type: _types.QualifiedNameType*) → _types.QualifiedName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_associated_type_archive_type_source)
    :   Determine the local source type name for a given archive type

        Parameters:
        :   - **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Target type archive
            - **archive_type** (*_types.QualifiedNameType*) – Name of target archive type

        Returns:
        :   Name of source analysis type, if this type is associated. None otherwise.

        Return type:
        :   _types.QualifiedName | *None*

    get_associated_type_archive_type_source_by_id(*archive_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *archive_type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_associated_type_archive_type_source_by_id)
    :   Determine the local source type id for a given archive type

        Parameters:
        :   - **archive_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of target type archive
            - **archive_type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – Id of target archive type

        Returns:
        :   Id of source analysis type, if this type is associated. None otherwise.

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_associated_type_archive_type_target(*name: _types.QualifiedNameType*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_associated_type_archive_type_target)
    :   Determine the target archive / type id of a given analysis type

        Parameters:
        :   **name** (*_types.QualifiedNameType*) – Analysis type

        Returns:
        :   (archive, archive type id) if the type is associated. None otherwise.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive") | *None*,
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] |
            *None*

    get_associated_type_archive_type_target_by_id(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_associated_type_archive_type_target_by_id)
    :   Determine the target archive / type id of a given analysis type

        Parameters:
        :   **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Analysis type id

        Returns:
        :   (archive id, archive type id) if the type is associated. None otherwise.

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")] | *None*

    get_associated_types_from_archive(*archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_associated_types_from_archive)
    :   Get a list of all types in the analysis that are associated with a specific type archive

        Returns:
        :   Map of all analysis types to their corresponding archive id

        Parameters:
        :   **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive")) –

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[[*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName"),
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]

    get_associated_types_from_archive_by_id(*archive_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_associated_types_from_archive_by_id)
    :   Get a list of all types in the analysis that are associated with a specific type archive
        :return: Map of all analysis types to their corresponding archive id

        Parameters:
        :   **archive_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_basic_blocks_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_basic_blocks_at)
    :   `get_basic_blocks_at` get a list of
        [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
        "binaryninja.basicblock.BasicBlock") objects which exist at the provided virtual
        address.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address of BasicBlock desired

        Returns:
        :   a list of [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock") objects

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock"))

    get_basic_blocks_starting_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_basic_blocks_starting_at)
    :   `get_basic_blocks_starting_at` get a list of
        [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
        "binaryninja.basicblock.BasicBlock") objects which start at the provided virtual
        address.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address of BasicBlock desired

        Returns:
        :   a list of [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock") objects

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock"))

    get_callees(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_callees)
    :   `get_callees` returns a list of virtual addresses called by the call site in the
        function `func`, of the architecture `arch`, and at the address `addr`. If no function
        is specified, call sites from all functions and containing the address will be
        considered. If no architecture is specified, the architecture of the function will be
        used.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the call site to query for callees
            - **func** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the function that the call site
              belongs to
            - **func** – (optional) the architecture of the call site
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

    get_callers(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[ReferenceSource](#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_callers)
    :   `get_callers` returns a list of ReferenceSource objects (xrefs or cross-references) that
        call the provided virtual address. In this case, tail calls, jumps, and ordinary calls
        are considered.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address of callee to query for callers

        Returns:
        :   List of References that call the given virtual address

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*ReferenceSource*](#binaryninja.binaryview.ReferenceSource
            "binaryninja.binaryview.ReferenceSource"))

        Example:
        :   ```
            >>> bv.get_callers(here)
            [<ref: x86@0x4165ff>]
            >>>
            ```

    get_code_refs(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[ReferenceSource](#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_code_refs)
    :   `get_code_refs` returns a generator of
        [`ReferenceSource`](#binaryninja.binaryview.ReferenceSource
        "binaryninja.binaryview.ReferenceSource") objects (xrefs or cross-references) that point
        to the provided virtual address. This function returns both autoanalysis (“auto”) and
        user-specified (“user”) xrefs. To add a user-specified reference, see
        [`add_user_code_ref`](function.md#binaryninja.function.Function.add_user_code_ref
        "binaryninja.function.Function.add_user_code_ref").

        The related [`get_data_refs`](#binaryninja.binaryview.BinaryView.get_data_refs
        "binaryninja.binaryview.BinaryView.get_data_refs") is used to find data references to an
        address unlike this API which returns references that exist in code.

        Note

        Note that get_code_refs returns xrefs to code that references the address being queried.
        get_data_refs on the other hand returns references that exist in data (pointers in
        global variables for example). The related
        [`get_code_refs_from`](#binaryninja.binaryview.BinaryView.get_code_refs_from
        "binaryninja.binaryview.BinaryView.get_code_refs_from") looks for references that are
        outgoing from the queried address to other locations.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   A generator of References for the given virtual address

        Return type:
        :   *Generator*[[*ReferenceSource*](#binaryninja.binaryview.ReferenceSource
            "binaryninja.binaryview.ReferenceSource"), *None*, *None*]

        Example:
        :   ```
            >>> bv.get_code_refs(here)
            [<ref: x86@0x4165ff>]
            >>>
            ```

    get_code_refs_for_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[ReferenceSource](#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_code_refs_for_type)
    :   `get_code_refs_for_type` returns a Generator[ReferenceSource] objects (xrefs or
        cross-references) that reference the provided QualifiedName.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   List of References for the given type

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*ReferenceSource*](#binaryninja.binaryview.ReferenceSource
            "binaryninja.binaryview.ReferenceSource"))

        Example:
        :   ```
            >>> bv.get_code_refs_for_type('A')
            [<ref: x86@0x4165ff>]
            >>>
            ```

    get_code_refs_for_type_field(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[TypeFieldReference](types.md#binaryninja.types.TypeFieldReference "binaryninja.types.TypeFieldReference"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_code_refs_for_type_field)
    :   `get_code_refs_for_type` returns a Generator[TypeFieldReference] objects (xrefs or
        cross-references) that reference the provided type field.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field, relative to the type
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   Generator of References for the given type

        Return type:
        :   *Generator*[[*TypeFieldReference*](types.md#binaryninja.types.TypeFieldReference
            "binaryninja.types.TypeFieldReference")]

        Example:
        :   ```
            >>> bv.get_code_refs_for_type_field('A', 0x8)
            [<ref: x86@0x4165ff>]
            >>>
            ```

    get_code_refs_for_type_fields_from(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeReferenceSource](types.md#binaryninja.types.TypeReferenceSource "binaryninja.types.TypeReferenceSource")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_code_refs_for_type_fields_from)
    :   `get_code_refs_for_type_fields_from` returns a list of type fields referenced by code in
        the function `func`, of the architecture `arch`, and at the address `addr`. If no
        function is specified, references from all functions and containing the address will be
        returned. If no architecture is specified, the architecture of the function will be
        used.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Returns:
        :   list of references

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*TypeReferenceSource*](types.md#binaryninja.types.TypeReferenceSource
            "binaryninja.types.TypeReferenceSource"))

    get_code_refs_for_type_from(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeReferenceSource](types.md#binaryninja.types.TypeReferenceSource "binaryninja.types.TypeReferenceSource")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_code_refs_for_type_from)
    :   `get_code_refs_for_type_from` returns a list of types referenced by code in the function
        `func`, of the architecture `arch`, and at the address `addr`. If no function is
        specified, references from all functions and containing the address will be returned. If
        no architecture is specified, the architecture of the function will be used.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Returns:
        :   list of references

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*TypeReferenceSource*](types.md#binaryninja.types.TypeReferenceSource
            "binaryninja.types.TypeReferenceSource"))

    get_code_refs_from(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_code_refs_from)
    :   `get_code_refs_from` returns a list of virtual addresses referenced by code in the
        function `func`, of the architecture `arch`, and at the address `addr`. If no function
        is specified, references from all functions and containing the address will be returned.
        If no architecture is specified, the architecture of the function will be used. This
        function returns both autoanalysis (“auto”) and user-specified (“user”) xrefs. To add a
        user-specified reference, see
        [`add_user_code_ref`](function.md#binaryninja.function.Function.add_user_code_ref
        "binaryninja.function.Function.add_user_code_ref").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – optional architecture of query
            - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

    get_comment_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_comment_at)
    :   `get_comment_at` returns the address-based comment attached to the given address in this
        BinaryView Note that address-based comments are different from function-level comments
        which are specific to each [`Function`](function.md#binaryninja.function.Function
        "binaryninja.function.Function"). For more information, see
        [`address_comments`](#binaryninja.binaryview.BinaryView.address_comments
        "binaryninja.binaryview.BinaryView.address_comments").

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address within the current BinaryView to apply the comment to

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_component(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Component](component.md#binaryninja.component.Component "binaryninja.component.Component") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_component)
    :   Lookup a Component by its GUID

        Parameters:
        :   **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – GUID of the component to look up

        Returns:
        :   The Component with that Guid

        Return type:
        :   [*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component") | *None*

    get_component_by_path(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Component](component.md#binaryninja.component.Component "binaryninja.component.Component") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_component_by_path)
    :   Lookup a Component by its pathname

        Note:
        :   This is a convenience method, and for performance-sensitive lookups, GetComponentByGuid
            is very highly recommended.

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component") | *None*

        Lookups are done based on the .display_name of the Component.

        All lookups are absolute from the root component, and are case-sensitive. Pathnames are
        delimited with “/”

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Pathname of the desired Component

        Returns:
        :   The Component at that pathname

        Example:
        :   ```
            >>> c = bv.create_component(name="MyComponent")
            >>> c2 = bv.create_component(name="MySubComponent", parent=c)
            >>> bv.get_component_by_path("/MyComponent/MySubComponent") == c2
            True
            >>> c3 = bv.create_component(name="MySubComponent", parent=c)
            >>> c3
            <Component "MySubComponent (1)" "(20712aff...")>
            >>> bv.get_component_by_path("/MyComponent/MySubComponent (1)") == c3
            True
            ```

        Return type:
        :   [*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component") | *None*

    get_data_offset_for_address(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_offset_for_address)
    :   `get_data_offset_for_address` returns the file offset that maps to the given virtual
        address, if possible.

        If address falls within a bss segment or an external segment, for example, no mapping is
        possible, and None will be returned.

        Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address

        Returns:
        :   the file location that is mapped to the given virtual address, or None if no such
            mapping is possible

        Return type:
        :   Int

    get_data_refs(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_refs)
    :   `get_data_refs` returns a list of virtual addresses of _data_ (not code) which
        references `addr`, optionally specifying a length. When `length` is set `get_data_refs`
        returns the data which references in the range `addr`-``` addr``+``length ```. This
        function returns both autoanalysis (“auto”) and user-specified (“user”) xrefs. To add a
        user-specified reference, see
        [`add_user_data_ref`](#binaryninja.binaryview.BinaryView.add_user_data_ref
        "binaryninja.binaryview.BinaryView.add_user_data_ref").

        Warning

        If you’re looking at this API, please double check that you don’t mean to use
        [`get_code_refs`](#binaryninja.binaryview.BinaryView.get_code_refs
        "binaryninja.binaryview.BinaryView.get_code_refs") instead. get_code_refs returns
        references from code to the specified address while this API returns references from
        data (pointers in global variables for example). Also, note there exists
        [`get_data_refs_from`](#binaryninja.binaryview.BinaryView.get_data_refs_from
        "binaryninja.binaryview.BinaryView.get_data_refs_from").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

        Example:
        :   ```
            >>> bv.get_data_refs(here)
            [4203812]
            >>>
            ```

    get_data_refs_for_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_refs_for_type)
    :   `get_data_refs_for_type` returns a list of virtual addresses of data which references
        the type `name`. Note, the returned addresses are the actual start of the queried type.
        For example, suppose there is a DataVariable at 0x1000 that has type A, and type A
        contains type B at offset 0x10. Then get_data_refs_for_type(‘B’) will return 0x1010 for
        it.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

        Example:
        :   ```
            >>> bv.get_data_refs_for_type('A')
            [4203812]
            >>>
            ```

    get_data_refs_for_type_field(*name: _types.QualifiedNameType*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_refs_for_type_field)
    :   `get_data_refs_for_type_field` returns a list of virtual addresses of data which
        references the type `name`. Note, the returned addresses are the actual start of the
        queried type field. For example, suppose there is a DataVariable at 0x1000 that has type
        A, and type A contains type B at offset 0x10. Then get_data_refs_for_type_field(‘B’,
        0x8) will return 0x1018 for it.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field, relative to the type
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

        Example:
        :   ```
            >>> bv.get_data_refs_for_type_field('A', 0x8)
            [4203812]
            >>>
            ```

    get_data_refs_from(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_refs_from)
    :   `get_data_refs_from` returns a list of virtual addresses referenced by the address
        `addr`. Optionally specifying a length. When `length` is set `get_data_refs_from`
        returns the data referenced in the range `addr`-``` addr``+``length ```. This function
        returns both autoanalysis (“auto”) and user-specified (“user”) xrefs. To add a
        user-specified reference, see
        [`add_user_data_ref`](#binaryninja.binaryview.BinaryView.add_user_data_ref
        "binaryninja.binaryview.BinaryView.add_user_data_ref"). Also, note there exists
        [`get_data_refs`](#binaryninja.binaryview.BinaryView.get_data_refs
        "binaryninja.binaryview.BinaryView.get_data_refs").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for references
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of query

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

        Example:
        :   ```
            >>> bv.get_data_refs_from(here)
            [4200327]
            >>>
            ```

    get_data_refs_from_for_type_field(*name: _types.QualifiedNameType*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_refs_from_for_type_field)
    :   `get_data_refs_from_for_type_field` returns a list of virtual addresses of data which
        are referenced by the type `name`.

        Only data referenced by structures with the `__data_var_refs` attribute are included.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field, relative to the type
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   list of integers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(integer)

        Example:
        :   ```
            >>> bv.get_data_refs_from_for_type_field('A', 0x8)
            [4203812]
            >>>
            ```

    get_data_var_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_var_at)
    :   `get_data_var_at` returns the data type at a given virtual address.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address to get the data type from

        Returns:
        :   returns the DataVariable at the given virtual address, None on error

        Return type:
        :   [*DataVariable*](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Example:
        :   ```
            >>> t = bv.parse_type_string("int foo")
            >>> bv.define_data_var(bv.entry_point, t[0])
            >>> bv.get_data_var_at(bv.entry_point)
            <var 0x100001174: int32_t>
            ```

    get_data_variable_parent_components(*data_variable: [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Component](component.md#binaryninja.component.Component "binaryninja.component.Component")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_data_variable_parent_components)
    :   Parameters:
        :   **data_variable** ([*DataVariable*](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component")]

    get_derived_string_code_refs(*str: [DerivedString](#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[ReferenceSource](#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_derived_string_code_refs)
    :   Parameters:
        :   - **str** ([*DerivedString*](#binaryninja.binaryview.DerivedString
              "binaryninja.binaryview.DerivedString")) –
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*ReferenceSource*](#binaryninja.binaryview.ReferenceSource
            "binaryninja.binaryview.ReferenceSource"), *None*, *None*]

    get_disassembly(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_disassembly)
    :   `get_disassembly` simple helper function for printing disassembly of a given address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of instruction
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – optional Architecture, `self.arch` is used
              if this parameter is None

        Returns:
        :   a str representation of the instruction at virtual address `addr` or None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") or
            *None*

        Example:
        :   ```
            >>> bv.get_disassembly(bv.entry_point)
            'push    ebp'
            >>>
            ```

        Note

        This API is very simplistic and only returns text. See
        [`disassembly_text`](#binaryninja.binaryview.BinaryView.disassembly_text
        "binaryninja.binaryview.BinaryView.disassembly_text") and instructions for more capable
        APIs.

    get_entropy(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *block_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_entropy)
    :   `get_entropy` returns the shannon entropy given the start `addr`, `length` in bytes, and
        optionally in `block_size` chunks.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – total length in bytes
            - **block_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional block size

        Returns:
        :   list of entropy values for each chunk

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*float*](https://docs.python.org/3/library/functions.html#float "(in Python
            v3.14)"))

    get_expression_parser_magic_value(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_expression_parser_magic_value)
    :   Get the value of an expression parser magic value

        If the queried magic value exists, the function returns true and the magic value is
        returned in value. If the queried magic value does not exist, the function returns None.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – name for the magic value to query

        Returns:

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            *None*

    get_external_libraries() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ExternalLibrary](externallibrary.md#binaryninja.externallibrary.ExternalLibrary "binaryninja.externallibrary.ExternalLibrary")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_external_libraries)
    :   Get a list of all ExternalLibrary in this BinaryView

        Returns:
        :   A list of ExternalLibraries in this BinaryView

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ExternalLibrary*](externallibrary.md#binaryninja.externallibrary.ExternalLibrary
            "binaryninja.externallibrary.ExternalLibrary")]

    get_external_library(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [ExternalLibrary](externallibrary.md#binaryninja.externallibrary.ExternalLibrary "binaryninja.externallibrary.ExternalLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_external_library)
    :   Get an ExternalLibrary in this BinaryView by name

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the external library

        Returns:
        :   An ExternalLibrary with the given name, or None

        Return type:
        :   [*ExternalLibrary*](externallibrary.md#binaryninja.externallibrary.ExternalLibrary
            "binaryninja.externallibrary.ExternalLibrary") | *None*

    get_external_location(*source_symbol: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [ExternalLocation](externallibrary.md#binaryninja.externallibrary.ExternalLocation "binaryninja.externallibrary.ExternalLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_external_location)
    :   Get the ExternalLocation with the given source symbol in this BinaryView

        Parameters:
        :   **source_symbol** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")) – The source symbol of the ExternalLocation

        Returns:
        :   An ExternalLocation with the given source symbol, or None

        Return type:
        :   [*ExternalLocation*](externallibrary.md#binaryninja.externallibrary.ExternalLocation
            "binaryninja.externallibrary.ExternalLocation") | *None*

    get_external_locations() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ExternalLocation](externallibrary.md#binaryninja.externallibrary.ExternalLocation "binaryninja.externallibrary.ExternalLocation")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_external_locations)
    :   Get a list of ExternalLocations in this BinaryView

        Returns:
        :   A list of ExternalLocations in this BinaryView

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ExternalLocation*](externallibrary.md#binaryninja.externallibrary.ExternalLocation
            "binaryninja.externallibrary.ExternalLocation")]

    get_function_analysis_update_disabled() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_function_analysis_update_disabled)
    :   Returns True when functions are prevented from being marked as updates required, False
        otherwise. :return:

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_function_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_function_at)
    :   `get_function_at` gets a Function object for the function that starts at virtual address
        `addr`:

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – starting virtual address of the desired function
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – platform of the desired function

        Returns:
        :   returns a Function object or None for the function at the virtual address provided

        Return type:
        :   [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")

        Example:
        :   ```
            >>> bv.get_function_at(bv.entry_point)
            <func: x86_64@0x100001174>
            >>>
            ```

    get_function_parent_components(*function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Component](component.md#binaryninja.component.Component "binaryninja.component.Component")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_function_parent_components)
    :   Parameters:
        :   **function** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component")]

    get_functions_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_functions_at)
    :   `get_functions_at` get a list of [`Function`](function.md#binaryninja.function.Function
        "binaryninja.function.Function") objects (one for each valid platform) that start at the
        given virtual address. Binary Ninja does not limit the number of platforms in a given
        file thus there may be multiple functions defined from different architectures at the
        same location. This API allows you to query all of valid platforms.

        You may also be interested in
        [`get_functions_containing`](#binaryninja.binaryview.BinaryView.get_functions_containing
        "binaryninja.binaryview.BinaryView.get_functions_containing") which is useful for
        requesting all function that contain a given address

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address of the desired Function object list.

        Returns:
        :   a list of [`Function`](function.md#binaryninja.function.Function
            "binaryninja.function.Function") objects defined at the provided virtual address

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function"))

    get_functions_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *ordered_filter: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SymbolType](enums.md#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_functions_by_name)
    :   `get_functions_by_name` returns a list of
        [`Function`](function.md#binaryninja.function.Function "binaryninja.function.Function")
        objects function with a [`Symbol`](types.md#binaryninja.types.Symbol
        "binaryninja.types.Symbol") of `name`.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the functions
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) – (optional) platform
            - **ordered_filter** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*(*[*SymbolType*](enums.md#binaryninja.enums.SymbolType
              "binaryninja.enums.SymbolType")*)*) – (optional) an ordered filter based on SymbolType

        Returns:
        :   returns a list of [`Function`](function.md#binaryninja.function.Function
            "binaryninja.function.Function") objects or an empty list

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function"))

        Example:
        :   ```
            >>> bv.get_functions_by_name("main")
            [<func: x86_64@0x1587>]
            >>>
            ```

    get_functions_containing(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_functions_containing)
    :   `get_functions_containing` returns a list of
        [`Function`](function.md#binaryninja.function.Function "binaryninja.function.Function")
        objects which contain the given address.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query.
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –

        Return type:
        :   list of [`Function`](function.md#binaryninja.function.Function
            "binaryninja.function.Function") objects

    get_incoming_direct_type_references(*name: _types.QualifiedNameType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedName][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_incoming_direct_type_references)
    :   Parameters:
        :   **name** (*_types.QualifiedNameType*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[_types.QualifiedName]

    get_incoming_recursive_type_references(*names: _types.QualifiedNameType | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedNameType]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedName][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_incoming_recursive_type_references)
    :   Parameters:
        :   **names** (*_types.QualifiedNameType* *|*
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")*[**_types.QualifiedNameType**]*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[_types.QualifiedName]

    get_instruction_length(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_instruction_length)
    :   `get_instruction_length` returns the number of bytes in the instruction of Architecture
        `arch` at the virtual address `addr`

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction query
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   Number of bytes in instruction

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> bv.get_instruction_length(0x100012f1)
            2L
            >>>
            ```

    get_linear_disassembly(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_linear_disassembly)
    :   `get_linear_disassembly` gets an iterator for all lines in the linear disassembly of the
        view for the given disassembly settings.

        Note

        - linear_disassembly doesn’t just return disassembly; it will return a single line from
          the linear view, and thus will contain both data views, and disassembly.
        - **Warning:** In order to get deterministic output, the WaitForIL DisassemblyOption
          should be set to True.

        Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings")) – instance specifying the desired output
            formatting. Defaults to None which will use default settings.

        Returns:
        :   An iterator containing formatted disassembly lines.

        Return type:
        :   LinearDisassemblyIterator

        Example:
        :   ```
            >>> settings = DisassemblySettings()
            >>> lines = bv.get_linear_disassembly(settings)
            >>> for line in lines:
            ...  print(line)
            ...  break
            ...
            cf fa ed fe 07 00 00 01  ........
            ```

    get_linear_disassembly_position_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LinearViewCursor](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_linear_disassembly_position_at)
    :   `get_linear_disassembly_position_at` instantiates a
        [`LinearViewCursor`](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor
        "binaryninja.lineardisassembly.LinearViewCursor") object for use in
        [`get_previous_linear_disassembly_lines`](#binaryninja.binaryview.BinaryView.get_previous_linear_disassembly_lines
        "binaryninja.binaryview.BinaryView.get_previous_linear_disassembly_lines") or
        [`get_next_linear_disassembly_lines`](#binaryninja.binaryview.BinaryView.get_next_linear_disassembly_lines
        "binaryninja.binaryview.BinaryView.get_next_linear_disassembly_lines").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of linear disassembly position
            - **settings**
              ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings")) – an instantiated
              [`DisassemblySettings`](function.md#binaryninja.function.DisassemblySettings
              "binaryninja.function.DisassemblySettings") object, defaults to None which will use
              default settings

        Returns:
        :   An instantiated
            [`LinearViewCursor`](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor
            "binaryninja.lineardisassembly.LinearViewCursor") object for the provided virtual
            address

        Return type:
        :   [*LinearViewCursor*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor
            "binaryninja.lineardisassembly.LinearViewCursor")

        Example:
        :   ```
            >>> settings = DisassemblySettings()
            >>> pos = bv.get_linear_disassembly_position_at(0x1000149f, settings)
            >>> lines = bv.get_previous_linear_disassembly_lines(pos)
            >>> lines
            [<0x1000149a: pop     esi>, <0x1000149b: pop     ebp>,
            <0x1000149c: retn    0xc>, <0x1000149f: >]
            ```

    get_load_settings(*type_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_load_settings)
    :   `get_load_settings` retrieve a [`Settings`](settings.md#binaryninja.settings.Settings
        "binaryninja.settings.Settings") object which defines the load settings for the given
        [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
        "binaryninja.binaryview.BinaryViewType") `type_name`

        Parameters:
        :   **type_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – the [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
            "binaryninja.binaryview.BinaryViewType") name

        Returns:
        :   the load settings

        Return type:
        :   [`Settings`](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings"),
            or `None`

    get_load_settings_type_names() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_load_settings_type_names)
    :   `get_load_settings_type_names` retrieve a list
        [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
        "binaryninja.binaryview.BinaryViewType") names for which load settings exist in this
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
        context

        Returns:
        :   list of [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
            "binaryninja.binaryview.BinaryViewType") names

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

    get_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → metadata.MetadataValueType | Any[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_metadata)
    :   get_metadata retrieves a metadata value associated with the given key stored in the
        current BinaryView.

        This method behaves like dict.get():

        - If the key exists, its metadata value is returned.
        - If the key does not exist and default is not provided, None is returned.
        - If the key does not exist and default is provided, default is returned.

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – key to query
            - **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")) – value to return if the key does not exist (defaults to None)

        Return type:
        :   metadata associated with the key or the default value

        Example:
        :   ```
            >>> bv.store_metadata("integer", 1337)
            >>> bv.get_metadata("integer")
            1337L
            >>> bv.get_metadata("missing")
            None
            >>> bv.get_metadata("missing", 42)
            42
            ```

    get_modification(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ModificationStatus](enums.md#binaryninja.enums.ModificationStatus "binaryninja.enums.ModificationStatus")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_modification)
    :   `get_modification` returns the modified bytes of up to `length` bytes from virtual
        address `addr`, or if `length` is None returns the ModificationStatus.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to get modification from
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length of modification

        Returns:
        :   List of ModificationStatus values for each byte in range

        Return type:
        :   *List*[[*ModificationStatus*](enums.md#binaryninja.enums.ModificationStatus
            "binaryninja.enums.ModificationStatus")]

    get_next_basic_block_start_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_basic_block_start_after)
    :   `get_next_basic_block_start_after` returns the virtual address of the BasicBlock that occurs after the virtual
        :   address `addr`

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the next BasicBlock

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.get_next_basic_block_start_after(bv.entry_point))
            '0x100014a8L'
            >>> hex(bv.get_next_basic_block_start_after(0x100014a8))
            '0x100014adL'
            >>>
            ```

    get_next_data_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_data_after)
    :   `get_next_data_after` retrieves the virtual address of the next non-code byte.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the next data byte which is data, not code

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.get_next_data_after(0x10000000))
            '0x10000001L'
            ```

    get_next_data_var_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_data_var_after)
    :   `get_next_data_var_after` retrieves the next
        [`DataVariable`](#binaryninja.binaryview.DataVariable
        "binaryninja.binaryview.DataVariable"), or None.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the next [`DataVariable`](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Return type:
        :   [*DataVariable*](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Example:
        :   ```
            >>> bv.get_next_data_var_after(0x10000000)
            <var 0x1000003c: int32_t>
            >>>
            ```

    get_next_data_var_start_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_data_var_start_after)
    :   `get_next_data_var_start_after` retrieves the next virtual address of the next
        [`DataVariable`](#binaryninja.binaryview.DataVariable
        "binaryninja.binaryview.DataVariable")

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the next [`DataVariable`](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.get_next_data_var_start_after(0x10000000))
            '0x1000003cL'
            >>> bv.get_data_var_at(0x1000003c)
            <var 0x1000003c: int32_t>
            >>>
            ```

    get_next_function_start_after(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_function_start_after)
    :   `get_next_function_start_after` returns the virtual address of the Function that occurs
        after the virtual address `addr`

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the next Function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_next_function_start_after(bv.entry_point)
            268441061L
            >>> hex(bv.get_next_function_start_after(bv.entry_point))
            '0x100015e5L'
            >>> hex(bv.get_next_function_start_after(0x100015e5))
            '0x10001629L'
            >>> hex(bv.get_next_function_start_after(0x10001629))
            '0x1000165eL'
            >>>
            ```

    get_next_linear_disassembly_lines(*pos: [LinearViewCursor](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_linear_disassembly_lines)
    :   `get_next_linear_disassembly_lines` retrieves a list of
        [`LinearDisassemblyLine`](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
        "binaryninja.lineardisassembly.LinearDisassemblyLine") objects for the next disassembly
        lines, and updates the LinearViewCursor passed in. This function can be called
        repeatedly to get more lines of linear disassembly.

        Parameters:
        :   **pos**
            ([*LinearViewCursor*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor
            "binaryninja.lineardisassembly.LinearViewCursor")) – Position to start retrieving linear
            disassembly lines from

        Returns:
        :   a list of
            [`LinearDisassemblyLine`](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine") objects for the next lines.

        Example:
        :   ```
            >>> settings = DisassemblySettings()
            >>> pos = bv.get_linear_disassembly_position_at(0x10001483, settings)
            >>> bv.get_next_linear_disassembly_lines(pos)
            [<0x10001483: xor     eax, eax  {0x0}>, <0x10001485: inc     eax  {0x1}>, ... , <0x10001488: >]
            >>> bv.get_next_linear_disassembly_lines(pos)
            [<0x10001488: push    dword [ebp+0x10 {arg_c}]>, ... , <0x1000149a: >]
            >>>
            ```

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine")]

    get_next_valid_offset(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_next_valid_offset)
    :   `get_next_valid_offset` returns the next valid offset in the BinaryView starting from
        the given virtual address `addr`.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to start checking from.

        Returns:
        :   The minimum of the next valid offset in the BinaryView and the end address of the
            BinaryView

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_outgoing_direct_type_references(*name: _types.QualifiedNameType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedName][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_outgoing_direct_type_references)
    :   Parameters:
        :   **name** (*_types.QualifiedNameType*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[_types.QualifiedName]

    get_outgoing_recursive_type_references(*names: _types.QualifiedNameType | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedNameType]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedName][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_outgoing_recursive_type_references)
    :   Parameters:
        :   **names** (*_types.QualifiedNameType* *|*
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")*[**_types.QualifiedNameType**]*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[_types.QualifiedName]

    get_previous_basic_block_end_before(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_basic_block_end_before)
    :   `get_previous_basic_block_end_before`

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the previous BasicBlock end

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.entry_point)
            '0x1000149fL'
            >>> hex(bv.get_next_basic_block_start_after(bv.entry_point))
            '0x100014a8L'
            >>> hex(bv.get_previous_basic_block_end_before(0x100014a8))
            '0x100014a8L'
            ```

    get_previous_basic_block_start_before(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_basic_block_start_before)
    :   `get_previous_basic_block_start_before` returns the virtual address of the BasicBlock
        that occurs prior to the provided virtual address

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the previous BasicBlock

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.entry_point)
            '0x1000149fL'
            >>> hex(bv.get_next_basic_block_start_after(bv.entry_point))
            '0x100014a8L'
            >>> hex(bv.get_previous_basic_block_start_before(0x100014a8))
            '0x1000149fL'
            >>>
            ```

    get_previous_data_before(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_data_before)
    :   `get_previous_data_before`

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the previous data (non-code) byte

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.get_previous_data_before(0x1000001))
            '0x1000000L'
            >>>
            ```

    get_previous_data_var_before(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_data_var_before)
    :   `get_previous_data_var_before` retrieves the previous
        [`DataVariable`](#binaryninja.binaryview.DataVariable
        "binaryninja.binaryview.DataVariable"), or None.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the previous [`DataVariable`](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Return type:
        :   [*DataVariable*](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Example:
        :   ```
            >>> bv.get_previous_data_var_before(0x1000003c)
            <var 0x10000000: int16_t>
            >>>
            ```

    get_previous_data_var_start_before(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_data_var_start_before)
    :   `get_previous_data_var_start_before`

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the previous
            [`DataVariable`](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.get_previous_data_var_start_before(0x1000003c))
            '0x10000000L'
            >>> bv.get_data_var_at(0x10000000)
            <var 0x10000000: int16_t>
            >>>
            ```

    get_previous_function_start_before(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_function_start_before)
    :   `get_previous_function_start_before` returns the virtual address of the Function that
        occurs prior to the virtual address provided

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – the virtual address to start looking from.

        Returns:
        :   the virtual address of the previous Function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> hex(bv.entry_point)
            '0x1000149fL'
            >>> hex(bv.get_next_function_start_after(bv.entry_point))
            '0x100015e5L'
            >>> hex(bv.get_previous_function_start_before(0x100015e5))
            '0x1000149fL'
            >>>
            ```

    get_previous_linear_disassembly_lines(*pos: [LinearViewCursor](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor "binaryninja.lineardisassembly.LinearViewCursor")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_previous_linear_disassembly_lines)
    :   `get_previous_linear_disassembly_lines` retrieves a list of
        [`LinearDisassemblyLine`](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
        "binaryninja.lineardisassembly.LinearDisassemblyLine") objects for the previous
        disassembly lines, and updates the LinearViewCursor passed in. This function can be
        called repeatedly to get more lines of linear disassembly.

        Parameters:
        :   **pos**
            ([*LinearViewCursor*](lineardisassembly.md#binaryninja.lineardisassembly.LinearViewCursor
            "binaryninja.lineardisassembly.LinearViewCursor")) – Position to start retrieving linear
            disassembly lines from

        Returns:
        :   a list of
            [`LinearDisassemblyLine`](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine") objects for the previous lines.

        Example:
        :   ```
            >>> settings = DisassemblySettings()
            >>> pos = bv.get_linear_disassembly_position_at(0x1000149a, settings)
            >>> bv.get_previous_linear_disassembly_lines(pos)
            [<0x10001488: push    dword [ebp+0x10 {arg_c}]>, ... , <0x1000149a: >]
            >>> bv.get_previous_linear_disassembly_lines(pos)
            [<0x10001483: xor     eax, eax  {0x0}>, ... , <0x10001488: >]
            ```

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LinearDisassemblyLine*](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine
            "binaryninja.lineardisassembly.LinearDisassemblyLine")]

    get_recent_basic_block_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_recent_basic_block_at)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*BasicBlock*](basicblock.md#binaryninja.basicblock.BasicBlock
            "binaryninja.basicblock.BasicBlock") | *None*

    get_recent_function_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_recent_function_at)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
            | *None*

    get_section_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Section](#binaryninja.binaryview.Section "binaryninja.binaryview.Section") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_section_by_name)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*Section*](#binaryninja.binaryview.Section "binaryninja.binaryview.Section") | *None*

    get_sections_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Section](#binaryninja.binaryview.Section "binaryninja.binaryview.Section")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_sections_at)
    :   Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Section*](#binaryninja.binaryview.Section "binaryninja.binaryview.Section")]

    get_segment_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Segment](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_segment_at)
    :   `get_segment_at` gets the Segment a given virtual address is located in

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – A virtual address

        Returns:
        :   The segment, if it was found

        Return type:
        :   [*Segment*](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment") | *None*

    get_sizes_referenced(*name: _types.QualifiedNameType*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_sizes_referenced)
    :   `get_sizes_referenced` returns a list of access sizes to the specified type.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field

        Returns:
        :   a list of sizes of the accesses to it.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_sizes_referenced('B', 16)
            [1, 8]
            >>>
            ```

    get_string_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *partial: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [StringReference](#binaryninja.binaryview.StringReference "binaryninja.binaryview.StringReference") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_string_at)
    :   `get_string_at` returns the string that falls on given virtual address.

        Note

        This returns discovered strings and is therefore governed by
        analysis.limits.minStringLength and other settings. For an alternative API that simply
        returns any potential c-string at a given location, use
        [`get_ascii_string_at`](#binaryninja.binaryview.BinaryView.get_ascii_string_at
        "binaryninja.binaryview.BinaryView.get_ascii_string_at").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to get the string from
            - **partial** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – whether to return a partial string reference or not

        Returns:
        :   returns the StringReference at the given virtual address, otherwise None.

        Return type:
        :   [*StringReference*](#binaryninja.binaryview.StringReference
            "binaryninja.binaryview.StringReference")

        Example:
        :   ```
            >>> bv.get_string_at(0x40302f)
            <StringType.AsciiString: 0x403028, len 0x12>
            ```

    get_strings(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StringReference](#binaryninja.binaryview.StringReference "binaryninja.binaryview.StringReference")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_strings)
    :   `get_strings` returns a list of strings defined in the binary in the optional virtual
        address range: `start-(start+length)`

        Note that this API will only return strings that have been identified by the
        string-analysis and thus governed by the minimum and maximum length settings and
        unrelated to the type system.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional virtual address to start the string list from, defaults to start of
              the binary
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional length range to return strings from, defaults to length of the
              binary

        Returns:
        :   a list of all strings or a list of strings defined between `start` and `start+length`

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*StringReference*](#binaryninja.binaryview.StringReference
            "binaryninja.binaryview.StringReference"))

        Example:
        :   ```
            >>> bv.get_strings(0x1000004d, 1)
            [<AsciiString: 0x1000004d, len 0x2c>]
            >>>
            ```

    get_symbol_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *namespace: _types.NameSpaceType = None*) → _types.CoreSymbol | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_symbol_at)
    :   `get_symbol_at` returns the Symbol at the provided virtual address.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to query for symbol
            - **namespace** (*_types.NameSpaceType*) – (optional) the namespace of the symbols to
              retrieve

        Returns:
        :   CoreSymbol for the given virtual address

        Return type:
        :   [*CoreSymbol*](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")

        Example:
        :   ```
            >>> bv.get_symbol_at(bv.entry_point)
            <FunctionSymbol: "_start" @ 0x100001174>
            >>>
            ```

    get_symbol_by_raw_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *namespace: _types.NameSpaceType = None*) → _types.CoreSymbol | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_symbol_by_raw_name)
    :   `get_symbol_by_raw_name` retrieves a Symbol object for the given raw (mangled) name.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – raw (mangled) name of Symbol to be retrieved
            - **namespace** (*_types.NameSpaceType*) – (optional) the namespace to search for the
              given symbol

        Returns:
        :   CoreSymbol object corresponding to the provided raw name

        Return type:
        :   [*CoreSymbol*](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")

        Example:
        :   ```
            >>> bv.get_symbol_by_raw_name('?testf@Foobar@@SA?AW4foo@1@W421@@Z')
            <FunctionSymbol: "public: static enum Foobar::foo __cdecl Foobar::testf(enum Foobar::foo)" @ 0x10001100>
            >>>
            ```

    get_symbols(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *namespace: _types.NameSpaceType = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.CoreSymbol][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_symbols)
    :   `get_symbols` retrieves the list of all Symbol objects in the optionally provided range.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) – optional start virtual address
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) – optional length
            - **namespace** (*_types.NameSpaceType*) –

        Returns:
        :   list of all Symbol objects, or those Symbol objects in the range of
            `start`-`start+length`

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Symbol*](types.md#binaryninja.types.Symbol "binaryninja.types.Symbol"))

        Example:
        :   ```
            >>> bv.get_symbols(0x1000200c, 1)
            [<ImportAddressSymbol: "KERNEL32!IsProcessorFeaturePresent" @ 0x1000200c>]
            >>>
            ```

    get_symbols_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *namespace: _types.NameSpaceType = None*, *ordered_filter: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SymbolType](enums.md#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.CoreSymbol][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_symbols_by_name)
    :   `get_symbols_by_name` retrieves a list of Symbol objects for the given symbol name and
        ordered filter

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of Symbol object to be retrieved
            - **namespace** (*_types.NameSpaceType*) – (optional) the namespace to search for the
              given symbol
            - **namespace** – (optional) the namespace to search for the given symbol
            - **ordered_filter** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*SymbolType*](enums.md#binaryninja.enums.SymbolType
              "binaryninja.enums.SymbolType")*]* *|* *None*) – (optional) an ordered filter based on
              SymbolType

        Returns:
        :   Symbol object corresponding to the provided name

        Return type:
        :   [*Symbol*](types.md#binaryninja.types.Symbol "binaryninja.types.Symbol")

        Example:
        :   ```
            >>> bv.get_symbols_by_name('?testf@Foobar@@SA?AW4foo@1@W421@@Z')
            [<FunctionSymbol: "public: static enum Foobar::foo __cdecl Foobar::testf(enum Foobar::foo)" @ 0x10001100>]
            >>>
            ```

    get_symbols_by_raw_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *namespace: _types.NameSpaceType = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.CoreSymbol][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_symbols_by_raw_name)
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **namespace** (*_types.NameSpaceType*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[_types.CoreSymbol]

    get_symbols_of_type(*sym_type: [SymbolType](enums.md#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *namespace: _types.NameSpaceType = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.CoreSymbol][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_symbols_of_type)
    :   `get_symbols_of_type` retrieves a list of all [`Symbol`](types.md#binaryninja.types.Symbol "binaryninja.types.Symbol") objects of the provided symbol type in the optionally
        :   provided range.

        Parameters:
        :   - **sym_type** ([*SymbolType*](enums.md#binaryninja.enums.SymbolType
              "binaryninja.enums.SymbolType")) – A Symbol type:
              [`SymbolType`](enums.md#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType")
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) – optional start virtual address
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) – optional length
            - **namespace** (*_types.NameSpaceType*) –

        Returns:
        :   list of all [`Symbol`](types.md#binaryninja.types.Symbol "binaryninja.types.Symbol")
            objects of type `sym_type`, or those [`Symbol`](types.md#binaryninja.types.Symbol
            "binaryninja.types.Symbol") objects in the range of `start`-`start+length`

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol"))

        Example:
        :   ```
            >>> bv.get_symbols_of_type(SymbolType.ImportAddressSymbol, 0x10002028, 1)
            [<ImportAddressSymbol: "KERNEL32!GetCurrentThreadId" @ 0x10002028>]
            >>>
            ```

    get_system_call_name(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_system_call_name)
    :   Parameters:
        :   - **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_system_call_type(*id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_system_call_type)
    :   Parameters:
        :   - **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) –

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") | *None*

    get_tag_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_tag_type)
    :   Get a tag type by its name.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the tag type

        Returns:
        :   The relevant tag type, if it exists

        Return type:
        :   [*TagType*](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")

    get_tags(*auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_tags)
    :   `tags` gets a list of all data [`Tag`](#binaryninja.binaryview.Tag
        "binaryninja.binaryview.Tag") objects in the view. Tags are returned as a list of
        (address, [`Tag`](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) pairs.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))

        Parameters:
        :   **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)") *|* *None*) –

    get_tags_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_tags_at)
    :   `get_data_tags_at` gets a list of [`Tag`](#binaryninja.binaryview.Tag
        "binaryninja.binaryview.Tag") objects for a data address.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address to get tags at
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If None, gets all tags, if True, gets auto tags, if False, gets user tags

        Returns:
        :   A list of data [`Tag`](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag") objects

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))

    get_tags_in_range(*address_range: [AddressRange](variable.md#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange")*, *auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_tags_in_range)
    :   `get_data_tags_in_range` gets a list of all data [`Tag`](#binaryninja.binaryview.Tag
        "binaryninja.binaryview.Tag") objects in a given range. Range is inclusive at the start,
        exclusive at the end.

        Parameters:
        :   - **address_range** ([*AddressRange*](variable.md#binaryninja.variable.AddressRange
              "binaryninja.variable.AddressRange")) – address range from which to get tags
            - **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If None, gets all tags, if True, gets auto tags, if False, gets auto tags

        Returns:
        :   A list of (address, data tag) tuples

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")))

    get_type_archive(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_archive)
    :   Look up a connected archive by its id

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of archive

        Returns:
        :   Archive, if one exists with that id. Otherwise None

        Return type:
        :   [*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive") | *None*

    get_type_archive_path(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_archive_path)
    :   Look up the path for an attached (but not necessarily connected) type archive by its id

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Id of archive

        Returns:
        :   Archive path, if it is attached. Otherwise None.

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_type_archives_for_type_name(*name: _types.QualifiedNameType*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_archives_for_type_name)
    :   Get a list of all connected type archives that have a given type name

        Returns:
        :   (archive, archive type id) for all archives

        Parameters:
        :   **name** (*_types.QualifiedNameType*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
            "binaryninja.typearchive.TypeArchive"),
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]

    get_type_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_by_id)
    :   `get_type_by_id` returns the defined type whose unique identifier corresponds with the
        provided `id`

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Unique identifier to lookup

        Returns:
        :   A `Type` or None if the type does not exist

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") or *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> type_id = Type.generate_auto_type_id("source", name)
            >>> bv.define_type(type_id, name, type)
            >>> bv.get_type_by_id(type_id)
            <type: int32_t>
            >>>
            ```

    get_type_by_name(*name: _types.QualifiedNameType*) → _types.Type | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_by_name)
    :   `get_type_by_name` returns the defined type whose name corresponds with the provided
        `name`

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – Type name to lookup

        Returns:
        :   A `Type` or None if the type does not exist

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") or *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> bv.define_user_type(name, type)
            >>> bv.get_type_by_name(name)
            <type: int32_t>
            >>>
            ```

    get_type_id(*name: _types.QualifiedNameType*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_id)
    :   `get_type_id` returns the unique identifier of the defined type whose name corresponds
        with the provided `name`

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – Type name to lookup

        Returns:
        :   The unique identifier of the type

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> type_id = Type.generate_auto_type_id("source", name)
            >>> registered_name = bv.define_type(type_id, name, type)
            >>> bv.get_type_id(registered_name) == type_id
            True
            >>>
            ```

    get_type_library(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_library)
    :   `get_type_library` returns the TypeLibrary

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Library name to lookup

        Returns:
        :   The Type Library object, if any

        Return type:
        :   [*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary") or *None*

        Example:

    get_type_name_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_name_by_id)
    :   `get_type_name_by_id` returns the defined type name whose unique identifier corresponds
        with the provided `id`

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Unique identifier to lookup

        Returns:
        :   A QualifiedName or None if the type does not exist

        Return type:
        :   [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName") or *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> type_id = Type.generate_auto_type_id("source", name)
            >>> bv.define_type(type_id, name, type)
            'foo'
            >>> bv.get_type_name_by_id(type_id)
            'foo'
            >>>
            ```

    get_type_refs_for_type(*name: _types.QualifiedNameType*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.TypeReferenceSource][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_refs_for_type)
    :   `get_type_refs_for_type` returns a list of TypeReferenceSource objects (xrefs or
        cross-references) that reference the provided QualifiedName.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   List of references for the given type

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*TypeReferenceSource*](types.md#binaryninja.types.TypeReferenceSource
            "binaryninja.types.TypeReferenceSource"))

        Example:
        :   ```
            >>> bv.get_type_refs_for_type('A')
            ['<type D, offset 0x8, direct>', '<type C, offset 0x10, indirect>']
            >>>
            ```

    get_type_refs_for_type_field(*name: _types.QualifiedNameType*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *max_items: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.TypeReferenceSource][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_type_refs_for_type_field)
    :   `get_type_refs_for_type` returns a list of TypeReferenceSource objects (xrefs or
        cross-references) that reference the provided type field.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field, relative to the type
            - **max_items** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – optional maximum number of references to fetch

        Returns:
        :   List of references for the given type

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*TypeReferenceSource*](types.md#binaryninja.types.TypeReferenceSource
            "binaryninja.types.TypeReferenceSource"))

        Example:
        :   ```
            >>> bv.get_type_refs_for_type_field('A', 0x8)
            ['<type D, offset 0x8, direct>', '<type C, offset 0x10, indirect>']
            >>>
            ```

    get_types_referenced(*name: [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_types_referenced)
    :   `get_types_referenced` returns a list of types related to the type field access.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – name of type to query for references
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of the field

        Returns:
        :   a list of types related to the type field access.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_types_referenced('B', 0x10)
            [<type: bool>, <type: char, 0% confidence>]
            >>>
            ```

    get_unique_section_names(*name_list: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_unique_section_names)
    :   Parameters:
        :   **name_list** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_view_of_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.get_view_of_type)
    :   `get_view_of_type` returns the BinaryView associated with the provided name if it
        exists.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the view to be retrieved

        Returns:
        :   BinaryView object associated with the provided name or None on failure

        Return type:
        :   [*BinaryView*](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
            or *None*

    has_initial_analysis() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.has_initial_analysis)
    :   `has_initial_analysis` check for the presence of an initial analysis in this BinaryView.

        Returns:
        :   True if the BinaryView has a valid initial analysis, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    hlil_functions(*preload_limit: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function_generator: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.hlil_functions)
    :   Generates a list of il functions. This method should be used instead of ‘functions’
        property if HLIL is needed and performance is a concern.

        Parameters:
        :   - **preload_limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*) –
            - **function_generator**
              ([*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in
              Python v3.14)")*[*[*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")*,* *None**,* *None**]* *|* *None*) –

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*HighLevelILFunction*](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction
            "binaryninja.highlevelil.HighLevelILFunction"), *None*, *None*]

    import_library_object(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *lib: [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary"), [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.import_library_object)
    :   `import_library_object` recursively imports an object from the specified type library,
        or, if no library was explicitly provided, the first type library associated with the
        current [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView") that provides the name requested.

        This may have the impact of loading other type libraries as dependencies on other type
        libraries are lazily resolved when references to types provided by them are first
        encountered.

        Note

        If you are implementing a custom BinaryView and use this method to import object types,
        you should then call `record_imported_object` with the details of where the object is
        located.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **lib** ([*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) –

        Returns:
        :   the object type, with any interior NamedTypeReferences renamed as necessary to be
            appropriate for the current view

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")

    import_library_type(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *lib: [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.import_library_type)
    :   `import_library_type` recursively imports a type from the specified type library, or, if
        no library was explicitly provided, the first type library associated with the current
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
        that provides the name requested.

        This may have the impact of loading other type libraries as dependencies on other type
        libraries are lazily resolved when references to types provided by them are first
        encountered.

        Note that the name actually inserted into the view may not match the name as it exists
        in the type library in the event of a name conflict. To aid in this, the `Type` object
        returned is a NamedTypeReference to the deconflicted name used.

        Parameters:
        :   - **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) –
            - **lib** ([*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) –

        Returns:
        :   a NamedTypeReference to the type, taking into account any renaming performed

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")

    import_type_by_guid(*guid: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.import_type_by_guid)
    :   `import_type_by_guid` recursively imports a type interface given its GUID.

        Note

        To support this type of lookup a type library must have contain a metadata key called
        “type_guids” which is a map Dict[string_guid, string_type_name] or Dict[string_guid,
        Tuple[string_type_name, type_library_name]]

        Parameters:
        :   **guid** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – GUID of the COM interface to import

        Returns:
        :   the object type, with any interior NamedTypeReferences renamed as necessary to be
            appropriate for the current view

        Return type:
        :   [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")

    init() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.init)
    :   Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    insert(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.insert)
    :   `insert` inserts the bytes in `data` to the virtual address `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to write to.
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – data to be inserted at addr.

        Returns:
        :   number of bytes inserted to virtual address `addr`

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.insert(0,"BBBB")
            4
            >>> bv.read(0,8)
            'BBBBAAAA'
            ```

    *static* internal_namespace() → [NameSpace](types.md#binaryninja.types.NameSpace "binaryninja.types.NameSpace")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.internal_namespace)
    :   Internal namespace for the current BinaryView

        Return type:
        :   [*NameSpace*](types.md#binaryninja.types.NameSpace "binaryninja.types.NameSpace")

    invert_branch(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.invert_branch)
    :   `invert_branch` convert the branch instruction of architecture `arch` at the virtual
        address `addr` to the inverse branch.

        Note

        This API performs a binary patch, analysis may need to be updated afterward.
        Additionally the binary file must be saved in order to preserve the changes made.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be modified
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x1000130e)
            'je      0x10001317'
            >>> bv.invert_branch(0x1000130e)
            True
            >>>
            >>> bv.get_disassembly(0x1000130e)
            'jne     0x10001317'
            >>>
            ```

    is_always_branch_patch_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_always_branch_patch_available)
    :   `is_always_branch_patch_available` queries the architecture plugin to determine if the
        instruction at `addr` can be made to **always branch**. The actual logic of which is
        implemented in the `perform_is_always_branch_patch_available` in the corresponding
        architecture.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture for the current
              view

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012ed)
            'test    eax, eax'
            >>> bv.is_always_branch_patch_available(0x100012ed)
            False
            >>> bv.get_disassembly(0x100012ef)
            'jg      0x100012f5'
            >>> bv.is_always_branch_patch_available(0x100012ef)
            True
            >>>
            ```

    is_invert_branch_patch_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_invert_branch_patch_available)
    :   `is_invert_branch_patch_available` queries the architecture plugin to determine if the
        instruction at `addr` is a branch that can be inverted. The actual logic of which is
        implemented in the `perform_is_invert_branch_patch_available` in the corresponding
        architecture.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012ed)
            'test    eax, eax'
            >>> bv.is_invert_branch_patch_available(0x100012ed)
            False
            >>> bv.get_disassembly(0x100012ef)
            'jg      0x100012f5'
            >>> bv.is_invert_branch_patch_available(0x100012ef)
            True
            >>>
            ```

    is_never_branch_patch_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_never_branch_patch_available)
    :   `is_never_branch_patch_available` queries the architecture plugin to determine if the
        instruction at the instruction at `addr` can be made to **never branch**. The actual
        logic of which is implemented in the `perform_is_never_branch_patch_available` in the
        corresponding architecture.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012ed)
            'test    eax, eax'
            >>> bv.is_never_branch_patch_available(0x100012ed)
            False
            >>> bv.get_disassembly(0x100012ef)
            'jg      0x100012f5'
            >>> bv.is_never_branch_patch_available(0x100012ef)
            True
            >>>
            ```

    is_offset_backed_by_file(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_backed_by_file)
    :   `is_offset_backed_by_file` checks if a virtual address `addr` is backed by the original
        file.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is backed by original file, False if the not backed by
            original file or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_code_semantics(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_code_semantics)
    :   `is_offset_code_semantics` checks if a virtual address `addr` is semantically valid for
        code.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is valid for code semantics, False if the virtual address is
            invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_executable(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_executable)
    :   `is_offset_executable` checks if a virtual address `addr` is valid for executing.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is valid for executing, False if the virtual address is
            invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_extern_semantics(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_extern_semantics)
    :   `is_offset_extern_semantics` checks if a virtual address `addr` is semantically valid
        for external references.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   true if the virtual address is valid for external references, false if the virtual
            address is invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_readable(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_readable)
    :   `is_offset_readable` checks if a virtual address `addr` is valid for reading.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is valid for reading, False if the virtual address is
            invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_readonly_semantics(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_readonly_semantics)
    :   `is_offset_readonly_semantics` checks if a virtual address `addr` is semantically
        read-only. This considers both section semantics and segment permissions to determine if
        an address should be treated as read-only for analysis purposes.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is semantically read-only, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_writable(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_writable)
    :   `is_offset_writable` checks if a virtual address `addr` is valid for writing.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is valid for writing, False if the virtual address is
            invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_offset_writable_semantics(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_offset_writable_semantics)
    :   `is_offset_writable_semantics` checks if a virtual address `addr` is semantically
        writable. Some sections may have writable permissions for linking purposes but can be
        treated as read-only for the purposes of analysis.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is valid for writing, False if the virtual address is
            invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_skip_and_return_value_patch_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_skip_and_return_value_patch_available)
    :   `is_skip_and_return_value_patch_available` queries the architecture plugin to determine
        if the instruction at `addr` is similar to an x86 “call” instruction which can be made
        to return a value. The actual logic of which is implemented in the
        `perform_is_skip_and_return_value_patch_available` in the corresponding architecture.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f6)
            'mov     dword [0x10003020], eax'
            >>> bv.is_skip_and_return_value_patch_available(0x100012f6)
            False
            >>> bv.get_disassembly(0x100012fb)
            'call    0x10001629'
            >>> bv.is_skip_and_return_value_patch_available(0x100012fb)
            True
            >>>
            ```

    is_skip_and_return_zero_patch_available(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_skip_and_return_zero_patch_available)
    :   `is_skip_and_return_zero_patch_available` queries the architecture plugin to determine
        if the instruction at `addr` is similar to an x86 “call” instruction which can be made
        to return zero. The actual logic of which is implemented in the
        `perform_is_skip_and_return_zero_patch_available` in the corresponding architecture.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the virtual address of the instruction to be patched
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True if the instruction can be patched, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f6)
            'mov     dword [0x10003020], eax'
            >>> bv.is_skip_and_return_zero_patch_available(0x100012f6)
            False
            >>> bv.get_disassembly(0x100012fb)
            'call    0x10001629'
            >>> bv.is_skip_and_return_zero_patch_available(0x100012fb)
            True
            >>>
            ```

    is_type_auto_defined(*name: _types.QualifiedNameType*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_type_auto_defined)
    :   `is_type_auto_defined` queries the user type list of name. If name is not in the *user*
        type list then the name is considered an *auto* type.

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – Name of type to query

        Returns:
        :   True if the type is not a *user* type. False if the type is a *user* type.

        Example:
        :   ```
            >>> bv.is_type_auto_defined("foo")
            True
            >>> bv.define_user_type("foo", bv.parse_type_string("struct {int x,y;}")[0])
            >>> bv.is_type_auto_defined("foo")
            False
            >>>
            ```

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_valid_offset(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.is_valid_offset)
    :   `is_valid_offset` checks if a virtual address `addr` is valid.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   True if the virtual address is valid, False if the virtual address is invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *static* load(*source: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python v3.14)") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")*, *update_analysis: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *options: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] = {}*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.load)
    :   `load` opens, generates default load options (which are overridable), and returns the
        first available [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView"). If no
        [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
        "binaryninja.binaryview.BinaryViewType") is available, then a `Mapped`
        [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
        "binaryninja.binaryview.BinaryViewType") is used to load the
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
        with the specified load options. The `Mapped` view type attempts to auto-detect the
        architecture of the file during initialization. If no architecture is detected or
        specified in the load options, then the `Mapped` view type fails to initialize and
        returns `None`.

        Note

        Container file support enables automatic extraction from container formats such as
        Universal (Fat) Mach-O archives. The architecture preference for Universal archives can
        be controlled with the **‘files.universal.architecturePreference’** setting. When set,
        the first matching architecture is automatically selected for loading. When unset,
        headless operation defaults to the first available architecture, while interactive
        operation presents all available architectures for selection. This setting is scoped to
        SettingsUserScope and can be modified as follows

        ```
        >>> Settings().set_string_list("files.universal.architecturePreference", ["arm64"])
        ```

        It’s also possible to specify the architecture preference directly with
        [`load`](#binaryninja.binaryview.BinaryView.load
        "binaryninja.binaryview.BinaryView.load")

        ```
        >>> bv = binaryninja.load('/bin/ls', options={'files.universal.architecturePreference': ['arm64']})
        ```

        Warning

        The recommended code pattern for opening a BinaryView is to use the
        [`load`](https://api.binary.ninja/index.html#binaryninja.load "binaryninja.load") API as
        a context manager like `with load('/bin/ls') as bv:` which will automatically clean up
        when done with the view. If using this API directly you will need to call
        bv.file.close() before the BinaryView leaves scope to ensure the reference is properly
        removed and prevents memory leaks.

        Parameters:
        :   - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)") *|* [*bytearray*](https://docs.python.org/3/library/stdtypes.html#bytearray
              "(in Python v3.14)") *|* [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer") *|*
              [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
              *|* [*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*ProjectFile*](project.md#binaryninja.project.ProjectFile
              "binaryninja.project.ProjectFile")) – path to file/bndb, raw bytes, or raw view to load
            - **update_analysis** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – whether or not to run
              [`update_analysis_and_wait`](#binaryninja.binaryview.BinaryView.update_analysis_and_wait
              "binaryninja.binaryview.BinaryView.update_analysis_and_wait") after opening a
              [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView"),
              defaults to `True`
            - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count
            - **options** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
              v3.14)")) – a dictionary in the form {setting identifier string : object value}
            - **source** –

        Returns:
        :   returns a [`BinaryView`](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView") object for the given filename or `None`

        Return type:
        :   [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
            or `None`

        Example:
        :   ```
            >>> binaryninja.load('/bin/ls', options={'loader.imageBase': 0xfffffff0000, 'loader.macho.processFunctionStarts' : False})
            <BinaryView: '/bin/ls', start 0xfffffff0000, len 0xa290>
            >>>
            ```

    lookup_imported_object_library(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.lookup_imported_object_library)
    :   `lookup_imported_object_library` gives you details of which type library and name was
        used to determine the type of a symbol at a given address

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address of symbol at import site
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform of symbol at import site

        Returns:
        :   A tuple of [TypeLibrary, QualifiedName] with the library and name used, or None if it
            was not imported

        Return type:
        :   *Tuple*[[*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary"),
            [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")]

    lookup_imported_type_library(*name: _types.QualifiedNameType*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary"), _types.QualifiedName] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.lookup_imported_type_library)
    :   `lookup_imported_type_library` gives you details of from which type library and name a
        given type in the analysis was imported.

        Parameters:
        :   **name** (*_types.QualifiedNameType*) – Name of type in analysis

        Returns:
        :   A tuple of [TypeLibrary, QualifiedName] with the library and name used, or None if it
            was not imported

        Return type:
        :   *Optional*[*Tuple*[[*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
            "binaryninja.typelibrary.TypeLibrary"),
            [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")]]

    lookup_imported_type_platform(*name: _types.QualifiedNameType*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[_platform.Platform, _types.QualifiedName] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.lookup_imported_type_platform)
    :   `lookup_imported_type_platform` gives you details of from which platform and name a
        given type in the analysis was imported.

        Parameters:
        :   **name** (*_types.QualifiedNameType*) – Name of type in analysis

        Returns:
        :   A tuple of [Platform, QualifiedName] with the platform and name used, or None if it was
            not imported

        Return type:
        :   *Optional*[*Tuple*[[*Platform*](platform.md#binaryninja.platform.Platform
            "binaryninja.platform.Platform"),
            [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")]]

    mlil_functions(*preload_limit: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function_generator: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.mlil_functions)
    :   Generates a list of il functions. This method should be used instead of ‘functions’
        property if MLIL is needed and performance is a concern.

        Parameters:
        :   - **preload_limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)") *|* *None*) –
            - **function_generator**
              ([*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in
              Python v3.14)")*[*[*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")*,* *None**,* *None**]* *|* *None*) –

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*MediumLevelILFunction*](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction
            "binaryninja.mediumlevelil.MediumLevelILFunction"), *None*, *None*]

    navigate(*view_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.navigate)
    :   `navigate` navigates the UI to the specified virtual address in the specified View

        The View name is created by combining a View type (e.g. “Graph”) with a BinaryView type
        (e.g. “Mach-O”), separated by a colon, resulting in something like “Graph:Mach-O”.

        Parameters:
        :   - **view_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – view name
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address to navigate to

        Returns:
        :   whether navigation succeeded

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.navigate(bv.view, bv.start)
            True
            >>> bv.file.existing_views
            ['Mach-O', 'Raw']
            >>> import binaryninjaui
            >>> [i.getName() for i in binaryninjaui.ViewType.getTypes()]
            ['Graph', 'Hex', 'Linear', 'Strings', 'Types', 'Triage', 'Bytes']
            >>> bv.navigate('Graph:Mach-O', bv.entry_point)
            True
            ```

    never_branch(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.never_branch)
    :   `never_branch` convert the branch instruction of architecture `arch` at the virtual
        address `addr` to a fall through.

        Note

        This API performs a binary patch, analysis may need to be updated afterward.
        Additionally the binary file must be saved in order to preserve the changes made.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be modified
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x1000130e)
            'jne     0x10001317'
            >>> bv.never_branch(0x1000130e)
            True
            >>> bv.get_disassembly(0x1000130e)
            'nop'
            >>>
            ```

    *static* new(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python v3.14)") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *file_metadata: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.new)
    :   `new` creates a new, Raw [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView") for the provided data.

        Parameters:
        :   - **data** (Union[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "(in
              Python v3.14)"), [`DataBuffer`](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer"),
              [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
              v3.14)"), [`BinaryView`](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")]) – path to file/bndb, raw bytes, or raw view to
              load
            - **file_metadata**
              ([`FileMetadata`](filemetadata.md#binaryninja.filemetadata.FileMetadata
              "binaryninja.filemetadata.FileMetadata")) – Optional FileMetadata object for this new
              view

        Returns:
        :   returns a [`BinaryView`](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView") object for the given filename or `None`

        Return type:
        :   [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
            or `None`

        Example:
        :   ```
            >>> binaryninja.load('/bin/ls', options={'loader.imageBase': 0xfffffff0000, 'loader.macho.processFunctionStarts' : False})
            <BinaryView: '/bin/ls', start 0xfffffff0000, len 0xa290>
            >>>
            ```

    notify_data_inserted(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.notify_data_inserted)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    notify_data_removed(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.notify_data_removed)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    notify_data_written(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.notify_data_written)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *static* open(*src*, *file_metadata=None*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.open)
    :   Return type:
        :   [*BinaryView*](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") |
            *None*

    parse_expression(*expression: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *here: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.parse_expression)
    :   Evaluates a string expression to an integer value.

        The parser uses the following rules:

        > - Symbols are defined by the lexer as `[A-Za-z0-9_:<>][A-Za-z0-9_:$\-<>]+` or anything
        >   enclosed in either single or double quotes
        > - Symbols are everything in `bv.symbols`, unnamed DataVariables (i.e. `data_00005000`),
        >   unnamed functions (i.e. `sub_00005000`), or section names (i.e. `.text`)
        > - Numbers are defaulted to hexadecimal thus _printf + 10 is equivalent to printf + 0x10 If
        >   decimal numbers required use the decimal prefix.
        > - Since numbers and symbols can be ambiguous its recommended that you prefix your numbers
        >   with the following:
        >
        >   > - `0x` - Hexadecimal
        >   > - `0n` - Decimal
        >   > - `0` - Octal
        > - In the case of an ambiguous number/symbol (one with no prefix) for instance `12345` we
        >   will first attempt to look up the string as a symbol, if a symbol is found its address
        >   is used, otherwise we attempt to convert it to a hexadecimal number.
        > - The following operations are valid: `+, -, \*, /, %, (), &, \|, ^, ~, ==, !=, >, <, >=,
        >   <=`
        >
        >   > - Comparison operators return 1 if the condition is true, 0 otherwise.
        > - In addition to the above operators there are dereference operators similar to BNIL style
        >   IL:
        >
        >   > - `[<expression>]` - read the current address size at `<expression>`
        >   > - `[<expression>].b` - read the byte at `<expression>`
        >   > - `[<expression>].w` - read the word (2 bytes) at `<expression>`
        >   > - `[<expression>].d` - read the dword (4 bytes) at `<expression>`
        >   > - `[<expression>].q` - read the quadword (8 bytes) at `<expression>`
        > - The `$here` (or more succinctly: `$`) keyword can be used in calculations and is defined
        >   as the `here` parameter, or the currently selected address
        > - The `$start`/`$end` keyword represents the address of the first/last bytes in the file
        >   respectively
        > - Arbitrary magic values (name-value-pairs) can be added to the expression parser via the
        >   [`add_expression_parser_magic_value`](#binaryninja.binaryview.BinaryView.add_expression_parser_magic_value
        >   "binaryninja.binaryview.BinaryView.add_expression_parser_magic_value") API. Notably, the
        >   debugger adds all register values into the expression parser so they can be used
        >   directly when navigating. The register values can be referenced like $rbp, $x0, etc. For
        >   more details, refer to the related [debugger
        >   docs](https://docs.binary.ninja/guide/debugger/index.html#navigating-the-binary).

        Parameters:
        :   - **expression** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Arithmetic expression to be evaluated
            - **here** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – (optional) Base address for relative expressions, defaults to zero

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    parse_possiblevalueset(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *state: [RegisterValueType](enums.md#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType")*, *here: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.parse_possiblevalueset)
    :   Evaluates a string representation of a PossibleValueSet into an instance of the
        `PossibleValueSet` value.

        Note

        Values are evaluated based on the rules as specified for
        [`parse_expression`](#binaryninja.binaryview.BinaryView.parse_expression
        "binaryninja.binaryview.BinaryView.parse_expression") API. This implies that a
        `ConstantValue [0x4000].d` can be provided given that 4 bytes can be read at `0x4000`.
        All constants are considered to be in hexadecimal form by default.

        The parser uses the following rules:
        :   - ConstantValue - `<value>`
            - ConstantPointerValue - `<value>`
            - StackFrameOffset - `<value>`
            - SignedRangeValue - `<value>:<value>:<value>{,<value>:<value>:<value>}*` (Multiple
              ValueRanges can be provided by separating them by commas)
            - UnsignedRangeValue - `<value>:<value>:<value>{,<value>:<value>:<value>}*` (Multiple
              ValueRanges can be provided by separating them by commas)
            - InSetOfValues - `<value>{,<value>}*`
            - NotInSetOfValues - `<value>{,<value>}*`

        Parameters:
        :   - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – PossibleValueSet value to be parsed
            - **state** ([*RegisterValueType*](enums.md#binaryninja.enums.RegisterValueType
              "binaryninja.enums.RegisterValueType")) – State for which the value is to be parsed
            - **here** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – (optional) Base address for relative expressions, defaults to zero

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

        Example:
        :   ```
            >>> psv_c = bv.parse_possiblevalueset("400", RegisterValueType.ConstantValue)
            >>> psv_c
            <const 0x400>
            >>> psv_ur = bv.parse_possiblevalueset("1:10:1", RegisterValueType.UnsignedRangeValue)
            >>> psv_ur
            <unsigned ranges: [<range: 0x1 to 0x10>]>
            >>> psv_is = bv.parse_possiblevalueset("1,2,3", RegisterValueType.InSetOfValues)
            >>> psv_is
            <in set([0x1, 0x2, 0x3])>
            >>>
            ```

    parse_type_string(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *import_dependencies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type"), [QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.parse_type_string)
    :   `parse_type_string` parses string containing C into a single type `Type`. In contrast to
        the
        [`parse_types_from_source`](platform.md#binaryninja.platform.Platform.parse_types_from_source
        "binaryninja.platform.Platform.parse_types_from_source") or
        [`parse_types_from_source_file`](platform.md#binaryninja.platform.Platform.parse_types_from_source_file
        "binaryninja.platform.Platform.parse_types_from_source_file"), `parse_type_string` can
        only load a single type, though it can take advantage of existing type information in
        the binary view, while those two APIs do not.

        Parameters:
        :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – C source code string of type to create
            - **import_dependencies** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – If Type Library types should be imported during parsing

        Returns:
        :   A tuple of a `Type` and type name

        Return type:
        :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python
            v3.14)")([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type"),
            [*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName"))

        Example:
        :   ```
            >>> bv.parse_type_string("int foo")
            (<type: int32_t>, 'foo')
            >>>
            ```

    parse_types_from_string(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *include_dirs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *import_dependencies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [BasicTypeParserResult](typeparser.md#binaryninja.typeparser.BasicTypeParserResult "binaryninja.typeparser.BasicTypeParserResult")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.parse_types_from_string)
    :   `parse_types_from_string` parses string containing C into a `BasicTypeParserResult`
        objects. This API unlike the
        [`parse_types_from_source`](platform.md#binaryninja.platform.Platform.parse_types_from_source
        "binaryninja.platform.Platform.parse_types_from_source") allows the reference of types
        already defined in the BinaryView.

        Parameters:
        :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – C source code string of types, variables, and function types, to create
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of string options to be passed into the
              type parser
            - **include_dirs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]* *|* *None*) – Optional list of header search directories
            - **import_dependencies** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – If Type Library types should be imported during parsing

        Returns:
        :   [`BasicTypeParserResult`](typeparser.md#binaryninja.typeparser.BasicTypeParserResult
            "binaryninja.typeparser.BasicTypeParserResult") (a SyntaxError is thrown on parse error)

        Return type:
        :   [*BasicTypeParserResult*](typeparser.md#binaryninja.typeparser.BasicTypeParserResult
            "binaryninja.typeparser.BasicTypeParserResult")

        Example:
        :   ```
            >>> bv.parse_types_from_string('int foo;\nint bar(int x);\nstruct bas{int x,y;};\n')
            ({types: {'bas': <type: struct bas>}, variables: {'foo': <type: int32_t>}, functions:{'bar':
            <type: int32_t(int32_t x)>}}, '')
            >>>
            ```

    *abstract* perform_get_address_size() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_address_size)
    :   Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_get_default_endianness() → [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_default_endianness)
    :   `perform_get_default_endianness` implements a check which returns the Endianness of the
        BinaryView

        Note

        This method **may** be implemented for custom BinaryViews that are not LittleEndian.

        Warning

        This method **must not** be called directly.

        Returns:
        :   either [`Endianness.LittleEndian`](enums.md#binaryninja.enums.Endianness.LittleEndian
            "binaryninja.enums.Endianness.LittleEndian") or
            [`Endianness.BigEndian`](enums.md#binaryninja.enums.Endianness.BigEndian
            "binaryninja.enums.Endianness.BigEndian")

        Return type:
        :   [*Endianness*](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")

    perform_get_entry_point() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_entry_point)
    :   `perform_get_entry_point` implements a query for the initial entry point for code
        execution.

        Note

        This method **should** be implemented for custom BinaryViews that are executable.

        Warning

        This method **must not** be called directly.

        Returns:
        :   the virtual address of the entry point

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_get_length() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_length)
    :   `perform_get_length` implements a query for the size of the virtual address range used
        by the BinaryView.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Returns:
        :   returns the size of the virtual address range used by the BinaryView

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_get_modification(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ModificationStatus](enums.md#binaryninja.enums.ModificationStatus "binaryninja.enums.ModificationStatus")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_modification)
    :   `perform_get_modification` implements query to the whether the virtual address `addr` is
        modified.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   one of the following: Original = 0, Changed = 1, Inserted = 2

        Return type:
        :   [*ModificationStatus*](enums.md#binaryninja.enums.ModificationStatus
            "binaryninja.enums.ModificationStatus")

    perform_get_next_valid_offset(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_next_valid_offset)
    :   `perform_get_next_valid_offset` implements a query for the next valid readable,
        writable, or executable virtual memory address.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to start checking from.

        Returns:
        :   the next readable, writable, or executable virtual memory address

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_get_start() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_get_start)
    :   `perform_get_start` implements a query for the first readable, writable, or executable
        virtual address in the BinaryView.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Returns:
        :   returns the first virtual address in the BinaryView

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_insert(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_insert)
    :   `perform_insert` implements a mapping between a virtual address and an absolute file
        offset, inserting the bytes `data` to rebased address `addr`.

        Note

        This method **may** be overridden by custom BinaryViews. If not overridden, inserting is
        disallowed

        Warning

        This method **must not** be called directly.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – a virtual address
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – the data to be inserted

        Returns:
        :   length of data inserted, should return 0 on error

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_is_executable() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_is_executable)
    :   `perform_is_executable` implements a check which returns true if the BinaryView is
        executable.

        Note

        This method **must** be implemented for custom BinaryViews that are executable.

        Warning

        This method **must not** be called directly.

        Returns:
        :   true if the current BinaryView is executable, false if it is not executable or on error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_is_offset_executable(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_is_offset_executable)
    :   `perform_is_offset_executable` implements a check if a virtual address `addr` is
        executable.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   true if the virtual address is executable, false if the virtual address is not
            executable or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_is_offset_readable(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_is_offset_readable)
    :   `perform_is_offset_readable` implements a check if a virtual address is readable.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   true if the virtual address is readable, false if the virtual address is not readable or
            error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_is_offset_writable(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_is_offset_writable)
    :   `perform_is_offset_writable` implements a check if a virtual address `addr` is writable.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   true if the virtual address is writable, false if the virtual address is not writable or
            error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_is_relocatable() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_is_relocatable)
    :   `perform_is_relocatable` implements a check which returns true if the BinaryView is
        relocatable. Defaults to False

        Note

        This method **may** be implemented for custom BinaryViews that are relocatable.

        Warning

        This method **must not** be called directly.

        Returns:
        :   True if the BinaryView is relocatable, False otherwise

        Return type:
        :   boolean

    perform_is_valid_offset(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_is_valid_offset)
    :   `perform_is_valid_offset` implements a check if a virtual address `addr` is valid.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – a virtual address to be checked

        Returns:
        :   true if the virtual address is valid, false if the virtual address is invalid or error

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_on_after_snapshot_data_applied() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_on_after_snapshot_data_applied)
    :   Return type:
        :   *None*

    perform_read(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_read)
    :   `perform_read` implements a mapping between a virtual address and an absolute file
        offset, reading `length` bytes from the rebased address `addr`.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – a virtual address to attempt to read from
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the number of bytes to be read

        Returns:
        :   length bytes read from addr, should return empty string on error

        Return type:
        :   [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")

    perform_remove(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_remove)
    :   `perform_remove` implements a mapping between a virtual address and an absolute file
        offset, removing `length` bytes from the rebased address `addr`.

        Note

        This method **may** be overridden by custom BinaryViews. If not overridden, removing
        data is disallowed

        Warning

        This method **must not** be called directly.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – a virtual address
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the number of bytes to be removed

        Returns:
        :   length of data removed, should return 0 on error

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    perform_save(*accessor*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_save)
    :   Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    perform_write(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.perform_write)
    :   `perform_write` implements a mapping between a virtual address and an absolute file
        offset, writing the bytes `data` to rebased address `addr`.

        Note

        This method **may** be overridden by custom BinaryViews. Use
        [`add_auto_segment`](#binaryninja.binaryview.BinaryView.add_auto_segment
        "binaryninja.binaryview.BinaryView.add_auto_segment") to provide data without overriding
        this method.

        Warning

        This method **must not** be called directly.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – a virtual address
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – the data to be written

        Returns:
        :   length of data written, should return 0 on error

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    pull_types_from_archive(*archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *names: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedNameType]*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[_types.QualifiedName, [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[_types.QualifiedName, _types.Type]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.pull_types_from_archive)
    :   Pull types from a type archive, updating them and any dependencies

        Parameters:
        :   - **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Target type archive
            - **names** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[**_types.QualifiedNameType**]*) – Names of desired types in type
              archive

        Returns:
        :   { name: (name, type) } Mapping from archive name to (analysis name, definition), None on
            error

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[_types.QualifiedName,
            [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[_types.QualifiedName, _types.Type]] | *None*

    pull_types_from_archive_by_id(*archive_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *archive_type_ids: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.pull_types_from_archive_by_id)
    :   Pull types from a type archive by id, updating them and any dependencies

        Parameters:
        :   - **archive_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Target type archive id
            - **archive_type_ids** ([*List*](https://docs.python.org/3/library/typing.html#typing.List
              "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – Ids of desired types in type archive

        Returns:
        :   { id: id } Mapping from archive type id to analysis type id, None on error

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")] | *None*

    push_types_to_archive(*archive: [TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")*, *names: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[_types.QualifiedNameType]*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[_types.QualifiedName, [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[_types.QualifiedName, _types.Type]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.push_types_to_archive)
    :   Push a collection of types, and all their dependencies, into a type archive

        Parameters:
        :   - **archive** ([*TypeArchive*](typearchive.md#binaryninja.typearchive.TypeArchive
              "binaryninja.typearchive.TypeArchive")) – Target type archive
            - **names** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[**_types.QualifiedNameType**]*) – Names of types in analysis

        Returns:
        :   { name: (name, type) } Mapping from analysis name to (archive name, definition), None on
            error

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[_types.QualifiedName,
            [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[_types.QualifiedName, _types.Type]] | *None*

    push_types_to_archive_by_id(*archive_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *type_ids: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.push_types_to_archive_by_id)
    :   Push a collection of types, and all their dependencies, into a type archive

        Parameters:
        :   - **archive_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Id of target type archive
            - **type_ids** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) – Ids of types in analysis

        Returns:
        :   True if successful

        Return type:
        :   [*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")] | *None*

    query_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → metadata.MetadataValueType[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.query_metadata)
    :   query_metadata retrieves a metadata associated with the given key stored in the current
        BinaryView.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – key to query

        Return type:
        :   metadata associated with the key

        Example:
        :   ```
            >>> bv.store_metadata("integer", 1337)
            >>> bv.query_metadata("integer")
            1337L
            >>> bv.store_metadata("list", [1,2,3])
            >>> bv.query_metadata("list")
            [1L, 2L, 3L]
            >>> bv.store_metadata("string", "my_data")
            >>> bv.query_metadata("string")
            'my_data'
            ```

    range_contains_relocation(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.range_contains_relocation)
    :   Checks if the specified range overlaps with a relocation

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    read(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.read)
    :   `read` returns the data reads at most `length` bytes from virtual address `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to read from.
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to read.

        Returns:
        :   at most `length` bytes from the virtual address `addr`, empty string on error or no data

        Return type:
        :   [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")

        Example:
        :   ```
            >>> #Opening a x86_64 Mach-O binary
            >>> bv = BinaryView.new("/bin/ls") # note that we are using `new` instead of `load` to get the raw view
            >>> bv.read(0,4)
            b'\xcf\xfa\xed\xfe'
            ```

    read_int(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.read_int)
    :   Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness") *|* *None*) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    read_pointer(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.read_pointer)
    :   Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    read_uuid(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *ms_format: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.read_uuid)
    :   Reads a UUID from the specified address in the binary view.

        Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The address to read the UUID from.
            - **ms_format** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether to return the UUID in Microsoft format (True) or standard
              format (False).

        Returns:
        :   A UUID object

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in
            Python v3.14)") – If 16 bytes couldn’t be read from the specified address.

        Return type:
        :   [*UUID*](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")

    reader(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [BinaryReader](#binaryninja.binaryview.BinaryReader "binaryninja.binaryview.BinaryReader")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.reader)
    :   Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|* *None*) –

        Return type:
        :   [*BinaryReader*](#binaryninja.binaryview.BinaryReader
            "binaryninja.binaryview.BinaryReader")

    reanalyze() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.reanalyze)
    :   `reanalyze` causes all functions to be reanalyzed. This function does not wait for the
        analysis to finish.

        Return type:
        :   *None*

    rebase(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *force: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = False*, *progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.rebase)
    :   `rebase` rebase the existing [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView") into a new
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
        at the specified virtual address

        Note

        This method does not update corresponding UI components. If the BinaryView is associated
        with UI components then initiate the rebase operation within the UI, e.g. using the
        command palette or `binaryninjaui.UIContext.activeContext().rebaseCurrentView()`. If
        working with views that are not associated with UI components while the UI is active,
        then set `force` to `True` to enable rebasing.

        Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the start of the
              [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
            - **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – enable rebasing while the UI is active
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]* *|* *None*) –

        Returns:
        :   the new [`BinaryView`](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView") object or `None` on failure

        Return type:
        :   [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
            or `None`

        Example:
        :   ```
            >>> from binaryninja import load
            >>> bv = load('/bin/ls')
            >>> print(bv)
            <BinaryView: '/bin/ls', start 0x100000000, len 0x182f8>
            >>> newbv = bv.rebase(0x400000)
            >>> print(newbv)
            <BinaryView: '/bin/ls', start 0x400000, len 0x182f8>
            >>>
            >>> # For rebasing the current view in the UI:
            >>> import binaryninjaui
            >>> execute_on_main_thread_and_wait(lambda: binaryninjaui.UIContext.activeContext().rebaseCurrentView(0x800000))
            ```

    record_imported_object_library(*lib: [TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.record_imported_object_library)
    :   `record_imported_object_library` should be called by custom py:py:class:BinaryView
        implementations when they have successfully imported an object from a type library (e.g.
        a symbol’s type). Values recorded with this function will then be queryable via
        `lookup_imported_object_library`.

        Parameters:
        :   - **lib** ([*TypeLibrary*](typelibrary.md#binaryninja.typelibrary.TypeLibrary
              "binaryninja.typelibrary.TypeLibrary")) – Type Library containing the imported type
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the object in the type library
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address of symbol at import site
            - **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform") *|* *None*) – Platform of symbol at import site

        Return type:
        :   *None*

    redo() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.redo)
    :   `redo` redo the last committed transaction in the undo database.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)
            True
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> bv.redo()
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>>
            ```

    *classmethod* register() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.register)
    :   Return type:
        :   *None*

    register_notification(*notify: [BinaryDataNotification](#binaryninja.binaryview.BinaryDataNotification "binaryninja.binaryview.BinaryDataNotification")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.register_notification)
    :   register_notification enables the receipt of callbacks for various analysis events. A
        full list of callbacks is available in the
        [`BinaryDataNotification`](#binaryninja.binaryview.BinaryDataNotification
        "binaryninja.binaryview.BinaryDataNotification") class. If the notification_barrier is
        enabled, then it is triggered upon the initial call to register_notification. Subsequent
        calls for an already registered `notify` instance also trigger a notification_barrier
        callback.

        Parameters:
        :   **notify** ([*BinaryDataNotification*](#binaryninja.binaryview.BinaryDataNotification
            "binaryninja.binaryview.BinaryDataNotification")) – notify is a subclassed instance of
            [`BinaryDataNotification`](#binaryninja.binaryview.BinaryDataNotification
            "binaryninja.binaryview.BinaryDataNotification").

        Return type:
        :   *None*

    register_platform_types(*platform: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.register_platform_types)
    :   `register_platform_types` ensures that the platform-specific types for a `Platform` are
        available for the current [`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView"). This is automatically performed when adding a new
        function or setting the default platform.

        Parameters:
        :   **platform** ([*Platform*](platform.md#binaryninja.platform.Platform
            "binaryninja.platform.Platform")) – Platform containing types to be registered

        Return type:
        :   *None*

        Example:
        :   ```
            >>> platform = Platform["linux-x86"]
            >>> bv.register_platform_types(platform)
            >>>
            ```

    relocation_ranges_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.relocation_ranges_at)
    :   List of relocation range tuples for a given address

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]]

    relocation_ranges_in_range(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.relocation_ranges_in_range)
    :   List of relocation range tuples for a given range

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")]]

    relocations_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Relocation](#binaryninja.binaryview.Relocation "binaryninja.binaryview.Relocation")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.relocations_at)
    :   List of relocations for a given address

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Relocation*](#binaryninja.binaryview.Relocation
            "binaryninja.binaryview.Relocation")]

    remove(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove)
    :   `remove` removes at most `length` bytes from virtual address `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to remove from.
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to remove.

        Returns:
        :   number of bytes removed from virtual address `addr`

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.read(0,8)
            'BBBBAAAA'
            >>> bv.remove(0,4)
            4
            >>> bv.read(0,4)
            'AAAA'
            ```

    remove_auto_data_tag(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag: [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_auto_data_tag)
    :   `remove_auto_data_tag` removes a Tag object at a data address.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to remove the tag
            - **tag** ([*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) – Tag object
              to be removed

        Return type:
        :   *None*

    remove_auto_data_tags_of_type(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_auto_data_tags_of_type)
    :   `remove_auto_data_tags_of_type` removes all data tags at the given address of the given
        type.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to add the tags
            - **tag_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Tag type name to match for removing

        Return type:
        :   *None*

    remove_auto_section(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_auto_section)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   *None*

    remove_auto_segment(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_auto_segment)
    :   `remove_auto_segment` Removes an automatically generated segment from the current
        segment mapping. This method removes the most recently added ‘auto’ segment that either
        matches the specified start address or contains it.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the start of the segment
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – length of the segment (unused)

        Return type:
        :   *None*

        Warning

        This action is not persistent across saving of a BNDB and must be re-applied each time a
        BNDB is loaded.

    remove_component(*_component: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_component)
    :   Remove a component from the tree entirely.

        Parameters:
        :   **_component** ([*Component*](component.md#binaryninja.component.Component
            "binaryninja.component.Component") *|*
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –
            Component to remove

        Returns:
        :   Whether the removal was successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_data_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *to_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_data_ref)
    :   `remove_data_ref` removes an auto data cross-reference (xref) from the address
        `from_addr` to the address `to_addr`. This function will only remove ones generated
        during autoanalysis. If the reference does not exist, no action is performed.

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s source virtual address.
            - **to_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s destination virtual address.

        Return type:
        :   *None*

        Note

        It is intended to be used from within workflows or other reoccurring analysis tasks.
        Removed references will be re-created whenever auto analysis is re-run for the

    remove_expression_parser_magic_value(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_expression_parser_magic_value)
    :   Remove a magic value from the expression parser.

        If the magic value gets referenced after removal, an error will occur during the
        parsing.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – name for the magic value to remove

        Returns:

        Return type:
        :   *None*

    remove_expression_parser_magic_values(*names: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_expression_parser_magic_values)
    :   Remove a list of magic value from the expression parser

        If any of the magic values gets referenced after removal, an error will occur during the
        parsing.

        Parameters:
        :   **names** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")*)*) – names for the magic value to remove

        Returns:

        Return type:
        :   *None*

    remove_external_library(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_external_library)
    :   Remove an ExternalLibrary from this BinaryView by name. Any associated ExternalLocations
        will be unassociated from the ExternalLibrary

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Name of the external library to remove

    remove_external_location(*source_symbol: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_external_location)
    :   Remove the ExternalLocation with the given source symbol from this BinaryView

        Parameters:
        :   **source_symbol** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")) – Source symbol that will be used to determine the
            ExternalLocation to remove

    remove_function(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *update_refs=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_function)
    :   `remove_function` removes the function `func` from the list of functions

        Warning

        This method should only be used when the function that is removed is expected to
        re-appear after any other analysis executes that could re-add it. Most users will want
        to use [`remove_user_function`](#binaryninja.binaryview.BinaryView.remove_user_function
        "binaryninja.binaryview.BinaryView.remove_user_function") in their scripts.

        Parameters:
        :   - **func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function")) – a Function object.
            - **update_refs** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – automatically update other functions that were referenced

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.functions
            [<func: x86_64@0x1>]
            >>> bv.remove_function(next(bv.functions))
            >>> bv.functions
            []
            ```

    remove_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_metadata)
    :   remove_metadata removes the metadata associated with key from the current BinaryView.

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – key associated with metadata to remove from the BinaryView

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.store_metadata("integer", 1337)
            >>> bv.remove_metadata("integer")
            ```

    remove_tag_type(*tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_tag_type)
    :   `remove_tag_type` removes a [`TagType`](#binaryninja.binaryview.TagType
        "binaryninja.binaryview.TagType") and all tags that use it

        Parameters:
        :   **tag_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – The name of the tag type to remove

        Return type:
        :   *None*

    remove_user_data_ref(*from_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *to_addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_user_data_ref)
    :   `remove_user_data_ref` removes a user-specified data cross-reference (xref) from the
        address `from_addr` to the address `to_addr`. This function will only remove
        user-specified references, not ones generated during autoanalysis. If the reference does
        not exist, no action is performed.

        Parameters:
        :   - **from_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s source virtual address.
            - **to_addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the reference’s destination virtual address.

        Return type:
        :   *None*

    remove_user_data_tag(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag: [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_user_data_tag)
    :   `remove_user_data_tag` removes a [`Tag`](#binaryninja.binaryview.Tag
        "binaryninja.binaryview.Tag") object at a data address. Since this removes a user tag,
        it will be added to the current undo buffer.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to remove the tag
            - **tag** ([*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) –
              [`Tag`](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag") object to be removed

        Return type:
        :   *None*

    remove_user_data_tags_of_type(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tag_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_user_data_tags_of_type)
    :   `remove_user_data_tags_of_type` removes all data tags at the given address of the given
        type. Since this removes user tags, it will be added to the current undo buffer.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address at which to add the tags
            - **tag_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Tag type name to match for removing

        Return type:
        :   *None*

    remove_user_function(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_user_function)
    :   `remove_user_function` removes the function `func` from the list of functions as a user
        action.

        Note

        This API will prevent the function from being re-created if any analysis later triggers
        that would re-add it, unlike
        [`remove_function`](#binaryninja.binaryview.BinaryView.remove_function
        "binaryninja.binaryview.BinaryView.remove_function").

        Parameters:
        :   **func** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) – a Function object.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.functions
            [<func: x86_64@0x1>]
            >>> bv.remove_user_function(next(bv.functions))
            >>> bv.functions
            []
            ```

    remove_user_section(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_user_section)
    :   Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   *None*

    remove_user_segment(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.remove_user_segment)
    :   `remove_user_segment` Removes a user-defined segment from the current segment mapping.
        This method removes the most recently added ‘user’ segment that either matches the
        specified start address or contains it.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the start of the segment
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – length of the segment (unused)

        Return type:
        :   *None*

    rename_type(*old_name: _types.QualifiedNameType*, *new_name: _types.QualifiedNameType*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.rename_type)
    :   `rename_type` renames a type in the global list of types for the current
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")

        Parameters:
        :   - **old_name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – Existing name of type to be renamed
            - **new_name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
              "binaryninja.types.QualifiedName")) – New name of type to be renamed

        Return type:
        :   *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> bv.define_user_type(name, type)
            >>> bv.get_type_by_name("foo")
            <type: int32_t>
            >>> bv.rename_type("foo", "bar")
            >>> bv.get_type_by_name("bar")
            <type: int32_t>
            >>>
            ```

    revert_undo_actions(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.revert_undo_actions)
    :   `revert_undo_actions` reverts the actions taken since a call to
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions") Pass as id the value returned by
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions"). Empty values of id will revert
        all changes since the last call to
        [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
        "binaryninja.binaryview.BinaryView.begin_undo_actions").

        Parameters:
        :   **id** (*Optional**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
            Python v3.14)")*]*) – id of undo state, from
            [`begin_undo_actions`](#binaryninja.binaryview.BinaryView.begin_undo_actions
            "binaryninja.binaryview.BinaryView.begin_undo_actions")

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> state = bv.begin_undo_actions()
            >>> bv.convert_to_nop(0x100012f1)
            True
            >>> bv.revert_undo_actions(state)
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>>
            ```

    save(*dest: [FileAccessor](fileaccessor.md#binaryninja.fileaccessor.FileAccessor "binaryninja.fileaccessor.FileAccessor") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.save)
    :   `save` saves the original binary file to the provided destination `dest` along with any
        modifications.

        Warning

        This API will only save the original file from a view. To save a database, use
        [`create_database`](#binaryninja.binaryview.BinaryView.create_database
        "binaryninja.binaryview.BinaryView.create_database").

        Parameters:
        :   **dest** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – destination path and filename of file to be written

        Returns:
        :   True on success, False on failure

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    save_auto_snapshot(*progress_func: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *settings: [SaveSettings](filemetadata.md#binaryninja.filemetadata.SaveSettings "binaryninja.filemetadata.SaveSettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.save_auto_snapshot)
    :   `save_auto_snapshot` saves the current database to the already created file.

        Note

        [`create_database`](#binaryninja.binaryview.BinaryView.create_database
        "binaryninja.binaryview.BinaryView.create_database") should have been called prior to
        executing this method

        Parameters:
        :   - **progress_func** (*callback*) – optional function to be called with the current
              progress and total count.
            - **settings** ([*SaveSettings*](filemetadata.md#binaryninja.filemetadata.SaveSettings
              "binaryninja.filemetadata.SaveSettings")) – optional argument for special save options.

        Returns:
        :   True if it successfully saved the snapshot, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    search(*pattern: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *raw: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *ignore_case: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overlap: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *limit: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *progress_callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *match_callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [QueueGenerator](#binaryninja.binaryview.BinaryView.QueueGenerator "binaryninja.binaryview.BinaryView.QueueGenerator")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.search)
    :   Searches for matches of the specified `pattern` within this BinaryView with an
        optionally provided address range specified by `start` and `end`. This is the API used
        by the advanced binary search UI option. The search pattern can be interpreted in
        various ways:

        > - specified as a string of hexadecimal digits where whitespace is ignored, and the ‘?’
        >   character acts as a wildcard
        > - a regular expression suitable for working with bytes
        > - or if the `raw` option is enabled, the pattern is interpreted as a raw string, and any
        >   special characters are escaped and interpreted literally

        Parameters:
        :   - **pattern** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The pattern to search for.
            - **start** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The address to start the search from. (default: None)
            - **end** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The address to end the search (inclusive). (default: None)
            - **raw** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether to interpret the pattern as a raw string (default: False).
            - **ignore_case** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether to perform case-insensitive matching (default: False).
            - **overlap** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether to allow matches to overlap (default: False).
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The alignment of matches, must be a power of 2 (default: 1).
            - **limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The maximum number of matches to return (default: None).
            - **progress_callback** (*callback*) – An optional function to be called with the current
              progress and total count. This function should return a boolean value that decides
              whether the search should continue or stop.
            - **match_callback** (*callback*) – A function that gets called when a match is found. The
              callback takes two parameters: the address of the match, and the actual DataBuffer that
              satisfies the search. This function can return a boolean value that decides whether the
              search should continue or stop.

        Returns:
        :   A generator object that yields the offset and matched DataBuffer for each match found.

        Return type:
        :   [*QueueGenerator*](#binaryninja.binaryview.BinaryView.QueueGenerator
            "binaryninja.binaryview.BinaryView.QueueGenerator")

        Example:
        :   ```
            >>> from binaryninja import load
            >>> bv = load('/bin/ls')
            >>> print(bv)
            <BinaryView: '/bin/ls', start 0x100000000, len 0x182f8>
            >>> bytes(list(bv.search("50 ?4"))[0][1]).hex()
            '5004'
            >>> bytes(list(bv.search("[\x20-\x25][\x60-\x67]"))[0][1]).hex()
            '2062'
            ```

    set_analysis_hold(*enable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_analysis_hold)
    :   `set_analysis_hold` control the analysis hold for this BinaryView. Enabling analysis
        hold defers all future analysis updates, therefore causing
        [`update_analysis`](#binaryninja.binaryview.BinaryView.update_analysis
        "binaryninja.binaryview.BinaryView.update_analysis") or
        [`update_analysis_and_wait`](#binaryninja.binaryview.BinaryView.update_analysis_and_wait
        "binaryninja.binaryview.BinaryView.update_analysis_and_wait") to take no action.

        Return type:
        :   *None*

        Parameters:
        :   **enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) –

    set_comment_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *comment: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_comment_at)
    :   `set_comment_at` sets a comment for the BinaryView at the address specified

        Note that these are different from function-level comments which are specific to each
        [`Function`](function.md#binaryninja.function.Function "binaryninja.function.Function").
        For more information, see
        [`address_comments`](#binaryninja.binaryview.BinaryView.address_comments
        "binaryninja.binaryview.BinaryView.address_comments").

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address within the current BinaryView to apply the comment to
            - **comment** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – string comment to apply

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.set_comment_at(here, "hi")
            ```

    *static* set_default_session_data(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_default_session_data)
    :   `set_default_session_data` saves a variable to the BinaryView. Session data is ephemeral
        not saved to a database. Consider using
        [`store_metadata`](#binaryninja.binaryview.BinaryView.store_metadata
        "binaryninja.binaryview.BinaryView.store_metadata") if permanence is needed.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – name of the variable to be saved
            - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – value of the variable to be saved

        Example:
        :   ```
            >>> BinaryView.set_default_session_data("variable_name", "value")
            >>> bv.session_data.variable_name
            'value'
            ```

        Return type:
        :   *None*

    set_function_analysis_update_disabled(*disabled: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_function_analysis_update_disabled)
    :   `set_function_analysis_update_disabled` prevents any function from being marked as
        updates required, so that they would NOT be re-analyzed when the analysis is updated.
        The main difference between this API and `set_analysis_hold` is that `set_analysis_hold`
        only temporarily holds the analysis, and the functions are still arranged to be updated
        when the hold is turned off. However, with `set_function_analysis_update_disabled`,
        functions would not be put into the analysis queue at all.

        Use with caution – in most cases, this is NOT what you want, and you should use
        `set_analysis_hold` instead.

        Parameters:
        :   **disabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) –

        Returns:

        Return type:
        :   *None*

    set_load_settings(*type_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *settings: [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_load_settings)
    :   `set_load_settings` set a [`Settings`](settings.md#binaryninja.settings.Settings
        "binaryninja.settings.Settings") object which defines the load settings for the given
        [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
        "binaryninja.binaryview.BinaryViewType") `type_name`

        Parameters:
        :   - **type_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the [`BinaryViewType`](#binaryninja.binaryview.BinaryViewType
              "binaryninja.binaryview.BinaryViewType") name
            - **settings** ([*Settings*](settings.md#binaryninja.settings.Settings
              "binaryninja.settings.Settings")) – the load settings

        Return type:
        :   *None*

    set_manual_type_source_override(*entries: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_manual_type_source_override)
    :   > This allows for fine-grained control over how types from this BinaryView are exported to
        > a TypeLibrary by export_type_to_library and export_object_to_library. Types identified
        > by the keys of the dict will NOT be exported to the destination TypeLibrary, but will
        > instead be treated as a type that had come from the string component of the value tuple.
        > This results in the destination TypeLibrary gaining a new dependency.
        >
        > This is useful if a BinaryView was automatically marked up with a lot of debug
        > information but you want to export only a subset of that information into a new
        > TypeLibrary. By creating a description of which local types correspond to types in other
        > already extant libraries, those types will be avoided during the recursive export.
        >
        > This data is not persisted and does not impact analysis.
        >
        > For example, if a BinaryView contains the following types:

        ```
        struct RECT { ... }; // omitted
        struct ContrivedExample { RECT rect; };
        ```

        Then the following python:

        ```
        overrides = {"RECT": ("tagRECT", "winX64common")}
        bv.set_manual_type_source_override(overrides)
        bv.export_type_to_library(dest_new_typelib, "ContrivedExample", bv.get_type_by_name("ContrivedExample"))
        ```

        Results in dest_new_typelib only having ContrivedExample added, and “RECT” being
        inserted as a dependency to a the type “tagRECT” found in the typelibrary “winX64common”

        Parameters:
        :   **entries** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping
            "(in Python v3.14)")*[*[*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")*,*
            [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")*[*[*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")*,*
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]**]*)
            –

    set_user_global_pointer_value(*value: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*, *confidence=255*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.set_user_global_pointer_value)
    :   Set a user global pointer value. This is useful when the auto analysis fails to find out
        the value of the global pointer, or the value is wrong. In this case, we can call
        `set_user_global_pointer_value` with a `ConstantRegisterValue` or
        `ConstantPointerRegisterValue` to provide a user global pointer value to assist the
        analysis.

        On the other hand, if the auto analysis figures out a global pointer value, but there
        should not be one, we can call `set_user_global_pointer_value` with an Undetermined
        value to override it.

        Whenever a user global pointer value is set/cleared, an analysis update must occur for
        it to take effect and all functions using the global pointer to be updated.

        We can use `user_global_pointer_value_set` to query whether a user global pointer value
        is set, and use `clear_user_global_pointer_value` to clear a user global pointer value.
        Note, `clear_user_global_pointer_value` is different from calling
        `set_user_global_pointer_value` with an `Undetermined` value. The former clears the user
        global pointer value and let the analysis decide the global pointer value, whereas the
        latte forces the global pointer value to become undetermined.

        Parameters:
        :   - **value** ([*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
              "binaryninja.variable.RegisterValue")) – the user global pointer value to be set
            - **confidence** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the confidence value of the user global pointer value. In most cases this
              should be set to 255. Setting a value lower than the confidence of the global pointer
              value from the auto analysis will cause undesired effect.

        Returns:
        :   None

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.global_pointer_value
            <const ptr 0x3fd4>
            >>> bv.set_user_global_pointer_value(ConstantPointerRegisterValue(0x12345678))
            >>> bv.global_pointer_value
            <const ptr 0x12345678>
            >>> bv.user_global_pointer_value_set
            True
            >>> bv.clear_user_global_pointer_value()
            >>> bv.global_pointer_value
            <const ptr 0x3fd4>
            >>> bv.set_user_global_pointer_value(Undetermined())
            >>> bv.global_pointer_value
            <undetermined>
            ```

    should_skip_target_analysis(*source_location: [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")*, *source_function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*, *end: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *target_location: [ArchAndAddr](function.md#binaryninja.function.ArchAndAddr "binaryninja.function.ArchAndAddr")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.should_skip_target_analysis)
    :   `should_skip_target_analysis` checks if target analysis should be skipped.

        Note

        This method is intended for use by architecture plugins only.

        Parameters:
        :   - **source_location** (*_function.ArchAndAddr*) – The source location.
            - **source_function** (*_function.Function*) – The source function.
            - **end** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The end address of the source branch instruction.
            - **target_location** (*_function.ArchAndAddr*) – The target location.

        Returns:
        :   True if the target analysis should be skipped, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    show_graph_report(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.show_graph_report)
    :   `show_graph_report` displays a `FlowGraph` object graph in a new tab with `title`.

        Parameters:
        :   - **title** (*Text string title* *of* *the tab*) – Title of the graph
            - **graph** (`FlowGraph` object) – The graph you wish to display

        Return type:
        :   *None*

    show_html_report(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *plaintext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.show_html_report)
    :   `show_html_report` displays the HTML contents in UI applications and plaintext in
        command-line applications. HTML reports support hyperlinking into the BinaryView.
        Hyperlinks can be specified as follows: `binaryninja://?expr=_start` Where `expr=`
        specifies an expression parsable by the
        [`parse_expression`](#binaryninja.binaryview.BinaryView.parse_expression
        "binaryninja.binaryview.BinaryView.parse_expression") API.

        Note

        This API function differently on the command-line vs the UI. In the UI a pop-up is used.
        On the command-line a simple text prompt is used.

        Parameters:
        :   - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – HTML contents to display
            - **plaintext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Plain text version to display (used on the command-line)
            - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.show_html_report("title", "<h1>Contents</h1>", "Plain text contents")
            Plain text contents
            ```

    show_markdown_report(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *plaintext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.show_markdown_report)
    :   `show_markdown_report` displays the markdown contents in UI applications and plaintext
        in command-line applications. Markdown reports support hyperlinking into the BinaryView.
        Hyperlinks can be specified as follows: `binaryninja://?expr=_start` Where `expr=`
        specifies an expression parsable by the
        [`parse_expression`](#binaryninja.binaryview.BinaryView.parse_expression
        "binaryninja.binaryview.BinaryView.parse_expression") API.

        Note

        This API functions differently on the command-line vs the UI. In the UI a pop-up is
        used. On the command-line a simple text prompt is used.

        Parameters:
        :   - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – markdown contents to display
            - **plaintext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Plain text version to display (used on the command-line)
            - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.show_markdown_report("title", "##Contents", "Plain text contents")
            Plain text contents
            ```

    show_plain_text_report(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.show_plain_text_report)
    :   Parameters:
        :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    skip_and_return_value(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.skip_and_return_value)
    :   `skip_and_return_value` convert the `call` instruction of architecture `arch` at the
        virtual address `addr` to the equivalent of returning a value.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be modified
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – value to make the instruction *return*
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) the architecture of the
              instructions if different from the default

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.get_disassembly(0x1000132a)
            'call    0x1000134a'
            >>> bv.skip_and_return_value(0x1000132a, 42)
            True
            >>> #The return value from x86 functions is stored in eax thus:
            >>> bv.get_disassembly(0x1000132a)
            'mov     eax, 0x2a'
            >>>
            ```

    store_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *md: [Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*, *isAuto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.store_metadata)
    :   store_metadata stores an object for the given key in the current BinaryView. Objects
        stored using store_metadata can be retrieved when the database is reopened. Objects
        stored are not arbitrary python objects! The values stored must be able to be held in a
        Metadata object. See [`Metadata`](metadata.md#binaryninja.metadata.Metadata
        "binaryninja.metadata.Metadata") for more information. Python objects could obviously be
        serialized using pickle but this intentionally a task left to the user since there is
        the potential security issues.

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – key value to associate the Metadata object with
            - **md** (*Varies*) – object to store.
            - **isAuto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – whether the metadata is an auto metadata. Most metadata should keep this as
              False. Only those automatically generated metadata should have this set to True. Auto
              metadata is not saved into the database and is presumably re-generated when re-opening
              the database.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.store_metadata("integer", 1337)
            >>> bv.query_metadata("integer")
            1337L
            >>> bv.store_metadata("list", [1,2,3])
            >>> bv.query_metadata("list")
            [1L, 2L, 3L]
            >>> bv.store_metadata("string", "my_data")
            >>> bv.query_metadata("string")
            'my_data'
            ```

    stringify_unicode_data(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *buffer: [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*, *null_terminates: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *allow_short_strings: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.stringify_unicode_data)
    :   `stringify_unicode_data` converts a buffer of unicode data into a string representation.
        :param arch: The architecture to use for stringification, or None to use the current
        architecture of the BinaryView :param buffer: The DataBuffer containing the unicode data
        to stringify :param null_terminates: If True, stops stringification at the first null
        character, otherwise continues until the end of the buffer :param allow_short_strings:
        If True, allows short strings to be returned, otherwise only long strings are returned
        :return: A tuple containing the string representation and its type, or (None, None) if
        the stringification fails :rtype: Tuple[Optional[str], Optional[StringType]]

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **buffer** ([*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer")) –
            - **null_terminates** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **allow_short_strings** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") | *None*, [*StringType*](enums.md#binaryninja.enums.StringType
            "binaryninja.enums.StringType") | *None*]

    tags_by_type(*tag_type: [TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.tags_by_type)
    :   `tags_by_type` fetches tags of a specific type.

        Parameters:
        :   **tag_type** ([*TagType*](#binaryninja.binaryview.TagType
            "binaryninja.binaryview.TagType")) – The type of tags to fetch.

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
            Python v3.14)")[[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]]

    tags_for_data_by_type(*tag_type: [TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.tags_for_data_by_type)
    :   `tags_for_data_by_type` fetches data-specific tags of a specific type.

        Parameters:
        :   **tag_type** ([*TagType*](#binaryninja.binaryview.TagType
            "binaryninja.binaryview.TagType")) – The type of tags to filter by.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))

    tags_for_data_with_source(*auto: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]][[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.tags_for_data_with_source)
    :   `tags_for_data_with_source` fetches data-specific tags filtered by source.

        Parameters:
        :   **auto** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) – If True, fetch auto tags. If False, fetch user tags.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))

    typed_data_accessor(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*) → [TypedDataAccessor](#binaryninja.binaryview.TypedDataAccessor "binaryninja.binaryview.TypedDataAccessor")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.typed_data_accessor)
    :   Parameters:
        :   - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –

        Return type:
        :   [*TypedDataAccessor*](#binaryninja.binaryview.TypedDataAccessor
            "binaryninja.binaryview.TypedDataAccessor")

    undefine_auto_symbol(*sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undefine_auto_symbol)
    :   `undefine_auto_symbol` removes a symbol from the internal list of automatically
        discovered Symbol objects.

        Parameters:
        :   **sym** ([*Symbol*](types.md#binaryninja.types.Symbol "binaryninja.types.Symbol")) – the
            symbol to undefine

        Return type:
        :   *None*

    undefine_data_var(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *blacklist: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undefine_data_var)
    :   `undefine_data_var` removes the non-user data variable at the virtual address `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to define the data variable to be removed
            - **blacklist** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – whether to add the address to the data variable black list so that
              the auto analysis would not recreat the variable on re-analysis

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.undefine_data_var(bv.entry_point)
            >>>
            ```

    undefine_type(*type_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undefine_type)
    :   `undefine_type` removes a `Type` from the global list of types for the current
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")

        Parameters:
        :   **type_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Unique identifier of type to be undefined

        Return type:
        :   *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> type_id = Type.generate_auto_type_id("source", name)
            >>> bv.define_type(type_id, name, type)
            >>> bv.get_type_by_name(name)
            <type: int32_t>
            >>> bv.undefine_type(type_id)
            >>> bv.get_type_by_name(name)
            >>>
            ```

    undefine_user_data_var(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undefine_user_data_var)
    :   `undefine_user_data_var` removes the user data variable at the virtual address `addr`.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – virtual address to define the data variable to be removed

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.undefine_user_data_var(bv.entry_point)
            >>>
            ```

    undefine_user_symbol(*sym: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undefine_user_symbol)
    :   `undefine_user_symbol` removes a symbol from the internal list of user added Symbol
        objects.

        Parameters:
        :   **sym** ([*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")) – the symbol to undefine

        Return type:
        :   *None*

    undefine_user_type(*name: _types.QualifiedNameType*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undefine_user_type)
    :   `undefine_user_type` removes a `Type` from the global list of user types for the current
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")

        Parameters:
        :   **name** ([*QualifiedName*](types.md#binaryninja.types.QualifiedName
            "binaryninja.types.QualifiedName")) – Name of user type to be undefined

        Return type:
        :   *None*

        Example:
        :   ```
            >>> type, name = bv.parse_type_string("int foo")
            >>> bv.define_user_type(name, type)
            >>> bv.get_type_by_name(name)
            <type: int32_t>
            >>> bv.undefine_user_type(name)
            >>> bv.get_type_by_name(name)
            >>>
            ```

    undo() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undo)
    :   `undo` undo the last committed transaction in the undo database.

        Return type:
        :   *None*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)
            True
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> bv.redo()
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>>
            ```

    undoable_transaction() → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.undoable_transaction)
    :   `undoable_transaction` gives you a context in which you can make changes to analysis,
        and creates an Undo state containing those actions. If an exception is thrown, any
        changes made to the analysis inside the transaction are reverted.

        Returns:
        :   Transaction context manager, which will commit/revert actions depending on if an
            exception is thrown when it goes out of scope.

        Return type:
        :   *Generator*

        Example:
        :   ```
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> # Actions inside the transaction will be committed to the undo state upon exit
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)
            True
            >>> bv.get_disassembly(0x100012f1)
            'nop'
            >>> bv.undo()
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            >>> # A thrown exception inside the transaction will undo all changes made inside it
            >>> with bv.undoable_transaction():
            >>>     bv.convert_to_nop(0x100012f1)  # Reverted on thrown exception
            >>>     raise RuntimeError("oh no")
            RuntimeError: oh no
            >>> bv.get_disassembly(0x100012f1)
            'xor     eax, eax'
            ```

    unregister_notification(*notify: [BinaryDataNotification](#binaryninja.binaryview.BinaryDataNotification "binaryninja.binaryview.BinaryDataNotification")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.unregister_notification)
    :   unregister_notification unregisters the
        [`BinaryDataNotification`](#binaryninja.binaryview.BinaryDataNotification
        "binaryninja.binaryview.BinaryDataNotification") object passed to register_notification

        Parameters:
        :   **notify** ([*BinaryDataNotification*](#binaryninja.binaryview.BinaryDataNotification
            "binaryninja.binaryview.BinaryDataNotification")) – notify is a subclassed instance of
            [`BinaryDataNotification`](#binaryninja.binaryview.BinaryDataNotification
            "binaryninja.binaryview.BinaryDataNotification").

        Return type:
        :   *None*

    update_analysis() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.update_analysis)
    :   `update_analysis` asynchronously starts the analysis process and returns immediately.

        **Usage**: Call `update_analysis` after making changes that could affect the analysis
        results, such as adding or modifying functions. This ensures that the analysis is
        updated to reflect the latest changes. The analysis runs in the background, allowing
        other operations to continue.

        Return type:
        :   *None*

    update_analysis_and_wait() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.update_analysis_and_wait)
    :   `update_analysis_and_wait` starts the analysis process and blocks until it is complete.
        This method should be used when it is necessary to ensure that analysis results are
        fully updated before proceeding with further operations. If an update is already in
        progress, this method chains a new update request to ensure that the update processes
        all pending changes before the call was made.

        **Usage**: Call `update_analysis_and_wait` after making changes that could affect the
        analysis results, such as adding or modifying functions, to ensure that the analysis
        reflects the latest changes. Unlike `update_analysis`, this method waits for the
        analysis to finish before returning.

        **Thread Restrictions**:

        > - **Worker Threads**: This function cannot be called from a worker thread. If called from
        >   a worker thread, an error will be logged, and the function will return immediately.
        > - **UI Threads**: This function cannot be called from a UI thread. If called from a UI
        >   thread, an error will be logged, and the function will return immediately.

        Return type:
        :   *None*

    write(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *except_on_relocation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.write)
    :   `write` writes the bytes in `data` to the virtual address `addr`.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address to write to.
            - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) – data to be written at addr.
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   number of bytes written to virtual address `addr`

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

        Example:
        :   ```
            >>> bv.read(0,4)
            b'BBBB'
            >>> bv.write(0, b"AAAA")
            4
            >>> bv.read(0,4)
            b'AAAA'
            ```

    writer(*address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [BinaryWriter](#binaryninja.binaryview.BinaryWriter "binaryninja.binaryview.BinaryWriter")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryView.writer)
    :   Parameters:
        :   **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)") *|* *None*) –

        Return type:
        :   [*BinaryWriter*](#binaryninja.binaryview.BinaryWriter
            "binaryninja.binaryview.BinaryWriter")

    *property* address_comments*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   Returns a read-only dict of the address comments attached to this BinaryView

        Note that these are different from function-level comments which are specific to each
        `Function`. For annotating code, it is recommended to use comments attached to functions
        rather than address comments attached to the BinaryView. On the other hand, BinaryView
        comments can be attached to data whereas function comments cannot.

        To create a function-level comment, use
        [`set_comment_at`](function.md#binaryninja.function.Function.set_comment_at
        "binaryninja.function.Function.set_comment_at").

    *property* address_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Address size of the binary (read-only)

    *property* allocated_ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[AddressRange](variable.md#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange")]*
    :   List of valid address ranges for this view (read-only) Deprecated: 4.1.5902 Use
        mapped_address_ranges instead.

    *property* analysis_changed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   boolean analysis state changed of the currently running analysis (read-only)

    *property* analysis_info*: [AnalysisInfo](#binaryninja.binaryview.AnalysisInfo "binaryninja.binaryview.AnalysisInfo")*
    :   Provides instantaneous analysis state information and a list of current functions under
        analysis (read-only). All times are given in units of milliseconds (ms). Per-function
        analysis_time is the aggregation of time spent performing incremental updates and is
        reset on a full function update. Per-function update_count tracks the current number of
        incremental updates and is reset on a full function update. Per-function submit_count
        tracks the current number of full updates that have completed.

        Note

        submit_count is currently not reset across analysis updates.

    *property* analysis_is_aborted*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   `analysis_is_aborted` checks if the analysis has been aborted.

        Note

        This property is intended for use by architecture plugins only.

        Returns:
        :   True if the analysis has been aborted, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* analysis_progress*: [AnalysisProgress](#binaryninja.binaryview.AnalysisProgress "binaryninja.binaryview.AnalysisProgress")*
    :   Status of current analysis (read-only)

    *property* analysis_state*: [AnalysisState](enums.md#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState")*
    :   State of current analysis (read-only)

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The architecture associated with the current
        [`BinaryView`](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")
        (read/write)

    *property* associated_type_archive_type_ids*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Get a list of all types in the analysis that are associated with type archives

        Returns:
        :   Map of all analysis types to their corresponding archive / id

    *property* associated_type_archive_types*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Get a list of all types in the analysis that are associated with attached type archives

        Returns:
        :   Map of all analysis types to their corresponding archive / id. If a type is associated
            with a disconnected type archive, the archive will be None.

    *property* attached_type_archives*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   All attached type archive ids and paths (read-only)

    *property* auto_metadata*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), metadata.MetadataValueType]*
    :   metadata retrieves the metadata associated with the current BinaryView.

        Return type:
        :   metadata associated with the BinaryView

        Example:
        :   ```
            >>> bv.metadata
            <metadata: {}>
            ```

    *property* auto_type_container*: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*
    :   Type Container for ONLY auto types in the BinaryView. Any changes to types will NOT
        promote auto types to user types. :return: Auto types only Type Container

    *property* available_view_types*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[BinaryViewType](#binaryninja.binaryview.BinaryViewType "binaryninja.binaryview.BinaryViewType")]*
    :   Available view types (read-only)

    *property* backed_address_ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[AddressRange](variable.md#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange")]*
    :   List of backed address ranges for this view (read-only)

    *property* basic_blocks*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[BasicBlock](basicblock.md#binaryninja.basicblock.BasicBlock "binaryninja.basicblock.BasicBlock"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of all BasicBlock objects in the BinaryView

    *property* connected_type_archives*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive")]*
    :   All connected type archive objects (read-only)

    *property* data_vars*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")]*
    :   List of data variables (read-only)

    *property* debug_info*: [DebugInfo](debuginfo.md#binaryninja.debuginfo.DebugInfo "binaryninja.debuginfo.DebugInfo")*
    :   The current debug info object for this binary view

    *property* dependency_sorted_types*: [TypeMapping](#binaryninja.binaryview.TypeMapping "binaryninja.binaryview.TypeMapping")*
    :   List of all types, sorted such that types are after all types on which they depend
        (read-only)

        Order is guaranteed for any collection of types with no cycles. If you have cycles in
        type dependencies, order for types in a cycle is not guaranteed.

        Note

        Dependency order is based on named type references for all non-structure types, i.e.
        `struct Foo m_foo` will induce a dependency, whereas `struct Foo* m_pFoo` will not.

        Returns:
        :   sorted types as defined above

    *property* derived_strings*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DerivedString](#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString")]*

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   End offset of the binary (read-only)

    *property* endianness*: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*
    :   Endianness of the binary (read-only)

    *property* entry_function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Entry function (read-only)

    *property* entry_functions*: [FunctionList](#binaryninja.binaryview.FunctionList "binaryninja.binaryview.FunctionList")*
    :   A List of entry functions (read-only) This list contains vanilla entry function, and
        functions like init_array, fini_array, and TLS callbacks etc. User-added entry
        functions(via add_entry_point) are also included.

        We see entry_functions as good starting points for analysis, these functions normally
        don’t have internal references. However, note that exported functions in a dll/so file
        are not included.

        Note the difference with entry_function

        Example:
        :   ```
            >>> bv.entry_function
            <func: x86@0x4014c8>
            >>> bv.entry_functions
            [<func: x86@0x4014c8>, <func: x86@0x401618>]
            ```

        Returns:
        :   a list of functions, containing the vanilla entry and other platform-specific entry
            functions

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function"))

    *property* entry_point*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Entry point of the binary (read-only)

    *property* executable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the binary is an executable (read-only)

    *property* file*: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata")*
    :   [`FileMetadata`](filemetadata.md#binaryninja.filemetadata.FileMetadata
        "binaryninja.filemetadata.FileMetadata") backing the BinaryView

    *property* functions*: [FunctionList](#binaryninja.binaryview.FunctionList "binaryninja.binaryview.FunctionList")*
    :   returns a FunctionList object (read-only)

    *property* global_pointer_value*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*
    :   Discovered value of the global pointer register, if the binary uses one (read-only)

    *property* has_data_variables*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean whether the binary has data variables (read-only)

    *property* has_database*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   boolean has a database been written to disk (read-only)

    *property* has_functions*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean whether the binary has functions (read-only)

    *property* has_symbols*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean whether the binary has symbols (read-only)

    *property* hlil_basic_blocks*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[HighLevelILBasicBlock](highlevelil.md#binaryninja.highlevelil.HighLevelILBasicBlock "binaryninja.highlevelil.HighLevelILBasicBlock"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of all HighLevelILBasicBlock objects in the BinaryView

    *property* hlil_instructions*: highlevelil.HLILInstructionsType*
    :   A generator of hlil instructions

    *property* image_base*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Image base of the binary

    *property* instructions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of instruction tokens and their start addresses

    *property* length

    *property* libraries*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

    *property* linear_disassembly*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[LinearDisassemblyLine](lineardisassembly.md#binaryninja.lineardisassembly.LinearDisassemblyLine "binaryninja.lineardisassembly.LinearDisassemblyLine")]*
    :   Iterator for all lines in the linear disassembly of the view

    *property* llil_basic_blocks*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[LowLevelILBasicBlock](lowlevelil.md#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of all LowLevelILBasicBlock objects in the BinaryView

    *property* llil_instructions*: lowlevelil.LLILInstructionsType*
    :   A generator of llil instructions

    long_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    *property* mapped_address_ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[AddressRange](variable.md#binaryninja.variable.AddressRange "binaryninja.variable.AddressRange")]*
    :   List of mapped address ranges for this view (read-only)

    *property* max_function_size_for_analysis*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Maximum size of function (sum of basic block sizes in bytes) for auto analysis

    *property* memory_map
    :   `memory_map` returns the MemoryMap object for the current BinaryView. The MemoryMap
        object is a proxy object that provides a high-level view of the memory map, allowing you
        to query and manipulate memory regions. This proxy ensures that the memory map always
        reflects the latest state of the core MemoryMap object in the underlying BinaryView.

    *property* metadata*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), metadata.MetadataValueType]*
    :   metadata retrieves the metadata associated with the current BinaryView.

        Return type:
        :   metadata associated with the BinaryView

        Example:
        :   ```
            >>> bv.metadata
            <metadata: {}>
            ```

    *property* mlil_basic_blocks*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[MediumLevelILBasicBlock](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of all MediumLevelILBasicBlock objects in the BinaryView

    *property* mlil_instructions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of mlil instructions

    *property* modified*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   boolean modification state of the BinaryView (read/write)

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")* *= None*

    *property* namespaces*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[NameSpace](types.md#binaryninja.types.NameSpace "binaryninja.types.NameSpace")]*
    :   Returns a list of namespaces for the current BinaryView

    *property* new_auto_function_analysis_suppressed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether or not automatically discovered functions will be analyzed

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* original_base*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Original image base of the binary. Deprecated: 4.1.5902 Use original_image_base instead.

    *property* original_image_base*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Original image base of the binary

    *property* parameters_for_analysis

    *property* parent_view*: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   View that contains the raw data used by this view (read-only)

    *property* parse_only*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* platform*: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The platform associated with the current BinaryView (read/write)

    *property* preload_limit*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* project*: [Project](project.md#binaryninja.project.Project "binaryninja.project.Project") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* project_file*: [ProjectFile](project.md#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    registered_view_type *= None*

    *property* relocatable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean - is the binary relocatable (read-only)

    *property* relocation_ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*
    :   List of relocation range tuples (read-only)

    *property* root_component*: [Component](component.md#binaryninja.component.Component "binaryninja.component.Component")*
    :   The root component for the BinaryView (read-only)

        This Component cannot be removed, and houses all unparented Components.

        Returns:
        :   The root component

    *property* saved*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   boolean state of whether or not the file has been saved (read/write)

    *property* sections*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Section](#binaryninja.binaryview.Section "binaryninja.binaryview.Section")]*
    :   Dictionary of sections (read-only)

    *property* segments*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Segment](#binaryninja.binaryview.Segment "binaryninja.binaryview.Segment")]*
    :   List of resolved segments (read-only)

    *property* session_data
    :   Dictionary object where plugins can store arbitrary data associated with the view. This
        data is ephemeral and not saved to a database. Consider using
        [`store_metadata`](#binaryninja.binaryview.BinaryView.store_metadata
        "binaryninja.binaryview.BinaryView.store_metadata") if permanence is needed.

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Start offset of the binary (read-only)

    *property* strings*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[StringReference](#binaryninja.binaryview.StringReference "binaryninja.binaryview.StringReference")]*
    :   List of strings (read-only)

    *property* symbols*: [SymbolMapping](#binaryninja.binaryview.SymbolMapping "binaryninja.binaryview.SymbolMapping")*
    :   Dict of symbols (read-only) Items in the dict are lists of all symbols matching that
        name.

        Example:
        :   ```
            >>> bv.symbols['_main']
            [<FunctionSymbol: "_main" @ 0x1dd0>]
            >>> list(bv.symbols)
            ['_start', '_main', '_printf', '_scanf', ...]
            >>> bv.symbols['foo']
            KeyError: "'foo': symbol not found"
            ```

        Returns:
        :   a dict-like generator of symbol names and values

        Return type:
        :   *Generator*[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), *None*, *None*]

    *property* tag_types*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")]]*
    :   `tag_types` gets a dictionary of all Tag Types present for the view, structured as {Tag
        Type Name => Tag Type}.

        Warning

        This method inconsistently returns a list of [`TagType`](#binaryninja.binaryview.TagType
        "binaryninja.binaryview.TagType") objects or a single
        [`TagType`](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType") this
        behavior will change in future revisions

        Return type:
        :   [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of
            ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),
            [*TagType*](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType"))

    *property* tags*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]]*
    :   `tags` gets a list of all data [`Tag`](#binaryninja.binaryview.Tag
        "binaryninja.binaryview.Tag") objects in the view. Tags are returned as a list of
        (address, [`Tag`](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")) pairs.

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)"), [*Tag*](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag"))

    *property* tags_all_scopes*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]]*
    :   `tags_all_scopes` fetches all tags in all scopes.

    *property* tags_for_address*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]]*
    :   `tags_for_address` fetches all address-specific tags.

    *property* tags_for_data*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]]*
    :   `tags_for_data` fetches all data-specific tags.

    *property* tags_for_function*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Tag](#binaryninja.binaryview.Tag "binaryninja.binaryview.Tag")]]*
    :   `tags_for_function` fetches all function-specific tags.

    *property* type_archive_type_names*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[TypeArchive](typearchive.md#binaryninja.typearchive.TypeArchive "binaryninja.typearchive.TypeArchive"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]]*
    :   Get a list of all available type names in all connected archives, and their archive/type
        id pair

        Returns:
        :   name <-> [(archive, archive type id)] for all type names

    *property* type_container*: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*
    :   Type Container for all types (user and auto) in the BinaryView. Any auto types modified
        through the Type Container will be converted into user types. :return: Full view Type
        Container

    *property* type_libraries*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[TypeLibrary](typelibrary.md#binaryninja.typelibrary.TypeLibrary "binaryninja.typelibrary.TypeLibrary")]*
    :   List of imported type libraries (read-only)

    *property* type_names*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[QualifiedName](types.md#binaryninja.types.QualifiedName "binaryninja.types.QualifiedName")]*
    :   List of defined type names (read-only)

        Note

        Sort order is not guaranteed in 5.2 and later.

    *property* types*: [TypeMapping](#binaryninja.binaryview.TypeMapping "binaryninja.binaryview.TypeMapping")*

    *property* user_global_pointer_value_set*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check whether a user global pointer value has been set

    *property* user_type_container*: [TypeContainer](typecontainer.md#binaryninja.typecontainer.TypeContainer "binaryninja.typecontainer.TypeContainer")*
    :   Type Container for ONLY user types in the BinaryView. :return: User types only Type
        Container

    *property* view*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* view_type*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   View type (read-only)

    *property* workflow*: [Workflow](workflow.md#binaryninja.workflow.Workflow "binaryninja.workflow.Workflow") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## BinaryViewEvent

*class* BinaryViewEvent[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewEvent)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `BinaryViewEvent` object provides a mechanism for receiving callbacks when a
    BinaryView is Finalized or the initial analysis is finished. The BinaryView finalized
    callbacks run before the initial analysis starts. The callbacks run one-after-another in
    the same order as they get registered. It is a good place to modify the BinaryView to
    add extra information to it.

    For newly opened binaries, the initial analysis completion callbacks run after the
    initial analysis, as well as linear sweep and signature matcher (if they are configured
    to run), completed. For loading old databases, the callbacks run after the database is
    loaded, as well as any automatic analysis update finishes.

    The callback function receives a BinaryView as its parameter. It is possible to call
    BinaryView.add_analysis_completion_event() on it to set up other callbacks for analysis
    completion.

    Example:
    :   ```
        >>> def callback(bv):
        ...     print('start: 0x%x' % bv.start)
        ...
        >>> BinaryViewType.add_binaryview_finalized_event(callback)
        ```

    *classmethod* register(*event_type: [BinaryViewEventType](enums.md#binaryninja.enums.BinaryViewEventType "binaryninja.enums.BinaryViewEventType")*, *callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewEvent.register)
    :   Parameters:
        :   - **event_type** ([*BinaryViewEventType*](enums.md#binaryninja.enums.BinaryViewEventType
              "binaryninja.enums.BinaryViewEventType")) –
            - **callback** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
              "(in Python v3.14)")*[**[*[*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")*]**,* *None**]*) –

        Return type:
        :   *None*

    BinaryViewEventCallback
    :   alias of `Callable`[[[`BinaryView`](#binaryninja.binaryview.BinaryView
        "binaryninja.binaryview.BinaryView")],
        [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]

## BinaryViewType

*class* BinaryViewType[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `BinaryViewType` object is used internally and should not be directly instantiated.

    __init__(*handle: LP_BNBinaryViewType*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.__init__)
    :   Parameters:
        :   **handle** (*LP_BNBinaryViewType*) –

    *static* add_binaryview_finalized_event(*callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.add_binaryview_finalized_event)
    :   add_binaryview_finalized_event adds a callback that gets executed when new binaryview is
        finalized. For more details, please refer to the documentation of BinaryViewEvent.

        Warning

        The callback provided **must** stay in scope for the lifetime of the process, deletion
        or garbage collection of the callback will result in a crash.

        Parameters:
        :   **callback** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
            "(in Python v3.14)")*[**[*[*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")*]**,* *None**]*) –

        Return type:
        :   *None*

    *static* add_binaryview_initial_analysis_completion_event(*callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.add_binaryview_initial_analysis_completion_event)
    :   add_binaryview_initial_analysis_completion_event adds a callback that gets executed
        after the initial analysis, as well as linear sweep and signature matcher (if they are
        configured to run) completed. For more details, please refer to the documentation of
        BinaryViewEvent.

        Warning

        The callback provided **must** stay in scope for the lifetime of the process, deletion
        or garbage collection of the callback will result in a crash.

        Parameters:
        :   **callback** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
            "(in Python v3.14)")*[**[*[*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")*]**,* *None**]*) –

        Return type:
        :   *None*

    create(*data: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.create)
    :   Parameters:
        :   **data** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*BinaryView*](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") |
            *None*

    get_arch(*ident: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*) → [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.get_arch)
    :   Parameters:
        :   - **ident** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness")) –

        Return type:
        :   [*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture") | *None*

    get_load_settings_for_data(*data: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [Settings](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.get_load_settings_for_data)
    :   Parameters:
        :   **data** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*Settings*](settings.md#binaryninja.settings.Settings "binaryninja.settings.Settings")
            | *None*

    get_platform(*ident: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*) → [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.get_platform)
    :   Parameters:
        :   - **ident** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –

        Return type:
        :   [*Platform*](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")
            | *None*

    is_valid_for_data(*data: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.is_valid_for_data)
    :   Parameters:
        :   **data** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    open(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")*, *file_metadata: [FileMetadata](filemetadata.md#binaryninja.filemetadata.FileMetadata "binaryninja.filemetadata.FileMetadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.open)
    :   Parameters:
        :   - **src** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in
              Python v3.14)")) –
            - **file_metadata**
              ([*FileMetadata*](filemetadata.md#binaryninja.filemetadata.FileMetadata
              "binaryninja.filemetadata.FileMetadata") *|* *None*) –

        Return type:
        :   [*BinaryView*](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") |
            *None*

    parse(*data: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.parse)
    :   Parameters:
        :   **data** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*BinaryView*](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") |
            *None*

    recognize_platform(*ident*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*, *view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *metadata*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.recognize_platform)
    :   Parameters:
        :   - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness")) –
            - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –

    register_arch(*ident: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.register_arch)
    :   Parameters:
        :   - **ident** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –

        Return type:
        :   *None*

    register_default_platform(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.register_default_platform)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) –

        Return type:
        :   *None*

    register_platform(*ident: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *plat: [Platform](platform.md#binaryninja.platform.Platform "binaryninja.platform.Platform")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.register_platform)
    :   Parameters:
        :   - **ident** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **plat** ([*Platform*](platform.md#binaryninja.platform.Platform
              "binaryninja.platform.Platform")) –

        Return type:
        :   *None*

    register_platform_recognizer(*ident*, *endian*, *cb*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryViewType.register_platform_recognizer)

    *property* is_deprecated*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   returns if the BinaryViewType is deprecated (read-only)

    *property* is_force_loadable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   returns if the BinaryViewType is force loadable (read-only)

    *property* long_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   BinaryView long name (read-only)

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   BinaryView name (read-only)

## BinaryWriter

*class* BinaryWriter[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class BinaryWriter` is a convenience class for writing binary data.

    BinaryWriter can be instantiated as follows and the rest of the document will start from
    this context

    ```
    >>> from binaryninja import *
    >>> bv = load("/bin/ls")
    >>> br = BinaryReader(bv)
    >>> br.offset
    4294967296
    >>> bw = BinaryWriter(bv)
    >>>
    ```

    Or using the optional endian parameter

    ```
    >>> from binaryninja import *
    >>> bv = load("/bin/ls")
    >>> br = BinaryReader(bv, Endianness.BigEndian)
    >>> bw = BinaryWriter(bv, Endianness.BigEndian)
    >>>
    ```

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness") *|* *None*) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

    seek(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.seek)
    :   `seek` update internal offset to `offset`.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to set the internal offset to

        Return type:
        :   *None*

        Example:
        :   ```
            >>> hex(bw.offset)
            '0x100000008L'
            >>> bw.seek(0x100000000)
            >>> hex(bw.offset)
            '0x100000000L'
            >>>
            ```

    seek_relative(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.seek_relative)
    :   `seek_relative` updates the internal offset by `offset`.

        Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – offset to add to the internal offset

        Return type:
        :   *None*

        Example:
        :   ```
            >>> hex(bw.offset)
            '0x100000008L'
            >>> bw.seek_relative(-8)
            >>> hex(bw.offset)
            '0x100000000L'
            >>>
            ```

    write(*value: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write)
    :   `write` writes `len(value)` bytes to the internal offset, without regard to endianness.

        Parameters:
        :   - **bytes** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes to be written at current offset
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation
            - **value** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) –

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bw.write("AAAA")
            True
            >>> br.read(4)
            'AAAA'
            >>>
            ```

    write16(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write16)
    :   `write16` writes the lowest order two bytes from the integer `value` to the current
        offset, using internal endianness.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write16be(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write16be)
    :   `write16be` writes the lowest order two bytes from the big endian integer `value` to the
        current offset.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write16le(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write16le)
    :   `write16le` writes the lowest order two bytes from the little endian integer `value` to
        the current offset.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write32(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write32)
    :   `write32` writes the lowest order four bytes from the integer `value` to the current
        offset, using internal endianness.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write32be(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write32be)
    :   `write32be` writes the lowest order four bytes from the big endian integer `value` to
        the current offset.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write32le(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write32le)
    :   `write32le` writes the lowest order four bytes from the little endian integer `value` to
        the current offset.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write64(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write64)
    :   `write64` writes the lowest order eight bytes from the integer `value` to the current
        offset, using internal endianness.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write64be(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write64be)
    :   `write64be` writes the lowest order eight bytes from the big endian integer `value` to
        the current offset.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write64le(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write64le)
    :   `write64le` writes the lowest order eight bytes from the little endian integer `value`
        to the current offset.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to write.
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    write8(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *except_on_relocation=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#BinaryWriter.write8)
    :   `write8` lowest order byte from the integer `value` to the current offset.

        Parameters:
        :   - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – bytes to be written at current offset
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset to set the internal offset before writing
            - **except_on_relocation** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – (default True) raise exception when write overlaps a relocation

        Returns:
        :   boolean

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> bw.write8(0x42)
            True
            >>> br.read(1)
            'B'
            >>>
            ```

    *property* endianness*: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*
    :   The Endianness to written data. (read/write)

        Getter:
        :   returns the endianness of the reader

        Setter:
        :   sets the endianness of the reader (BigEndian or LittleEndian)

        Type:
        :   [*Endianness*](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The current write offset (read/write).

        Getter:
        :   returns the current internal offset

        Setter:
        :   sets the internal offset

        Type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## CoreDataVariable

*class* CoreDataVariable[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#CoreDataVariable)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    CoreDataVariable(_address: int, _type: ‘_types.Type’, _auto_discovered: bool)

    __init__(*_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *_auto_discovered: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **_auto_discovered** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –

        Return type:
        :   *None*

    *property* address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* auto_discovered*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

## DataVariable

*class* DataVariable[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DataVariable)
:   Bases: [`CoreDataVariable`](#binaryninja.binaryview.CoreDataVariable
    "binaryninja.binaryview.CoreDataVariable")

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *auto_discovered: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DataVariable.__init__)
    :   Parameters:
        :   - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **auto_discovered** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

    *classmethod* from_core_struct(*var: BNDataVariable*, *view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*) → [DataVariable](#binaryninja.binaryview.DataVariable "binaryninja.binaryview.DataVariable")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DataVariable.from_core_struct)
    :   Parameters:
        :   - **var** (*BNDataVariable*) –
            - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –

        Return type:
        :   [*DataVariable*](#binaryninja.binaryview.DataVariable
            "binaryninja.binaryview.DataVariable")

    *property* code_refs*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[ReferenceSource](#binaryninja.binaryview.ReferenceSource "binaryninja.binaryview.ReferenceSource"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   code references to this data variable (read-only)

    *property* components*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Component](component.md#binaryninja.component.Component "binaryninja.component.Component")]*

    *property* data_refs*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   data cross references to this data variable (read-only)

    *property* data_refs_from*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   data cross references from this data variable (read-only)

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* symbol*: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

    *property* value*: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*

## DataVariableAndName

*class* DataVariableAndName[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DataVariableAndName)
:   Bases: [`CoreDataVariable`](#binaryninja.binaryview.CoreDataVariable
    "binaryninja.binaryview.CoreDataVariable")

    __init__(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *var_type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *var_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *auto_discovered: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DataVariableAndName.__init__)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **var_type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **var_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **auto_discovered** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

        Return type:
        :   *None*

## DerivedString

*class* DerivedString[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DerivedString)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Contains a string derived from code or data. The string does not need to be directly
    present in the binary in its raw form. Derived strings can have optional locations to
    data or code. When creating new derived strings, a custom type should be registered with
    [`register`](stringrecognizer.md#binaryninja.stringrecognizer.CustomStringType.register
    "binaryninja.stringrecognizer.CustomStringType.register") on
    [`CustomStringType`](stringrecognizer.md#binaryninja.stringrecognizer.CustomStringType
    "binaryninja.stringrecognizer.CustomStringType").

    __init__(*value: [StringRef](#binaryninja.binaryview.StringRef "binaryninja.binaryview.StringRef") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python v3.14)") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")*, *location: [DerivedStringLocation](#binaryninja.binaryview.DerivedStringLocation "binaryninja.binaryview.DerivedStringLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *custom_type: [CustomStringType](stringrecognizer.md#binaryninja.stringrecognizer.CustomStringType "binaryninja.stringrecognizer.CustomStringType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DerivedString.__init__)
    :   Parameters:
        :   - **value** ([*StringRef*](#binaryninja.binaryview.StringRef
              "binaryninja.binaryview.StringRef") *|*
              [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|*
              [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") *|*
              [*bytearray*](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python
              v3.14)") *|* [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer")) –
            - **location** ([*DerivedStringLocation*](#binaryninja.binaryview.DerivedStringLocation
              "binaryninja.binaryview.DerivedStringLocation") *|* *None*) –
            - **custom_type**
              ([*CustomStringType*](stringrecognizer.md#binaryninja.stringrecognizer.CustomStringType
              "binaryninja.stringrecognizer.CustomStringType") *|* *None*) –

    custom_type*: [CustomStringType](stringrecognizer.md#binaryninja.stringrecognizer.CustomStringType "binaryninja.stringrecognizer.CustomStringType") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    location*: [DerivedStringLocation](#binaryninja.binaryview.DerivedStringLocation "binaryninja.binaryview.DerivedStringLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    value*: [StringRef](#binaryninja.binaryview.StringRef "binaryninja.binaryview.StringRef")*

## DerivedStringLocation

*class* DerivedStringLocation[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#DerivedStringLocation)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Location associated with a derived string. Locations are optional.

    __init__(*location_type: [DerivedStringLocationType](enums.md#binaryninja.enums.DerivedStringLocationType "binaryninja.enums.DerivedStringLocationType")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **location_type**
              ([*DerivedStringLocationType*](enums.md#binaryninja.enums.DerivedStringLocationType
              "binaryninja.enums.DerivedStringLocationType")) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    location_type*: [DerivedStringLocationType](enums.md#binaryninja.enums.DerivedStringLocationType "binaryninja.enums.DerivedStringLocationType")*

## FunctionList

*class* FunctionList[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#FunctionList)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#FunctionList.__init__)
    :   Parameters:
        :   **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

## MemoryMap

*class* MemoryMap[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    > > Live proxy to the memory map of a BinaryView.
    > >
    > > A MemoryMap describes how a BinaryView is loaded into memory. It contains *regions*,
    > > which are raw and possibly overlapping memory definitions, and exposes *resolved
    > > ranges*, which are a computed disjoint view of the address space produced by splitting
    > > overlapping regions.
    > >
    > > Each BinaryView contributes its portion of the overall system memory layout through the
    > > segments and regions defined within that view. When regions overlap, the most recently
    > > added region takes precedence by default. Mutation is always performed by region name.
    > >
    > > **Container semantics:** Iteration (`__iter__`), length (`__len__`), and indexing
    > > (`__getitem__`) operate on *resolved ranges*, the computed non-overlapping view of the
    > > address space. Configured regions are accessed explicitly via `regions`, `get_region`,
    > > and name-based membership (`__contains__`).
    > >
    > > **Snapshot semantics:** `MemoryRegionInfo` and `ResolvedRange` objects are frozen
    > > snapshot value types captured at query time. They are not updated by later mutations to
    > > the memory map. The proxy itself (`view.memory_map`) always reflects the current state.
    > >
    > > **Architecture note:** This Python `MemoryMap` object is a proxy that accesses the
    > > BinaryView’s current memory map state through the FFI boundary. Internally, the core
    > > uses immutable copy-on-write data structures to manage memory map updates, but the proxy
    > > presents a simple mutable interface.
    > >
    > > **Analysis note:** For lock-free access during analysis, `AnalysisContext` provides
    > > memory layout query methods such as `is_valid_offset()`, `is_offset_readable()`,
    > > `get_start()`, and `get_length()`. These operate on an immutable snapshot of the
    > > MemoryMap captured when analysis begins.
    > >
    > > Note
    > >
    > > Repeated property access, for example `regions` or `ranges`, returns fresh snapshots of
    > > the current memory map state.
    > >
    > > All MemoryMap APIs support undo and redo operations. During BinaryView::Init, these APIs
    > > should be used conditionally:
    > >
    > > - Initial load: Use the MemoryMap APIs to define the memory regions that compose the
    > >   system.
    > > - Database load: Do not use the MemoryMap APIs, as the regions are already persisted and
    > >   will be restored automatically.
    > >
    > > This conditional usage prevents redundant operations and ensures database consistency.
    > > Using these APIs when loading from a database will also mark the analysis as modified,
    > > which is undesirable.
    >
    > Example:

    ```
    >>> base = 0x10000
    >>> rom_base = 0xc0000000
    >>> segments = SegmentDescriptorList(base)
    >>> segments.append(start=base, length=0x1000, data_offset=0, data_length=0x1000, flags=SegmentFlag.SegmentReadable|SegmentFlag.SegmentExecutable)
    >>> segments.append(start=rom_base, length=0x1000, flags=SegmentFlag.SegmentReadable)
    >>> view = load(bytes.fromhex('5054ebfe'), options={'loader.imageBase': base, 'loader.platform': 'x86', 'loader.segments': json.dumps(segments)})
    >>> view.memory_map
            <range: 0x10000 - 0x10004>
                    size: 0x4
                    regions:
                            'origin<Mapped>@0x0' | Mapped<Absolute> | <r-x>

            <range: 0xc0000000 - 0xc0001000>
                    size: 0x1000
                    regions:
                            'origin<Mapped>@0xbfff0000' | Unmapped | <r--> | FILL<0x0>

            <range: 0xc0001000 - 0xc0001014>
                    size: 0x14
                    regions:
                            'origin<Mapped>@0xbfff1000' | Unmapped | <---> | FILL<0x0>
    >>> view.memory_map.add_memory_region("rom", rom_base, b'\x90' * 4096, SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable)
    True
    >>> view.memory_map
            <range: 0x10000 - 0x10004>
                    size: 0x4
                    regions:
                            'origin<Mapped>@0x0' | Mapped<Absolute> | <r-x>

            <range: 0xc0000000 - 0xc0001000>
                    size: 0x1000
                    regions:
                            'rom' | Mapped<Relative> | <r-x>
                            'origin<Mapped>@0xbfff0000' | Unmapped | <r--> | FILL<0x0>

            <range: 0xc0001000 - 0xc0001014>
                    size: 0x14
                    regions:
                            'origin<Mapped>@0xbfff1000' | Unmapped | <---> | FILL<0x0>
    >>> view.read(rom_base, 16)
    b'\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
    >>> view.memory_map.add_memory_region("pad", rom_base, b'\xa5' * 8)
    True
    >>> view.read(rom_base, 16) # "pad" wins for first 8 bytes
    b'\xa5\xa5\xa5\xa5\xa5\xa5\xa5\xa5\x90\x90\x90\x90\x90\x90\x90\x90'
    >>> view.memory_map # resolved ranges show the split
            <range: 0x10000 - 0x10004>
                    size: 0x4
                    regions:
                            'origin<Mapped>@0x0' | Mapped<Absolute> | <r-x>

            <range: 0xc0000000 - 0xc0000008>
                    size: 0x8
                    regions:
                            'pad' | Mapped<Relative> | <--->
                            'rom' | Mapped<Relative> | <r-x>
                            'origin<Mapped>@0xbfff0000' | Unmapped | <r--> | FILL<0x0>

            <range: 0xc0000008 - 0xc0001000>
                    size: 0xff8
                    regions:
                            'rom' | Mapped<Relative> | <r-x>
                            'origin<Mapped>@0xbfff0000' | Unmapped | <r--> | FILL<0x0>

            <range: 0xc0001000 - 0xc0001014>
                    size: 0x14
                    regions:
                            'origin<Mapped>@0xbfff1000' | Unmapped | <---> | FILL<0x0>
    ```

    __init__(*handle: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.__init__)
    :   Parameters:
        :   **handle** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

    add_memory_region(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source: [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python v3.14)") | [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [FileAccessor](fileaccessor.md#binaryninja.fileaccessor.FileAccessor "binaryninja.fileaccessor.FileAccessor") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag") = 0*, *fill: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.add_memory_region)
    :   Adds a memory region to the memory map. Depending on the source parameter, the memory
        region is created as one of the following types:

        - **BinaryMemoryRegion** (***Unimplemented***): Represents a memory region loaded from a
          binary format.
        - **DataMemoryRegion**: Region backed by flat file or raw data (str, bytes, DataBuffer).
        - **RemoteMemoryRegion**: Ephemeral memory region via FileAccessor.
        - **UnbackedMemoryRegion**: Region not backed by any data source (requires length to be
          set).

        The source parameter determines the type:

        > - os.PathLike or str: File path to be loaded into memory as a DataMemoryRegion.
        > - bytes or bytearray: Directly loaded into memory as a DataMemoryRegion.
        > - databuffer.DataBuffer: Loaded as a DataMemoryRegion.
        > - fileaccessor.FileAccessor: Remote proxy source.
        > - BinaryView: (Reserved for future).
        > - None: Creates an unbacked memory region (must specify length).

        Note

        If no flags are specified and the new memory region overlaps with one or more existing
        regions, the overlapping portions of the new region will inherit the flags of the
        respective underlying regions.

        Parameters:
        :   name (str): A unique name for the memory region. start (int): Starting address. source
            (Optional[Union[os.PathLike, str, bytes, bytearray, BinaryView, databuffer.DataBuffer,
            fileaccessor.FileAccessor]]): Source of data or None for unbacked. length
            (Optional[int]): Required if source is None (unbacked). flags (SegmentFlag): Flags to
            apply to the memory region. Defaults to 0 (no flags). fill (int): Fill byte for unbacked
            regions. Defaults to 0.

        Returns:
        :   bool: True if the memory region was successfully added, False otherwise.

        Raises:
        :   NotImplementedError: If source type is unsupported. ValueError: If source is None and
            length is not specified.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **source** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in
              Python v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)") *|*
              [*bytearray*](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python
              v3.14)") *|* [*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*DataBuffer*](databuffer.md#binaryninja.databuffer.DataBuffer
              "binaryninja.databuffer.DataBuffer") *|*
              [*FileAccessor*](fileaccessor.md#binaryninja.fileaccessor.FileAccessor
              "binaryninja.fileaccessor.FileAccessor") *|* *None*) –
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) –
            - **fill** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    description(*base: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.description)
    :   Return the memory map description as a dict. If *base* is True, return the unresolved
        base map.

        Parameters:
        :   **base** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) –

        Return type:
        :   [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    format_description(*description: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.format_description)
    :   Format a memory map description dict as a human-readable string. Keep public for
        compatibility.

        Parameters:
        :   **description** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in
            Python v3.14)")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_active_memory_region_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_active_memory_region_at)
    :   Return the name of the active region at *addr*, or an empty string if no region covers
        the address.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_active_region_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [MemoryRegionInfo](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_active_region_at)
    :   Return the active region snapshot covering *addr*, or None if no region covers the
        address.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*MemoryRegionInfo*](#binaryninja.binaryview.MemoryRegionInfo
            "binaryninja.binaryview.MemoryRegionInfo") | *None*

    get_memory_region_display_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_memory_region_display_name)
    :   Return the display name for the named region.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_memory_region_fill(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_memory_region_fill)
    :   Return the fill byte for the named region.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_memory_region_flags(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_memory_region_flags)
    :   Return the flags for the named region.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")

    get_region(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [MemoryRegionInfo](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_region)
    :   Look up a memory region by name, returning None if not found.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*MemoryRegionInfo*](#binaryninja.binaryview.MemoryRegionInfo
            "binaryninja.binaryview.MemoryRegionInfo") | *None*

    get_resolved_range_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ResolvedRange](#binaryninja.binaryview.ResolvedRange "binaryninja.binaryview.ResolvedRange") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.get_resolved_range_at)
    :   Return the resolved range snapshot covering *addr*, or None if no range covers the
        address.

        Parameters:
        :   **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*ResolvedRange*](#binaryninja.binaryview.ResolvedRange
            "binaryninja.binaryview.ResolvedRange") | *None*

    is_memory_region_enabled(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.is_memory_region_enabled)
    :   Return whether the named region is enabled.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_memory_region_local(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.is_memory_region_local)
    :   Return whether the named region is local.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_memory_region_rebaseable(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.is_memory_region_rebaseable)
    :   Return whether the named region is rebaseable.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_memory_region(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.remove_memory_region)
    :   Remove a memory region by name. Returns True on success.

        Parameters:
        :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    reset() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.reset)
    :   Reset the memory map to its initial state. Supports undo.

        Return type:
        :   *None*

    set_logical_memory_map_enabled(*enabled: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.set_logical_memory_map_enabled)
    :   Enable or disable the logical memory map.

        When enabled, the memory map will present a simplified, logical view that merges and
        abstracts virtual memory regions based on criteria such as contiguity and flag
        consistency. This view is designed to provide a higher-level representation for user
        analysis, hiding underlying mapping details.

        When disabled, the memory map will revert to displaying the virtual view, which
        corresponds directly to the individual segments mapped from the raw file without any
        merging or abstraction.

        Parameters:
        :   **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) – True to enable the logical view, False to revert to the virtual view.

        Return type:
        :   *None*

    set_memory_region_display_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *display_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.set_memory_region_display_name)
    :   Set the display name for the named region.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **display_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_memory_region_enabled(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *enabled: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.set_memory_region_enabled)
    :   Set the enabled state for the named region.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_memory_region_fill(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *fill: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.set_memory_region_fill)
    :   Set the fill byte for the named region.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **fill** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_memory_region_flags(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag") | [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.set_memory_region_flags)
    :   Set flags for the named region. Accepts SegmentFlag or a set of flags.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag") *|*
              [*set*](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_memory_region_rebaseable(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *rebaseable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryMap.set_memory_region_rebaseable)
    :   Set the rebaseable state for the named region.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **rebaseable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* base_description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Formatted string of the base memory map, consisting of unresolved auto and user segments
        (read-only).

    *property* is_activated*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Whether the memory map is activated for the associated view.

        Returns `True` if this MemoryMap represents a parsed BinaryView with real segments (ELF,
        PE, Mach-O, etc.). Returns `False` for Raw BinaryViews or views that failed to parse
        segments.

        This is determined by whether the BinaryView has a parent view - parsed views have a
        parent Raw view, while Raw views have no parent.

        Use this to gate features that require parsed binary structure (sections, imports,
        relocations, etc.). For basic analysis queries (start, length, is_offset_readable,
        etc.), use the MemoryMap directly regardless of activation state - all BinaryViews have
        a usable MemoryMap.

        Returns:
        :   True if this is an activated (parsed) memory map, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* ranges*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ResolvedRange](#binaryninja.binaryview.ResolvedRange "binaryninja.binaryview.ResolvedRange")]*
    :   List of resolved, non-overlapping address ranges sorted by start address.

        Each range contains an ordered list of memory regions at that interval, with the first
        being the active (highest-priority) region. This is the computed address-space view,
        analogous to segments.

        Returns immutable snapshot objects that are not updated after later memory map
        mutations.

    *property* regions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MemoryRegionInfo](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo")]*
    :   List of all memory regions (including disabled ones) as snapshot value types.

        Returns immutable snapshot objects that are not updated after later memory map
        mutations.

## MemoryRegionInfo

*class* MemoryRegionInfo[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#MemoryRegionInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Snapshot of a memory region’s properties at the time of query.

    This is a frozen value type. Modifying the memory map will not update existing
    MemoryRegionInfo instances. To mutate a region, use the corresponding MemoryMap methods
    (e.g., `memory_map.set_memory_region_flags(region.name, new_flags)`).

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *display_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*, *enabled: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *rebaseable: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *fill: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *has_target: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *absolute_address_mode: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *local: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **display_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) –
            - **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **rebaseable** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **fill** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **has_target** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) –
            - **absolute_address_mode**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –
            - **local** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    absolute_address_mode*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    display_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    enabled*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    fill*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    flags*: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*

    has_target*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    local*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    rebaseable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## ReferenceSource

*class* ReferenceSource[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#ReferenceSource)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ReferenceSource(function: Optional[ForwardRef(‘_function.Function’)], arch:
    Optional[ForwardRef(‘architecture.Architecture’)], address: int)

    __init__(*function: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* hlil*: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the high level il instruction at the current location if one exists

    *property* hlils*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*
    :   Returns the high level il instructions at the current location if any exists

    *property* llil*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the low level il instruction at the current location if one exists

    *property* llils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*
    :   Returns the low level il instructions at the current location if any exists

    *property* mlil*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Returns the medium level il instruction at the current location if one exists

    *property* mlils*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*
    :   Returns the medium level il instructions at the current location if any exists

## Relocation

*class* Relocation[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Relocation)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: LP_BNRelocation*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Relocation.__init__)
    :   Parameters:
        :   **handle** (*LP_BNRelocation*) –

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The architecture associated with the [`Relocation`](#binaryninja.binaryview.Relocation
        "binaryninja.binaryview.Relocation") (read/write)

    *property* info*: [RelocationInfo](#binaryninja.binaryview.RelocationInfo "binaryninja.binaryview.RelocationInfo")*

    *property* reloc*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   The actual pointer that needs to be relocated

    *property* symbol*: [CoreSymbol](types.md#binaryninja.types.CoreSymbol "binaryninja.types.CoreSymbol") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* target*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Where the reloc needs to point to

## RelocationInfo

*class* RelocationInfo[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#RelocationInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    RelocationInfo(info: binaryninja._binaryninjacore.BNRelocationInfo)

    __init__(*info: BNRelocationInfo*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#RelocationInfo.__init__)
    :   Parameters:
        :   **info** (*BNRelocationInfo*) –

    addend*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    base*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    base_relative*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    data_relocation*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    external*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    has_sign*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    implicit_addend*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    native_type*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    pc_relative*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    section_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    symbol_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    target*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    truncate_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [RelocationType](enums.md#binaryninja.enums.RelocationType "binaryninja.enums.RelocationType")*

## ResolvedRange

*class* ResolvedRange[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#ResolvedRange)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    A computed, non-overlapping interval in the resolved address space.

    Overlapping raw regions are split into disjoint intervals. Each ResolvedRange holds the
    regions that cover it, ordered by precedence, with the active region first. The
    `active_region` property returns the highest-precedence region.

    __init__(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *regions: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MemoryRegionInfo](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **regions** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*MemoryRegionInfo*](#binaryninja.binaryview.MemoryRegionInfo
              "binaryninja.binaryview.MemoryRegionInfo")*]*) –

        Return type:
        :   *None*

    *property* active_region*: [MemoryRegionInfo](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The highest-priority region at this range, or None if empty.

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* flags*: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*
    :   Flags of the active (highest-priority) region.

    length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Name of the active region, or None if empty.

    regions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MemoryRegionInfo](#binaryninja.binaryview.MemoryRegionInfo "binaryninja.binaryview.MemoryRegionInfo")]*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## Section

*class* Section[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Section)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `Section` object is returned during BinaryView creation and should not be directly
    instantiated.

    __init__(*handle: LP_BNSection*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Section.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSection*) –

    *classmethod* serialize(*image_base: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *semantics: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics") = SectionSemantics.DefaultSectionSemantics*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *entry_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *link: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_data: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *sections: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '[]'*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Section.serialize)
    :   Serialize section parameters into a JSON string. This is useful for generating a
        properly formatted section description as options when using load.

        Parameters:
        :   - **image_base** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The base address of the image.
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The name of the section.
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The start address of the section.
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The length of the section.
            - **semantics** ([*SectionSemantics*](enums.md#binaryninja.enums.SectionSemantics
              "binaryninja.enums.SectionSemantics")) – The semantics of the section.
            - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The type of the section.
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The alignment of the section.
            - **entry_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The entry size of the section.
            - **link** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The linked section of the section.
            - **info_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – The info section of the section.
            - **info_data** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The info data of the section.
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether the section is auto-defined.
            - **sections** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – An optional, existing array of sections to append to.

        Returns:
        :   A JSON string representing the section.

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Deprecated since version 4.3.6653: Use SectionDescriptorList instead.

    *property* align*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* auto_defined*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* entry_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* info_data*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* info_section*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* length

    *property* linked_section*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* section_info*: [SectionInfo](#binaryninja.binaryview.SectionInfo "binaryninja.binaryview.SectionInfo")*
    :   Returns a section info object representing this section.

    *property* semantics*: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics")*

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* type*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## SectionDescriptorList

*class* SectionDescriptorList[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SectionDescriptorList)
:   Bases: [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python
    v3.14)")

    __init__(*image_base: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SectionDescriptorList.__init__)
    :   Initialize the SectionDescriptorList with a base image address.

        Parameters:
        :   **image_base** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – The base address of the image.

    append(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *semantics: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics") = SectionSemantics.DefaultSectionSemantics*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *entry_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *link: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *info_data: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SectionDescriptorList.append)
    :   Append a section descriptor to the list.

        Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The name of the section.
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The start address of the section.
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The length of the section.
            - **semantics** ([*SectionSemantics*](enums.md#binaryninja.enums.SectionSemantics
              "binaryninja.enums.SectionSemantics")) – The semantics of the section.
            - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – The type of the section.
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The alignment of the section.
            - **entry_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The size of each entry in the section.
            - **link** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – An optional link field.
            - **info_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) – An optional info_section field.
            - **info_data** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – An optional info_data field.
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether the section is auto-defined.

## SectionInfo

*class* SectionInfo[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SectionInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SectionInfo is a helper class for describing sections to be added to a BinaryView. See
    BinaryView.add_auto_sections and BinaryView.add_auto_section for more details or see
    class Section for accessing section information from an existing BinaryView.

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *semantics: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics")*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *align: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *entry_size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *linked_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *info_section: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *info_data: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **semantics** ([*SectionSemantics*](enums.md#binaryninja.enums.SectionSemantics
              "binaryninja.enums.SectionSemantics")) –
            - **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **align** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **entry_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **linked_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **info_section** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –
            - **info_data** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    align*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    entry_size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    info_data*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    info_section*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    linked_section*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    semantics*: [SectionSemantics](enums.md#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    type*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## Segment

*class* Segment[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Segment)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `Segment` object is returned during BinaryView creation and should not be directly
    instantiated.

    __init__(*handle: LP_BNSegment*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Segment.__init__)
    :   Parameters:
        :   **handle** (*LP_BNSegment*) –

    *classmethod* serialize(*image_base: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *data_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag") = SegmentFlag.SegmentReadable*, *auto_defined=True*, *segments: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '[]'*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Segment.serialize)
    :   Serialize segment parameters into a JSON string. This is useful for generating a
        properly formatted segment description as options when using load.

        Parameters:
        :   - **image_base** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The base address of the image.
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The start address of the segment.
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The length of the segment.
            - **data_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – The offset of the data within the segment.
            - **data_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – The length of the data within the segment.
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) – The flags of the segment.
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether the segment is auto-defined.
            - **segments** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – An optional, existing array of segments to append to.

        Returns:
        :   A JSON string representing the segment.

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

        Example::
        :   ```
            >>> base = 0x400000
            >>> rom_base = 0xffff0000
            >>> segments = SegmentDescriptorList(base)
            >>> segments.append(start=base, length=0x1000, data_offset=0, data_length=0x1000, flags=SegmentFlag.SegmentReadable|SegmentFlag.SegmentExecutable)
            >>> segments.append(start=rom_base, length=0x1000, flags=SegmentFlag.SegmentReadable)
            >>> view = load(bytes.fromhex('5054ebfe'), options={'loader.imageBase': base, 'loader.platform': 'x86', 'loader.segments': json.dumps(segments)})
            ```

        Deprecated since version 4.3.6653: Use SegmentDescriptorList instead.

    *property* auto_defined*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* data_end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* data_length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* data_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* end*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* executable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* length

    *property* readable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* segment_info*: [SegmentInfo](#binaryninja.binaryview.SegmentInfo "binaryninja.binaryview.SegmentInfo")*

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* writable*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## SegmentDescriptorList

*class* SegmentDescriptorList[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SegmentDescriptorList)
:   Bases: [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python
    v3.14)")

    __init__(*image_base: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SegmentDescriptorList.__init__)
    :   Initialize the SegmentDescriptorList with a base image address.

        Parameters:
        :   **image_base** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – The base address of the image.

    append(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *data_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag") = SegmentFlag.SegmentReadable*, *auto_defined: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SegmentDescriptorList.append)
    :   Append a segment descriptor to the list.

        Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The start address of the segment.
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – The length of the segment.
            - **data_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – The offset of the data within the segment.
            - **data_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – The length of the data within the segment.
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) – The flags of the segment.
            - **auto_defined** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – Whether the segment is auto-defined.

## SegmentInfo

*class* SegmentInfo[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SegmentInfo)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    This class helper class holds Segment information used to describe segments when
    creating a BinaryView. See BinaryView.add_auto_segments and BinaryView.add_user_segments
    for usage. See class Segment for segment information retrieval from an existing
    BinaryView.

    __init__(*start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data_length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **data_offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **data_length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **flags** ([*SegmentFlag*](enums.md#binaryninja.enums.SegmentFlag
              "binaryninja.enums.SegmentFlag")) –

        Return type:
        :   *None*

    data_length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    data_offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    flags*: [SegmentFlag](enums.md#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag")*

    length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## StringRef

*class* StringRef[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#StringRef)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Deduplicated reference to a string owned by the Binary Ninja core. Use str or bytes to
    convert this to a standard Python string or sequence of bytes.

    __init__(*handle*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#StringRef.__init__)

## StringReference

*class* StringReference[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#StringReference)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*bv: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *string_type: [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")*, *start: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#StringReference.__init__)
    :   Parameters:
        :   - **bv** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **string_type** ([*StringType*](enums.md#binaryninja.enums.StringType
              "binaryninja.enums.StringType")) –
            - **start** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **length** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

    *property* length*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* raw*: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*

    *property* start*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* type*: [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")*

    *property* value*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* view*: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*

## StructuredDataValue

*class* StructuredDataValue[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#StructuredDataValue)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    StructuredDataValue()

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    endian*: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*

    *property* int*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* str*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

    value*: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*

    *property* width*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## SymbolMapping

*class* SymbolMapping[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SymbolMapping)
:   Bases:
    [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping
    "(in Python v3.14)")

    SymbolMapping object is used to improve performance of the bv.symbols API. This allows
    pythonic code like this to have reasonable performance characteristics

    ```
    >>> my_symbols = get_my_symbols()
    >>> for symbol in my_symbols:
    >>>  if bv.symbols[symbol].address == 0x41414141:
    >>>    print("Found")
    ```

    __init__(*view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SymbolMapping.__init__)
    :   Parameters:
        :   **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SymbolMapping.get)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **default** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
              "binaryninja.types.CoreSymbol")*]* *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")] | *None*

    items() → a set-like object providing a view on D's items[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SymbolMapping.items)
    :   Return type:
        :   [*ItemsView*](https://docs.python.org/3/library/typing.html#typing.ItemsView "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"), [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")]]

    keys() → a set-like object providing a view on D's keys[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SymbolMapping.keys)
    :   Return type:
        :   [*KeysView*](https://docs.python.org/3/library/typing.html#typing.KeysView "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    values() → an object providing a view on D's values[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#SymbolMapping.values)
    :   Return type:
        :   [*ValuesView*](https://docs.python.org/3/library/typing.html#typing.ValuesView "(in
            Python v3.14)")[[*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")[[*CoreSymbol*](types.md#binaryninja.types.CoreSymbol
            "binaryninja.types.CoreSymbol")]]

## Tag

*class* Tag[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Tag)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `Tag` object is created by other APIs (create_*_tag) and should not be directly
    instantiated.

    __init__(*handle: LP_BNTag*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#Tag.__init__)
    :   Parameters:
        :   **handle** (*LP_BNTag*) –

    *property* data*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* type*: [TagType](#binaryninja.binaryview.TagType "binaryninja.binaryview.TagType")*

## TagType

*class* TagType[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TagType)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    The `TagType` object is created by the create_tag_type API and should not be directly
    instantiated.

    __init__(*handle: LP_BNTagType*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TagType.__init__)
    :   Parameters:
        :   **handle** (*LP_BNTagType*) –

    *property* icon*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Unicode str containing an emoji to be used as an icon

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Unique id of the TagType

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Name of the TagType

    *property* type*: [TagTypeType](enums.md#binaryninja.enums.TagTypeType "binaryninja.enums.TagTypeType")*
    :   Type from enums.TagTypeType

    *property* visible*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean for whether the tags of this type are visible

## TypeMapping

*class* TypeMapping[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypeMapping)
:   Bases:
    [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping
    "(in Python v3.14)")

    TypeMapping object is used to improve performance of the bv.types API. This allows
    pythonic code like this to have reasonable performance characteristics

    ```
    >>> my_types = get_my_types()
    >>> for type_name in my_types:
    >>>  if bv.types[type_name].width == 4:
    >>>    print("Found")
    ```

    __init__(*view: ~binaryninja.binaryview.BinaryView*, *get_list_fn=<function BNGetAnalysisTypeList>*)[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypeMapping.__init__)
    :   Parameters:
        :   **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
            "binaryninja.binaryview.BinaryView")) –

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypeMapping.get)

    items() → a set-like object providing a view on D's items[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypeMapping.items)

    keys() → a set-like object providing a view on D's keys[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypeMapping.keys)

    values() → an object providing a view on D's values[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypeMapping.values)

## TypedDataAccessor

*class* TypedDataAccessor[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypedDataAccessor)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    TypedDataAccessor(type: ‘_types.Type’, address: int, view: ‘BinaryView’, endian:
    binaryninja.enums.Endianness)

    __init__(*type: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *view: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **type** ([*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type")) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **view** ([*BinaryView*](#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness")) –

        Return type:
        :   *None*

    as_uuid(*ms_format: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypedDataAccessor.as_uuid)
    :   Converts the object to a UUID object using Microsoft byte ordering.

        Parameters:
        :   **ms_format** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
            Python v3.14)")) – Flag indicating whether to use Microsoft byte ordering. Default is
            True.

        Returns:
        :   The UUID object representing the byte array.

        Return type:
        :   [*UUID*](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in
            Python v3.14)") – If the byte array representation of this data is not exactly 16 bytes
            long.

    *static* byte_order(*endian*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypedDataAccessor.byte_order)
    :   Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    *static* int_from_bytes(*data: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sign: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *endian: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/binaryview.html#TypedDataAccessor.int_from_bytes)
    :   Parameters:
        :   - **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
              v3.14)")) –
            - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **sign** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **endian** ([*Endianness*](enums.md#binaryninja.enums.Endianness
              "binaryninja.enums.Endianness") *|* *None*) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    endian*: [Endianness](enums.md#binaryninja.enums.Endianness "binaryninja.enums.Endianness")*

    type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

    *property* value*: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*

    view*: [BinaryView](#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*

## TypedDataReader

TypedDataReader
:   alias of [`TypedDataAccessor`](#binaryninja.binaryview.TypedDataAccessor
    "binaryninja.binaryview.TypedDataAccessor")
