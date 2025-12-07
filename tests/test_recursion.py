from src.recursion import fibonacci, flatten

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55

def test_flatten():
    assert flatten([1,[2,[3,4]],5]) == [1,2,3,4,5]
    assert flatten([]) == []
