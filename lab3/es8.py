"""
Write a function listdivisible(a, b, c, d) with a single instruction 
(the return of a list comprehension) that takes as parameters four natural 
numbers and returns the list of all the numbers from a to b (both included) 
that are divisible by all the numbers from c to d (both included).

The len() function and a nested list comprehension can be useful.
"""

def listdivisible(a, b, c, d):
    return [x for x in range(a, b + 1) if len([divisor for divisor in range(c, d + 1) if x % divisor == 0]) ==  len(range(c, d + 1))]

print(listdivisible(1,1000, 2, 6))