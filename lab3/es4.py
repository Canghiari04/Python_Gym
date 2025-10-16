"""
Write a function flatten(LL) that takes a list of lists of integers,
and creates a new list wich is simply a list of integers. Use only one
instruction (return of a list comprehension) inside the function.
"""

def flatten(LL):
    return [value for _list in LL for value in _list]

print(flatten([[1,2,3], [4,5,6], [7,8,9]]))