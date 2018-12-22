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
* *link to mp4 recording* **TODO: Dec 2018**
* [Powerpoint slides](https://1drv.ms/p/s!AjeHBmwgk7Hto1USV9VWha1ny9jG)

## Unit testing with `pytest`
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

* From the OSX (or Linux) command prompt issue the command `pytest --version`.i
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



