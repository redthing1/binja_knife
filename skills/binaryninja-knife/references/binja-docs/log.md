# log module

| Class | Description |
| --- | --- |
| [`binaryninja.log.Logger`](#binaryninja.log.Logger "binaryninja.log.Logger") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.log.close_logs`](#binaryninja.log.close_logs "binaryninja.log.close_logs") | `close_logs` close all log files. |
| [`binaryninja.log.is_output_redirected_to_log`](#binaryninja.log.is_output_redirected_to_log "binaryninja.log.is_output_redirected_to_log") |  |
| [`binaryninja.log.log`](#binaryninja.log.log "binaryninja.log.log") | `log` writes messages to the log console for the given log level. |
| [`binaryninja.log.log_alert`](#binaryninja.log.log_alert "binaryninja.log.log_alert") | `log_alert` Logs message console and to a pop up window if run through the GUI. |
| [`binaryninja.log.log_alert_for_exception`](#binaryninja.log.log_alert_for_exception "binaryninja.log.log_alert_for_exception") | `log_alert_for_exception` Logs message console, including a stack trace for the current exception. |
| [`binaryninja.log.log_alert_with_traceback`](#binaryninja.log.log_alert_with_traceback "binaryninja.log.log_alert_with_traceback") | `log_alert_with_traceback` Logs message console, including a stack trace. A pop up window is… |
| [`binaryninja.log.log_debug`](#binaryninja.log.log_debug "binaryninja.log.log_debug") | `log_debug` Logs debugging information messages to the console. |
| [`binaryninja.log.log_debug_for_exception`](#binaryninja.log.log_debug_for_exception "binaryninja.log.log_debug_for_exception") | `log_debug_for_exception` Logs debugging information messages to the console, including a… |
| [`binaryninja.log.log_debug_with_traceback`](#binaryninja.log.log_debug_with_traceback "binaryninja.log.log_debug_with_traceback") | `log_debug_with_traceback` Logs debugging information messages to the console, including a… |
| [`binaryninja.log.log_error`](#binaryninja.log.log_error "binaryninja.log.log_error") | `log_error` Logs message to console, if run through the GUI it logs with **Error** icon,… |
| [`binaryninja.log.log_error_for_exception`](#binaryninja.log.log_error_for_exception "binaryninja.log.log_error_for_exception") | `log_error_for_exception` Logs message to console, including a stack trace for the current… |
| [`binaryninja.log.log_error_with_traceback`](#binaryninja.log.log_error_with_traceback "binaryninja.log.log_error_with_traceback") | `log_error_with_traceback` Logs message to console, including a stack trace. When run through… |
| [`binaryninja.log.log_for_exception`](#binaryninja.log.log_for_exception "binaryninja.log.log_for_exception") | `log_for_exception` writes messages to the log console for the given log level, including a… |
| [`binaryninja.log.log_info`](#binaryninja.log.log_info "binaryninja.log.log_info") | `log_info` Logs general information messages to the console. |
| [`binaryninja.log.log_info_for_exception`](#binaryninja.log.log_info_for_exception "binaryninja.log.log_info_for_exception") | `log_info_for_exception` Logs general information messages to the console, including a stack… |
| [`binaryninja.log.log_info_with_traceback`](#binaryninja.log.log_info_with_traceback "binaryninja.log.log_info_with_traceback") | `log_info_with_traceback` Logs general information messages to the console, including a stack… |
| [`binaryninja.log.log_to_file`](#binaryninja.log.log_to_file "binaryninja.log.log_to_file") | `log_to_file` redirects minimum log level to a file named `path`, optionally appending… |
| [`binaryninja.log.log_to_stderr`](#binaryninja.log.log_to_stderr "binaryninja.log.log_to_stderr") | `log_to_stderr` redirects minimum log level to standard error. |
| [`binaryninja.log.log_to_stdout`](#binaryninja.log.log_to_stdout "binaryninja.log.log_to_stdout") | `log_to_stdout` redirects minimum log level to standard out. |
| [`binaryninja.log.log_warn`](#binaryninja.log.log_warn "binaryninja.log.log_warn") | `log_warn` Logs message to console, if run through the GUI it logs with **Warning** icon. |
| [`binaryninja.log.log_warn_for_exception`](#binaryninja.log.log_warn_for_exception "binaryninja.log.log_warn_for_exception") | `log_warn_for_exception` Logs message to console, including a stack trace for the current… |
| [`binaryninja.log.log_warn_with_traceback`](#binaryninja.log.log_warn_with_traceback "binaryninja.log.log_warn_with_traceback") | `log_warn_with_traceback` Logs message to console, including a stack trace. When run through… |
| [`binaryninja.log.log_with_traceback`](#binaryninja.log.log_with_traceback "binaryninja.log.log_with_traceback") | `log_with_traceback` writes messages to the log console for the given log level, including a… |
| [`binaryninja.log.redirect_output_to_log`](#binaryninja.log.redirect_output_to_log "binaryninja.log.redirect_output_to_log") |  |

## Logger

*class* Logger[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*session_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *logger_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.__init__)
    :   Parameters:
        :   - **session_id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)"))
            - **logger_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

    log(*level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log)
    :   Parameters:
        :   - **level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
              "binaryninja.enums.LogLevel"))
            - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    log_alert(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_alert)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_alert_for_exception(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_alert_for_exception)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_alert_with_traceback(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_alert_with_traceback)
    :   Parameters:
        :   - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

    log_debug(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_debug)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_debug_for_exception(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_debug_for_exception)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_debug_with_traceback(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_debug_with_traceback)
    :   Parameters:
        :   - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

    log_error(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_error)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_error_for_exception(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_error_for_exception)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_error_with_traceback(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_error_with_traceback)
    :   Parameters:
        :   - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

    log_for_exception(*level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_for_exception)
    :   Parameters:
        :   - **level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
              "binaryninja.enums.LogLevel"))
            - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    log_info(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_info)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_info_for_exception(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_info_for_exception)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_info_with_traceback(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_info_with_traceback)
    :   Parameters:
        :   - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

    log_warn(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_warn)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_warn_for_exception(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_warn_for_exception)
    :   Parameters:
        :   **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   *None*

    log_warn_with_traceback(*message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_warn_with_traceback)
    :   Parameters:
        :   - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

    log_with_traceback(*level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *message: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#Logger.log_with_traceback)
    :   Parameters:
        :   - **level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
              "binaryninja.enums.LogLevel"))
            - **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

        Return type:
        :   *None*

## close_logs

close_logs()[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#close_logs)
:   `close_logs` close all log files.

    Return type:
    :   *None*

## is_output_redirected_to_log

is_output_redirected_to_log()[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#is_output_redirected_to_log)

## log

log(*level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *session: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log)
:   `log` writes messages to the log console for the given log level.

    > | LogLevelName | LogLevel | Description |
    > | --- | --- | --- |
    > | DebugLog | 0 | Logs debugging information messages to the console. |
    > | InfoLog | 1 | Logs general information messages to the console. |
    > | WarningLog | 2 | Logs message to console with **Warning** icon. |
    > | ErrorLog | 3 | Logs message to console with **Error** icon, focusing the error console. |
    > | AlertLog | 4 | Logs message to pop up window. |

    Parameters:
    :   - **level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
          "binaryninja.enums.LogLevel")) – Log level to use
        - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))
        - **session** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_alert

log_alert(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_alert)
:   `log_alert` Logs message console and to a pop up window if run through the GUI.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

    Example:
    :   ```
        >>> log_to_stdout(LogLevel.DebugLog)
        >>> log_alert("Kielbasa!")
        Kielbasa!
        >>>
        ```

## log_alert_for_exception

log_alert_for_exception(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_alert_for_exception)
:   `log_alert_for_exception` Logs message console, including a stack trace for the current
    exception. A pop up window is created if run through the GUI.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_alert_with_traceback

log_alert_with_traceback(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_alert_with_traceback)
:   `log_alert_with_traceback` Logs message console, including a stack trace. A pop up
    window is created if run through the GUI.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – optional explicit trace string to attach; if omitted, the current Python
          stack is used.
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_debug

log_debug(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_debug)
:   `log_debug` Logs debugging information messages to the console.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

    Example:
    :   ```
        >>> log_to_stdout(LogLevel.DebugLog)
        >>> log_debug("Hotdogs!")
        Hotdogs!
        ```

## log_debug_for_exception

log_debug_for_exception(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_debug_for_exception)
:   `log_debug_for_exception` Logs debugging information messages to the console, including
    a stack trace for the current exception.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_debug_with_traceback

log_debug_with_traceback(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_debug_with_traceback)
:   `log_debug_with_traceback` Logs debugging information messages to the console, including
    a stack trace.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – optional explicit trace string to attach; if omitted, the current Python
          stack is used.
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_error

log_error(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_error)
:   `log_error` Logs message to console, if run through the GUI it logs with **Error** icon,
    focusing the error console.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

    Example:
    :   ```
        >>> log_to_stdout(LogLevel.DebugLog)
        >>> log_error("Spanferkel!")
        Spanferkel!
        >>>
        ```

## log_error_for_exception

log_error_for_exception(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_error_for_exception)
:   `log_error_for_exception` Logs message to console, including a stack trace for the
    current exception. When run through the GUI it logs with **Error** icon, focusing the
    error console.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_error_with_traceback

log_error_with_traceback(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_error_with_traceback)
:   `log_error_with_traceback` Logs message to console, including a stack trace. When run
    through the GUI it logs with **Error** icon, focusing the error console.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – optional explicit trace string to attach; if omitted, the current Python
          stack is used.
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_for_exception

log_for_exception(*level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *session: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_for_exception)
:   `log_for_exception` writes messages to the log console for the given log level,
    including a stack trace for the current exception.

    > | LogLevelName | LogLevel | Description |
    > | --- | --- | --- |
    > | DebugLog | 0 | Logs debugging information messages to the console. |
    > | InfoLog | 1 | Logs general information messages to the console. |
    > | WarningLog | 2 | Logs message to console with **Warning** icon. |
    > | ErrorLog | 3 | Logs message to console with **Error** icon, focusing the error console. |
    > | AlertLog | 4 | Logs message to pop up window. |

    Parameters:
    :   - **level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
          "binaryninja.enums.LogLevel")) – Log level to use
        - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))
        - **session** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_info

log_info(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_info)
:   `log_info` Logs general information messages to the console.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

    Example:
    :   ```
        >>> log_info("Saucisson!")
        Saucisson!
        >>>
        ```

## log_info_for_exception

log_info_for_exception(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_info_for_exception)
:   `log_info_for_exception` Logs general information messages to the console, including a
    stack trace for the current exception.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_info_with_traceback

log_info_with_traceback(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_info_with_traceback)
:   `log_info_with_traceback` Logs general information messages to the console, including a
    stack trace.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – optional explicit trace string to attach; if omitted, the current Python
          stack is used.
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_to_file

log_to_file(*min_level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *append: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_to_file)
:   `log_to_file` redirects minimum log level to a file named `path`, optionally appending
    rather than overwriting.

    Parameters:
    :   - **min_level** (*enums.Log_Level*) – minimum level to log
        - **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – path to log to
        - **append** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – optional flag for specifying appending. True = append, False = overwrite.

    Return type:
    :   *None*

## log_to_stderr

log_to_stderr(*min_level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_to_stderr)
:   `log_to_stderr` redirects minimum log level to standard error.

    Parameters:
    :   **min_level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
        "binaryninja.enums.LogLevel")) – minimum level to log to

    Return type:
    :   *None*

## log_to_stdout

log_to_stdout(*min_level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel") = LogLevel.InfoLog*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_to_stdout)
:   `log_to_stdout` redirects minimum log level to standard out.

    Parameters:
    :   **min_level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
        "binaryninja.enums.LogLevel")) – minimum level to log to

    Return type:
    :   *None*

    Example:
    :   ```
        >>> log_debug("Hotdogs!")
        >>> log_to_stdout(LogLevel.DebugLog)
        >>> log_debug("Hotdogs!")
        Hotdogs!
        >>>
        ```

## log_warn

log_warn(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_warn)
:   `log_warn` Logs message to console, if run through the GUI it logs with **Warning**
    icon.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

    Example:
    :   ```
        >>> log_to_stdout(LogLevel.DebugLog)
        >>> log_warn("Chilidogs!")
        Chilidogs!
        >>>
        ```

## log_warn_for_exception

log_warn_for_exception(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_warn_for_exception)
:   `log_warn_for_exception` Logs message to console, including a stack trace for the
    current exception. When run through the GUI it logs with **Warning** icon.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_warn_with_traceback

log_warn_with_traceback(*text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_warn_with_traceback)
:   `log_warn_with_traceback` Logs message to console, including a stack trace. When run
    through the GUI it logs with **Warning** icon.

    Parameters:
    :   - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – optional explicit trace string to attach; if omitted, the current Python
          stack is used.
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))

    Return type:
    :   *None*

## log_with_traceback

log_with_traceback(*level: [LogLevel](enums.md#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel")*, *text: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *logger: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *session: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *stack_trace: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#log_with_traceback)
:   `log_with_traceback` writes messages to the log console for the given log level,
    including a stack trace.

    > | LogLevelName | LogLevel | Description |
    > | --- | --- | --- |
    > | DebugLog | 0 | Logs debugging information messages to the console. |
    > | InfoLog | 1 | Logs general information messages to the console. |
    > | WarningLog | 2 | Logs message to console with **Warning** icon. |
    > | ErrorLog | 3 | Logs message to console with **Error** icon, focusing the error console. |
    > | AlertLog | 4 | Logs message to pop up window. |

    Parameters:
    :   - **level** ([*LogLevel*](enums.md#binaryninja.enums.LogLevel
          "binaryninja.enums.LogLevel")) – Log level to use
        - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – message to print
        - **stack_trace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – optional explicit trace string to attach (shown behind the log entry’s
          “Details…” link). If omitted, the current Python stack is used. Callers can pass
          subprocess output, a decoded exception, etc.
        - **logger** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))
        - **session** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
          v3.14)"))

    Return type:
    :   *None*

## redirect_output_to_log

redirect_output_to_log()[[source]](https://api.binary.ninja/_modules/binaryninja/log.html#redirect_output_to_log)
