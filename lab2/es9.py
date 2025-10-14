"""
Write a function vowels(s) that takes as parameter a string and
returns a list containing, only once, the vowels present in s.

In the list the vowels are presented as lowercase, but they must
be considered both the lower case ones and the upper case ones in the original string s.

The order of the vowels in the returned list is the same one with 
which they appear (the first time) in the string. 

Use the while loop and the lower() method.

Do not use the for loop - to check this, you are not allowed in 
this test to use any words (even in comments) containing the substring for. 
"""

def vowels(s: str):
    if len(s) > 0: 
        lower_s = s.lower()
        list_contained_vowels = []
        list_vowels = ['a', 'e', 'i', 'o', 'u'] 

        i = 0
        while i < len(lower_s):
            current_value = lower_s[i]

            if current_value in list_vowels and current_value not in list_contained_vowels:
                list_contained_vowels.append(current_value)

            i += 1

        return list_contained_vowels

    return []

print(vowels("AAA"))