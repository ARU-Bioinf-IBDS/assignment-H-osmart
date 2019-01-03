# Introducting Software Testing
In this practical we are going to see how testing can be used to
aid software development. First watch this video:

* *"Software Testing"*\
  **TODO: osmart Dec 2018: record**\
  **TODO: osmart Dec 2018: Embed Myplayer video player here**\
  ["Software Testing" Powerpoint slides](
   https://1drv.ms/p/s!AjeHBmwgk7Hto1USV9VWha1ny9jG)

## Using `pytest` for testing
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

## Exercises: Using pytest to unit test code 

These are follow-me exercises to introduce `pytest` unit tests.

* First print out (or view) a reference card on pytest:
  *  [pytest_basic_usage_reference_card.pdf](
     ../.instructions/0_starting_pytest/pytest_basic_usage_reference_card.pdf)
     (PDF for printing)
  *  [pytest_basic_usage_reference_card.md](
     ../.instructions/0_starting_pytest/pytest_basic_usage_reference_card.md)
     (markdown for viewing)

* Then view and follow along the follow-me exercise videos:
  * *"Introducing pytest"*\
    **TODO: osmart Dec 2018: record**\
    **TODO: osmart Dec 2018: Embed Myplayer video player here**\
    [My notes for making the video *"Introducing pytest"*](
    ../.instructions/0_starting_pytest/introducing_pytest_video_notes.md) 
  * *"Practical Example of pytest"*\
    **TODO: osmart Dec 2018: record**\
    **TODO: osmart Dec 2018: Embed Myplayer video player here**\
    [My notes for making the video *"Practical Example of pytest"*](
    ../.instructions/0_starting_pytest/practical_example_video_notes.md)

<hr>

*Back to:* [Instructions for Assignment H: Unit tests and File IO](../.instructions/README.md)
