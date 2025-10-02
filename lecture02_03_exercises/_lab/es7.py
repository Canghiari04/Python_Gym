"""
Write a function floyd(k) that takes an integer k
and prints the so-called Floyd triangle of size k.
"""

def floyd(k: int):
    count = 0
    for i in range(1, k + 1):
        l = []
        for j in range(0, i):
            count += 1
            l.append(count)

        print(tuple(l))

floyd(10)