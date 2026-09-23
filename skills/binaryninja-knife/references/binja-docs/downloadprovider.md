# downloadprovider module

| Class | Description |
| --- | --- |
| [`binaryninja.downloadprovider.DownloadInstance`](#binaryninja.downloadprovider.DownloadInstance "binaryninja.downloadprovider.DownloadInstance") |  |
| [`binaryninja.downloadprovider.DownloadProvider`](#binaryninja.downloadprovider.DownloadProvider "binaryninja.downloadprovider.DownloadProvider") |  |
| [`binaryninja.downloadprovider.PythonDownloadInstance`](#binaryninja.downloadprovider.PythonDownloadInstance "binaryninja.downloadprovider.PythonDownloadInstance") |  |
| [`binaryninja.downloadprovider.PythonDownloadProvider`](#binaryninja.downloadprovider.PythonDownloadProvider "binaryninja.downloadprovider.PythonDownloadProvider") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.downloadprovider.to_bytes`](#binaryninja.downloadprovider.to_bytes "binaryninja.downloadprovider.to_bytes") |  |

## DownloadInstance

*class* DownloadInstance[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    *class* Response[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.Response)
    :   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
        v3.14)")

        __init__(*status_code*, *headers*, *content*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.Response.__init__)

    __init__(*provider*, *handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.__init__)

    get(*url*, *headers=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.get)

    get_response(*url*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.get_response)

    *abstract* perform_custom_request(*method*, *url*, *headers*, *data_generator*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.perform_custom_request)

    *abstract* perform_destroy_instance()[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.perform_destroy_instance)

    *abstract* perform_request(*url*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.perform_request)

    post(*url*, *headers=None*, *data=None*, *json=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.post)

    put(*url*, *headers=None*, *data=None*, *json=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.put)

    request(*method*, *url*, *headers=None*, *data=None*, *json=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadInstance.request)

## DownloadProvider

*class* DownloadProvider[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadProvider)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle=None*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadProvider.__init__)

    create_instance()[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadProvider.create_instance)

    register()[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#DownloadProvider.register)

    instance_class *= None*

    name *= None*

## PythonDownloadInstance

*class* PythonDownloadInstance[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#PythonDownloadInstance)
:   Bases: [`DownloadInstance`](#binaryninja.downloadprovider.DownloadInstance
    "binaryninja.downloadprovider.DownloadInstance")

    __init__(*provider*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#PythonDownloadInstance.__init__)

    perform_custom_request(*method*, *url*, *headers*, *data_generator*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#PythonDownloadInstance.perform_custom_request)

    perform_destroy_instance()[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#PythonDownloadInstance.perform_destroy_instance)

    perform_request(*url*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#PythonDownloadInstance.perform_request)

## PythonDownloadProvider

*class* PythonDownloadProvider[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#PythonDownloadProvider)
:   Bases: [`DownloadProvider`](#binaryninja.downloadprovider.DownloadProvider
    "binaryninja.downloadprovider.DownloadProvider")

    instance_class
    :   alias of [`PythonDownloadInstance`](#binaryninja.downloadprovider.PythonDownloadInstance
        "binaryninja.downloadprovider.PythonDownloadInstance")

    name *= 'PythonDownloadProvider'*

## to_bytes

to_bytes(*field*)[[source]](https://api.binary.ninja/_modules/binaryninja/downloadprovider.html#to_bytes)
