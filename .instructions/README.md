# Instructions for Assignment H: Unit tests and File IO

## Practical Learning Outcomes
By the end of this practical you will be able to:
* Understand how unit tests can be used in the software development process.
* Use `pytest` to run existing Python unit tests.
* Write Python code to read and write to files.   
* Understand how functions can be used to split up a complex problem into a
  series of simplier testable functions.
* Write simple Python command line scripts.


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

## 0. Introducing Software Testing 
To become familiar with Software Testing using `pytest` see:
["Introducting Software Testing"](../0_starting_pytest/README.md)

## 1. Reading and Writing to Files

To be able to tackle this week's task you are going to read
sequences from a file.
Reading and writing files in Python is straightforward,
as you will see in the
video follow-me exercise 
["Reading and writing files in Python"](../1_file_io/README.md)

## 2. Tackling the Rosalind Computing GC Content Problem 

We are going to tackle this week's assignment by splitting it up into 
relevant functions with unit tests, see 
[Tackling the Rosalind Computing GC Content Problem](../2_fasta_gc_content/README.md)
