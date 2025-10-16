"""
Complete the class Angle which represents an angular size in degrees(sexagesimal, i.e. between 0 and 359).
Consider (without checking) only integer values for the size.
The class must implement a method get that returns the size of the Angle on which it is invoked.

The class must also redefine four magic methods __add__, __sub__, __mul__, __floordiv__, in order to perform the four operations of:
    - summation and subtraction of the angle with another angle;
    - multiplication and integer division of the angle by an integer.

NB: Do not modify the method __str__
"""

class Angle:
    def __init__(self, size):
        self.__size = size % 360

    def get(self):
        return self.__size

    def __str__(self):
        return str(self.__size) + '°'
    
    def __add__(self, angle):
        return Angle(size = (self.__size + angle._Angle__size))
    
    def __sub__(self, angle):
        return Angle(size = (self.__size - angle._Angle__size))
    
    def __mul__(self, factor):
        return Angle((self.__size * factor) % 360)
    
    def __floordiv__(self, divisor):
        return Angle(self.__size // divisor)

print(Angle(180) * 2)