"""
pytest test for function lines_from_file using file 'example_in.txt'
in this directory.

Note this is not really a UNIT test as it opens an actual file, it
is more of an integration test.
A unit test tests the functioning of the module in isolation from
other modules, particularly if they involve inteaction with external
resources such as disk files, database access or web access. This
is normally done by mocking. 

see 
http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
"""
import os
from task_2_function_to_read_a_file_into_lines import lines_from_file

def example_in_dot_txt_filename():
    """
    returns the absolute path for file 'example_in.txt'
    in the same directory as this file.
    Needed because tests need to run independently from
    any directory
    """
    this_directory = os.path.dirname(os.path.abspath(__file__))
    test_filename = os.path.join(this_directory, 'example_in.txt')
    if not os.path.isfile(test_filename):
        raise RuntimeError('test setup failed to find file:' + test_filename)
    return test_filename

def test_read_lines_from_example_in_dot_txt():
    example_in_dot_txt = example_in_dot_txt_filename()
    assert lines_from_file(example_in_dot_txt) == \
        ['this is first line from example_in.txt', 
         'second line!', '3rd and final line.']

