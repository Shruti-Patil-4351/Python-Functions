"""Decorators: timing, type checking and helpers."""
import time
import functools
from typing import Callable

def timeit(fn: Callable) -> Callable:
    """Decorator that returns a wrapper which returns (result, elapsed_seconds).

    Keeps 4 decimals of precision for elapsed seconds.
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        elapsed = round(end - start, 4)
        return result, elapsed
    return wrapper

def type_check(**types):
    """Decorator factory verifying types of named arguments.

    Usage:
        @type_check(x=int, y=str)
        def f(x, y='a'): ...
    It checks types for provided named parameters if present in the call.
    """
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            bound = {}
            # Check kwargs first
            for name, expected in types.items():
                if name in kwargs:
                    if not isinstance(kwargs[name], expected):
                        raise TypeError(f"Argument '{name}' must be {expected}, got {type(kwargs[name])}")
            # Not performing full signature binding to keep implementation small and focused on named args.
            return fn(*args, **kwargs)
        return wrapper
    return decorator
