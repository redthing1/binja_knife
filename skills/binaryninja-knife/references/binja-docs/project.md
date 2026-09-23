# project module

| Class | Description |
| --- | --- |
| [`binaryninja.project.Project`](#binaryninja.project.Project "binaryninja.project.Project") | Class representing a project |
| [`binaryninja.project.ProjectFile`](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | Class representing a file in a project |
| [`binaryninja.project.ProjectFolder`](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder") | Class representing a folder in a project |

## Project

*class* Project[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class representing a project

    __init__(*handle: LP_BNProject*)[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.__init__)
    :   Parameters:
        :   **handle** (*LP_BNProject*) –

    bulk_operation()[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.bulk_operation)
    :   A context manager to speed up bulk project operations. Project modifications are synced
        to disk in chunks, and the project on disk vs in memory may not agree on state if an
        exception occurs while a bulk operation is happening.

        Example:
        :   ```
            >>> from pathlib import Path
            >>> with project.bulk_operation():
            ...     for i in Path('/bin/').iterdir():
            ...             if i.is_file() and not i.is_symlink():
            ...                     project.create_file_from_path(i, None, i.name)
            ```

    close() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.close)
    :   Close an opened project

        Returns:
        :   True if the project is now closed, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    create_file(*contents: bytes, folder: ~binaryninja.project.ProjectFolder | None, name: str, description: str = '', progress_func: ~typing.Callable[[int, int], bool] = <function _nop>*) → [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.create_file)
    :   Create a file in the project

        Parameters:
        :   - **contents** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in
              Python v3.14)")) – Bytes of the file that will be created
            - **folder** ([*ProjectFolder*](#binaryninja.project.ProjectFolder
              "binaryninja.project.ProjectFolder") *|* *None*) – Folder to place the created file in
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name to assign to the created file
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Description to assign to the created file
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]*) – Progress function that will be called as the file is being added

        Return type:
        :   [*ProjectFile*](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")

    create_file_from_path(*path: ~os.PathLike | str, folder: ~binaryninja.project.ProjectFolder | None, name: str, description: str = '', progress_func: ~typing.Callable[[int, int], bool] = <function _nop>*) → [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.create_file_from_path)
    :   Create a file in the project from a path on disk

        Parameters:
        :   - **path** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
              v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Path on disk
            - **folder** ([*ProjectFolder*](#binaryninja.project.ProjectFolder
              "binaryninja.project.ProjectFolder") *|* *None*) – Folder to place the created file in
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name to assign to the created file
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Description to assign to the created file
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]*) – Progress function that will be called as the file is being added

        Return type:
        :   [*ProjectFile*](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")

    create_folder(*parent: [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *description: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.create_folder)
    :   Recursively create files and folders in the project from a path on disk

        Parameters:
        :   - **parent** ([*ProjectFolder*](#binaryninja.project.ProjectFolder
              "binaryninja.project.ProjectFolder") *|* *None*) – Parent folder in the project that
              will contain the new folder
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name for the created folder
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Description for created folder

        Returns:
        :   Created folder

        Return type:
        :   [*ProjectFolder*](#binaryninja.project.ProjectFolder
            "binaryninja.project.ProjectFolder")

    create_folder_from_path(*path: ~os.PathLike | str, parent: ~binaryninja.project.ProjectFolder | None = None, description: str = '', progress_func: ~typing.Callable[[int, int], bool] = <function _nop>*) → [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.create_folder_from_path)
    :   Recursively create files and folders in the project from a path on disk

        Parameters:
        :   - **path** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
              v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Path to folder on disk
            - **parent** ([*ProjectFolder*](#binaryninja.project.ProjectFolder
              "binaryninja.project.ProjectFolder") *|* *None*) – Parent folder in the project that
              will contain the new contents
            - **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Description for created root folder
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]*) – Progress function that will be called

        Returns:
        :   Created root folder

        Return type:
        :   [*ProjectFolder*](#binaryninja.project.ProjectFolder
            "binaryninja.project.ProjectFolder")

    *static* create_project(*path: [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Project](#binaryninja.project.Project "binaryninja.project.Project")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.create_project)
    :   Create a new project

        Parameters:
        :   - **path** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
              v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Path to the project directory (.bnpr)
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Name of the new project

        Returns:
        :   Opened project

        Raises:
        :   [**ProjectException**](exceptions.md#binaryninja.exceptions.ProjectException
            "binaryninja.exceptions.ProjectException") – If there was an error creating the project

        Return type:
        :   [*Project*](#binaryninja.project.Project "binaryninja.project.Project")

    delete_file(*file: [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.delete_file)
    :   Delete a file from the project

        Parameters:
        :   **file** ([*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")) – File to delete

        Returns:
        :   True if the file was deleted, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    delete_folder(*folder: ~binaryninja.project.ProjectFolder, progress_func: ~typing.Callable[[int, int], bool] = <function _nop>*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.delete_folder)
    :   Recursively delete a folder from the project

        Parameters:
        :   - **folder** ([*ProjectFolder*](#binaryninja.project.ProjectFolder
              "binaryninja.project.ProjectFolder")) – Folder to delete recursively
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]*) – Progress function that will be called as objects get deleted

        Returns:
        :   True if the folder was deleted, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_file_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.get_file_by_id)
    :   Retrieve a file in the project by unique id

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Unique identifier for a file

        Returns:
        :   File with the requested id or None

        Return type:
        :   [*ProjectFile*](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") |
            *None*

    get_file_by_path_on_disk(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.get_file_by_path_on_disk)
    :   Retrieve a file in the project by its path on disk

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Path of the file on the disk

        Returns:
        :   File with the requested path or None

        Return type:
        :   [*ProjectFile*](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile") |
            *None*

    get_files_by_path_in_project(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")][[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.get_files_by_path_in_project)
    :   Retrieve a file(s) by path in the project Note that files in a project can share names
        and paths within the project but are uniquely identified by a disk path or id.

        Parameters:
        :   **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Path of the file(s) in the project, separate from their path on disk.

        Returns:
        :   List of files with the requested path

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")]

    get_files_in_folder(*folder: [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")][[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.get_files_in_folder)
    :   Get the list of files in a folder

        Returns:
        :   List of files contained in the folder

        Parameters:
        :   **folder** ([*ProjectFolder*](#binaryninja.project.ProjectFolder
            "binaryninja.project.ProjectFolder") *|* *None*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")]

    get_folder_by_id(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.get_folder_by_id)
    :   Retrieve a folder in the project by unique id

        Parameters:
        :   **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Unique identifier for a folder

        Returns:
        :   Folder with the requested id or None

        Return type:
        :   [*ProjectFolder*](#binaryninja.project.ProjectFolder
            "binaryninja.project.ProjectFolder") | *None*

    get_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → metadata.MetadataValueType | Any[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.get_metadata)
    :   get_metadata retrieves a metadata value associated with the given key stored in the
        current Project.

        This method behaves like dict.get():

        - If the key exists, its metadata value is returned.
        - If the key does not exist and default is not provided, None is returned.
        - If the key does not exist and default is provided, default is returned.

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – key to query
            - **default** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")) – value to return if the key does not exist (defaults to None)

        Return type:
        :   metadata associated with the key or the default value

        Example:
        :   ```
            >>> current_project.store_metadata("integer", 1337)
            >>> current_project.get_metadata("integer")
            1337L
            >>> current_project.get_metadata("missing")
            None
            >>> current_project.get_metadata("missing", 42)
            42
            ```

    open() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.open)
    :   Open a closed project

        Returns:
        :   True if the project is now open, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *static* open_project(*path: [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Project](#binaryninja.project.Project "binaryninja.project.Project")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.open_project)
    :   Open an existing project

        Parameters:
        :   **path** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
            v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Path to the project directory (.bnpr) or project metadata file (.bnpm)

        Returns:
        :   Opened project

        Raises:
        :   [**ProjectException**](exceptions.md#binaryninja.exceptions.ProjectException
            "binaryninja.exceptions.ProjectException") – If there was an error opening the project

        Return type:
        :   [*Project*](#binaryninja.project.Project "binaryninja.project.Project")

    query_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.query_metadata)
    :   Retrieves metadata stored under a key from the project

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Key to query

        Return type:
        :   [*Metadata*](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata")
            | [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") |
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") |
            [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*Metadata*](metadata.md#binaryninja.metadata.Metadata
            "binaryninja.metadata.Metadata") |
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") |
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") |
            [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[MetadataValueType] |
            [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[MetadataValueType] |
            [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] |
            [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*Metadata*](metadata.md#binaryninja.metadata.Metadata
            "binaryninja.metadata.Metadata") |
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") |
            [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") |
            [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") |
            [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") |
            [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[MetadataValueType] |
            [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[MetadataValueType] |
            [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] |
            [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    remove_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.remove_metadata)
    :   Removes the metadata associated with this key from the project

        Parameters:
        :   **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Key associated with the metadata object to remove

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    store_metadata(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Metadata](metadata.md#binaryninja.metadata.Metadata "binaryninja.metadata.Metadata") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[MetadataValueType] | [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[MetadataValueType] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")] | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#Project.store_metadata)
    :   Stores metadata within the project

        Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Key under which to store the Metadata object
            - **value** (*Varies*) – Object to store

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the description of the project

        Returns:
        :   Description of the project

    *property* files*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")]*
    :   Get a list of files in the project

        Returns:
        :   List of files in the project

    *property* folders*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder")]*
    :   Get a list of folders in the project

        Returns:
        :   List of folders in the project

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the unique id of this project

        Returns:
        :   Unique identifier of project

    *property* is_open*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if the project is currently open

        Returns:
        :   True if the project is currently open, False otherwise

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the name of the project

        Returns:
        :   Name of the project

    *property* path*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the path of the project

        Returns:
        :   Path of the project’s .bnpr directory

## ProjectFile

*class* ProjectFile[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class representing a file in a project

    __init__(*handle: LP_BNProjectFile*)[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.__init__)
    :   Parameters:
        :   **handle** (*LP_BNProjectFile*) –

    add_dependency(*file: [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.add_dependency)
    :   Add a ProjectFile as a dependency of this file

        Returns:
        :   True on success, False otherwise

        Parameters:
        :   **file** ([*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    export(*dest: [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.export)
    :   Export this file to disk

        Parameters:
        :   **dest** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
            v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)")) – Destination path for the exported contents

        Returns:
        :   True if the export succeeded, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    get_dependencies() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")][[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.get_dependencies)
    :   Get the list of files that this file depends on

        Returns:
        :   List of ProjectFiles that this file depends on

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")]

    get_path_in_project() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.get_path_in_project)
    :   Get this file’s path in its parent project

        Returns:
        :   The path in the project or None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_path_on_disk() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.get_path_on_disk)
    :   Get this file’s path on disk

        Returns:
        :   The path on disk of the file or None

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    get_required_by() → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")][[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.get_required_by)
    :   Get the list of files that depend on this file

        Returns:
        :   List of ProjectFiles that depend on this file

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")]

    remove_dependency(*file: [ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFile.remove_dependency)
    :   Remove a ProjectFile as a dependency of this file

        Returns:
        :   True on success, False otherwise

        Parameters:
        :   **file** ([*ProjectFile*](#binaryninja.project.ProjectFile
            "binaryninja.project.ProjectFile")) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the description of this file

        Returns:
        :   Description of this file

    *property* exists_on_disk*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Check if this file’s contents exist on disk

        Returns:
        :   True if this file’s contents exist on disk, False otherwise

    *property* folder*: [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the folder that contains this file

        Returns:
        :   Folder that contains this file, or None

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the unique id of this file

        Returns:
        :   Unique identifier of this file

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the name of this file

        Returns:
        :   Name of this file

    *property* path_on_disk*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the path on disk to this file’s contents

        Returns:
        :   Path on disk as a string

    *property* project*: [Project](#binaryninja.project.Project "binaryninja.project.Project")*
    :   Get the project that owns this file

        Returns:
        :   Project that owns this file

## ProjectFolder

*class* ProjectFolder[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFolder)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class representing a folder in a project

    __init__(*handle: LP_BNProjectFolder*)[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFolder.__init__)
    :   Parameters:
        :   **handle** (*LP_BNProjectFolder*) –

    export(*dest: ~os.PathLike | str, progress_func: ~typing.Callable[[int, int], bool] = <function _nop>*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/project.html#ProjectFolder.export)
    :   Recursively export this folder to disk

        Parameters:
        :   - **dest** ([*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike "(in Python
              v3.14)") *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Destination path for the exported contents
            - **progress_func**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")*]*) – Progress function that will be called as contents are exporting

        Returns:
        :   True if the export succeeded, False otherwise

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    *property* description*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the description of this folder

        Returns:
        :   Description of this folder

    *property* files*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ProjectFile](#binaryninja.project.ProjectFile "binaryninja.project.ProjectFile")]*
    :   Get the list of files in this folder

        Returns:
        :   List of files contained in the folder

    *property* id*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the unique id of this folder

        Returns:
        :   Unique identifier of this folder

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*
    :   Get the name of this folder

        Returns:
        :   Name of this folder

    *property* parent*: [ProjectFolder](#binaryninja.project.ProjectFolder "binaryninja.project.ProjectFolder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Get the parent folder of this folder

        Returns:
        :   Folder that contains this folder, or None if it is a root folder

    *property* project*: [Project](#binaryninja.project.Project "binaryninja.project.Project")*
    :   Get the project that owns this folder

        Returns:
        :   Project that owns this folder
