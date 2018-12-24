# Using pytest to unit test code

This directory has files for a follow-me exercise introducing `pytest` unit 
tests.

You should view the video: ["Using pytest to unit test code"](a myplayer link) 
**TODO: record osmart Dec 2018** but you may also find the notes below useful.

## Run thru Video "Using pytest to unit test code"  Notes

* Start by checking that you have `pytest` installed.
  ```
  $ pytest --version
  This is pytest version 3.2.1, imported from /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest.py
  setuptools registered plugins:
    pytest-cov-2.6.0 at /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest_cov/plugin.py
  ```
* Start by changing directory:
  ```
  cd 0_starting_pytest
  ```
## Cheat sheet
* In this directory you can find a "cheat sheet" (or reference card) that
  quickly summarises the basis use of `pytest`:


## An initial example `pytest` test.
* Then edit `test_add_one.py`:
  ```
  edit test_add_one.py
  ```
  * explain that `pytest` tests python files have to names starting with 
    `test_` or ending in `_test` 
  * talk through the NOTE - normal to import
  * the actual tests are functions with names starting with 
    `test_`.
  * these functions normally have an `assert` statement that if `True` means
    the test passes but if `False` means the test fails.
    
    Although normal Python has an `assert` statement if should be avoided in 
    practice just use it in `pytest`.
* Switch back to the command line and show that:

  ```
  python test_add_one.py
  ```
  
  does nothing! Although it is valid Python the functions do nothing.
* Instead to run the tests use the `pytest` command:
  ```
  pytest test_add_one.py
  ```
  look at the fail messages: there are two fail messages.
* So pytest runs multiple tests. If you want to run a single test 
  this is most easily done with the `-k EXPRESSION` argument where 
  only tests with a substring match to `EXPRESSION` are run. In this
  case to run just the test with an input `0` use:
  ```
  pytest -k zero test_add_one.py
  ```
  
* Looking at the test results easy to see current `add_one` has a simple bug
* Correct bug by changing minus to a +. Save and rerun test. 
  Result is green success with **"2 passed"**
* Commit the bug fix with a decent commit message - saying tests now pass.

## show more about pytest comparisons

* edit the file:
```
edit test_show_pytest_comparisons.py
```
  * TODO 
