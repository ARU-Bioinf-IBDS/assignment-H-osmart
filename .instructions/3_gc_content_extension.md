# 3. Computing GC Content Extension

The original Rosalind Problem got you to calculate the maximum %GC content
for a set of sequences read from a FASTA file. But in practice
it would be more useful to order the sequences by their %GC content.
This could be useful for instance to identify which sequence is from
prokaryote contamination.

So the task here is to write a new script `fasta_order_gc` that
* reads in a FASTA sequence file - getting the filename as a command line argument.
* prints out a list of the sequences ordered by %GC content:
  <pre>
  $ <b>./fasta_order_gc rosalind_sample.txt</b>
  %GC    sequence_id
  53.571 Rosalind_5959
  53.750 Rosalind_6404
  60.920 Rosalind_0808
  </pre>
  note that percentages are written to 3 decimal places.
* If a second command line argument is given then the script should open this as
  an output CSV file and write out the list of the sequences ordered by %GC content
  to this as well:
  <pre>
  $ <b>./fasta_order_gc rosalind_sample.txt rosalind_sample_out.csv</b>
  %GC    sequence_id
  53.571 Rosalind_5959
  53.750 Rosalind_6404
  60.920 Rosalind_0808
  $ <b>cat rosalind_sample_out.csv</b>
  %GC,sequence_id
  53.571,Rosalind_5959
  53.75,Rosalind_6404
  60.92,Rosalind_0808
  </pre>
* As you develop your script then record how you are testing it. Manual testing is fine but
  should be recorded. pytest tests are optional (but desirable!). Unit testing file output 
  is tricky.
* **Hint** if `sorted()` is called on a list of tuples then it sort based on the first
  field. So
  <pre>
  $ <b>python</b>
  Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct  6 2017, 12:04:38)
  [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> <b>list_of_tuples = [(3, 'a_3'), (1, 'b_1'), (7, 'c_7'), (0, 'd_0')]</b>
  >>> <b>sorted_lt = sorted(list_of_tuples)</b>
  >>> <b>sorted_lt</b>
  [(0, 'd_0'), (1, 'b_1'), (3, 'a_3'), (7, 'c_7')]
  </pre>


## Final Test of the `fasta_order_gc` script.

* Run you script on the test set [rosalind_final_test.txt](./rosalind_final_test.txt)
  and report the results on:
  * [Reflection on Practical H: Unit tests and File IO](
    https://canvas.anglia.ac.uk/courses/1490/TODO-LINK)\
    **TODO: osmart Jan 2019: add link to Canvas page**\
    So that you can compare results with your classmates.
  * The **Notes about this assignment** in the top [README.md](
    ../README.md#notes-about-this-assignment)



<hr>

*Back to:* [Instructions for Assignment H: Unit tests and File IO](../.instructions/README.md)
