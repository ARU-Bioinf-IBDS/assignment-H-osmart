"""
first example of a pytest test
"""


# the function we want to test (normally this is got by an import)
def add_one(x):
    """ add one to a number"""
    return x-1


def test_add_one_with_0():
    assert add_one(0) == 1


def test_add_one_with_3():
    assert add_one(3) == 4
