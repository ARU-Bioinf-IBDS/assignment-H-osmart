# My Notes for making Run thru Video "Practical Example of pytest" 

## A real practical example.

* Start with the file:
  ```
  edit test_count_vowels.py
  ```
* This has Instructions:

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

* then write function `count_vowels.py`:
```python 
def count_vowels(in_string):
    """ returns the number of vowels in in_string """
    answer = 0
    for v in 'aeiouAEIOU':
        answer += in_string.count(v)
    return answer 
    # could be simplified   
    # return sum([in_string.count(v) for v in 'aeiouAEIOU'])\
```
* Note we have written the tests and then function. This is an example
  of *Test Driven Development (TTD)*

* Suppose `count_vowels` is being used as a part of a security system
  for generating questions about peoples passwords for an telephone
  banking system. An email arrives:
  ```
  edit email_add_french_accented_vowels.txt
  ```
* So add the feature but first add a test (or two).
```python
# test_count_vowels.py
from count_vowels import count_vowels

#.... other tests 

def test_french_characters():
    assert count_vowels('éàèùÉÀÈÙ') == 8
```
* a function that passes:
```python
def count_vowels(in_string):
    """ returns the number of vowels in in_string """
    vowels = 'aeiouéàèù'
    vowels += vowels.upper()
    return sum([in_string.count(v) for v in vowels])
```


