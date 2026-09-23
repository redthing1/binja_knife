# collaboration module

| Class | Description |
| --- | --- |
| [`binaryninja.collaboration.changeset.Changeset`](https://api.binary.ninja/binaryninja.collaboration.changeset-module.html#binaryninja.collaboration.changeset.Changeset "binaryninja.collaboration.changeset.Changeset") | Class representing a collection of snapshots in a local database |
| [`binaryninja.collaboration.file.RemoteFile`](https://api.binary.ninja/binaryninja.collaboration.file-module.html#binaryninja.collaboration.file.RemoteFile "binaryninja.collaboration.file.RemoteFile") | Class representing a remote project file. It controls the various snapshots and raw file… |
| [`binaryninja.collaboration.folder.RemoteFolder`](https://api.binary.ninja/binaryninja.collaboration.folder-module.html#binaryninja.collaboration.folder.RemoteFolder "binaryninja.collaboration.folder.RemoteFolder") | Class representing a remote folder in a project. |
| [`binaryninja.collaboration.group.Group`](https://api.binary.ninja/binaryninja.collaboration.group-module.html#binaryninja.collaboration.group.Group "binaryninja.collaboration.group.Group") | Class representing a remote Group |
| [`binaryninja.collaboration.project.RemoteProject`](https://api.binary.ninja/binaryninja.collaboration.project-module.html#binaryninja.collaboration.project.RemoteProject "binaryninja.collaboration.project.RemoteProject") | Class representing a remote project |
| [`binaryninja.collaboration.remote.Remote`](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | Class representing a connection to a Collaboration server |
| [`binaryninja.collaboration.snapshot.CollabSnapshot`](https://api.binary.ninja/binaryninja.collaboration.snapshot-module.html#binaryninja.collaboration.snapshot.CollabSnapshot "binaryninja.collaboration.snapshot.CollabSnapshot") | Class representing a remote Snapshot |
| [`binaryninja.collaboration.snapshot.UndoEntry`](https://api.binary.ninja/binaryninja.collaboration.snapshot-module.html#binaryninja.collaboration.snapshot.UndoEntry "binaryninja.collaboration.snapshot.UndoEntry") | Class representing a remote undo entry |
| [`binaryninja.collaboration.user.User`](https://api.binary.ninja/binaryninja.collaboration.user-module.html#binaryninja.collaboration.user.User "binaryninja.collaboration.user.User") | Class representing a remote User |

| Function | Description |
| --- | --- |
| [`binaryninja.collaboration.active_remote`](#binaryninja.collaboration.active_remote "binaryninja.collaboration.active_remote") | Get the single actively connected Remote (for ux simplification) |
| [`binaryninja.collaboration.create_remote`](#binaryninja.collaboration.create_remote "binaryninja.collaboration.create_remote") | Create a Remote and add it to the list of known remotes (saved to Settings) |
| [`binaryninja.collaboration.enterprise_remote`](#binaryninja.collaboration.enterprise_remote "binaryninja.collaboration.enterprise_remote") | Get whichever known Remote has the same address as the Enterprise license server |
| [`binaryninja.collaboration.get_remote_by_address`](#binaryninja.collaboration.get_remote_by_address "binaryninja.collaboration.get_remote_by_address") | Get Remote by address |
| [`binaryninja.collaboration.get_remote_by_id`](#binaryninja.collaboration.get_remote_by_id "binaryninja.collaboration.get_remote_by_id") | Get Remote by unique id |
| [`binaryninja.collaboration.get_remote_by_name`](#binaryninja.collaboration.get_remote_by_name "binaryninja.collaboration.get_remote_by_name") | Get Remote by name |
| [`binaryninja.collaboration.known_remotes`](#binaryninja.collaboration.known_remotes "binaryninja.collaboration.known_remotes") | List of known/connected Remotes |
| [`binaryninja.collaboration.load_remotes`](#binaryninja.collaboration.load_remotes "binaryninja.collaboration.load_remotes") | Load the list of known Remotes from local Settings |
| [`binaryninja.collaboration.remove_known_remote`](#binaryninja.collaboration.remove_known_remote "binaryninja.collaboration.remove_known_remote") | Remove a Remote from the list of known remotes (saved to Settings) |
| [`binaryninja.collaboration.save_remotes`](#binaryninja.collaboration.save_remotes "binaryninja.collaboration.save_remotes") | Save the list of known Remotes to local Settings |
| [`binaryninja.collaboration.set_active_remote`](#binaryninja.collaboration.set_active_remote "binaryninja.collaboration.set_active_remote") | Set the single actively connected Remote |

## active_remote

active_remote() → [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#active_remote)
:   Get the single actively connected Remote (for ux simplification)

    Returns:
    :   Active Remote, if one is set. None, otherwise.

    Return type:
    :   [*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote") | *None*

## create_remote

create_remote(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *address: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#create_remote)
:   Create a Remote and add it to the list of known remotes (saved to Settings)

    Parameters:
    :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Identifier for remote
        - **address** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Base address (HTTPS) for all api requests

    Return type:
    :   [*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote")

## enterprise_remote

enterprise_remote() → [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#enterprise_remote)
:   Get whichever known Remote has the same address as the Enterprise license server

    Returns:
    :   Relevant known Remote, or None if one is not found

    Return type:
    :   [*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote") | *None*

## get_remote_by_address

get_remote_by_address(*address: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#get_remote_by_address)
:   Get Remote by address

    Parameters:
    :   **address** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – Base address of remote api

    Returns:
    :   Remote, if found, else None

    Return type:
    :   [*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote") | *None*

## get_remote_by_id

get_remote_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#get_remote_by_id)
:   Get Remote by unique id

    Parameters:
    :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – Unique id of the Remote

    Returns:
    :   Remote, if known, else None

    Return type:
    :   [*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote") | *None*

## get_remote_by_name

get_remote_by_name(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#get_remote_by_name)
:   Get Remote by name

    Parameters:
    :   **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – Name of Remote

    Returns:
    :   Remote, if found, else None

    Return type:
    :   [*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote") | *None*

## known_remotes

known_remotes() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote")][[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#known_remotes)
:   List of known/connected Remotes

    Returns:
    :   All known remotes

    Return type:
    :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
        v3.14)")[[*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote")]

## load_remotes

load_remotes()[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#load_remotes)
:   Load the list of known Remotes from local Settings

    Raises:
    :   [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in
        Python v3.14)") – If there was an error

## remove_known_remote

remove_known_remote(*remote: [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#remove_known_remote)
:   Remove a Remote from the list of known remotes (saved to Settings)

    Parameters:
    :   **remote**
        ([*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote")) – Remote to remove

    Return type:
    :   *None*

## save_remotes

save_remotes()[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#save_remotes)
:   Save the list of known Remotes to local Settings

    Raises:
    :   [**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in
        Python v3.14)") – If there was an error

## set_active_remote

set_active_remote(*remote: [Remote](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote "binaryninja.collaboration.remote.Remote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/collaboration.html#set_active_remote)
:   Set the single actively connected Remote

    Parameters:
    :   **remote**
        ([*Remote*](https://api.binary.ninja/binaryninja.collaboration.remote-module.html#binaryninja.collaboration.remote.Remote
        "binaryninja.collaboration.remote.Remote") *|* *None*) – New active Remote, or None to
        clear it.
