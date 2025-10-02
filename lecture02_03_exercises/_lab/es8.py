"""
Write a function compatibility(name1, name2) that returns an integer between 
0 and 100 that represents the love compatibility between name1 and name2, 
with the following algorithm. 

The algorithm is based on the word Love. It counts the number of L, O, V and E
in the two names.

The percentage is calculated as:
        (number of Ls + number of Os) * 10 + (number of Vs + number of Es)
"""

def compatibility(name1: str, name2: str) -> float:
    characters_l_o = ['L', 'O']
    characters_v_e = ['V', 'E']

    name1 = name1.upper()
    name2 = name2.upper()

    count_l_o = 0
    count_v_e = 0
    for char in name1:
        if char in characters_l_o:
            count_l_o += 1
        if char in characters_v_e:
            count_v_e += 1

    for char in name2:
        if char in characters_l_o:
            count_l_o += 1
        if char in characters_v_e:
            count_v_e += 1

    return ((count_l_o * 10) + count_v_e) % 100

print(compatibility("Lorella Evelina", "Lorenzo Eulo"))