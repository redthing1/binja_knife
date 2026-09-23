# settings module

| Class | Description |
| --- | --- |
| [`binaryninja.settings.Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings") | [`Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings") provides a way to define and access settings in a hierarchical fashion. |

## Settings

*class* Settings[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    [`Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings") provides a
    way to define and access settings in a hierarchical fashion. The value of a setting can
    be defined for each hierarchical level, where each level overrides the preceding level.
    The backing-store for setting values at each level is also configurable. This allows for
    ephemeral or platform-independent persistent settings storage for components within
    Binary Ninja or consumers of the Binary Ninja API.

    Each [`Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings")
    instance has an `instance_id` which identifies a schema. The schema defines the settings
    contents and the way in which settings are retrieved and manipulated. A new
    [`Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings") instance
    defaults to using a value of *‘default’* for the `instance_id`. The *‘default’* settings
    schema defines all of the settings available for the active Binary Ninja components
    which include at a minimum, the settings defined by the Binary Ninja core. The
    *‘default’* schema may additionally define settings for the UI and/or installed plugins.
    Extending existing schemas, or defining new ones is accomplished by calling
    [`register_group`](#binaryninja.settings.Settings.register_group
    "binaryninja.settings.Settings.register_group") and
    [`register_setting`](#binaryninja.settings.Settings.register_setting
    "binaryninja.settings.Settings.register_setting") methods, or by deserializing an
    existing schema with
    [`deserialize_schema`](#binaryninja.settings.Settings.deserialize_schema
    "binaryninja.settings.Settings.deserialize_schema").

    Note

    All settings in the *‘default’* settings schema are rendered with UI elements in the
    Settings View of Binary Ninja UI.

    Allowing setting overrides is an important feature and Binary Ninja accomplishes this by
    allowing one to override a setting at various levels. The levels and their associated
    storage are shown in the following table. Default setting values are optional, and if
    specified, saved in the schema itself.

    > | Setting Level | Settings Scope | Preference | Storage |
    > | --- | --- | --- | --- |
    > | Default | SettingsDefaultScope | Lowest | Settings Schema |
    > | User | SettingsUserScope |  | <User Directory>/settings.json |
    > | Project | SettingsProjectScope |  | <Project Directory>/settings.json |
    > | Resource | SettingsResourceScope | Highest | Raw BinaryView (Storage in BNDB) |

    Settings are identified by a key, which is a string in the form of **‘<group>.<name>’**
    or **‘<group>.<subGroup>.<name>’**. Groups provide a simple way to categorize settings.
    Sub-groups are optional and multiple sub-groups are allowed. When defining a settings
    group, the [`register_group`](#binaryninja.settings.Settings.register_group
    "binaryninja.settings.Settings.register_group") method allows for specifying a UI
    friendly title for use in the Binary Ninja UI. Defining a new setting requires a unique
    setting key and a JSON string of property, value pairs. The following table describes
    the available properties and values.

    > | Property | JSON Data Type | Prerequisite | Optional | {Allowed Values} and Notes |
    > | --- | --- | --- | --- | --- |
    > | “title” | string | None | No | Concise Setting Title |
    > | “type” | string | None | No | {“array”, “boolean”, “number”, “string”, “object”} |
    > | “sorted” | boolean | “type” is “array” | Yes | Automatically sort list items (default is false) |
    > | “isSerialized” | boolean | “type” is “string” | Yes | Treat the string as a serialized JSON object |
    > | “enum” | array : {string} | “type” is “string” | Yes | Enumeration definitions |
    > | “enumDescriptions” | array : {string} | “type” is “string” | Yes | Enumeration descriptions that match “enum” array |
    > | “minValue” | number | “type” is “number” | Yes | Specify 0 to infer unsigned (default is signed) |
    > | “maxValue” | number | “type” is “number” | Yes | Values less than or equal to INT_MAX result in a QSpinBox UI element |
    > | “precision” | number | “type” is “number” | Yes | Specify precision for a QDoubleSpinBox |
    > | “default” | {array, boolean, number, string, null} | None | Yes | Specify optimal default value |
    > | “aliases” | array : {string} | None | Yes | Array of deprecated setting key(s) |
    > | “description” | string | None | No | Detailed setting description |
    > | “ignore” | array : {string} | None | Yes | {“SettingsUserScope”, “SettingsProjectScope”, “SettingsResourceScope”} |
    > | “message” | string | None | Yes | An optional message with additional emphasis |
    > | “readOnly” | boolean | None | Yes | Only enforced by UI elements |
    > | “optional” | boolean | None | Yes | Indicates setting can be null |
    > | “hidden” | bool | “type” is “string” | Yes | Indicates the UI should conceal the content. The “ignore” property is required to specify the applicable storage scopes |
    > | “requiresRestart” | boolean | None | Yes | Enable restart notification in the UI upon change |
    > | “uiSelectionAction” | string | “type” is “string” | Yes | {“file”, “directory”, <Registered UIAction Name>} Informs the UI to add a button to open a selection dialog or run a registered UIAction |
    > | “quickSettingsGroup” | string | None | Yes | Groups related items in the quick settings context menu using dividers to separate groups |

    Note

    In order to facilitate deterministic analysis results, settings from the *‘default’*
    schema that impact analysis are serialized from Default, User, and Project scope into
    Resource scope during initial BinaryView analysis. This allows an analysis database to
    be opened at a later time with the same settings, regardless if Default, User, or
    Project settings have been modified.

    Note

    Settings that do not impact analysis (e.g. many UI settings) should use the *“ignore”*
    property to exclude *“SettingsProjectScope”* and *“SettingsResourceScope”* from the
    applicable scopes for the setting.

    Example analysis plugin setting:

    ```
    >>> my_settings = Settings()
    >>> title = "My Pre-Analysis Plugin"
    >>> description = "Enable extra analysis before core analysis."
    >>> properties = f'{{"title" : "{title}", "description" : "{description}", "type" : "boolean", "default" : false}}'
    >>> my_settings.register_group("myPlugin", "My Plugin")
    True
    >>> my_settings.register_setting("myPlugin.enablePreAnalysis", properties)
    True
    >>> my_bv = load("/bin/ls", options={'myPlugin.enablePreAnalysis' : True})
    >>> Settings().get_bool("myPlugin.enablePreAnalysis")
    False
    >>> Settings().get_bool("myPlugin.enablePreAnalysis", my_bv)
    True
    ```

    Example UI plugin setting:

    ```
    >>> my_settings = Settings()
    >>> title = "My UI Plugin"
    >>> description = "Enable My UI Plugin table display."
    >>> properties = f'{{"title" : "{title}", "description" : "{description}", "type" : "boolean", "default" : true, "ignore" : ["SettingsProjectScope", "SettingsResourceScope"]}}'
    >>> my_settings.register_group("myPlugin", "My Plugin")
    True
    >>> my_settings.register_setting("myPlugin.enableTableView", properties)
    True
    >>> my_bv = load("/bin/ls", options={'myPlugin.enableTableView' : True})
    >>> Settings().get_bool("myPlugin.enableTableView")
    True
    ```

    __init__(*instance_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.__init__)
    :   Parameters:
        :   **instance_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*) –

    contains(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.contains)
    :   `contains` determine if a setting identifier exists in the active settings schema

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – the setting identifier

        Returns:
        :   True if the identifier exists in this active settings schema, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    deserialize_schema(*schema: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*, *merge: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.deserialize_schema)
    :   Parameters:
        :   - **schema** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –
            - **merge** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    deserialize_settings(*contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.deserialize_settings)
    :   Parameters:
        :   - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_bool(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_bool)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_bool_with_scope(*key: str*, *resource: ~binaryninja.binaryview.BinaryView | ~binaryninja.function.Function | None = None*, *scope: ~binaryninja.enums.SettingsScope = SettingsScope.SettingsAutoScope) -> (<class 'bool'>*, *<enum 'SettingsScope'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_bool_with_scope)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   (<class ‘bool’>, <enum ‘SettingsScope’>)

    get_double(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_double)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –

        Return type:
        :   [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")

    get_double_with_scope(*key: str*, *resource: ~binaryninja.binaryview.BinaryView | ~binaryninja.function.Function | None = None*, *scope: ~binaryninja.enums.SettingsScope = SettingsScope.SettingsAutoScope) -> (<class 'float'>*, *<enum 'SettingsScope'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_double_with_scope)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   (<class ‘float’>, <enum ‘SettingsScope’>)

    get_integer(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_integer)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_integer_with_scope(*key: str*, *resource: ~binaryninja.binaryview.BinaryView | ~binaryninja.function.Function | None = None*, *scope: ~binaryninja.enums.SettingsScope = SettingsScope.SettingsAutoScope) -> (<class 'int'>*, *<enum 'SettingsScope'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_integer_with_scope)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   (<class ‘int’>, <enum ‘SettingsScope’>)

    get_json(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_json)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_json_with_scope(*key: str*, *resource: ~binaryninja.binaryview.BinaryView | ~binaryninja.function.Function | None = None*, *scope: ~binaryninja.enums.SettingsScope = SettingsScope.SettingsAutoScope) -> (<class 'str'>*, *<enum 'SettingsScope'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_json_with_scope)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   (<class ‘str’>, <enum ‘SettingsScope’>)

    get_string(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_string)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    get_string_list(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_string_list)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    get_string_list_with_scope(*key: str, resource: ~binaryninja.binaryview.BinaryView | ~binaryninja.function.Function | None = None, scope: ~binaryninja.enums.SettingsScope = SettingsScope.SettingsAutoScope) -> (typing.List[str], <enum 'SettingsScope'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_string_list_with_scope)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")], <enum ‘SettingsScope’>)

    get_string_with_scope(*key: str*, *resource: ~binaryninja.binaryview.BinaryView | ~binaryninja.function.Function | None = None*, *scope: ~binaryninja.enums.SettingsScope = SettingsScope.SettingsAutoScope) -> (<class 'str'>*, *<enum 'SettingsScope'>*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.get_string_with_scope)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   (<class ‘str’>, <enum ‘SettingsScope’>)

    is_empty(*resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.is_empty)
    :   `is_empty` determine if the active settings schema is empty

        Parameters:
        :   - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) – a BinaryView or Function object to check for emptiness
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) – the SettingsScope to check for emptiness

        Returns:
        :   True if the active settings schema is empty, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    keys() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.keys)
    :   `keys` retrieve the list of setting identifiers in the active settings schema

        Returns:
        :   list of setting identifiers

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

    load_settings_file(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.load_settings_file)
    :   Parameters:
        :   - **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    query_property_string(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *property_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.query_property_string)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **property_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    query_property_string_list(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *property_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.query_property_string_list)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **property_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")]

    register_group(*group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.register_group)
    :   `register_group` registers a group in the schema for this
        [`Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings") instance

        Parameters:
        :   - **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a unique identifier
            - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a user friendly name appropriate for UI presentation

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> Settings().register_group("solver", "Solver")
            True
            >>>
            ```

    register_setting(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *properties: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.register_setting)
    :   `register_setting` registers a new setting with this
        [`Settings`](#binaryninja.settings.Settings "binaryninja.settings.Settings") instance

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a unique setting identifier in the form **‘<group>.<name>’**
            - **properties** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – a JSON string describes the setting schema

        Returns:
        :   True on success, False on failure.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Example:
        :   ```
            >>> Settings().register_group("solver", "Solver")
            True
            >>> Settings().register_setting("solver.basicBlockSlicing", '{"description" : "Enable the basic block slicing in the solver.", "title" : "Basic Block Slicing", "default" : true, "type" : "boolean"}')
            True
            ```

    reset(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.reset)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    reset_all(*resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*, *schema_only=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.reset_all)
    :   Parameters:
        :   - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    serialize_schema() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.serialize_schema)
    :   Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    serialize_settings(*resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.serialize_settings)
    :   Parameters:
        :   - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    set_bool(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_bool)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_double(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_double)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_integer(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_integer)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_json(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_json)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_resource_id(*resource_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_resource_id)
    :   `set_resource_id` Sets the resource identifier for this class:Settings instance. When
        accessing setting values at the `SettingsResourceScope` level, the resource identifier
        is passed along through the backing store interface.

        Note

        Currently the only available backing store for `SettingsResourceScope` is a `BinaryView`
        object. In the context of a `BinaryView` the resource identifier is the `BinaryViewType`
        name. All settings for this type of backing store are saved in the *‘Raw’*
        `BinaryViewType`. This enables the configuration of setting values such that they are
        available during `BinaryView` creation and initialization.

        Parameters:
        :   **resource_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – a unique identifier

        Return type:
        :   *None*

    set_string(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_string)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    set_string_list(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *resource: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scope: [SettingsScope](enums.md#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") = SettingsScope.SettingsAutoScope*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.set_string_list)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **value** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*) –
            - **resource** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|*
              [*Function*](function.md#binaryninja.function.Function "binaryninja.function.Function")
              *|* *None*) –
            - **scope** ([*SettingsScope*](enums.md#binaryninja.enums.SettingsScope
              "binaryninja.enums.SettingsScope")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    update_property(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *setting_property: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/settings.html#Settings.update_property)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **setting_property** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    default_handle *= <binaryninja._binaryninjacore.LP_BNSettings object>*

    *property* instance_id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Returns the `instance_id` for this [`Settings`](#binaryninja.settings.Settings
        "binaryninja.settings.Settings") repository (read-only)
