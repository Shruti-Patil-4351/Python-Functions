"""Lambdas, closures and higher-order functions."""
from typing import Callable, List, Iterable

def make_multiplier(m: int) -> Callable[[int], int]:
    """Return a function that multiplies its input by m (closure)."""
    def multiplier(x: int) -> int:
        return m * x
    return multiplier

def apply_on_list(fn, items: List) -> List:
    """Apply fn to each item and return a new list."""
    return [fn(x) for x in items]

def filter_custom(items: Iterable, predicate) -> List:
    """Return a list of items where predicate(item) is True. Implemented via comprehension.""
    return [item for item in items if predicate(item)]
