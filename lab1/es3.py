"""
Write a compare(s1, s2) function that takes as parameters 
two non-empty strings s1 and s2 and returns the tuple of 
indexes i such thath s1[i] is equal to one of the characters 
s2[i -1], s2[i] or s2[i + 1].
"""

import string

def compare(s1: str, s2: str) -> tuple:
    if len(s1) != 0 and len(s2) != 0:
        s1 = s1.lower()

        i = 0
        j = len(s1)

        _t = []
        while i < j:
            if s1[i] == s2[i - 1] or s1[i] == s2[i] or s1[i] == s2[i + 1]:
                _t.append(i)
                
            i += 1

        return tuple(_t)

    return tuple()

print(compare("asca", "lasca"))