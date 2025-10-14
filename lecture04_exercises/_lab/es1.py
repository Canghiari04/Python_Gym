"""
Collatz conjecture is based on the following algorithm:
    - Take a positive integer number m.
    - If m=1 the algorithm terminates.
    - If m is even, divide it by 2 (integer division); if m is odd, multiply it by 3 and sum 1.
    - Start again with the new m updated as above.

The conjecture, yet unproven, states this algorithm always terminates. 

Write a function collatz(m) that returns a list containing all the numbers of the Collatz sequence from m to 1.
"""

def collatz(m: int):
    _list = [m]

    if m > 0:
        while m != 1:
            if m == 1:
                return _list
            
            if m % 2 == 0:
                res = m // 2

                _list.append(res)
            else: 
                res = (m * 3) + 1
                _list.append(res)

            m = res
        
    return []

print(collatz(4))