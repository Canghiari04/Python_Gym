"""
Write a function threes(a,b) that takes 2 integers as parameters and returns,
using only one instruction (return of a list comprehension), the list of integers
between a and b (both endpoints included!) that contain the digit 3.
"""

def threes(a, b): 
    return [x for x in range(a, b + 1) if '3' in str(x)]

print(threes(3,33))