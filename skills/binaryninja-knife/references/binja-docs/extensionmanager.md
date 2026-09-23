# extensionmanager module

| Class | Description |
| --- | --- |
| [`binaryninja.extensionmanager.Extension`](#binaryninja.extensionmanager.Extension "binaryninja.extensionmanager.Extension") | `Extension` is mostly read-only, however you can install/uninstall enable/disable plugins. |
| [`binaryninja.extensionmanager.ExtensionVersion`](#binaryninja.extensionmanager.ExtensionVersion "binaryninja.extensionmanager.ExtensionVersion") |  |
| [`binaryninja.extensionmanager.ExtensionVersionPlatform`](#binaryninja.extensionmanager.ExtensionVersionPlatform "binaryninja.extensionmanager.ExtensionVersionPlatform") |  |
| [`binaryninja.extensionmanager.PluginDependencyConflict`](#binaryninja.extensionmanager.PluginDependencyConflict "binaryninja.extensionmanager.PluginDependencyConflict") |  |
| [`binaryninja.extensionmanager.PluginDependencyRequirement`](#binaryninja.extensionmanager.PluginDependencyRequirement "binaryninja.extensionmanager.PluginDependencyRequirement") |  |
| [`binaryninja.extensionmanager.Repository`](#binaryninja.extensionmanager.Repository "binaryninja.extensionmanager.Repository") | `Repository` is a read-only class. Use RepositoryManager to Enable/Disable/Install/Uninstall… |
| [`binaryninja.extensionmanager.RepositoryManager`](#binaryninja.extensionmanager.RepositoryManager "binaryninja.extensionmanager.RepositoryManager") | `RepositoryManager` Keeps track of all the repositories and keeps the enabled_plugins.json… |

| Function | Description |
| --- | --- |
| [`binaryninja.extensionmanager.RepoPlugin`](#binaryninja.extensionmanager.RepoPlugin "binaryninja.extensionmanager.RepoPlugin") | Deprecated since version 5.3: Use `binaryninja.Extension` instead. |

## Extension

*class* Extension[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `Extension` is mostly read-only, however you can install/uninstall enable/disable
    plugins. Extensions are created by parsing the plugins.json in a plugin repository.

    __init__(*handle: core.BNRepoPluginHandle*)[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.__init__)
    :   Parameters:
        :   **handle** (*core.BNRepoPluginHandle*)

    cancel_uninstall() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.cancel_uninstall)
    :   Cancel an uninstall that is pending until restart.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    dependencies_for_version(*version_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.dependencies_for_version)
    :   Dependencies required for installing a specific plugin version.

        Parameters:
        :   **version_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    dependency_conflicts_for_version(*version_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginDependencyConflict](#binaryninja.extensionmanager.PluginDependencyConflict "binaryninja.extensionmanager.PluginDependencyConflict")][[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.dependency_conflicts_for_version)
    :   Dependency conflicts for a specific version, or the plugin default when version_id is
        None.

        Parameters:
        :   **version_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") *|* *None*)

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*PluginDependencyConflict*](#binaryninja.extensionmanager.PluginDependencyConflict
            "binaryninja.extensionmanager.PluginDependencyConflict")]

    enable(*force: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.enable)
    :   Enable this plugin, optionally trying to force it. Force loading a plugin with ignore
        platform and api constraints. (e.g. The plugin author says the plugin will only work on
        Linux but you’d like to attempt to load it on macOS)

        Parameters:
        :   **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    install(*version_id=None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.install)
    :   Attempt to install the given plugin. Defaults to the latest available version.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    install_dependencies(*version_id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *excluded_package_names: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.install_dependencies)
    :   Install dependencies for a plugin version, optionally excluding packages by canonical
        name.

        Parameters:
        :   - **version_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)
            - **excluded_package_names**
              ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")*]* *|* *None*)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    uninstall() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Extension.uninstall)
    :   Attempt to uninstall the given plugin

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* api*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   String indicating the API used by the plugin

    *property* author*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String of the plugin author

    *property* author_url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String URL of the plugin author’s url

    *property* being_deleted*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin is being deleted

    *property* being_updated*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin is being updated

    *property* current_version*: [ExtensionVersion](#binaryninja.extensionmanager.ExtensionVersion "binaryninja.extensionmanager.ExtensionVersion")*
    :   Current version metadata for the plugin

    *property* delete_pending*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin will be deleted after the next restart

    *property* dependencies*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Dependencies required for installing this plugin

    *property* dependencies_being_installed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin’s dependencies are currently being installed

    *property* dependency_conflicts*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginDependencyConflict](#binaryninja.extensionmanager.PluginDependencyConflict "binaryninja.extensionmanager.PluginDependencyConflict")]*
    :   Dependency conflicts with installed plugins, or an empty list for custom Python
        environments.

    *property* deprecated*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if the plugin is marked deprecated by its repository

    *property* description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String short description of the plugin

        Deprecated since version 5.3: Use
        [`current_version`](#binaryninja.extensionmanager.Extension.current_version
        "binaryninja.extensionmanager.Extension.current_version") in combination with
        [`versions`](#binaryninja.extensionmanager.Extension.versions
        "binaryninja.extensionmanager.Extension.versions") instead.

    *property* disable_pending*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin will be disabled after the next restart

    *property* enabled*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if the plugin is currently enabled, False otherwise

    *property* install_platforms*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   List of platforms this plugin can execute on

    *property* installed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if the plugin is installed, False otherwise

    *property* is_paid*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if this plugin requires payment, False otherwise

    *property* last_update*: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")*
    :   Returns a datetime object representing the plugins last update

        Deprecated since version 5.3: Use
        [`versions`](#binaryninja.extensionmanager.Extension.versions
        "binaryninja.extensionmanager.Extension.versions") in combination with
        [`current_version`](#binaryninja.extensionmanager.Extension.current_version
        "binaryninja.extensionmanager.Extension.current_version") to check for updates instead.

    *property* latest_version_id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Latest version id available for this platform

    *property* license_text*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String complete license text for the given plugin

        Deprecated since version 5.3: This field will be removed.

    *property* listed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if the plugin is present in its repository’s latest successful listing

    *property* long_description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String long description of the plugin

    *property* maximum_version_info*: [CoreVersionInfo](https://api.binary.ninja/index.html#binaryninja.CoreVersionInfo "binaryninja.CoreVersionInfo")*
    :   Maximum version info the plugin will support

    minimum_version
    :   Minimum version the plugin was tested on

        Deprecated since version 4.0.5366: Use
        [`minimum_version_info`](#binaryninja.extensionmanager.Extension.minimum_version_info
        "binaryninja.extensionmanager.Extension.minimum_version_info") instead.

    *property* minimum_version_info*: [CoreVersionInfo](https://api.binary.ninja/index.html#binaryninja.CoreVersionInfo "binaryninja.CoreVersionInfo")*
    :   Minimum version info the plugin was tested on

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String name of the plugin

    *property* package_url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String URL of the plugin’s zip file

        Deprecated since version 5.3: Use
        [`current_version`](#binaryninja.extensionmanager.Extension.current_version
        "binaryninja.extensionmanager.Extension.current_version") in combination with
        [`versions`](#binaryninja.extensionmanager.Extension.versions
        "binaryninja.extensionmanager.Extension.versions") instead.

    *property* path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Relative path from the base of the repository to the actual plugin

    *property* plugin_types*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginType](enums.md#binaryninja.enums.PluginType "binaryninja.enums.PluginType")]*
    :   List of PluginType enumeration objects indicating the plugin type(s)

    *property* project_data*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")*
    :   Gets a json object of the project data field

        Deprecated since version 5.3: This field will be removed.

    *property* project_url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String URL of the plugin’s git repository

    *property* running*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin is currently running

    *property* subdir*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Optional sub-directory the plugin code lives in as a relative path from the plugin root

    *property* update_available*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin has updates available

    *property* update_pending*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin has updates will be installed after the next
        restart

    *property* version*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String version of the plugin

        Deprecated since version 5.3: Use
        [`current_version`](#binaryninja.extensionmanager.Extension.current_version
        "binaryninja.extensionmanager.Extension.current_version") in combination with
        [`versions`](#binaryninja.extensionmanager.Extension.versions
        "binaryninja.extensionmanager.Extension.versions") instead.

    *property* versions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ExtensionVersion](#binaryninja.extensionmanager.ExtensionVersion "binaryninja.extensionmanager.ExtensionVersion")]*
    :   Version metadata for all available plugin versions

## ExtensionVersion

*class* ExtensionVersion[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#ExtensionVersion)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *version: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *long_description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *changelog: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *minimum_client_version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *platforms: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ExtensionVersionPlatform](#binaryninja.extensionmanager.ExtensionVersionPlatform "binaryninja.extensionmanager.ExtensionVersionPlatform")]*, *created: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **long_description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **changelog** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **minimum_client_version** ([*int*](https://docs.python.org/3/library/functions.html#int
              "(in Python v3.14)"))
            - **platforms** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python
              v3.14)")*[*[*ExtensionVersionPlatform*](#binaryninja.extensionmanager.ExtensionVersionPlatform
              "binaryninja.extensionmanager.ExtensionVersionPlatform")*]*)
            - **created** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    changelog*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    created*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    long_description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    minimum_client_version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    platforms*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ExtensionVersionPlatform](#binaryninja.extensionmanager.ExtensionVersionPlatform "binaryninja.extensionmanager.ExtensionVersionPlatform")]*

    version*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## ExtensionVersionPlatform

*class* ExtensionVersionPlatform[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#ExtensionVersionPlatform)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *download_url: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *untracked_download_url: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **download_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **untracked_download_url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str
              "(in Python v3.14)"))

        Return type:
        :   *None*

    download_url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    untracked_download_url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## PluginDependencyConflict

*class* PluginDependencyConflict[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#PluginDependencyConflict)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*status: [PluginDependencyConflictStatus](enums.md#binaryninja.enums.PluginDependencyConflictStatus "binaryninja.enums.PluginDependencyConflictStatus")*, *package_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *candidate_requirements: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginDependencyRequirement](#binaryninja.extensionmanager.PluginDependencyRequirement "binaryninja.extensionmanager.PluginDependencyRequirement")]*, *installed_requirements: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginDependencyRequirement](#binaryninja.extensionmanager.PluginDependencyRequirement "binaryninja.extensionmanager.PluginDependencyRequirement")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **status**
              ([*PluginDependencyConflictStatus*](enums.md#binaryninja.enums.PluginDependencyConflictStatus
              "binaryninja.enums.PluginDependencyConflictStatus"))
            - **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **candidate_requirements**
              ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*PluginDependencyRequirement*](#binaryninja.extensionmanager.PluginDependencyRequirement
              "binaryninja.extensionmanager.PluginDependencyRequirement")*]*)
            - **installed_requirements**
              ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
              v3.14)")*[*[*PluginDependencyRequirement*](#binaryninja.extensionmanager.PluginDependencyRequirement
              "binaryninja.extensionmanager.PluginDependencyRequirement")*]*)

        Return type:
        :   *None*

    candidate_requirements*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginDependencyRequirement](#binaryninja.extensionmanager.PluginDependencyRequirement "binaryninja.extensionmanager.PluginDependencyRequirement")]*

    installed_requirements*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginDependencyRequirement](#binaryninja.extensionmanager.PluginDependencyRequirement "binaryninja.extensionmanager.PluginDependencyRequirement")]*

    package_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    status*: [PluginDependencyConflictStatus](enums.md#binaryninja.enums.PluginDependencyConflictStatus "binaryninja.enums.PluginDependencyConflictStatus")*

## PluginDependencyRequirement

*class* PluginDependencyRequirement[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#PluginDependencyRequirement)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*plugin_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *requirement: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **plugin_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **requirement** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))

        Return type:
        :   *None*

    plugin_name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    requirement*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## Repository

*class* Repository[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Repository)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `Repository` is a read-only class. Use RepositoryManager to
    Enable/Disable/Install/Uninstall plugins.

    __init__(*handle: LP_BNRepository*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#Repository.__init__)
    :   Parameters:
        :   **handle** (*LP_BNRepository*)

        Return type:
        :   *None*

    *property* full_path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String full path the repository

    *property* path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String local path to store the given plugin repository

    *property* plugins*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Extension](#binaryninja.extensionmanager.Extension "binaryninja.extensionmanager.Extension")]*
    :   List of Extension objects contained within this repository

    *property* url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String URL of the git repository where the plugin repository’s are stored

## RepositoryManager

*class* RepositoryManager[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#RepositoryManager)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `RepositoryManager` Keeps track of all the repositories and keeps the
    enabled_plugins.json file coherent with the plugins that are installed/uninstalled
    enabled/disabled

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#RepositoryManager.__init__)

    add_repository(*url: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *repopath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#RepositoryManager.add_repository)
    :   `add_repository` adds a new plugin repository for the manager to track.

        To remove a repository, restart Binary Ninja (and don’t re-add the repository!). File
        artifacts will remain on disk under repositories/ file in the User Folder.

        Before you can query plugin metadata from a repository, you need to call
        `check_for_updates`.

        Parameters:
        :   - **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – URL to the plugins.json containing the records for this repository
            - **repopath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – path to where the repository will be stored on disk locally

        Returns:
        :   Boolean value True if the repository was successfully added, False otherwise.

        Return type:
        :   Boolean

        Example:
        :   ```
            >>> mgr = RepositoryManager()
            >>> mgr.add_repository("https://raw.githubusercontent.com/Vector35/community-plugins/master/plugins.json", "community")
            True
            >>> mgr.check_for_updates()
            >>>
            ```

    check_for_updates() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#RepositoryManager.check_for_updates)
    :   Check for updates for all managed Repository objects

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* default_repository*: [Repository](#binaryninja.extensionmanager.Repository "binaryninja.extensionmanager.Repository")*
    :   Gets the default Repository

    *property* plugins*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Extension](#binaryninja.extensionmanager.Extension "binaryninja.extensionmanager.Extension")]]*
    :   List of all Extensions in each repository

    *property* repositories*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Repository](#binaryninja.extensionmanager.Repository "binaryninja.extensionmanager.Repository")]*
    :   List of Repository objects being managed

## RepoPlugin

RepoPlugin(*handle: core.BNRepoPluginHandle*)[[source]](https://api.binary.ninja/_modules/binaryninja/extensionmanager.html#RepoPlugin)
:   Deprecated since version 5.3: Use `binaryninja.Extension` instead.

    Parameters:
    :   **handle** (*core.BNRepoPluginHandle*)
