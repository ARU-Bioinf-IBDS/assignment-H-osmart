# 2. Tackling the Rosalind Computing GC Content Problem 

We are going to tackle this week's assignment by splitting it up into 
relevant functions with unit tests.

* Video showing the approach.
* Then open a terminal and in your copy of the assignment repo
  change directory to [2_fasta_gc_content](./) where you
  will find starting code and tests, leading you through.
* Write functions in [fasta_gc_content.py](
  ./fasta_gc_content.py) to pass the unit tests provided.
  Where possible use a call to a previously written function. git commit changes 
  as you go including information about what test is passed.

  Suggested order to write functions:
  * [test_lines_from_file.py](./test_lines_from_file.py)
    for `lines_from_file(filename)` that returns a list of lines read from 
    filename.
  * [test_parse_fasta_lines.py](./test_parse_fasta_lines.py)
    for `parse_fasta_from_lines(lines)` that supplied with a list of lines 
    from a FASTA format file returns a tuple (list of the IDs, list of 
    the sequences).
  * [test_parse_fasta_file.py](./test_parse_fasta_file.py)
    for `parse_fasta_file(filename)` that supplied with a filename of a 
    FASTA file returns a tuple (list of the IDs, list of the sequences).
  * [test_gc_percent.py](./test_gc_percent.py) 
    for `gc_percent(sequence)` function that calculates %GC content 
    for a sequence.
  * [test_gc_percentages.py](./test_gc_percentages.py) 
    for `gc_percentages(seqs)` function that returns a list of GC percentages
    for each of the seqs.
  * [test_highest_gc_in_fasta_file.py](./test_highest_gc_in_fasta_file.py)
    for `highest_gc_in_fasta_file(filename)` function that 
    reads DNA sequences from the input FASTA format file_name
    returns the (id, sequence) with the highest %GC content
 
  Once you have implemented the `highest_gc_in_fasta_file(filename)` function so that
  [test_highest_gc_in_fasta_file.py](./test_highest_gc_in_fasta_file.py) 
  passes then the functionality needed for 
  [Rosalind Problem: Computing GC Content](http://rosalind.info/problems/gc/)
  has been completed. But to be able to easily apply it to a given new test set,
  for instance [rosalind_final_test.txt](./rosalind_final_test.txt)
  it is easiest to write a command line script to apply 
  `highest_gc_in_fasta_file(filename)` to any FASTA file.
