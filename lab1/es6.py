"""
Write a perfect(k) function that takes as parameter a natural number
k and returns True if the number is perfect, False otherwise.
"""

def perfect(k: int) -> bool:
    if k != 1:
        divisors = []
        for divisor in range(1, k):
            if k % divisor == 0:
                divisors.append(divisor)

        _sum = sum(divisors)

        if _sum == k:
            return True
        
        return False
    return False

print(perfect(28))