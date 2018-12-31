""" unit tests for function percent_gc """
import pytest
from fasta_gc_content import percent_gc


def test_percent_gc_G():
    assert percent_gc('G') == pytest.approx(100.)


def test_percent_gc_A():
    assert percent_gc('A') == pytest.approx(0.)


def test_percent_gc_AGAGAGAG():
    assert percent_gc('AGAGAGAG') == pytest.approx(50.)


def test_percent_gc_AGCTATAG():
    # from http://rosalind.info/problems/gc/
    # For example, the GC-content of "AGCTATAG" is 37.5%.
    assert percent_gc('AGCTATAG') == pytest.approx(37.5)


def test_percent_gc_has_docstring():
    # just check there is one as cannot check that it is human readable
    assert len(percent_gc.__doc__) > 0