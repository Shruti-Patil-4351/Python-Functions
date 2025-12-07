import time
from src.decorators import timeit, type_check
from src.recursion import fibonacci

def test_timeit_on_function():
    @timeit
    def add(x,y): return x+y
    (res, elapsed) = add(2,3)
    assert res == 5
    assert isinstance(elapsed, float)
    assert elapsed >= 0

def test_timeit_on_fib():
    fn = timeit(fibonacci)
    (res, elapsed) = fn(20)  # should be reasonably fast due to memoization
    assert res == 6765
    assert isinstance(elapsed, float)

def test_type_check_pass_and_fail():
    @type_check(x=int, y=str)
    def f(x, y='a'):
        return True
    assert f(1, y='b')
    import pytest
    with pytest.raises(TypeError):
        f(x='not int', y='b')
