from src.args_kwargs import concat, update_profile, sum_multiples_of

def test_concat():
    assert concat('one','two', sep='-') == 'one-two'
    assert concat(1,2,3, sep=':') == '1:2:3'

def test_update_profile():
    user = {'name':'Ravi', 'age':20}
    updated = update_profile(user, age=21, city='Pune')
    assert updated['age'] == 21
    assert updated['city'] == 'Pune'
    assert user['age'] == 20  # original unchanged

def test_sum_multiples_of():
    assert sum_multiples_of(10, 3,5) == 33
    assert sum_multiples_of(0, 3) == 0
    assert sum_multiples_of(10) == 0
