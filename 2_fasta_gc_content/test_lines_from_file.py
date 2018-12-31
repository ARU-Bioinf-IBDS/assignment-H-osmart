"""
pytest test for function lines_from_file using files in this directory.

Note this is not really a UNIT test as it reads actual files, it
is more of an integration test.
A unit test tests the functioning of the module in isolation from
other modules, particularly if they involve inteaction with external
resources such as disk files, database access or web access. This
is normally done by mocking.

see
http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
"""
import os
from fasta_gc_content import lines_from_file


def test_read_lines_from_simple_fasta_dot_txt():
    simple_fasta_dot_txt = filename_in_this_directory('simple_fasta.txt')
    assert lines_from_file(simple_fasta_dot_txt) == \
        ['>minimal_fasta_with_single_short_sequence', 'ATGC']


def test_read_lines_from_rosalind_sample_dot_txt():
    rosalind_sample_dot_txt = filename_in_this_directory('rosalind_sample.txt')
    # file has nine lines simply test for this
    assert len(lines_from_file(rosalind_sample_dot_txt)) == 9


def test_function_has_docstring():
    # just check there is one as cannot check that it is human readable
    assert len(filename_in_this_directory.__doc__) > 0


def filename_in_this_directory(filename):
    """
    returns the absolute path for file filename
    in the same directory as this file.

    Needed because tests need to run independently from
    any directory

    Raises:
        RuntimeError if the filename does not exist
    """
    this_directory = os.path.dirname(os.path.abspath(__file__))
    test_filename = os.path.join(this_directory, filename)
    if not os.path.isfile(test_filename):
        raise RuntimeError('test setup failed to find file:' + test_filename)
    return test_filename
