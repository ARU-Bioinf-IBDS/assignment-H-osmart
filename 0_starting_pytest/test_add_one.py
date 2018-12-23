"""
first example of a pytest test
"""


# the function we want to test 
# NOTE this is not normally in the test_ file instead
#      the test_ will import it from another file 
def add_one(x):
    """ add one to a number"""
    return x - 1


def test_add_one_with_0():
    assert add_one(0) == 1


def test_add_one_with_3():
    assert add_one(3) == 4
