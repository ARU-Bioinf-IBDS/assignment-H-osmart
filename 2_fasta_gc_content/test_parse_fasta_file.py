"""
pytest test for function parse_fasta_file(filename)
that supplied with a filename of a FASTA file returns a 
tuple (list of the IDs, list of the sequences).

uses two files in this directory.
"""
from fasta_gc_content import parse_fasta_file
from test_lines_from_file import filename_in_this_directory


def test_read_from_simple_fasta_dot_txt():
    simple_fasta_dot_txt = filename_in_this_directory('simple_fasta.txt')
    ids, seqs = parse_fasta_file(simple_fasta_dot_txt)
    assert ids == ['minimal_fasta_with_single_short_sequence']
    assert seqs == ['ATGC']

def test_read_from_rosalind_sample_dot_txt():
    rosalind_sample_dot_txt = filename_in_this_directory('rosalind_sample.txt')
    ids, seqs = parse_fasta_file(rosalind_sample_dot_txt)
    assert ids == ['Rosalind_6404', 'Rosalind_5959', 'Rosalind_0808']
    assert len(seqs) == 3 

def test_function_has_docstring():
    # just check there is one as cannot check that it is human readable
    assert len(parse_fasta_file.__doc__) > 0
