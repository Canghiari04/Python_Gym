"""
The mode of a list is the most frequent item on the list. For example,
the mode of [2,7,5,7,7,2,4] is 7, which appears 3 times. The most frequent
values (tie) can be more than one. For example, the mode of [1,2,99,1,0,2]
is 1, 2 which appears 2 times each. 

Write a function mode(L) which returns the mode of L as a list.

Suppose (without checking) that the elements of L are immutable (and
therefore can be dictionary keys).
"""

def biggest(_dict: dict):
    counter = 0
    for value in _dict.values():
        if value > counter:
            counter = value

    return counter

def mode(L):
    _dict = {}

    for l in L:
        if l in _dict:
            _dict[l] += 1
        else:
            _dict[l] = 1

    counter =  biggest(_dict)

    _list_keys = []
    for key, value in _dict.items():
        if value == counter:
            _list_keys.append(key)

    return _list_keys

print(sorted(mode([2,7,5,7,'libro',7,2,4])))