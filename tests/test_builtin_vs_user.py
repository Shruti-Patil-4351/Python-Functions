from src.builtin_vs_user import safe_len, call_if_callable

def test_safe_len_and_call():
    assert safe_len([1,2,3]) == 3
    assert call_if_callable(5) == 5
    assert call_if_callable(lambda x: x+1, 5) == 6
    import pytest
    with pytest.raises(TypeError):
        safe_len(3.14)
