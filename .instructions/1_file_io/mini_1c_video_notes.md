# Mini-exercise 1c. Write a FASTA sequence file
##  Notes for making Run thru Video 

* They should be in the `1_file_io`  directory
  ```
  pwd
  ```
* Show them the reference card 
** Open the task 3 file:
  ```
  edit 1_file_io/mini_1c_write_a_file.py
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
  label='Test_fasta_99999'
  sequence='CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACT'
  with open('test_out.fasta', mode='w') as file_out:
      file_out.write('>' + label + '\n')
      file_out.write(sequence + '\n')

  ```
  first write without the the new lines
* git add / then commit / then push working code 
