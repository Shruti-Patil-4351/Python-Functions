"""Recursive functions: fibonacci and list flattening."""
from functools import lru_cache
from typing import List, Any

# Plain recursive fibonacci (inefficient) - shown for educational purposes.
def fibonacci_plain(n: int) -> int:
    """Plain recursive fibonacci. Exponential time: do not use for large n.""\            if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci_plain(n-1) + fibonacci_plain(n-2)

# Efficient fibonacci with memoization
@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Fibonacci using recursion with memoization (fast enough for tests up to n=30)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def flatten(nested_list: List[Any]) -> List[Any]:
    """Recursively flatten nested lists of arbitrary depth.

    Approach: iterate items; if an item is a list or tuple, recurse and extend result;
    otherwise append the item.
    """
    result = []
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(list(item)))
        else:
            result.append(item)
    return result
