# pytest basic usage reference card

## testing you have pytest installed and working
* at the command line issue type command:
  ```
  pytest --version
  ```
  this should produce a response starting **This is pytest version...**.

## writing pytest tests
* The Python file for a test must be called `test_`*something*`.py` 
  or  *something*`_test.py`
* Use `import` to access the function to be tested:
  ```python
  from somewhere import something
  ```
  this will import the function `something` from the Python file `somewhere.py`
* pytest tests are functions whose name starts with `test_` this should be 
  followed by a human readable description of what is tested. Within the 
  function use `assert` to perform the test:
  ```python
  def test_description_of_what_is_tested():
      assert something(some_param=some_value) == known_return_value
  ```
  where `known_return_value` could be a single value or a list or something
  else depending on the test.