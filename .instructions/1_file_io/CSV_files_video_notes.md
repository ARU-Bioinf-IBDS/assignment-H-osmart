# My Notes for making Run thru Video 
# "Reading and writing CSV/TSV files."

* This follows on from reading writing plain vanilla text files.
* Show them page 2 of the reference card on CSV and TSV files.
* Change to the appropriate directory
  ```
  cd IBDS
  cd assignment-H-osmart
  cd 1_file_io
  ```
* You are provided an example CSV file `example_in.csv` this can be edited:
  ```
  edit example_in.csv
  ```
  or opened in a spreadsheet:
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

### task 4 read a TSV and write CSV

* task 4 instructions:
  ```
  $ cat task_4_read_tsv_write_csv.py
  # instructions: write Python to read in the data from tsv file 
  # 'lmb_nobel_prizes.tsv' then
  # (a) in the Nobel Prize Winners items, replace the '&' characters with 'and'
  # (b) print out each row 
  # (c) save just the dates and names in a CSV file 'lmb_out.csv'
  #
  # Question: in 2002 there are 3 prize winners and so there is a comma in the 
  # names field how is this handled in the output CSV file?
  ```
* first lets look at the input file (Nobel Prize winners from the LMB laboratory in Cambridge).
  ```
  edit lmb_nobel_prizes.tsv
  ```
  in TextWrangler "View" "Text Display" "Show Invisibles" to show up tabs as triangles 
* TSV file handled fine in Numbers spreadsheet:
  ```
  open lmb_nobel_prizes.tsv
  ```
* Now do task 
  ```
  edit task_4_read_tsv_write_csv.py
  ````
  Working python:
  ```python
  import csv
  with open('lmb_nobel_prizes.tsv') as tsv:
      reader = csv.reader(tsv, delimiter='\t')
      data = list(reader)

  for row in data:
      row[1] = row[1].replace('&', 'and')
      print(row)

  with open('lmb_out.csv', 'w') as f_out:
      writer = csv.writer(f_out)
      for row in data:
          writer.writerow(row[:2]) 
   ```
* Answer to question the 2002 names are surrounded with " characters meaning that the comma
  is regarded as part of the field. Show by:
  ```
  cat lmb_out.csv
  open lmb_out.csv
  ```
* see the advantage of using standardized format and established Python modules.
