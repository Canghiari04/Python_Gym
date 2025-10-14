"""
Write a function increasing(L) that checks if a list L is sorted in ascending order (<=).

Suppose that L is a list and contains objects that can be ordered, without checkin.

Then, write a function join_ordered(L1, L2) which took as parameters two lists ordered in 
ascending order (check it using the increasing function), creates and returns a third one,
also ordered, from the union of the two.

If at least one of the two lists is not in ascending order, return None.

Do not use the sort function (or analogous, e.g. sorted) - for us to check this, you are
not allowed in this test to use any words (even in comments) containing the substring sort.
"""

def increasing(L):
    for i in range(0, len(L) - 1):
        if (L[i] >= L[i + 1]):
            return False
        
    return True

def join_ordered(L1, L2):
    if len(L1) != 0 or len(L2) != 0:
        if increasing(L1) and increasing(L2):
            _L3 = []
            _L = L1 + L2

            for i in range(0, len(_L)):
                _min = min(_L)
                _L.remove(_min)

                _L3.append(_min)            

            return _L3
        
        return None

    return []

print(join_ordered([5, 6], [3, 4]))