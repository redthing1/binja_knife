# mainthread module

This module provides two ways to execute “jobs”:

1. On the Binary Ninja main thread (the UI event thread when running in the GUI application):
   :   - [`execute_on_main_thread`](#binaryninja.mainthread.execute_on_main_thread
         "binaryninja.mainthread.execute_on_main_thread")
       - [`execute_on_main_thread_and_wait`](#binaryninja.mainthread.execute_on_main_thread_and_wait
         "binaryninja.mainthread.execute_on_main_thread_and_wait")
2. On a worker thread

Any manipulation of the GUI should be performed on the main thread, but any non-GUI work
is generally better to be performed using a worker. This is especially true for any
longer-running work, as the user interface will be unable to update itself while a job
is executing on the main thread.

There are three worker queues, in order of decreasing priority:

> 1. The Interactive Queue
>    ([`worker_interactive_enqueue`](#binaryninja.mainthread.worker_interactive_enqueue
>    "binaryninja.mainthread.worker_interactive_enqueue"))
> 2. The Priority Queue
>    ([`worker_priority_enqueue`](#binaryninja.mainthread.worker_priority_enqueue
>    "binaryninja.mainthread.worker_priority_enqueue"))
> 3. The Worker Queue ([`worker_enqueue`](#binaryninja.mainthread.worker_enqueue
>    "binaryninja.mainthread.worker_enqueue"))

All of these queues are serviced by the same pool of worker threads. The difference
between the queues is basically one of priority: one queue must be empty of jobs before
a worker thread will execute a job from a lower priority queue.

The default maximum number of concurrent worker threads is controlled by the
analysis.limits.workerThreadCount setting but can be adjusted at runtime via
[`set_worker_thread_count`](#binaryninja.mainthread.set_worker_thread_count
"binaryninja.mainthread.set_worker_thread_count").

The worker threads are native threads, managed by the Binary Ninja core. If more control
over the thread is required, consider using the
[`BackgroundTaskThread`](plugin.md#binaryninja.plugin.BackgroundTaskThread
"binaryninja.plugin.BackgroundTaskThread") class.

| Function | Description |
| --- | --- |
| [`binaryninja.mainthread.execute_on_main_thread`](#binaryninja.mainthread.execute_on_main_thread "binaryninja.mainthread.execute_on_main_thread") | The `execute_on_main_thread` function takes a single parameter which is a function that will… |
| [`binaryninja.mainthread.execute_on_main_thread_and_wait`](#binaryninja.mainthread.execute_on_main_thread_and_wait "binaryninja.mainthread.execute_on_main_thread_and_wait") | The `execute_on_main_thread` function takes a single parameter which is a function that will… |
| [`binaryninja.mainthread.get_worker_thread_count`](#binaryninja.mainthread.get_worker_thread_count "binaryninja.mainthread.get_worker_thread_count") | The `get_worker_thread_count` function returns the number of worker threads that are currently… |
| [`binaryninja.mainthread.is_main_thread`](#binaryninja.mainthread.is_main_thread "binaryninja.mainthread.is_main_thread") |  |
| [`binaryninja.mainthread.set_worker_thread_count`](#binaryninja.mainthread.set_worker_thread_count "binaryninja.mainthread.set_worker_thread_count") | The `set_worker_thread_count` function sets the number of worker threads that are currently… |
| [`binaryninja.mainthread.worker_enqueue`](#binaryninja.mainthread.worker_enqueue "binaryninja.mainthread.worker_enqueue") |  |
| [`binaryninja.mainthread.worker_interactive_enqueue`](#binaryninja.mainthread.worker_interactive_enqueue "binaryninja.mainthread.worker_interactive_enqueue") |  |
| [`binaryninja.mainthread.worker_priority_enqueue`](#binaryninja.mainthread.worker_priority_enqueue "binaryninja.mainthread.worker_priority_enqueue") |  |

## execute_on_main_thread

execute_on_main_thread(*func*)[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#execute_on_main_thread)
:   The `execute_on_main_thread` function takes a single parameter which is a function that
    will be executed on the main Binary Ninja thread.

    > Warning
    >
    > May be required for some GUI operations, but should be used sparingly as it can block
    > the UI.
    >
    > Example:
    > :   ```
    >     >>> # Execute a GUI operation on the main thread
    >     >>> import binaryninjaui
    >     >>> from binaryninja import execute_on_main_thread
    >     >>> execute_on_main_thread(lambda: binaryninjaui.UIContext.activeContext().openFileContext(context))
    >     ```

## execute_on_main_thread_and_wait

execute_on_main_thread_and_wait(*func*)[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#execute_on_main_thread_and_wait)
:   The `execute_on_main_thread` function takes a single parameter which is a function that
    will be executed on the main Binary Ninja thread and will block execution of further
    python until the function returns.

    > Warning
    >
    > May be required for some GUI operations, but should be used sparingly as it can block
    > the UI.
    >
    > Example:
    > :   ```
    >     >>> # Execute a GUI operation and wait for it to complete
    >     >>> import binaryninjaui
    >     >>> from binaryninja import execute_on_main_thread_and_wait
    >     >>> execute_on_main_thread_and_wait(lambda: binaryninjaui.UIContext.activeContext().rebaseCurrentView(0x800000))
    >     ```

## get_worker_thread_count

get_worker_thread_count()[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#get_worker_thread_count)
:   The `get_worker_thread_count` function returns the number of worker threads that are
    currently running. By default, this is the number of cores on the system minus one,
    however this can be changed with `set_worker_thread_count`.

## is_main_thread

is_main_thread()[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#is_main_thread)

## set_worker_thread_count

set_worker_thread_count(*count*)[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#set_worker_thread_count)
:   The `set_worker_thread_count` function sets the number of worker threads that are
    currently running. By default, this is the number of cores on the system minus one.

## worker_enqueue

worker_enqueue(*func*, *name=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#worker_enqueue)

## worker_interactive_enqueue

worker_interactive_enqueue(*func*, *name=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#worker_interactive_enqueue)

## worker_priority_enqueue

worker_priority_enqueue(*func*, *name=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/mainthread.html#worker_priority_enqueue)
