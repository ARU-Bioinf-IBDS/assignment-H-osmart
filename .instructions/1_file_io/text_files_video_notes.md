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
