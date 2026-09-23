# bncompleter module

This file is a modified version of rlcompleter.py from the Python project under the
Python Software Foundation License 2:
<https://github.com/python/cpython/blob/master/Lib/rlcompleter.py>
<https://github.com/python/cpython/blob/master/LICENSE>

The only changes made were to modify the regular expression in attr_matches and all code
that relied on GNU readline (the later more for readability as it wasn’t required).

---

Word completion for GNU readline.

The completer completes keywords, built-ins and globals in a selectable namespace (which
defaults to __main__); when completing NAME.NAME…, it evaluates (!) the expression up to
the last dot and completes its attributes.

It’s very cool to do “import sys” type “sys.”, hit the completion key (twice), and see
the list of names defined by the sys module!

Tip: to use the tab key as the completion key, call

> readline.parse_and_bind(“tab: complete”)

Notes:

- Exceptions raised by the completer function are *ignored* (and generally cause the
  completion to fail). This is a feature – since readline sets the tty device in raw (or
  cbreak) mode, printing a traceback wouldn’t work well without some complicated hoopla to
  save, reset and restore the tty state.
- The evaluation of the NAME.NAME… form may cause arbitrary application defined code to be
  executed if an object with a __getattr__ hook is found. Since it is the responsibility
  of the application (or the user) to enable this feature, I consider this an acceptable
  risk. More complicated expressions (e.g. function calls or indexing operations) are
  *not* evaluated.
- When the original stdin is not a tty device, GNU readline is never used, and this module
  (and the readline module) are silently inactive.

| Class | Description |
| --- | --- |
| [`binaryninja.bncompleter.Completer`](#binaryninja.bncompleter.Completer "binaryninja.bncompleter.Completer") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.bncompleter.fnsignature`](#binaryninja.bncompleter.fnsignature "binaryninja.bncompleter.fnsignature") |  |
| [`binaryninja.bncompleter.fuzzy_match`](#binaryninja.bncompleter.fuzzy_match "binaryninja.bncompleter.fuzzy_match") |  |
| [`binaryninja.bncompleter.get_class_members`](#binaryninja.bncompleter.get_class_members "binaryninja.bncompleter.get_class_members") |  |

## Completer

*class* Completer[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*namespace=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer.__init__)
    :   Create a new completer for the command line.

        Completer([namespace]) -> completer instance.

        If unspecified, the default namespace where completions are performed is __main__
        (technically, __main__.__dict__). Namespaces should be given as dictionaries.

        Completer instances should be used as the completion mechanism of readline via the
        set_completer() call:

        readline.set_completer(Completer(my_namespace).complete)

    attr_matches(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer.attr_matches)
    :   Compute matches when text contains a dot.

        Assuming the text is of the form NAME.NAME….[NAME], and is evaluable in self.namespace,
        it will be evaluated and its attributes (as revealed by dir()) are used as possible
        completions. (For class instances, class members are also considered.)

        WARNING: this can still invoke arbitrary C code, if an object with a __getattr__ hook is
        evaluated.

    can_complete_arguments(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer.can_complete_arguments)
    :   A faster check to see if argument assistance is even needed currently.

        Parameters:
        :   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Returns:

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    complete(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *state*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer.complete)
    :   Return the next possible completion for ‘text’.

        This is called successively with state == 0, 1, 2, … until it returns None. The
        completion should begin with ‘text’.

        Parameters:
        :   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") |
            *None*

    complete_arguments(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer.complete_arguments)
    :   Given input up to the contents of ‘text’, return a HTML string containing the arguments
        for the function.

        Used in UI to display and highlight arguments of a function as the user types them.

        Parameters:
        :   **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)"))

        Return type:
        :   [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python
            v3.14)")[[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
            v3.14)") | *None*, [*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")]

    global_matches(*text*)[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#Completer.global_matches)
    :   Compute matches when text is a simple name.

        Return a list of all keywords, built-in functions and names currently defined in
        self.namespace that match.

## fnsignature

fnsignature(*obj*)[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#fnsignature)

## fuzzy_match

fuzzy_match(*target*, *query*)[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#fuzzy_match)

## get_class_members

get_class_members(*klass*)[[source]](https://api.binary.ninja/_modules/binaryninja/bncompleter.html#get_class_members)
