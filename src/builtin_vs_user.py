"""Demonstrate built-in vs user-defined behavior and edge cases."""
from typing import Any, Callable

def safe_len(obj: Any) -> int:
    """Return length for built-ins (list/tuple/dict/str).

    Raises TypeError with helpful message for unsupported types.
    """
    if isinstance(obj, (list, tuple, dict, str)):
        return len(obj)
    raise TypeError(f"safe_len: unsupported type {type(obj).__name__}")

def call_if_callable(obj: Any, *args, **kwargs):
    """If obj is callable, call it with provided args/kwargs and return result; otherwise return obj."""
    if callable(obj):
        return obj(*args, **kwargs)
    return obj
