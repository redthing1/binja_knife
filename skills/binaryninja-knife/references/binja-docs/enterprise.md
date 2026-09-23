# enterprise module

| Class | Description |
| --- | --- |
| [`binaryninja.enterprise.LicenseCheckout`](#binaryninja.enterprise.LicenseCheckout "binaryninja.enterprise.LicenseCheckout") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.enterprise.authenticate_with_credentials`](#binaryninja.enterprise.authenticate_with_credentials "binaryninja.enterprise.authenticate_with_credentials") | Authenticate to the Enterprise Server with username/password credentials. |
| [`binaryninja.enterprise.authenticate_with_method`](#binaryninja.enterprise.authenticate_with_method "binaryninja.enterprise.authenticate_with_method") | Authenticate to the Enterprise Server with a non-password method. Note that many of these will… |
| [`binaryninja.enterprise.authentication_methods`](#binaryninja.enterprise.authentication_methods "binaryninja.enterprise.authentication_methods") | Get a list of authentication methods accepted by the Enterprise Server. |
| [`binaryninja.enterprise.cancel_authentication`](#binaryninja.enterprise.cancel_authentication "binaryninja.enterprise.cancel_authentication") | Cancel a call to [`authenticate_with_credentials`](#binaryninja.enterprise.authenticate_with_credentials "binaryninja.enterprise.authenticate_with_credentials") or [`authenticate_with_method`](#binaryninja.enterprise.authenticate_with_method "binaryninja.enterprise.authenticate_with_method"). |
| [`binaryninja.enterprise.connect`](#binaryninja.enterprise.connect "binaryninja.enterprise.connect") | Connect to the Enterprise Server. |
| [`binaryninja.enterprise.deauthenticate`](#binaryninja.enterprise.deauthenticate "binaryninja.enterprise.deauthenticate") | Deauthenticate from the Enterprise server, clearing any cached credentials. |
| [`binaryninja.enterprise.initialize`](#binaryninja.enterprise.initialize "binaryninja.enterprise.initialize") | Initialize the Enterprise Client |
| [`binaryninja.enterprise.is_authenticated`](#binaryninja.enterprise.is_authenticated "binaryninja.enterprise.is_authenticated") | Determine if you have authenticated to the Enterprise Server. |
| [`binaryninja.enterprise.is_connected`](#binaryninja.enterprise.is_connected "binaryninja.enterprise.is_connected") | Determine if the Enterprise Server is currently connected. |
| [`binaryninja.enterprise.is_floating_license`](#binaryninja.enterprise.is_floating_license "binaryninja.enterprise.is_floating_license") | Determine if a floating license is currently active |
| [`binaryninja.enterprise.is_initialized`](#binaryninja.enterprise.is_initialized "binaryninja.enterprise.is_initialized") | Determine if the Enterprise Client has been initialized yet. |
| [`binaryninja.enterprise.is_license_still_activated`](#binaryninja.enterprise.is_license_still_activated "binaryninja.enterprise.is_license_still_activated") | Determine if your current license checkout is still valid. |
| [`binaryninja.enterprise.last_error`](#binaryninja.enterprise.last_error "binaryninja.enterprise.last_error") | Get a text representation the last error encountered by the Enterprise Client |
| [`binaryninja.enterprise.license_duration`](#binaryninja.enterprise.license_duration "binaryninja.enterprise.license_duration") | Get the duration of the current license checkout. |
| [`binaryninja.enterprise.license_expiration_time`](#binaryninja.enterprise.license_expiration_time "binaryninja.enterprise.license_expiration_time") | Get the expiry time of the current license checkout. |
| [`binaryninja.enterprise.release_license`](#binaryninja.enterprise.release_license "binaryninja.enterprise.release_license") | Release the currently checked out license back to the Enterprise Server. |
| [`binaryninja.enterprise.reservation_time_limit`](#binaryninja.enterprise.reservation_time_limit "binaryninja.enterprise.reservation_time_limit") | Get the maximum checkout duration allowed by the Enterprise Server. |
| [`binaryninja.enterprise.server_build_id`](#binaryninja.enterprise.server_build_id "binaryninja.enterprise.server_build_id") | Get the build id string of the server |
| [`binaryninja.enterprise.server_id`](#binaryninja.enterprise.server_id "binaryninja.enterprise.server_id") | Get the internal id of the server |
| [`binaryninja.enterprise.server_name`](#binaryninja.enterprise.server_name "binaryninja.enterprise.server_name") | Get the display name of the server |
| [`binaryninja.enterprise.server_url`](#binaryninja.enterprise.server_url "binaryninja.enterprise.server_url") | Get the url of the Enterprise Server. |
| [`binaryninja.enterprise.server_version`](#binaryninja.enterprise.server_version "binaryninja.enterprise.server_version") | Get the version number of the server |
| [`binaryninja.enterprise.set_server_url`](#binaryninja.enterprise.set_server_url "binaryninja.enterprise.set_server_url") | Set the url of the Enterprise Server. |
| [`binaryninja.enterprise.token`](#binaryninja.enterprise.token "binaryninja.enterprise.token") | Get the token of the currently authenticated user to the Enterprise Server. |
| [`binaryninja.enterprise.update_license`](#binaryninja.enterprise.update_license "binaryninja.enterprise.update_license") | Acquire or refresh a floating license from the Enterprise server. |
| [`binaryninja.enterprise.username`](#binaryninja.enterprise.username "binaryninja.enterprise.username") | Get the username of the currently authenticated user to the Enterprise Server. |

## LicenseCheckout

*class* LicenseCheckout[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#LicenseCheckout)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Helper class for scripts to make use of a license checkout in a scope.

    Parameters:
    :   - **duration** – Duration in seconds between refreshes
        - **_cache** – Deprecated but left in for compatibility
        - **release** – If the license should be released at the end of scope. If False, you can
          either manually release it later or it will expire after duration.

    Example:
    :   ```
        >>> enterprise.connect()
        >>> enterprise.authenticate_with_credentials("username", "password")
        >>> with enterprise.LicenseCheckout():
        ...     # Do some operation
        ...     with load("/bin/ls") as bv: # e.g.
        ...             print(hex(bv.start))
        # License is released at end of scope
        ```

    __init__(*duration: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 900*, *_cache: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *release: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#LicenseCheckout.__init__)
    :   Get a new license checkout

        Parameters:
        :   - **duration** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – Duration in seconds between refreshes
            - **_cache** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Deprecated but left in for compatibility
            - **release** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – If the license should be released at the end of scope. If False, you can
              either manually release it later or it will expire after duration.

    acquire()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#LicenseCheckout.acquire)

    release()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#LicenseCheckout.release)

## authenticate_with_credentials

authenticate_with_credentials(*username: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *password: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *remember: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#authenticate_with_credentials)
:   Authenticate to the Enterprise Server with username/password credentials.

    Parameters:
    :   - **username** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Username to use.
        - **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Password to use.
        - **remember** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – Remember token in keychain

## authenticate_with_method

authenticate_with_method(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *remember: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#authenticate_with_method)
:   Authenticate to the Enterprise Server with a non-password method. Note that many of
    these will open a URL for a browser-based login prompt, which may not be usable on
    headless installations. See
    [`authentication_methods`](#binaryninja.enterprise.authentication_methods
    "binaryninja.enterprise.authentication_methods") for a list of accepted methods.

    Parameters:
    :   - **method** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Name of method to use.
        - **remember** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – Remember token in keychain

## authentication_methods

authentication_methods() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#authentication_methods)
:   Get a list of authentication methods accepted by the Enterprise Server.

    Returns:
    :   List of (<method name>, <method display name>) tuples

    Return type:
    :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
        v3.14)")[[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
        Python v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")]]

## cancel_authentication

cancel_authentication()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#cancel_authentication)
:   Cancel a call to
    [`authenticate_with_credentials`](#binaryninja.enterprise.authenticate_with_credentials
    "binaryninja.enterprise.authenticate_with_credentials") or
    [`authenticate_with_method`](#binaryninja.enterprise.authenticate_with_method
    "binaryninja.enterprise.authenticate_with_method"). Note those functions are blocking,
    so this must be called on a separate thread.

## connect

connect()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#connect)
:   Connect to the Enterprise Server.

## deauthenticate

deauthenticate()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#deauthenticate)
:   Deauthenticate from the Enterprise server, clearing any cached credentials.

## initialize

initialize()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#initialize)
:   Initialize the Enterprise Client

## is_authenticated

is_authenticated() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#is_authenticated)
:   Determine if you have authenticated to the Enterprise Server.

    Returns:
    :   True if you are authenticated

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## is_connected

is_connected() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#is_connected)
:   Determine if the Enterprise Server is currently connected.

    Returns:
    :   True if connected

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## is_floating_license

is_floating_license() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#is_floating_license)
:   Determine if a floating license is currently active

    Returns:
    :   True if a floating license is active

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## is_initialized

is_initialized() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#is_initialized)
:   Determine if the Enterprise Client has been initialized yet.

    Returns:
    :   True if [`initialize`](#binaryninja.enterprise.initialize
        "binaryninja.enterprise.initialize") has been called

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## is_license_still_activated

is_license_still_activated() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#is_license_still_activated)
:   Determine if your current license checkout is still valid.

    Returns:
    :   True if your current checkout is still valid.

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## last_error

last_error() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#last_error)
:   Get a text representation the last error encountered by the Enterprise Client

    Returns:
    :   Last error message, or empty string if there is none.

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## license_duration

license_duration() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#license_duration)
:   Get the duration of the current license checkout.

    Returns:
    :   Duration, in seconds, of the total time of the current checkout.

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## license_expiration_time

license_expiration_time() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#license_expiration_time)
:   Get the expiry time of the current license checkout.

    Returns:
    :   Expiry time as a Unix epoch, or 0 if no license is checked out.

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## release_license

release_license()[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#release_license)
:   Release the currently checked out license back to the Enterprise Server.

    Note

    You must authenticate with the Enterprise Server before calling this.

    Note

    This will deactivate the Binary Ninja Enterprise client. You must call `acquire_license`
    again to continue using Binary Ninja Enterprise in the current process.

## reservation_time_limit

reservation_time_limit() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#reservation_time_limit)
:   Get the maximum checkout duration allowed by the Enterprise Server.

    Note

    You must authenticate with the Enterprise Server before calling this.

    Returns:
    :   Duration, in seconds, of the maximum time you are allowed to checkout a license.

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## server_build_id

server_build_id() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#server_build_id)
:   Get the build id string of the server

    Returns:
    :   Build id of the server

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## server_id

server_id() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#server_id)
:   Get the internal id of the server

    Returns:
    :   Id of the server

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## server_name

server_name() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#server_name)
:   Get the display name of the server

    Returns:
    :   Display name of the server

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## server_url

server_url() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#server_url)
:   Get the url of the Enterprise Server.

    Returns:
    :   The current url

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

## server_version

server_version() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#server_version)
:   Get the version number of the server

    Returns:
    :   Version of the server

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## set_server_url

set_server_url(*url: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#set_server_url)
:   Set the url of the Enterprise Server.

    Note

    This will raise an Exception if the server is already initialized

    Parameters:
    :   **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – New Enterprise Server url

## token

token() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#token)
:   Get the token of the currently authenticated user to the Enterprise Server.

    Returns:
    :   Token, if authenticated. None, otherwise.

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
        *None*

## update_license

update_license(*duration*, *_cache=True*)[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#update_license)
:   Acquire or refresh a floating license from the Enterprise server.

    Note

    You must authenticate with the Enterprise server before calling this.

    Parameters:
    :   - **duration** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
          v3.14)")) – Desired length of license checkout, in seconds.
        - **_cache** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – Deprecated but left in for compatibility

## username

username() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/enterprise.html#username)
:   Get the username of the currently authenticated user to the Enterprise Server.

    Returns:
    :   Username, if authenticated. None, otherwise.

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
        *None*
