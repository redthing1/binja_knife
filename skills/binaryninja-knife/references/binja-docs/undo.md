# undo module

| Class | Description |
| --- | --- |
| [`binaryninja.undo.UndoAction`](#binaryninja.undo.UndoAction "binaryninja.undo.UndoAction") | Class representing an action in an UndoEntry |
| [`binaryninja.undo.UndoEntry`](#binaryninja.undo.UndoEntry "binaryninja.undo.UndoEntry") | Class representing an entry in undo/redo history |

## UndoAction

*class* UndoAction[[source]](https://api.binary.ninja/_modules/binaryninja/undo.html#UndoAction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class representing an action in an UndoEntry

    __init__(*handle: LP_BNUndoAction*)[[source]](https://api.binary.ninja/_modules/binaryninja/undo.html#UndoAction.__init__)
    :   Parameters:
        :   **handle** (*LP_BNUndoAction*)

    *property* summary_text*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## UndoEntry

*class* UndoEntry[[source]](https://api.binary.ninja/_modules/binaryninja/undo.html#UndoEntry)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    Class representing an entry in undo/redo history

    __init__(*handle: LP_BNUndoEntry*)[[source]](https://api.binary.ninja/_modules/binaryninja/undo.html#UndoEntry.__init__)
    :   Parameters:
        :   **handle** (*LP_BNUndoEntry*)

    *property* actions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[UndoAction](#binaryninja.undo.UndoAction "binaryninja.undo.UndoAction")]*
    :   Get the list of actions in this entry

        Returns:
        :   List of UndoAction in this UndoEntry
