# Mini-exercise 1b. Write function to read a file and return list of lines
##  Notes for making Run thru Video 

* Show them the reference card 
* They should be in the `1_file_io`  directory
  ```
  pwd
  ```
* edit the Python file that has instructions in it
  ```
  edit mini_1b_function_to_read_a_file_into_lines.py
  ```
* task is to write a function to read a file and return a list of the lines in it (without any
  newline characters).

* To test the function use pytest test provided. 
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
        """reads input file filename and returns a list of lines from it."""
        with open(filename) as file_in:
            contents = file_in.read()
        return contents.splitlines()
    ```
  * git add , then commit working code including in message that it passes the test. 
