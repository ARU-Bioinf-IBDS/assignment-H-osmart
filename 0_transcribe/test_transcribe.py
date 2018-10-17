"""pytest unit tests of counting_dna function"""
from transcribe import transcribe_dna_to_rna


def test_with_single_t():
    assert transcribe_dna_to_rna('T') == 'U'


def test_with_atgc():
    assert transcribe_dna_to_rna('ATGC') == 'AUGC'


def test_with_rosalind_example():
    # from http://rosalind.info/problems/rna/
    rosalind_dna = 'GATGGAACTTGACTACGTAAATT'
    rosalind_rna = 'GAUGGAACUUGACUACGUAAAUU'
    assert transcribe_dna_to_rna(rosalind_dna) == rosalind_rna


def test_with_empty():
    assert transcribe_dna_to_rna('') == ''
