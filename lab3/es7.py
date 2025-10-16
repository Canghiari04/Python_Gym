"""
Write a function multiplicationmatrix(m) (with only one instruction: the
return of a list comprehension) that returns a list of lists of integers,
which is the multiplication matrix from 0 to m (included).

Each element of the returned list will be a list of the kind 
[i*0, i*1, ..., i*10], and i varies between 0 and m.
"""

def multiplicationmatrix(m):
    return [[i * j for i in range(10 + 1)] for j in range(m + 1)]

print(multiplicationmatrix(1))