def add(a, b):
    # BUG: should add the two numbers, but subtracts them
    return a - b


def test_add():
    # 2 + 3 must equal 5
    assert add(2, 3) == 5
