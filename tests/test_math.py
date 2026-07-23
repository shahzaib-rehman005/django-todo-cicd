def add(a, b):
    # BUG: should add the two numbers, but subtracts
    return a - b


def test_add():
    assert add(2, 3) == 5
