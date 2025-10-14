"""
Write a function greatersum(t) that verifies that every element of 
the tuple t is strictly grater than the sum of the previous ones.
"""

def greatersum(t: tuple) -> bool:
    if len(t) != 0:
        for i in range(1, len(t)):
            if t[i] <= sum(t[0:i]):
                return False
            
    return True

print(greatersum((1, 2, 4)))