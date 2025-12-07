import pytest
from src.basic_funcs import greet, is_prime, factorial

def test_greet():
    assert greet("Asha") == "Hello, Asha!"

def test_is_prime():
    assert is_prime(2)
    assert is_prime(17)
    assert not is_prime(1)
    assert not is_prime(15)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
