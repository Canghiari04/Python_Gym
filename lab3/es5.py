"""
Write a merge(LD) function that takes a list (assume it is, without controls) LD
of dictionaries as a parameter (if not, return None). Dictionary keys are of any 
type allowable for a key, the values of any type but not lists (if you find a list, 
return None). The function returns a new dictionary obtained by merging all dictionaries.

In case the same key is present in more than one LD dictionary:
    - if all values val associated with key in different dictionaries are
      the same, then the resulting dictionary will contain the key:val item only once;
    - if there are different values (val1, val2, ..., valk) for key in LD dictionaries,
      the resulting dictionary must have the item key:[val1,val2,...,valk].
"""

def dict_contains(_dict, key, value):
    cell = _dict[key]

    if isinstance(cell, (list)):
        if value not in cell:
            cell.append(value)
            _dict[key] = cell
    else:
        if value != cell:
            _dict[key] = [cell, value]

def merge(LD:list[dict]):
    for _dict in LD:
        if type(_dict) is not dict:
            return None
        for key, value in _dict.items():
            if type(key) is list or type(value) is list:
                return None    
    
    new_dict = {}
    for _dict in LD:
        for key, value in _dict.items():
            if key not in new_dict:
                new_dict[key] = value

    for _dict in LD:
        for key, value in _dict.items():
            dict_contains(new_dict, key, value)

    return new_dict
                
print(merge([{1:'E1', 2:['R4','F5'], 3:'M2'}, {2:'V3', 3:'M2', (5,'a'):'G?1'}]) == None)