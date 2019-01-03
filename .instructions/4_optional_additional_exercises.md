# 4. Optional Additional Exercises

N.B., these optional exercises are intended for those who found the basic
exercises easy. They are useful learning exercises but only undertake them
if you have time!

## 4.1 Grouping tests together.

The `pytest` tests provided to you have been given in separate files each testing
one function. In practice this quickly produces an unmanagable number of test
files. Instead it is much better to use a single test file but 
to group different sets of tests using classes as explained at 
https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class
Produce a single file `test_fasta_gc_content.py` that contains
all the provided tests separated into classes. How can you test a single
function once the change has been made. Once you have combined the
tests make sure that you get rid of the separate test from the repository.
Remember to stay DRY (Don't Repeat Yourself).


## 4.2 Proper command line parsing and options with argparse

Directly using `sys.argv` to access command line arguments quickly
becomes complicated. It is much better to use the `argparse` module.
Look at the [Argparse Tutorial](https://docs.python.org/3.7/howto/argparse.html)
and convert the scripts to use it.


## 4.3 Making sure your scripts' exit status is correct.

In Unix-like operating systems command lines (Linux and OSX) one 
can check whether the previous command worked or had an error by
examining shell variable `$?`. For instance using the ls command
list a file that exists produces an `$?` of zero indicating success:
<pre>
$ <b>ls /etc/passwd</b>
/etc/passwd
$ <b>echo $?</b>
0
</pre>
But listing a file that does not exist produces an error statement and `$?`
is set to something other than zero indicating a failure:
<pre>
$ <b>ls this_file_does_not_exist</b>
ls: this_file_does_not_exist: No such file or directory
$ <b>echo $?</b>
1
</pre>
It is important to make sure that scripts produce a sensible exit status
as it makes it much easier to use them in automated processes (that normally
need to stop if there is an error).

If you script/program ends with a Python exception then it will produce a non-zero
exit status for instance, using `python -c` to run single Python commands:
<pre>
$ <b>python -c 'len([1, 2])'</b>
$ echo $?
0
$ <b>python -c 'len(None)'</b>
Traceback (most recent call last):
  File "<string>", line 1, in <module>
TypeError: object of type 'NoneType' has no len()
$ echo $?
1
</pre>
You can see the first Python command worked, did not produce an error and
produced a zero exit status. In contrast the second command produced an error
and consequently a non-zero exit status.

Check whether your scripts produce a non-zero exit status if they are supplied
with a name of FASTA file that does not exist. To cleanly stop a script with
an non-zero error exit status then:
```python
import sys
sys.exit(1)  # terminate with error status
```

## 4.3 Handling FASTA file errors cleanly.

If you supply your script with an empty file as a FASTA file what happens. 
What happens if the file does not start '>an_id'? Make sure your FASTA
reading function(s) produce a sensible `ValueError` Exception 
if you are thorough then your script should catch this exception and
produce a nice human readable and non-zero exit status (see previous section).

## 4.4  pytests for script

Write pytests for the scripts. This could including using `mock` rather physical
fileIO..


## 4.5 Read FASTA file with biopython rather than DIY code


## 4.6 Use classes to produce cleaner code.
For those who have experience writing Python classes refactor code
to  use a class structure. I would suggest two classes `Sequence`
and `Sequences`


## 4.7 Make code into a pip instalable package


<hr>

*Back to:* [Instructions for Assignment H: Unit tests and File IO](../.instructions/README.md)
