# Instructions for Assignment H: Unit tests and File IO

## Practical Learning Outcomes
By the end of this practical you will be able to:
* Understand how unit tests can be used in the software development process.
* Use `pytest` to run existing Python unit tests.
* Write Python code to read and write to files.   


## Assignment task.

* This week's assignment is to tackle the [Rosalind Problem:
  Computing GC Content](http://rosalind.info/problems/gc/)
  where you are given a number of DNA sequences in a FASTA file format
  and we need to find the sequence with the highest %GC content.
  So firt read through the problem,
  including the section *Identifying Unknown DNA Quickly* (that you must
  click to expand).
* But do not start coding yet! We are going to see how to tackle the problem
  in a systematic approach using software testing. To do this work through
  the instructions below.

## Software Testing
In this practical we are going to see how testing can be used to
aid software development. First watch this video:
* ["Software Testing"](a myplayer link)  **TODO: record osmart Dec 2018**
* ["Software Testing" Powerpoint slides](
   https://1drv.ms/p/s!AjeHBmwgk7Hto1USV9VWha1ny9jG)

## 0. Using `pytest` for testing
In this practical you are going to start using 'Unit tests'
where individual 'units' of code are tested.
At this stage we will be testing individual functions
and the tests are a set of function input parameters
and expected return values.

Unit testing forms an important part of modern software development,
for more information see the Wikipedia page: 
https://en.wikipedia.org/wiki/Unit_testing

The Python standard library has a reasonable unit testing module called `unittest`
but using its syntax is difficult to use (there is a lot of 'boiler-plate'). So
we will be using `pytest` as it is easier to understand and use in practice. The
first thing to do is to check that you have pytest installed:

* From the OSX (or Linux) command prompt issue the command `pytest --version`.
  This should produce output showing the `pytest` command works and giving you
  version information:
  ```
  $ pytest --version
  This is pytest version 3.2.1, imported from /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest.py
  setuptools registered plugins:
    pytest-cov-2.6.0 at /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest_cov/plugin.py
  ```
  If instead of this you get a response like `-bash: pytest: command not found` then 
  pytest has not been installed. 
  To install pytest See https://docs.pytest.org/en/latest/getting-started.html#install-pytest 
  and if you continue to have problems ask for help, see
  [Help with programming (Module Canvas page)](
  https://canvas.anglia.ac.uk/courses/1490/pages/help-with-programming).

* To become familiar with pytest work through the video follow-me exercises:\
  ["Using pytest to unit test code"](../0_starting_pytest/README.md)

## 1. Reading and Writing to Files

To be able to tackle this week's task you are going to read
sequences from a file.
Reading and writing files in Python is straightforward,
as you will see in the
video follow-me exercise 
["Reading and writing files in Python"](../1_file_io/README.md)

## 2. Tackling the Rosalind Computing GC Content Problem 

We are going to tackle this week's assignment by splitting it up into 
relevant functions with unit tests.

* Video showing the approach.
* Then change directory to [2_fasta_gc_content](../2_fasta_gc_content) where you
  will find starting code and tests. 
* Write functions in [fasta_gc_content.py](
  ../2_fasta_gc_content/fasta_gc_content.py) to pass unit tests:
  * [test_percent_gc.py](../1_fasta_highest_gc/test_percent_gc.py) 
    for `percent_gc(sequence)` function that calculated %GC content for a sequence
  * [test_lines_from_file.py](../1_fasta_highest_gc/test_lines_from_file.py)
    for `lines_from_file(filename)` that returns a list of lines read from filename.



