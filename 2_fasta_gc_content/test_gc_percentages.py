""" 
unit tests for function gc_percentages(seqs) 
that for the input list of DNA sequences seqs
returns a list of GC percentages.
"""
import pytest
from fasta_gc_content import gc_percentages


def test_gc_percentages_single_sequence():
    assert gc_percentages(['ATGC']) == pytest.approx([50.])


def test_gc_percentages_three_sequences():
    assert gc_percentages(['AAA', 'AGA', 'GC']) == \
           pytest.approx([0., 33.3333333, 100.])


def test_function_has_docstring():
    # just check there is one as cannot check that it is human readable
    assert len(gc_percentages.__doc__) > 0
