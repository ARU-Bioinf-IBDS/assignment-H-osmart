# Mini-exercise 1e. Read a TSV file, modify things and write out as CSV file
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
* see the advantage of using standardized formats and established Python modules.
