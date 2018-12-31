""" 
unit tests for function gc_percent(sequence)
that finds the %GC content for a given DNA sequence
"""
import pytest
from fasta_gc_content import gc_percent


def test_gc_percent_G():
    assert gc_percent('G') == pytest.approx(100.)


def test_gc_percent_A():
    assert gc_percent('A') == pytest.approx(0.)


def test_gc_percent_AGAGAGAG():
    assert gc_percent('AGAGAGAG') == pytest.approx(50.)


def test_gc_percent_AGCTATAG():
    # from http://rosalind.info/problems/gc/
    # For example, the GC-content of "AGCTATAG" is 37.5%.
    assert gc_percent('AGCTATAG') == pytest.approx(37.5)


def test_gc_percent_has_docstring():
    # just check there is one as cannot check that it is human readable
    assert len(gc_percent.__doc__) > 0
