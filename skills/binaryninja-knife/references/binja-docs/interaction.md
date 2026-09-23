# interaction module

| Class | Description |
| --- | --- |
| [`binaryninja.interaction.AddressField`](#binaryninja.interaction.AddressField "binaryninja.interaction.AddressField") | `AddressField` prompts the user for an address. By passing the optional view and… |
| [`binaryninja.interaction.CheckboxField`](#binaryninja.interaction.CheckboxField "binaryninja.interaction.CheckboxField") | `CheckboxField` prompts the user to choose a yes/no option in a checkbox. Result is stored in… |
| [`binaryninja.interaction.ChoiceField`](#binaryninja.interaction.ChoiceField "binaryninja.interaction.ChoiceField") | `ChoiceField` prompts the user to choose from the list of strings provided in `choices`. |
| [`binaryninja.interaction.DirectoryNameField`](#binaryninja.interaction.DirectoryNameField "binaryninja.interaction.DirectoryNameField") | `DirectoryNameField` prompts the user to specify a directory name to open. Result is stored in… |
| [`binaryninja.interaction.FlowGraphReport`](#binaryninja.interaction.FlowGraphReport "binaryninja.interaction.FlowGraphReport") |  |
| [`binaryninja.interaction.HTMLReport`](#binaryninja.interaction.HTMLReport "binaryninja.interaction.HTMLReport") |  |
| [`binaryninja.interaction.IntegerField`](#binaryninja.interaction.IntegerField "binaryninja.interaction.IntegerField") | `IntegerField` add prompt for integer. Result is stored in self.result as an int. |
| [`binaryninja.interaction.InteractionHandler`](#binaryninja.interaction.InteractionHandler "binaryninja.interaction.InteractionHandler") |  |
| [`binaryninja.interaction.LabelField`](#binaryninja.interaction.LabelField "binaryninja.interaction.LabelField") | `LabelField` adds a text label to the display. |
| [`binaryninja.interaction.MarkdownReport`](#binaryninja.interaction.MarkdownReport "binaryninja.interaction.MarkdownReport") |  |
| [`binaryninja.interaction.MultilineTextField`](#binaryninja.interaction.MultilineTextField "binaryninja.interaction.MultilineTextField") | `MultilineTextField` add multi-line text string input field. Result is stored in self.result… |
| [`binaryninja.interaction.OpenFileNameField`](#binaryninja.interaction.OpenFileNameField "binaryninja.interaction.OpenFileNameField") | `OpenFileNameField` prompts the user to specify a file name to open. Result is stored in… |
| [`binaryninja.interaction.PlainTextReport`](#binaryninja.interaction.PlainTextReport "binaryninja.interaction.PlainTextReport") |  |
| [`binaryninja.interaction.ReportCollection`](#binaryninja.interaction.ReportCollection "binaryninja.interaction.ReportCollection") |  |
| [`binaryninja.interaction.SaveFileNameField`](#binaryninja.interaction.SaveFileNameField "binaryninja.interaction.SaveFileNameField") | `SaveFileNameField` prompts the user to specify a file name to save. Result is stored in… |
| [`binaryninja.interaction.SeparatorField`](#binaryninja.interaction.SeparatorField "binaryninja.interaction.SeparatorField") | `SeparatorField` adds vertical separation to the display. |
| [`binaryninja.interaction.TextLineField`](#binaryninja.interaction.TextLineField "binaryninja.interaction.TextLineField") | `TextLineField` Adds prompt for text string input. Result is stored in self.result as a string… |

| Function | Description |
| --- | --- |
| [`binaryninja.interaction.get_address_input`](#binaryninja.interaction.get_address_input "binaryninja.interaction.get_address_input") | `get_address_input` prompts the user for an address with the given prompt and title |
| [`binaryninja.interaction.get_checkbox_input`](#binaryninja.interaction.get_checkbox_input "binaryninja.interaction.get_checkbox_input") | `get_checkbox_input` prompts the user for a checkbox input :param prompt: String to prompt… |
| [`binaryninja.interaction.get_choice_input`](#binaryninja.interaction.get_choice_input "binaryninja.interaction.get_choice_input") | `get_choice_input` prompts the user to select the one of the provided choices |
| [`binaryninja.interaction.get_directory_name_input`](#binaryninja.interaction.get_directory_name_input "binaryninja.interaction.get_directory_name_input") | `get_directory_name_input` prompts the user for a directory name to save as, optionally… |
| [`binaryninja.interaction.get_form_input`](#binaryninja.interaction.get_form_input "binaryninja.interaction.get_form_input") | `get_from_input` Prompts the user for a set of inputs specified in `fields` with given title. |
| [`binaryninja.interaction.get_int_input`](#binaryninja.interaction.get_int_input "binaryninja.interaction.get_int_input") | `get_int_input` prompts the user to input a integer with the given prompt and title |
| [`binaryninja.interaction.get_large_choice_input`](#binaryninja.interaction.get_large_choice_input "binaryninja.interaction.get_large_choice_input") | `get_large_choice_input` prompts the user to select the one of the provided choices from a… |
| [`binaryninja.interaction.get_open_filename_input`](#binaryninja.interaction.get_open_filename_input "binaryninja.interaction.get_open_filename_input") | `get_open_filename_input` prompts the user for a file name to open |
| [`binaryninja.interaction.get_save_filename_input`](#binaryninja.interaction.get_save_filename_input "binaryninja.interaction.get_save_filename_input") | `get_save_filename_input` prompts the user for a file name to save as, optionally providing a… |
| [`binaryninja.interaction.get_text_line_input`](#binaryninja.interaction.get_text_line_input "binaryninja.interaction.get_text_line_input") | `get_text_line_input` prompts the user to input a string with the given prompt and title |
| [`binaryninja.interaction.markdown_to_html`](#binaryninja.interaction.markdown_to_html "binaryninja.interaction.markdown_to_html") | `markdown_to_html` converts the provided markdown to HTML |
| [`binaryninja.interaction.open_url`](#binaryninja.interaction.open_url "binaryninja.interaction.open_url") | `open_url` Opens a given url in the user’s web browser, if available. |
| [`binaryninja.interaction.run_progress_dialog`](#binaryninja.interaction.run_progress_dialog "binaryninja.interaction.run_progress_dialog") | `run_progress_dialog` runs a given task in a background thread, showing an updating progress… |
| [`binaryninja.interaction.show_graph_report`](#binaryninja.interaction.show_graph_report "binaryninja.interaction.show_graph_report") | `show_graph_report` displays a flow graph in UI applications and nothing in command-line… |
| [`binaryninja.interaction.show_html_report`](#binaryninja.interaction.show_html_report "binaryninja.interaction.show_html_report") | `show_html_report` displays the HTML contents in UI applications and plaintext in command-line… |
| [`binaryninja.interaction.show_markdown_report`](#binaryninja.interaction.show_markdown_report "binaryninja.interaction.show_markdown_report") | `show_markdown_report` displays the markdown contents in UI applications and plaintext in… |
| [`binaryninja.interaction.show_message_box`](#binaryninja.interaction.show_message_box "binaryninja.interaction.show_message_box") | `show_message_box` Displays a configurable message box in the UI, or prompts on the console as… |
| [`binaryninja.interaction.show_plain_text_report`](#binaryninja.interaction.show_plain_text_report "binaryninja.interaction.show_plain_text_report") | `show_plain_text_report` displays contents to the user in the UI or on the command-line |
| [`binaryninja.interaction.show_report_collection`](#binaryninja.interaction.show_report_collection "binaryninja.interaction.show_report_collection") | `show_report_collection` displays multiple reports in UI applications |

## AddressField

*class* AddressField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#AddressField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `AddressField` prompts the user for an address. By passing the optional view and
    current_address parameters offsets can be used instead of just an address. The result is
    stored as in int in self.result.

    Note

    This API currently functions differently on the command-line, as the view and
    current_address are disregarded. Additionally where as in the UI the result defaults to
    hexadecimal on the command-line 0x must be specified.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *current_address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *default: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#AddressField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)
            - **current_address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)"))
            - **default** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)

    *property* current_address
    :   current address to use as a base for relative calculations

    *property* prompt
    :   prompt to be presented to the user

    *property* result

    *property* view
    :   BinaryView for the address

## CheckboxField

*class* CheckboxField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#CheckboxField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `CheckboxField` prompts the user to choose a yes/no option in a checkbox. Result is
    stored in self.result as a boolean value.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Prompt to be presented to the user
        - **default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")) – Default state of the checkbox (False == unchecked, True == checked)

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#CheckboxField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)") *|* *None*)

    *property* default

    *property* prompt

    *property* result

## ChoiceField

*class* ChoiceField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#ChoiceField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `ChoiceField` prompts the user to choose from the list of strings provided in `choices`.
    Result is stored in self.result as an index in to the choices array.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Prompt to be presented to the user
        - **choices** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")*)*) – List of choices to choose from
        - **default** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int
          "(in Python v3.14)")*]*) – Optional index into choices that will be selected by default

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *choices: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *default: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#ChoiceField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **choices** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)")*]*)
            - **default** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)

    *property* choices*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*

    *property* default*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* prompt*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* result*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## DirectoryNameField

*class* DirectoryNameField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#DirectoryNameField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `DirectoryNameField` prompts the user to specify a directory name to open. Result is
    stored in self.result as a string.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#DirectoryNameField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

    *property* default_name

    *property* prompt

    *property* result

## FlowGraphReport

*class* FlowGraphReport[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#FlowGraphReport)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *graph: [FlowGraph](flowgraph.md#binaryninja.flowgraph.FlowGraph "binaryninja.flowgraph.FlowGraph")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#FlowGraphReport.__init__)
    :   Parameters:
        :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
              "binaryninja.flowgraph.FlowGraph"))
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)

    *property* graph

    *property* title

    *property* view

## HTMLReport

*class* HTMLReport[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#HTMLReport)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *plaintext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#HTMLReport.__init__)
    :   Parameters:
        :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **plaintext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)

    *property* contents

    *property* plaintext

    *property* title

    *property* view

## IntegerField

*class* IntegerField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#IntegerField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `IntegerField` add prompt for integer. Result is stored in self.result as an int.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#IntegerField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)") *|* *None*)

    *property* prompt

    *property* result

## InteractionHandler

*class* InteractionHandler[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__()[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.__init__)

    get_address_input(*prompt*, *title*, *view*, *current_address*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_address_input)

    get_checkbox_input(*prompt*, *default_choice*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_checkbox_input)

    get_choice_input(*prompt*, *title*, *choices*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_choice_input)

    get_directory_name_input(*prompt*, *default_name*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_directory_name_input)

    get_form_input(*fields*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_form_input)

    get_int_input(*prompt*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_int_input)

    get_large_choice_input(*prompt*, *title*, *choices*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_large_choice_input)

    get_open_filename_input(*prompt*, *ext*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_open_filename_input)

    get_save_filename_input(*prompt*, *ext*, *default_name*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_save_filename_input)

    get_text_line_input(*prompt*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.get_text_line_input)

    open_url(*url*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.open_url)

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.register)

    run_progress_dialog(*task: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.run_progress_dialog)
    :   Parameters:
        :   **task** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
            "(in Python
            v3.14)")*[**[*[*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
            "(in Python v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int
            "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int
            "(in Python v3.14)")*]**,*
            [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
            v3.14)")*]**]**,* *None**]*)

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    show_graph_report(*view*, *title*, *graph*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.show_graph_report)

    show_html_report(*view*, *title*, *contents*, *plaintext*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.show_html_report)

    show_markdown_report(*view*, *title*, *contents*, *plaintext*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.show_markdown_report)

    show_message_box(*title*, *text*, *buttons*, *icon*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.show_message_box)

    show_plain_text_report(*view*, *title*, *contents*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.show_plain_text_report)

    show_report_collection(*title*, *reports*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#InteractionHandler.show_report_collection)

## LabelField

*class* LabelField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#LabelField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `LabelField` adds a text label to the display.

    __init__(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#LabelField.__init__)
    :   Parameters:
        :   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

    *property* text*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

## MarkdownReport

*class* MarkdownReport[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#MarkdownReport)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *plaintext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#MarkdownReport.__init__)
    :   Parameters:
        :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **plaintext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)

    *property* contents

    *property* plaintext

    *property* title

    *property* view

## MultilineTextField

*class* MultilineTextField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#MultilineTextField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `MultilineTextField` add multi-line text string input field. Result is stored in
    self.result as a string. This option is not supported on the command-line.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#MultilineTextField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

    *property* prompt

    *property* result

## OpenFileNameField

*class* OpenFileNameField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#OpenFileNameField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `OpenFileNameField` prompts the user to specify a file name to open. Result is stored in
    self.result as a string.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#OpenFileNameField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **ext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

    *property* ext

    *property* prompt

    *property* result

## PlainTextReport

*class* PlainTextReport[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#PlainTextReport)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#PlainTextReport.__init__)
    :   Parameters:
        :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*)

    *property* contents

    *property* title

    *property* view

## ReportCollection

*class* ReportCollection[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#ReportCollection)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#ReportCollection.__init__)

    append(*report*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#ReportCollection.append)

    update(*i*, *report*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#ReportCollection.update)

## SaveFileNameField

*class* SaveFileNameField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#SaveFileNameField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `SaveFileNameField` prompts the user to specify a file name to save. Result is stored in
    self.result as a string.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *default_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#SaveFileNameField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **ext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)"))
            - **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

    *property* default_name

    *property* ext

    *property* prompt

    *property* result

## SeparatorField

*class* SeparatorField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#SeparatorField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `SeparatorField` adds vertical separation to the display.

## TextLineField

*class* TextLineField[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#TextLineField)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `TextLineField` Adds prompt for text string input. Result is stored in self.result as a
    string on completion.

    __init__(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#TextLineField.__init__)
    :   Parameters:
        :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)"))
            - **default** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* *None*)

    *property* prompt

    *property* result

## get_address_input

get_address_input(*prompt*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_address_input)
:   `get_address_input` prompts the user for an address with the given prompt and title

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – String to prompt with.
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title of the window when executed in the UI.

    Return type:
    :   integer value input by the user.

    Example:
    :   ```
        >>> get_address_input("PROMPT>", "getinfo")
        PROMPT> 10
        10L
        ```

## get_checkbox_input

get_checkbox_input(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_checkbox_input)
:   `get_checkbox_input` prompts the user for a checkbox input :param prompt: String to
    prompt with :param title: Title of the window when executed in the UI :param default:
    Optional default state for the checkbox (false == unchecked, true == checked), False if
    not set. :rtype: bool indicating the state of the checkbox

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)"))
        - **default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)"))

## get_choice_input

get_choice_input(*prompt*, *title*, *choices*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_choice_input)
:   `get_choice_input` prompts the user to select the one of the provided choices

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used. The UI uses a combo box.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – String to prompt with.
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title of the window when executed in the UI.
        - **choices** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")*)*) – A list of strings for the user to choose from.

    Return type:
    :   integer array index of the selected option

    Example:
    :   ```
        >>> get_choice_input("PROMPT>", "choices", ["Yes", "No", "Maybe"])
        choices
        1) Yes
        2) No
        3) Maybe
        PROMPT> 1
        0L
        ```

## get_directory_name_input

get_directory_name_input(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_directory_name_input)
:   `get_directory_name_input` prompts the user for a directory name to save as, optionally
    providing a default_name

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used. The UI uses the native window pop-up
    for file selection.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Prompt to display.
        - **default_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – Optional, default directory name.

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    Example:
    :   ```
        >>> get_directory_name_input("prompt")
        prompt dirname
        'dirname'
        ```

## get_form_input

get_form_input(*fields*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_form_input)
:   `get_from_input` Prompts the user for a set of inputs specified in `fields` with given
    title. The fields parameter is a list which can contain the following types:

    | FieldType | Description |
    | --- | --- |
    | str | an alias for LabelField |
    | None | an alias for SeparatorField |
    | LabelField | Text output |
    | SeparatorField | Vertical spacing |
    | TextLineField | Prompt for a string value |
    | MultilineTextField | Prompt for multi-line string value |
    | IntegerField | Prompt for an integer |
    | AddressField | Prompt for an address |
    | ChoiceField | Prompt for a choice from provided options |
    | OpenFileNameField | Prompt for file to open |
    | SaveFileNameField | Prompt for file to save to |
    | DirectoryNameField | Prompt for directory name |
    | CheckboxFormField | Prompt for a checkbox |

    This API is flexible and works both in the UI via a pop-up dialog and on the
    command-line.

    Note

    More complicated APIs should consider using the included pyside2 functionality in the
    binaryninjaui module. Returns true or false depending on whether the user submitted
    responses or cancelled the dialog.

    Parameters:
    :   - **fields** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")*) or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(**None**) or* [*list*](https://docs.python.org/3/library/stdtypes.html#list
          "(in Python v3.14)")*(*[*LabelField*](#binaryninja.interaction.LabelField
          "binaryninja.interaction.LabelField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*SeparatorField*](#binaryninja.interaction.SeparatorField
          "binaryninja.interaction.SeparatorField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*TextLineField*](#binaryninja.interaction.TextLineField
          "binaryninja.interaction.TextLineField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*MultilineTextField*](#binaryninja.interaction.MultilineTextField
          "binaryninja.interaction.MultilineTextField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*IntegerField*](#binaryninja.interaction.IntegerField
          "binaryninja.interaction.IntegerField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*AddressField*](#binaryninja.interaction.AddressField
          "binaryninja.interaction.AddressField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*ChoiceField*](#binaryninja.interaction.ChoiceField
          "binaryninja.interaction.ChoiceField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*OpenFileNameField*](#binaryninja.interaction.OpenFileNameField
          "binaryninja.interaction.OpenFileNameField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*SaveFileNameField*](#binaryninja.interaction.SaveFileNameField
          "binaryninja.interaction.SaveFileNameField")*) or*
          [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*DirectoryNameField*](#binaryninja.interaction.DirectoryNameField
          "binaryninja.interaction.DirectoryNameField")*)*) – A list containing these classes,
          strings or None
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – The title of the pop-up dialog

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    Example:
    :   ```
        >>> int_f = IntegerField("Specify Integer")
        >>> tex_f = TextLineField("Specify name")
        >>> choice_f = ChoiceField("Options", ["Yes", "No", "Maybe"])
        >>> get_form_input(["Get Data", None, int_f, tex_f, choice_f], "The options")
        Get Data
        <empty>
        Specify Integer 1337
        Specify name Peter
        The options
        1) Yes
        2) No
        3) Maybe
        Options 1
        >>> True
        >>> print(tex_f.result, int_f.result, choice_f.result)
        Peter 1337 0
        ```

## get_int_input

get_int_input(*prompt*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_int_input)
:   `get_int_input` prompts the user to input a integer with the given prompt and title

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – String to prompt with
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title of the window when executed in the UI

    Return type:
    :   integer value input by the user

    Example:
    :   ```
        >>> get_int_input("PROMPT>", "getinfo")
        PROMPT> 10
        10
        ```

## get_large_choice_input

get_large_choice_input(*prompt*, *title*, *choices*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_large_choice_input)
:   `get_large_choice_input` prompts the user to select the one of the provided choices from
    a large pool

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a text prompt is used. The UI uses a filterable list of entries

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Text for the button when executed in the UI. Prompt shown for selection
          headless.
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title of the window when executed in the UI.
        - **choices** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
          v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")*)*) – A list of strings for the user to choose from.

    Return type:
    :   integer array index of the selected option

    Example:
    :   ```
        >>> get_large_choice_input("Select Function", "Select a Function", [f.symbol.short_name for f in bv.functions])
        ```

## get_open_filename_input

get_open_filename_input(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_open_filename_input)
:   `get_open_filename_input` prompts the user for a file name to open

    Note

    This API functions differently on the command-line vs the UI. In the UI a pop-up is
    used. On the command-line a simple text prompt is used. The UI uses the native window
    pop-up for file selection.

    Multiple file selection groups can be included if separated by two semicolons. Multiple
    file wildcards may be specified by using a space within the parenthesis.

    Also, a simple selector of *.extension by itself may also be used instead of specifying
    the description.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Prompt to display.
        - **ext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Optional, file extension

    Example:
    :   ```
        >>> get_open_filename_input("filename:", "*.py")
        'test.py'
        >>> get_open_filename_input("filename:", "All Files (*)")
        'test.py'
        >>> get_open_filename_input("filename:", "Executables (*.exe)")
        'foo.exe'
        >>> get_open_filename_input("filename:", "Executables (*.exe *.com)")
        'foo.exe'
        >>> get_open_filename_input("filename:", "Executables (*.exe *.com);;Python Files (*.py);;All Files (*)")
        'foo.exe'
        ```

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
        *None*

## get_save_filename_input

get_save_filename_input(*prompt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *default_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_save_filename_input)
:   `get_save_filename_input` prompts the user for a file name to save as, optionally
    providing a file extension and default_name

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used. The UI uses the native window pop-up
    for file selection.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Prompt to display.
        - **ext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Optional, file extension
        - **default_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
          Python v3.14)")) – Optional, default file name.

    Example:
    :   ```
        >>> get_save_filename_input("filename:", "*.py", "test.py")
        filename: test.py
        'test.py'
        >>> get_save_filename_input("filename:", "All Files (*)", "test.py")
        filename: test.py
        'test.py'
        >>> get_save_filename_input("filename:", "Executables (*.exe)", "foo.exe")
        filename: foo.exe
        'foo.exe'
        >>> get_save_filename_input("filename:", "Executables (*.exe *.com)", "foo.exe")
        filename: foo.exe
        'foo.exe'
        >>> get_save_filename_input("filename:", "Executables (*.exe *.com);;Python Files (*.py);;All Files (*)", "foo.exe")
        filename: foo.exe
        'foo.exe'
        ```

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
        *None*

## get_text_line_input

get_text_line_input(*prompt*, *title*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#get_text_line_input)
:   `get_text_line_input` prompts the user to input a string with the given prompt and title

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used.

    Parameters:
    :   - **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – String to prompt with
        - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title of the window when executed in the UI

    Return type:
    :   str containing the input without trailing newline character

    Example:
    :   ```
        >>> get_text_line_input("PROMPT>", "getinfo")
        PROMPT> Input!
        'Input!'
        ```

## markdown_to_html

markdown_to_html(*contents*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#markdown_to_html)
:   `markdown_to_html` converts the provided markdown to HTML

    Parameters:
    :   **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – Markdown contents to convert to HTML

    Return type:
    :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    Example:
    :   ```
        >>> markdown_to_html("##Yay")
        '<h2>Yay</h2>'
        ```

## open_url

open_url(*url*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#open_url)
:   `open_url` Opens a given url in the user’s web browser, if available.

    Parameters:
    :   **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
        v3.14)")) – Url to open

    Returns:
    :   True if successful

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## run_progress_dialog

run_progress_dialog(*title: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *can_cancel: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *task: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#run_progress_dialog)
:   `run_progress_dialog` runs a given task in a background thread, showing an updating
    progress bar which the user can cancel.

    Parameters:
    :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Dialog title
        - **can_cancel** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
          Python v3.14)")) – If the task can be cancelled
        - **task** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
          "(in Python
          v3.14)")*[**[*[*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable
          "(in Python v3.14)")*[**[*[*int*](https://docs.python.org/3/library/functions.html#int
          "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int
          "(in Python v3.14)")*]**,*
          [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
          v3.14)")*]**]**,* *None**]*) – Function to perform the task, taking as a parameter a
          function which should be called to report progress updates and check for cancellation.
          If the progress function returns false, the user has requested to cancel, and the task
          should handle this appropriately.

    Returns:
    :   True if not cancelled

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## show_graph_report

show_graph_report(*title*, *graph*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#show_graph_report)
:   `show_graph_report` displays a flow graph in UI applications and nothing in command-line
    applications. This API doesn’t support clickable references into an existing BinaryView.
    Use the `BinaryView.show_html_report` API if hyperlinking is needed.

    Note

    This API function will have no effect outside the UI.

    Parameters:
    :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title to display in the tab
        - **graph** ([*FlowGraph*](flowgraph.md#binaryninja.flowgraph.FlowGraph
          "binaryninja.flowgraph.FlowGraph")) – Flow graph to display

    Return type:
    :   *None*

## show_html_report

show_html_report(*title*, *contents*, *plaintext=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#show_html_report)
:   `show_html_report` displays the HTML contents in UI applications and plaintext in
    command-line applications. This API doesn’t support hyperlinking into the BinaryView,
    use the `BinaryView.show_html_report` API if hyperlinking is needed.

    Parameters:
    :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title to display in the tab
        - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – HTML contents to display
        - **plaintext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Plain text version to display (used on the command-line)

    Return type:
    :   *None*

    Example:
    :   ```
        >>> show_html_report("title", "<h1>Contents</h1>", "Plain text contents")
        Plain text contents
        ```

## show_markdown_report

show_markdown_report(*title*, *contents*, *plaintext=''*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#show_markdown_report)
:   `show_markdown_report` displays the markdown contents in UI applications and plaintext
    in command-line applications. This API doesn’t support hyperlinking into the BinaryView,
    use the `BinaryView.show_markdown_report` API if hyperlinking is needed.

    Note

    This API function differently on the command-line vs the UI. In the UI a pop-up is used.
    On the command-line a simple text prompt is used.

    Parameters:
    :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – title to display in the tab
        - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – markdown contents to display
        - **plaintext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Plain text version to display (used on the command-line)

    Return type:
    :   *None*

    Example:
    :   ```
        >>> show_markdown_report("title", "##Contents", "Plain text contents")
        Plain text contents
        ```

## show_message_box

show_message_box(*title*, *text*, *buttons=MessageBoxButtonSet.OKButtonSet*, *icon=MessageBoxIcon.InformationIcon*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#show_message_box)
:   `show_message_box` Displays a configurable message box in the UI, or prompts on the
    console as appropriate

    Note:
    :   This uses a standard QDialog which means simple HTML will render as HTML, but links are
        not clickable and special characters need to be escaped.

    Parameters:
    :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)") *|* *None*) – Text title for the message box.
        - **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)") *|* *None*) – Text for the main body of the message box.
        - **buttons** ([*MessageBoxButtonSet*](enums.md#binaryninja.enums.MessageBoxButtonSet
          "binaryninja.enums.MessageBoxButtonSet")) – One of `MessageBoxButtonSet`
        - **icon** ([*MessageBoxIcon*](enums.md#binaryninja.enums.MessageBoxIcon
          "binaryninja.enums.MessageBoxIcon")) – One of `MessageBoxIcon`

    Returns:
    :   Which button was selected

    Return type:
    :   [*MessageBoxButtonResult*](enums.md#binaryninja.enums.MessageBoxButtonResult
        "binaryninja.enums.MessageBoxButtonResult")

## show_plain_text_report

show_plain_text_report(*title*, *contents*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#show_plain_text_report)
:   `show_plain_text_report` displays contents to the user in the UI or on the command-line

    Note

    This API functions differently on the command-line vs the UI. In the UI, a pop-up is
    used. On the command-line, a simple text prompt is used.

    Parameters:
    :   - **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Title to display in the tab
        - **contents** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
          v3.14)")) – Plaintext contents to display

    Return type:
    :   *None*

    Example:
    :   ```
        >>> show_plain_text_report("title", "contents")
        contents
        ```

## show_report_collection

show_report_collection(*title*, *reports*)[[source]](https://api.binary.ninja/_modules/binaryninja/interaction.html#show_report_collection)
:   `show_report_collection` displays multiple reports in UI applications

    Note

    This API function will have no effect outside the UI.

    Parameters:
    :   **reports** ([*ReportCollection*](#binaryninja.interaction.ReportCollection
        "binaryninja.interaction.ReportCollection")) – Reports to display

    Return type:
    :   *None*
