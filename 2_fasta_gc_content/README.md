# 2. Tackling the Rosalind Computing GC Content Problem 

We are going to tackle this week's assignment by splitting it up into 
relevant functions with unit tests.

* First watch the Video:\
  *"Tackling Rosalind Computing %GC using functions"*\
  **TODO: osmart Jan 2019: record**\
  **TODO: osmart Jan 2019 Embed Myplayer video player here**\
  [My notes to make the "Tackling Rosalind %GC" video](
  ../.instructions/2_fasta_gc_content/tackling_rosalind_gc_video_notes.md)
 
* Then open a terminal and in your copy of your assignment repo
  change directory to [2_fasta_gc_content](./) where you
  will find starting code and tests, leading you through.

## Writing functions to tackle the problem
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

## Writing a script 
* Now you have implemented the `highest_gc_in_fasta_file(filename)` function so that
  [test_highest_gc_in_fasta_file.py](./test_highest_gc_in_fasta_file.py) 
  passes then the functionality needed for 
  [Rosalind Problem: Computing GC Content](http://rosalind.info/problems/gc/)
  has been completed. 
* But to be able to easily apply it to a given new test set,
  for instance [rosalind_final_test.txt](./rosalind_final_test.txt)
  it is easiest to write a command line script to apply 
  `highest_gc_in_fasta_file(filename)` to any FASTA file.
* You will find an example script in the file [example_python_script](./example_python_script)
  * the script can be run from ae OSX or Linux command line terminal by first changing
    the directory to your assignment repo subdirectory [2_fasta_gc_content](./) 
    that contains the script. 

  * Then `ls` the script
    <pre>
    $ <b>ls -lh example_python_script</b>
    -rwxr-xr-x  1 osmart  staff   704B  2 Jan 14:43 example_python_script
    </pre>
    This confirms you are the correct directory. In addition the listing shows that the
    script has `x` executable permission.

  * You can run the script from the terminal command line.
    * First run without command line arguments:
      <pre>
      $ <b>./example_python_script</b>
      main function
      argv:  ['./example_python_script']
      name of script argv[0]:  ./example_python_script
      no command line arguments given
      </pre>
    * Then specify some arguments after the script name:
      <pre>
      $ <b>./example_python_script input.txt output.csv</b>
      main function
      argv:  ['./example_python_script', 'input.txt', 'output.csv']
      name of script argv[0]:  ./example_python_script
      2 command line arguments given
      list of command line arguments:  ['input.txt', 'output.csv']
      first command line argument:  input.txt
      </pre>
    * You can see how the script access the command line arguments and prints 
      them out.  Look at the source code [example_python_script](./example_python_script)
      to see how this is done.
* Note that although it is possible to run Python files on the command line using 
  `python filename.py`
  using scripts is good practice as it makes its clear which file is to be run
  and encourages development of good Command Line Interfaces (CLI) with sensible
  options and help messages.
* Using [example_python_script](./example_python_script) as a template now write a script
  `fasta_highest_gc` to that reads a fasta file containing DNA sequences and reports which
  entry has the highest percentage GC content.  This script should call the  
  `highest_gc_in_fasta_file(filename)` function written above.
  * Here are example runs showing how the script should perform:
    <pre> 
    $ <b>./fasta_highest_gc</b>
    ERROR you must supply the input fasta filename as a command line argument
    $ <b>./fasta_highest_gc simple_fasta.txt</b>
    minimal_fasta_with_single_short_sequence
    50.000000
    $ <b>./fasta_highest_gc rosalind_sample.txt</b>
    Rosalind_0808
    60.919540
    </pre>
  * When you commit your  `fasta_highest_gc` script make sure you include sample
    test output in the commit message showing that it works.

## Final Test of the `fasta_highest_gc` script.

* Run you script on the test set [rosalind_final_test.txt](./rosalind_final_test.txt)
  and report the results on:
  * [Reflection on Practical H: Unit tests and File IO](
    https://canvas.anglia.ac.uk/courses/1490/TODO-LINK)\
    **TODO: osmart Jan 2019: add link to Canvas page**\
    So that you can compare results with your classmate.
  * The **Notes about this assignment** in the top [README.md](
    ../README.md#notes-about-this-assignment)


<hr>

*Back to:* [Instructions for Assignment H: Unit tests and File IO](../.instructions/README.md)
