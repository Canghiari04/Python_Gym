"""
Write a one-line function invert(D) which takes as a
parameter a dictionary whose values are immutable objects 
returns a new dictionary, inverse of D, that is:
    - each distinct value of D becomes a key in the resulting 
      dictionary
    - for each inverted dictionary key, the value will be a 
      list of the original keys associated with that value
"""

def invert(D: dict):
    return {key:[_ for _, value in D.items() if key == value] for key in D.values()}

D = {'a':2, 'b':2, 'c':3, 'd':4, 'e':3,'f':0, 'g':3, 'h':2}
print(invert(D))