"""Demonstrates positional, *args and **kwargs usage."""
from typing import Any

def concat(*parts, sep=" ") -> str:
    """Join given parts (converted to str) with sep."""
    return sep.join(str(p) for p in parts)

def update_profile(user: dict, **kwargs) -> dict:
    """Return a new dict merging user's shallow copy with kwargs (non-mutating)."""
    new = user.copy()
    new.update(kwargs)
    return new

def sum_multiples_of(n: int, *multiples) -> int:
    """Sum numbers in 1..n that are multiples of any of the provided multiples.

    If no multiples are provided, returns 0.
    """
    if n < 1:
        return 0
    if not multiples:
        return 0
    mults = set()
    for m in multiples:
        if m == 0:
            continue
        for k in range(m, n+1, m):
            mults.add(k)
    return sum(mults)
