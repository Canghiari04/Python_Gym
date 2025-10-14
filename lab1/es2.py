"""
Write a function palindrome(s) that return True is s is palindrome, 
ignoring punctuation, whitespace and the case of the letters.
Try solving both by using double slices [::] and by not using them.
"""

import string

def palindrome(s: str) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    s = s.translate(str.maketrans(',', '.', string.punctuation))

    if len(s) != 0:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
    
    return True

print(palindrome("Angolo bar... a Bologna!"))