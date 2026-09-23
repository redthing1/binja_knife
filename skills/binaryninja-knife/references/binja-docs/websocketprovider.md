# websocketprovider module

| Class | Description |
| --- | --- |
| [`binaryninja.websocketprovider.WebsocketClient`](#binaryninja.websocketprovider.WebsocketClient "binaryninja.websocketprovider.WebsocketClient") | This class implements a websocket client. See [`connect`](#binaryninja.websocketprovider.WebsocketClient.connect "binaryninja.websocketprovider.WebsocketClient.connect") for more details. |
| [`binaryninja.websocketprovider.WebsocketProvider`](#binaryninja.websocketprovider.WebsocketProvider "binaryninja.websocketprovider.WebsocketProvider") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.websocketprovider.nop`](#binaryninja.websocketprovider.nop "binaryninja.websocketprovider.nop") |  |
| [`binaryninja.websocketprovider.to_bytes`](#binaryninja.websocketprovider.to_bytes "binaryninja.websocketprovider.to_bytes") |  |

## WebsocketClient

*class* WebsocketClient[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    This class implements a websocket client. See
    [`connect`](#binaryninja.websocketprovider.WebsocketClient.connect
    "binaryninja.websocketprovider.WebsocketClient.connect") for more details.

    __init__(*provider*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.__init__)

    connect(*url*, *headers=None*, *on_connected=<function nop>*, *on_disconnected=<function nop>*, *on_error=<function nop>*, *on_data=<function nop>*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.connect)
    :   Connect to a given url, asynchronously. The connection will be run in a separate thread
        managed by the websocket provider. Client callbacks are set according to whichever on_
        callback parameters you pass.

        Callbacks will be called **on the thread of the connection**, so be sure to
        execute_on_main_thread any long-running or gui operations in the callbacks.

        If the connection succeeds, on_connected will be called. On normal termination,
        on_disconnected will be called. If the connection succeeds, but later fails,
        on_disconnected will not be called, and on_error will be called instead. If the
        connection fails, neither on_connected nor on_disconnected will be called, and on_error
        will be called instead.

        If on_connected or on_data return false, the connection will be aborted.

        Parameters:
        :   - **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – full url with scheme, domain, optionally port, and path
            - **headers** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
              v3.14)")) – dictionary of string header keys to string header values
            - **on_connected** (*function**(**)* *-> bool*) – function to call when connection
              succeeds
            - **on_disconnected** (*function**(**)* *-> void*) – function to call when connection is
              closed normally
            - **on_error** (*function**(*[*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)")*)* *-> void*) – function to call when connection is closed with an
              error
            - **on_data**
              (*function**(*[*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")*)* *-> bool*) – function to call when data is read from the websocket

        Returns:
        :   if the connection has started, but not necessarily if it succeeded

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> provider = list(WebsocketProvider)[0]
            >>> client = provider.create_instance()
            >>> client.connect("ws://localhost:8080", {})
            True
            ```

    disconnect()[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.disconnect)
    :   Disconnect the websocket

        Returns:
        :   true if successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *abstract* perform_connect(*host*, *headers*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.perform_connect)

    *abstract* perform_destroy_client()[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.perform_destroy_client)

    *abstract* perform_disconnect()[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.perform_disconnect)

    *abstract* perform_write(*data*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.perform_write)

    write(*data*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketClient.write)
    :   Send some data to the websocket

        Parameters:
        :   **data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python
            v3.14)")) – data to write

        Returns:
        :   true if successful

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## WebsocketProvider

*class* WebsocketProvider[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketProvider)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketProvider.__init__)

    create_instance()[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketProvider.create_instance)

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#WebsocketProvider.register)

    instance_class *= None*

    name *= None*

## nop

nop(**args*, ***kwargs*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#nop)

## to_bytes

to_bytes(*field*)[[source]](https://api.binary.ninja/_modules/binaryninja/websocketprovider.html#to_bytes)
