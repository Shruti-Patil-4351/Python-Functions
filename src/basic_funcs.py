"""Basic functions: greeting, primality, factorial."""
from math import isqrt

def greet(name: str) -> str:
    """Return a greeting for name.

    Example:
        greet('Asha') -> 'Hello, Asha!'
    """
    return f"Hello, {name}!"

def is_prime(n: int) -> bool:
    """Return True if n is prime (n >= 2). Uses trial division up to sqrt(n)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

def factorial(n: int) -> int:
    """Iterative factorial for n >= 0. Raises ValueError on negative input."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
