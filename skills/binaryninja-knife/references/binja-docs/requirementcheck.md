# requirementcheck module

| Class | Description |
| --- | --- |
| [`binaryninja.requirementcheck.DependencyConflict`](#binaryninja.requirementcheck.DependencyConflict "binaryninja.requirementcheck.DependencyConflict") |  |
| [`binaryninja.requirementcheck.DependencyRequirement`](#binaryninja.requirementcheck.DependencyRequirement "binaryninja.requirementcheck.DependencyRequirement") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.requirementcheck.pip_dependency_conflicts`](#binaryninja.requirementcheck.pip_dependency_conflicts "binaryninja.requirementcheck.pip_dependency_conflicts") | Compare active requirements for a candidate plugin. |
| [`binaryninja.requirementcheck.pip_requirements_excluding_packages`](#binaryninja.requirementcheck.pip_requirements_excluding_packages "binaryninja.requirementcheck.pip_requirements_excluding_packages") | Returns dependency requirements without excluded packages. |
| [`binaryninja.requirementcheck.pip_requirements_from_dependency_metadata`](#binaryninja.requirementcheck.pip_requirements_from_dependency_metadata "binaryninja.requirementcheck.pip_requirements_from_dependency_metadata") |  |
| [`binaryninja.requirementcheck.pip_requirements_satisfied`](#binaryninja.requirementcheck.pip_requirements_satisfied "binaryninja.requirementcheck.pip_requirements_satisfied") |  |

## DependencyConflict

*class* DependencyConflict[[source]](https://api.binary.ninja/_modules/binaryninja/requirementcheck.html#DependencyConflict)
:   Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python
    v3.15)")

    __init__(*status: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*, *package_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*, *candidate_requirements: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.15)")[[DependencyRequirement](#binaryninja.requirementcheck.DependencyRequirement "binaryninja.requirementcheck.DependencyRequirement")]*, *installed_requirements: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.15)")[[DependencyRequirement](#binaryninja.requirementcheck.DependencyRequirement "binaryninja.requirementcheck.DependencyRequirement")]*) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
    :   Parameters:
        :   - **status** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
              v3.15)"))
            - **package_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in
              Python v3.15)"))
            - **candidate_requirements**
              ([*Sequence*](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python
              v3.15)")*[*[*DependencyRequirement*](#binaryninja.requirementcheck.DependencyRequirement
              "binaryninja.requirementcheck.DependencyRequirement")*]*)
            - **installed_requirements**
              ([*Sequence*](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python
              v3.15)")*[*[*DependencyRequirement*](#binaryninja.requirementcheck.DependencyRequirement
              "binaryninja.requirementcheck.DependencyRequirement")*]*)

        Return type:
        :   *None*

    candidate_requirements*: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.15)")[[DependencyRequirement](#binaryninja.requirementcheck.DependencyRequirement "binaryninja.requirementcheck.DependencyRequirement")]*

    installed_requirements*: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.15)")[[DependencyRequirement](#binaryninja.requirementcheck.DependencyRequirement "binaryninja.requirementcheck.DependencyRequirement")]*

    package_name*: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*

    status*: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*

## DependencyRequirement

*class* DependencyRequirement[[source]](https://api.binary.ninja/_modules/binaryninja/requirementcheck.html#DependencyRequirement)
:   Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python
    v3.15)")

    __init__(*plugin_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*, *requirement: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
    :   Parameters:
        :   - **plugin_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in
              Python v3.15)"))
            - **requirement** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in
              Python v3.15)"))

        Return type:
        :   *None*

    plugin_name*: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*

    requirement*: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*

## pip_dependency_conflicts

pip_dependency_conflicts(*candidate_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*, *candidate_dependencies: [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")*, *installed_plugins: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.15)")[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)"), [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")]]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.15)")[[DependencyConflict](#binaryninja.requirementcheck.DependencyConflict "binaryninja.requirementcheck.DependencyConflict")][[source]](https://api.binary.ninja/_modules/binaryninja/requirementcheck.html#pip_dependency_conflicts)
:   Compare active requirements for a candidate plugin.

    See the following for more on dependency and version specifiers:

    - <https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers>
    - <https://packaging.python.org/en/latest/specifications/version-specifiers/#version-specifiers>

    Markers that do not apply are ignored. Only a subset of the possible operators are
    handled and the result we hand back is conservative if we can’t prove a conflict.

    Parameters:
    :   - **candidate_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in
          Python v3.15)"))
        - **candidate_dependencies**
          ([*bytes*](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)"))
        - **installed_plugins**
          ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python
          v3.15)")*[*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python
          v3.15)")*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
          v3.15)")*,* [*bytes*](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python
          v3.15)")*]**]*)

    Return type:
    :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
        v3.15)")[[*DependencyConflict*](#binaryninja.requirementcheck.DependencyConflict
        "binaryninja.requirementcheck.DependencyConflict")]

## pip_requirements_excluding_packages

pip_requirements_excluding_packages(*dependencies: [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")*, *excluded_package_names: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.15)")[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")]*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.15)")[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")][[source]](https://api.binary.ninja/_modules/binaryninja/requirementcheck.html#pip_requirements_excluding_packages)
:   Returns dependency requirements without excluded packages.

    Requirements that cannot be parsed are kept to avoid hiding an unsupported or malformed
    dependency.

    Parameters:
    :   - **dependencies** ([*bytes*](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in
          Python v3.15)"))
        - **excluded_package_names**
          ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python
          v3.15)")*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
          v3.15)")*]*)

    Return type:
    :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
        v3.15)")[[*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
        v3.15)")]

## pip_requirements_from_dependency_metadata

pip_requirements_from_dependency_metadata(*dependencies: [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.15)")[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")][[source]](https://api.binary.ninja/_modules/binaryninja/requirementcheck.html#pip_requirements_from_dependency_metadata)
:   Parameters:
    :   **dependencies** ([*bytes*](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in
        Python v3.15)"))

    Return type:
    :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
        v3.15)")[[*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
        v3.15)")]

## pip_requirements_satisfied

pip_requirements_satisfied(*requirements: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.15)")[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")]*, *installed_versions: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.15)")[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)"), [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)") = None*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/requirementcheck.html#pip_requirements_satisfied)
:   Parameters:
    :   - **requirements**
          ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python
          v3.15)")*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
          v3.15)")*]*)
        - **installed_versions**
          ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
          v3.15)")*[*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
          v3.15)")*,* [*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
          v3.15)")*]* *|* *None*)

    Return type:
    :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
