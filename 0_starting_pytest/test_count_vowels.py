"""
Instructions:
    write pytest tests for a function count_vowels that returns the 
    number of vowels (a, e, i, o, u) in a string.  It should work 
    for lower and UPPER case strings. All strings will be in
    English.
"""
from count_vowels import count_vowels

def test_count_vowels_e():
    assert count_vowels('e') == 1
    

def test_count_vowels_lowercase_vowels():
    assert count_vowels('aeiou') == 5
    

def test_count_vowels_uppercase_IOU():
    assert count_vowels('IOU') == 3
    
def test_count_vowels_non_vowels():
    assert count_vowels('sthvxyz., & ') == 0
  
def test_count_vowels_Anglia_Ruskin():
    assert count_vowels('Anglia Ruskin University') == 9
  
def test_count_vowels_empty():
    assert count_vowels('') == 0

