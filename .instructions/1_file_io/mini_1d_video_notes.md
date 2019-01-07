# Mini-exercise 1d. Read a CSV file
##  Notes for making Run thru Video 

* They should be in the `1_file_io`  directory
  ```
  pwd
  ```
* Show them page 2 of the reference card on CSV and TSV files.
  This follows on from reading writing plain vanilla text files.
  CSV and TSV format files are a useful way to store and exchange structured
  data (there are many others for instance XML and JSON files).
* edit the Python file with instructions:
  ```
  edit mini_1d_read_a_csv_file.py
  ```
* You are provided an example CSV file `example_in.csv` this can be edited:
  ```
  edit example_in.csv
  ```
  or opened in a spreadsheet (in OSX):
  ```
  open example_in.csv
  ```
* It is easy to read in python - show them in the python prompt:
  ```python
  import csv
  with open('example_in.csv') as file_in:
      for row in csv.reader(file_in):
          print(row) 
  ```
  then go own and show them the alternative using list to store data.

