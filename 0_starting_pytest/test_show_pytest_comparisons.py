"""
showing off how pytest makes comparisons between
expected and actual easy.
"""
import pytest
from math import sqrt


def test_show_how_pytest_compares_lists():
    abcde = 'abcde'
    assert list('abcde') == ['a', 'b', 'c', 'd', 'e']
    

def test_show_how_to_compare_floats():
    # rounding errors can cause problems 
    # use pytest.approx fix
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_more_on_pytest_approx():
    # square root of 2.0 is 1.414213
    assert sqrt(2.) == pytest.approx(1.414213)


# to test that a particular kind of exception is raised.
def test_sqrt_negative_number_raises_exception():
    # N.B. sqrt negative number raises ValueError rather than IOError
    with pytest.raises(ValueError):
        sqrt(-2.0)
