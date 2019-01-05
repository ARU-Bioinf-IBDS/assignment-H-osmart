def count_vowels(str):
    """ returns the number of vowels (aeiou) in a string str. """
    vowels = 'aeiou'
    vowels += vowels.upper()
    answer = 0
    for v in vowels:
        answer += str.count(v)
    return answer