# deprecation module

| Class | Description |
| --- | --- |
| [`binaryninja.deprecation.DeprecatedWarning`](#binaryninja.deprecation.DeprecatedWarning "binaryninja.deprecation.DeprecatedWarning") | A warning class for deprecated methods |
| [`binaryninja.deprecation.UnsupportedWarning`](#binaryninja.deprecation.UnsupportedWarning "binaryninja.deprecation.UnsupportedWarning") | A warning class for methods to be removed |

| Function | Description |
| --- | --- |
| [`binaryninja.deprecation.deprecated`](#binaryninja.deprecation.deprecated "binaryninja.deprecation.deprecated") | Decorate a function to signify its deprecation |
| [`binaryninja.deprecation.fail_if_not_removed`](#binaryninja.deprecation.fail_if_not_removed "binaryninja.deprecation.fail_if_not_removed") | Decorate a test method to track removal of deprecated code |
| [`binaryninja.deprecation.parse_version`](#binaryninja.deprecation.parse_version "binaryninja.deprecation.parse_version") |  |

## DeprecatedWarning

*exception* DeprecatedWarning[[source]](https://api.binary.ninja/_modules/binaryninja/deprecation.html#DeprecatedWarning)
:   Bases:
    [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning
    "(in Python v3.14)")

    A warning class for deprecated methods

    This is a specialization of the built-in
    [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning
    "(in Python v3.14)"), adding parameters that allow us to get information into the
    __str__ that ends up being sent through the
    [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python
    v3.14)") system. The attributes aren’t able to be retrieved after the warning gets
    raised and passed through the system as only the class–not the instance–and message are
    what gets preserved.

    Parameters:
    :   - **function** – The function being deprecated.
        - **deprecated_in** – The version that `function` is deprecated in
        - **removed_in** – The version or
          [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in
          Python v3.14)") specifying when `function` gets removed.
        - **details** – Optional details about the deprecation. Most often this will include
          directions on what to use instead of the now deprecated code.

    __init__(*function*, *deprecated_in*, *removed_in*, *details=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/deprecation.html#DeprecatedWarning.__init__)

## UnsupportedWarning

*exception* UnsupportedWarning[[source]](https://api.binary.ninja/_modules/binaryninja/deprecation.html#UnsupportedWarning)
:   Bases: [`DeprecatedWarning`](#binaryninja.deprecation.DeprecatedWarning
    "binaryninja.deprecation.DeprecatedWarning")

    A warning class for methods to be removed

    This is a subclass of `DeprecatedWarning` and is used to output a proper message about a
    function being unsupported. Additionally, the `fail_if_not_removed` decorator will
    handle this warning and cause any tests to fail if the system under test uses code that
    raises this warning.

## deprecated

deprecated(*deprecated_in: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *removed_in=None*, *current_version=None*, *details=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/deprecation.html#deprecated)
:   Decorate a function to signify its deprecation

    This function wraps a method that will soon be removed and does two things:

    > - The docstring of the method will be modified to include a notice about deprecation,
    >   e.g., “Deprecated since 0.9.11. Use foo instead.”
    > - Raises a `DeprecatedWarning` via the
    >   [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python
    >   v3.14)") module, which is a subclass of the built-in
    >   [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning
    >   "(in Python v3.14)"). Note that built-in
    >   [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning
    >   "(in Python v3.14)") are ignored by default, so for users to be informed of said
    >   warnings they will need to enable them–see the
    >   [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python
    >   v3.14)") module documentation for more details.

    Parameters:
    :   - **deprecated_in** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – The version at which the decorated method is considered deprecated.
          This will usually be the next version to be released when the decorator is added.
        - **removed_in** – The version or
          [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in
          Python v3.14)") when the decorated method will be removed. The default is **None**,
          specifying that the function is not currently planned to be removed.
        - **current_version** – The source of version information for the currently running code.
          This will usually be a __version__ attribute on your library. The default is None. When
          current_version=None the automation to determine if the wrapped function is actually in
          a period of deprecation or time for removal does not work, causing a `DeprecatedWarning`
          to be raised in all cases.
        - **details** – Extra details to be added to the method docstring and warning. For
          example, the details may point users to a replacement method, such as “Use the foo_bar
          method instead”. By default there are no details.

## fail_if_not_removed

fail_if_not_removed(*method*)[[source]](https://api.binary.ninja/_modules/binaryninja/deprecation.html#fail_if_not_removed)
:   Decorate a test method to track removal of deprecated code

    This decorator catches `UnsupportedWarning` warnings that occur during testing and
    causes unittests to fail, making it easier to keep track of when code should be removed.

    Raises:
    :   [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "(in
        Python v3.14)") if an `UnsupportedWarning` is raised while running the test method.

## parse_version

parse_version(*version: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/deprecation.html#parse_version)
:   Parameters:
    :   **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)"))

    Return type:
    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
