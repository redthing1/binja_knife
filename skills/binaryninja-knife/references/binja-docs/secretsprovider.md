# secretsprovider module

| Class | Description |
| --- | --- |
| [`binaryninja.secretsprovider.SecretsProvider`](#binaryninja.secretsprovider.SecretsProvider "binaryninja.secretsprovider.SecretsProvider") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.secretsprovider.to_bytes`](#binaryninja.secretsprovider.to_bytes "binaryninja.secretsprovider.to_bytes") |  |

## SecretsProvider

*class* SecretsProvider[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider)
:   Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object "(in Python
    v3.15)")

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.__init__)

    delete_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.delete_data)
    :   Parameters:
        :   **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
            v3.15)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

    get_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.get_data)
    :   Parameters:
        :   **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
            v3.15)"))

        Return type:
        :   [*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

    has_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.has_data)
    :   Parameters:
        :   **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
            v3.15)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

    perform_delete_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.perform_delete_data)
    :   Parameters:
        :   **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
            v3.15)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

    perform_get_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.perform_get_data)
    :   Parameters:
        :   **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
            v3.15)"))

        Return type:
        :   [*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

    perform_has_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.perform_has_data)
    :   Parameters:
        :   **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
            v3.15)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

    perform_store_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*, *data: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.perform_store_data)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
              v3.15)"))
            - **data** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
              v3.15)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.register)

    store_data(*key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*, *data: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")*) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#SecretsProvider.store_data)
    :   Parameters:
        :   - **key** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
              v3.15)"))
            - **data** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python
              v3.15)"))

        Return type:
        :   [*bool*](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

    instance_class *= None*

    name *= None*

## to_bytes

to_bytes(*field*)[[source]](https://api.binary.ninja/_modules/binaryninja/secretsprovider.html#to_bytes)
