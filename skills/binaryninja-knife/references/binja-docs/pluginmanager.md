# pluginmanager module

| Class | Description |
| --- | --- |
| [`binaryninja.pluginmanager.RepoPlugin`](#binaryninja.pluginmanager.RepoPlugin "binaryninja.pluginmanager.RepoPlugin") | `RepoPlugin` is mostly read-only, however you can install/uninstall enable/disable plugins. |
| [`binaryninja.pluginmanager.Repository`](#binaryninja.pluginmanager.Repository "binaryninja.pluginmanager.Repository") | `Repository` is a read-only class. Use RepositoryManager to Enable/Disable/Install/Uninstall… |
| [`binaryninja.pluginmanager.RepositoryManager`](#binaryninja.pluginmanager.RepositoryManager "binaryninja.pluginmanager.RepositoryManager") | `RepositoryManager` Keeps track of all the repositories and keeps the enabled_plugins.json… |

## RepoPlugin

*class* RepoPlugin[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepoPlugin)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `RepoPlugin` is mostly read-only, however you can install/uninstall enable/disable
    plugins. RepoPlugins are created by parsing the plugins.json in a plugin repository.

    __init__(*handle: LP_BNRepoPlugin*)[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepoPlugin.__init__)
    :   Parameters:
        :   **handle** (*LP_BNRepoPlugin*) –

    enable(*force: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepoPlugin.enable)
    :   Enable this plugin, optionally trying to force it. Force loading a plugin with ignore
        platform and api constraints. (e.g. The plugin author says the plugin will only work on
        Linux but you’d like to attempt to load it on macOS)

        Parameters:
        :   **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    install() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepoPlugin.install)
    :   Attempt to install the given plugin

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    install_dependencies() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepoPlugin.install_dependencies)
    :   Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    uninstall() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepoPlugin.uninstall)
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

    *property* delete_pending*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin will be deleted after the next restart

    *property* dependencies*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Dependencies required for installing this plugin

    *property* dependencies_being_installed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin’s dependencies are currently being installed

    *property* description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String short description of the plugin

    *property* disable_pending*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean status indicating that the plugin will be disabled after the next restart

    *property* enabled*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if the plugin is currently enabled, False otherwise

    *property* install_platforms*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*
    :   List of platforms this plugin can execute on

    *property* installed*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Boolean True if the plugin is installed, False otherwise

    *property* last_update*: [date](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")*
    :   Returns a datetime object representing the plugins last update

    *property* license_text*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String complete license text for the given plugin

    *property* long_description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String long description of the plugin

    *property* maximum_version_info*: [CoreVersionInfo](https://api.binary.ninja/index.html#binaryninja.CoreVersionInfo "binaryninja.CoreVersionInfo")*
    :   Maximum version info the plugin will support

    minimum_version
    :   Minimum version the plugin was tested on

        Deprecated since version 4.0.5366: Use
        [`minimum_version_info`](#binaryninja.pluginmanager.RepoPlugin.minimum_version_info
        "binaryninja.pluginmanager.RepoPlugin.minimum_version_info") instead.

    *property* minimum_version_info*: [CoreVersionInfo](https://api.binary.ninja/index.html#binaryninja.CoreVersionInfo "binaryninja.CoreVersionInfo")*
    :   Minimum version info the plugin was tested on

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String name of the plugin

    *property* package_url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   String URL of the plugin’s zip file

    *property* path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Relative path from the base of the repository to the actual plugin

    *property* plugin_types*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[PluginType](enums.md#binaryninja.enums.PluginType "binaryninja.enums.PluginType")]*
    :   List of PluginType enumeration objects indicating the plugin type(s)

    *property* project_data*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")*
    :   Gets a json object of the project data field

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

## Repository

*class* Repository[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#Repository)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `Repository` is a read-only class. Use RepositoryManager to
    Enable/Disable/Install/Uninstall plugins.

    __init__(*handle: LP_BNRepository*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#Repository.__init__)
    :   Parameters:
        :   **handle** (*LP_BNRepository*) –

        Return type:
        :   *None*

    *property* full_path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String full path the repository

    *property* path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String local path to store the given plugin repository

    *property* plugins*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[RepoPlugin](#binaryninja.pluginmanager.RepoPlugin "binaryninja.pluginmanager.RepoPlugin")]*
    :   List of RepoPlugin objects contained within this repository

    *property* url*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   String URL of the git repository where the plugin repository’s are stored

## RepositoryManager

*class* RepositoryManager[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepositoryManager)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `RepositoryManager` Keeps track of all the repositories and keeps the
    enabled_plugins.json file coherent with the plugins that are installed/uninstalled
    enabled/disabled

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepositoryManager.__init__)

    add_repository(*url: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *repopath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepositoryManager.add_repository)
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

    check_for_updates() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/pluginmanager.html#RepositoryManager.check_for_updates)
    :   Check for updates for all managed Repository objects

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* default_repository*: [Repository](#binaryninja.pluginmanager.Repository "binaryninja.pluginmanager.Repository")*
    :   Gets the default Repository

    *property* plugins*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[RepoPlugin](#binaryninja.pluginmanager.RepoPlugin "binaryninja.pluginmanager.RepoPlugin")]]*
    :   List of all RepoPlugins in each repository

    *property* repositories*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Repository](#binaryninja.pluginmanager.Repository "binaryninja.pluginmanager.Repository")]*
    :   List of Repository objects being managed
