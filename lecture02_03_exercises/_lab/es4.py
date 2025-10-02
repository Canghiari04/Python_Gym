"""
Write a function average(grades) that takes a tuple grades as an argument and:
 - Checks that the tuple grades contains only integers and floats. Otherwise, return None
 - Computes the arithmetic mean/average of all the values in grades and return it as a float
 - The function does not compute and return anything if the tuple is empty
"""

def average(grades: tuple) -> float: 
    if len(grades) != 0:
        sum = 0
        for grade in grades:
            if type(grade) is int or type(grade) is float:
                sum += grade
            else:
                return None
            
        return sum / len(grades)
    return None

print(average((17, 18)))