# component module

| Class | Description |
| --- | --- |
| [`binaryninja.component.Component`](#binaryninja.component.Component "binaryninja.component.Component") | Components are objects that can contain Functions and other Components. |

## Component

*class* Component[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Components are objects that can contain Functions and other Components.

    They can be queried for information about the functions contained within them.

    Components have a Guid, which persistent across saves and loads of the database, and
    should be used for retrieving components when such is required and a reference to the
    Component cannot be held.

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.__init__)

    add_component(*component: [Component](#binaryninja.component.Component "binaryninja.component.Component")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.add_component)
    :   Move component to this component. This will remove it from the old parent.

        Parameters:
        :   **component** ([*Component*](#binaryninja.component.Component
            "binaryninja.component.Component")) – Component to add to this component.

        Returns:
        :   True if the component was successfully moved to this component

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    add_data_variable(*data_variable*)[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.add_data_variable)

    add_function(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.add_function)
    :   Add function to this component.

        Parameters:
        :   **func** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) – Function to add

        Returns:
        :   True if function was successfully added.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    contains_component(*component: [Component](#binaryninja.component.Component "binaryninja.component.Component")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.contains_component)
    :   Check whether this component contains a component.

        Parameters:
        :   **component** ([*Component*](#binaryninja.component.Component
            "binaryninja.component.Component")) – Component to check

        Returns:
        :   True if this component contains the component.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    contains_data_variable(*data_variable*)[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.contains_data_variable)

    contains_function(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.contains_function)
    :   Check whether this component contains a function.

        Parameters:
        :   **func** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) – Function to check

        Returns:
        :   True if this component contains the function.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_referenced_data_variables(*recursive=False*)[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.get_referenced_data_variables)
    :   Get data variables referenced by this component

        Parameters:
        :   **recursive** – Optional; Get all DataVariables referenced by this component and
            sub-components.

        Returns:
        :   List of DataVariables

    get_referenced_types(*recursive=False*)[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.get_referenced_types)
    :   Get Types referenced by this component

        Parameters:
        :   **recursive** – Optional; Get all Types referenced by this component and sub-components.

        Returns:
        :   List of Types

    remove_component(*component: [Component](#binaryninja.component.Component "binaryninja.component.Component")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.remove_component)
    :   Remove a component from the current component, moving it to the root.

        This function has no effect when used from the root component. Use
        BinaryView.remove_component to Remove a component from the tree entirely.

        Parameters:
        :   **component** ([*Component*](#binaryninja.component.Component
            "binaryninja.component.Component")) – Component to remove

        Returns:

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    remove_data_variable(*data_variable*)[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.remove_data_variable)

    remove_function(*func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/component.html#Component.remove_function)
    :   Remove function from this component.

        Parameters:
        :   **func** ([*Function*](function.md#binaryninja.function.Function
            "binaryninja.function.Function")) – Function to remove

        Returns:
        :   True if function was successfully removed.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* components*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Component](#binaryninja.component.Component "binaryninja.component.Component")]*
    :   `components` is an iterator for all Components contained within this Component

        Returns:
        :   A list of components

        Example:
        :   ```
            >>> for subcomp in component.components:
            ...  print(repr(component))
            ```

    *property* data_variable_list

    *property* data_variables

    *property* display_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Original Name of the component (read-only)

    *property* function_list*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function")]*
    :   `function_list` List of all Functions contained within this Component

        Warning:
        :   .functions Should be used instead of this in any performance sensitive context.

        Returns:
        :   A list of functions

        Example:
        :   ```
            >>> for func in component.functions:
            ...  print(func.name)
            ```

    *property* functions*: [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Function](function.md#binaryninja.function.Function "binaryninja.function.Function")]*
    :   `functions` is an iterator for all Functions contained within this Component

        Returns:
        :   An iterator containing Components

        Return type:
        :   ComponentIterator

        Example:
        :   ```
            >>> for func in component.functions:
            ...  print(func.name)
            ```

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Original name set for this component

        Note:
        :   The .display_name property should be used for bv.get_component_by_path() lookups.

        This can differ from the .display_name property if one of its sibling components has the
        same .original_name; In that case, .name will be an automatically generated unique name
        (e.g. “MyComponentName (1)”) while .original_name will remain what was originally set
        (e.g. “MyComponentName”)

        If this component has a duplicate name and is moved to a component where none of its
        siblings share its name, the .name property will return the original “MyComponentName”

    *property* parent*: [Component](#binaryninja.component.Component "binaryninja.component.Component") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   The component that contains this component, if it exists.

    *property* view
