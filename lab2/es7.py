"""
Write a function repeat_inplace(L) similar to the previous exercise,
but change the list passed as a parameter, without returning it. Do not
create new lists (or other structures).

P.S. 
To check that the modified list is actually the same as passed as 
a parameter, the test will check that the id (of the two lists) match,
and that list L has been modified correctly. However, you will not see
any results in automatic tests.
"""

def repeat_inplace(A: list):
    if len(A) > 0:
        _A = A.copy()
        del A[0:len(A)]

        for a in _A:
            for i in range(0, a):
                A.append(a)

        return A

    return []

A = [3,0,2,4]
AR = [3, 3, 3, 2, 2, 4, 4, 4, 4]

id_prev = id(A)

repeat_inplace(A)

print((id_prev == id(A)) and (A == AR))	