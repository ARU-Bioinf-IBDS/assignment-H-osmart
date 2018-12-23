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
* Then edit `test_add_one.py`:
  ```
  edit test_add_one.py
  ```
  * explain that `pytest` tests python files have to names starting with 
    `test_` or ending in `_test` 
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
  does nothing! Although it is valid Python the functions do nothing.
