# update module

| Class | Description |
| --- | --- |
| [`binaryninja.update.UpdateChannel`](#binaryninja.update.UpdateChannel "binaryninja.update.UpdateChannel") |  |
| [`binaryninja.update.UpdateProgressCallback`](#binaryninja.update.UpdateProgressCallback "binaryninja.update.UpdateProgressCallback") |  |
| [`binaryninja.update.UpdateVersion`](#binaryninja.update.UpdateVersion "binaryninja.update.UpdateVersion") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.update.are_auto_updates_enabled`](#binaryninja.update.are_auto_updates_enabled "binaryninja.update.are_auto_updates_enabled") | `are_auto_updates_enabled` queries if auto updates are enabled. |
| [`binaryninja.update.get_time_since_last_update_check`](#binaryninja.update.get_time_since_last_update_check "binaryninja.update.get_time_since_last_update_check") | `get_time_since_last_update_check` returns the time stamp for the last time updates were checked. |
| [`binaryninja.update.install_pending_update`](#binaryninja.update.install_pending_update "binaryninja.update.install_pending_update") | `install_pending_update` installs any pending updates |
| [`binaryninja.update.is_update_installation_pending`](#binaryninja.update.is_update_installation_pending "binaryninja.update.is_update_installation_pending") | `is_update_installation_pending` whether an update has been downloaded and is waiting installation |
| [`binaryninja.update.set_auto_updates_enabled`](#binaryninja.update.set_auto_updates_enabled "binaryninja.update.set_auto_updates_enabled") | `set_auto_updates_enabled` sets auto update enabled status. |
| [`binaryninja.update.updates_checked`](#binaryninja.update.updates_checked "binaryninja.update.updates_checked") |  |

## UpdateChannel

*class* UpdateChannel[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateChannel)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*name*, *desc*, *ver*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateChannel.__init__)

    update_to_latest(*progress=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateChannel.update_to_latest)

    *property* description

    *property* latest_version
    :   Latest version (read-only)

    *property* latest_version_num

    *property* name

    *property* updates_available
    :   Whether updates are available (read-only)

    *property* versions
    :   List of versions (read-only)

## UpdateProgressCallback

*class* UpdateProgressCallback[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateProgressCallback)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*func*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateProgressCallback.__init__)

    callback(*ctxt*, *progress*, *total*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateProgressCallback.callback)

    *property* active

## UpdateVersion

*class* UpdateVersion[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateVersion)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*channel*, *ver*, *notes*, *t*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateVersion.__init__)

    update(*progress=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#UpdateVersion.update)

    *property* channel

    *property* notes

    *property* time

    *property* version

## are_auto_updates_enabled

are_auto_updates_enabled()[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#are_auto_updates_enabled)
:   `are_auto_updates_enabled` queries if auto updates are enabled.

    Returns:
    :   boolean True if auto updates are enabled. False if they are disabled.

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## get_time_since_last_update_check

get_time_since_last_update_check()[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#get_time_since_last_update_check)
:   `get_time_since_last_update_check` returns the time stamp for the last time updates were
    checked.

    Returns:
    :   time stamp for last update check

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## install_pending_update

install_pending_update()[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#install_pending_update)
:   `install_pending_update` installs any pending updates

    Return type:
    :   *None*

## is_update_installation_pending

is_update_installation_pending()[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#is_update_installation_pending)
:   `is_update_installation_pending` whether an update has been downloaded and is waiting
    installation

    Returns:
    :   boolean True if an update is pending, false if no update is pending

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## set_auto_updates_enabled

set_auto_updates_enabled(*enabled*)[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#set_auto_updates_enabled)
:   `set_auto_updates_enabled` sets auto update enabled status.

    Parameters:
    :   **enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
        v3.14)")) – True to enable update, False to disable updates.

    Return type:
    :   *None*

## updates_checked

updates_checked()[[source]](https://api.binary.ninja/_modules/binaryninja/update.html#updates_checked)
