"""
A sequence of integers seqs is cyclic mod k (k is a positive integer) if:
    - for each index i, the element seq[i + 1] is the successor mod k of seq[i];
    - seq[0] is the successor mod k of the last seq element. 

Write a cycle(seq, k) function that takes a sequence (list,tuple,range) of
integers seq and an integer k greater than 0, and checks if seq is cyclic module k.

Use the while loop.
"""

def cycle(seq, k):
    if len(seq) > 0:
        first_value = seq[0]
        last_value = seq[len(seq) - 1]

        if first_value != (last_value + 1) % k:
            return False
        
        i = 1
        while i < len(seq) - 1:
            current_value = seq[i]

            if (current_value + 1) % k != seq[i + 1]:
                return False
            
            i += 1
            
        return True

    return True

print(cycle(range(9), 9))