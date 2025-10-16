"""
Write a function invert(D) which takes as a parameter a dictionary
whose values are immutable objects returns a new dictionary, inverse
of D, that is:
    - each distinct value of D becomes a key in the resulting dictionary
    - for each inverted dictionary key, the value will be a list of the original keys associated with that value
"""

def invert(D: dict):
    if len(D) > 0:
        new_dict = {}

        for value in D.values():
            if value not in new_dict:
                new_dict[value] = 0

        for new_key in new_dict.keys():
            _list = []
            for key, value in D.items():
                if value == new_key:
                    _list.append(key)
                    
            new_dict[new_key] = _list

        return new_dict

    return {}

print(invert({'a':'a', 'b':'a', 'c':'a'}))