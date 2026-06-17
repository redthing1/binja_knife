try:
    import binaryninja as _binaryninja  # noqa: F401
except ModuleNotFoundError:
    plugin = None
else:
    from . import plugin  # noqa: F401

__all__ = ["plugin"]
