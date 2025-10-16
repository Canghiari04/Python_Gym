"""
Write a function frequencies(s) that takes a string as parameter and 
returns a dictionary in which:
    - the keys are the alphanumeric characters (digits + ascii_letters of
      the string module) present in the string (if the last character appears 
      only at the end of the string, it doesn't matter to put it in the dictionary).
    - the values are dictionaries as well that have:
        - as keys any type of characters that follow immediately the character considered
        - as values the frequency with which that character follows the considered character
"""

def frequencies(s: str):
    _dict = {}
    for char in s[0:len(s) - 1]:
        if char.isalnum() and char not in _dict:
            _dict[char] = {}

    return _dict

print(frequencies("Ramarro marrone"))