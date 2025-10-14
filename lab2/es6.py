"""
Write a repeat_numbers(L) function which, given a list of natural numbers
(assume they are greater or equal to 0, without checking), returns a new
list in which the same elements of the list appear as parameter and in the 
same order, but each element of the list is repeated the number of times 
corresponding to the element (e.g. 0 will be repeated zero times, 1 once, 2 twice and so on).
"""

def repeat_numbers(L):
    if len(L) > 0:
        new_list = []
        for i in range(0, len(L)):
            current_val = L[i]
            for j in range(0, current_val):
                new_list.append(current_val)

        return new_list
    return []

print(repeat_numbers([2, 1, 3, 1, 2]))