from src.higher_order import make_multiplier, apply_on_list, filter_custom

def test_multiplier():
    times3 = make_multiplier(3)
    assert times3(4) == 12

def test_apply_and_filter():
    assert apply_on_list(lambda x: x+1, [1,2,3]) == [2,3,4]
    assert filter_custom([1,2,3,4], lambda x: x%2==0) == [2,4]
