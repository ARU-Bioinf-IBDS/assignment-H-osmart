# My Notes for making Run thru Video "Using pytest to unit test code" 

* Start by checking that you have `pytest` installed.
  ```
  $ pytest --version
  This is pytest version 3.2.1, imported from /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest.py
  setuptools registered plugins:
    pytest-cov-2.6.0 at /Users/osmart/anaconda3/lib/python3.6/site-packages/pytest_cov/plugin.py
  ```
* then changing directory:
  ```
  cd 0_starting_pytest
  ```
## Cheat sheet
* You should already have printed out a reference card that 
  quickly summarises the basis use of `pytest`


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

* Lets look at more about pytest comparisons in file:
  ```
  edit test_show_pytest_comparisons.py
  ```

* the first test shows how pytest assert can be used to compare lists. 
  Run it by
  ```
  pytest -k list test_show_pytest_comparisons.py
  ```
  * assert does a really good job at showing what is different in tests.
  * rerun test with `-v` option to show long comparison.
  * finally sort the first `compare_lists` test.
  
* the second test shows how to compare floats.
  ```
  pytest -k list test_show_pytest_comparisons.py
  ```
  * rounding errors need to avoided
  * use `pytest.approx`

* go own and look test `more_on_pytest_approx`
  ```
  pytest -k approx test_show_pytest_comparisons.py
  ```
  * `pytest.approx` takes a sensible approach to float comparison
    normally one place in a million.
    
* finally look at last test on exceptions:
  ```
  pytest -k exception test_show_pytest_comparisons.py
  ```
  * how to test for exceptions - different types of errors. Have not yet 
  covered in detail.

## A real practical example.

* in file:
  ```
  edit test_count_vowels.py
  ```
* Instructions:

    write pytest tests for a function count_vowels that returns the 
    number of vowels (a, e, i, o, u) in a string.  It should work 
    for lower and UPPER case strings. All strings will be in
    English.
* write the tests.

```python
# test_count_vowels.py
from count_vowels import count_vowels

def test_non_vowels():
    assert count_vowels('sthvxyz.,&') == 0

def test_single_vowel():
    assert count_vowels('a') == 1
    
def test_iou():
    assert count_vowels('iou') == 3
    
def test_upper_case_vowels():
    assert count_vowels('AEIOU') == 5
    
def test_ARU():
    assert count_vowels('Anglia Ruskin University') == 9
  ```
* then write function `count_vowels.py`
```python 
def count_vowels(in_string):
    """ returns the number of vowels in in_string """
    answer = 0
    for v in 'aeiouAEIOU':
        answer += in_string.count(v)
    return answer 
    # could be simplified   
    # return sum([in_string.count(v) for v in 'aeiouAEIOU'])```