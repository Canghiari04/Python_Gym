"""
Write a function contiguous(L) that takes a list L as a parameter and creates and returns a
new list with values taken from L - in which a series of equal contiguous values is replaced
by one single entry of the value followed by the number of occurrences of the equal contiguous values in L.
"""

def contiguous(L):
    if len(L) != 0:
        _list = []
        counter = 1

        for i in range(1, len(L)):
            if L[i - 1] != L[i]:
                _list.append(L[i - 1])
                
                if counter != 1:
                    _list.append(counter)

                    counter = 1
            else: 
                counter += 1

        _list.append(L[i])
        
        if counter != 1:
            _list.append(counter)
               
        return _list

    return []

print(contiguous([1,2, 2, 3]))