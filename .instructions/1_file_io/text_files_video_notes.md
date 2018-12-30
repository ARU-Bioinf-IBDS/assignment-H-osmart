# My Notes for making Run thru Video 
# "Reading and writing text files."

* They should have printed the reference card
* Change to the appropriate directory
  ```
  cd IBDS
  cd assignment-H-osmart
  cd 1_file_io
  ```
* First task is to read a file and print out its contents:
  ```
  edit task_1_read_a_file.py
  ```
  using open and close:
  ```python
  # instructions: write python to read file example_in.txt
  # and print out its contents.
  # You will find what you need on the reference card
  in_file = open('example_in.txt')
  contents = in_file.read()
  in_file.close()
  print(contents,  end='')
  ```
  the `end=''` is necessary as contents has all the newlines in the file.

### task 2: function to read a file and return list of lines
* Then write a function to read a file and return a list of the lines in it (without any
  newline characters).
  ```
  edit task_2_function_to_read_a_file_into_lines.py
  ```
  To test the function use pytest test provided. 
  * Show it to them using:
    ```
    edit test_lines_from_file.py
    ```
  * run by:
    ```
    pytest test_lines_from_file.py
    ```
  * My code to pass the test.
    ```python
    def lines_from_file(filename):
    """ 
    reads input file filename and returns a list of lines from it.
    """
    with open(filename) as file_in:
        contents = file_in.read()
    return contents.splitlines()
    ```
  * git add , then commit working code including in message that it passes the test. 

### task 3 - write a FASTA sequence file
* Open the task 3 file:
  ```
  edit task_3_write_a_file.py
  ```
* Task is to write a FASTA format file with given label and sequence. FASTA files
  have a line starting with > followed by a label then the sequence on next line
  that can be continued if long
* Check result by :
  ```
  cat test_out.fasta
  ```
* My code to complete the task.
  ```python
  # instructions: write python to write 
  # the label and sequence to a file 'test_out.fasta'
  # in a FASTA format
  label='Test_fasta_99999'
  sequence='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACT'
  with open('test_out.fasta', mode='w') as file_out:
      file_out.write('>' + label + '\n')
      file_out.write(sequence + '\n')

  ```
* git add / then commit working code 
