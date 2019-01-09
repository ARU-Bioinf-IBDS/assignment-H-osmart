# Instructions: 
#
# finish writing the function 'lines_from_file' below
# so that it passes the pytest tests in test_lines_from_file.py
#
# Hint: look at the fileio_in_python.pdf reference card! 
def lines_from_file(filename):
   """ 
   reads input file filename and returns a list of lines from it.
   """
   with open(filename) as file_in:
       contents = file_in.read()
   return contents.splitlines()
