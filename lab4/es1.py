"""
Define a class Fraction to represent fractions as objects with 
three elements: sign, numerator, denominator, of types respectively str, int, int.

The __init__ takes as parameters two integers N and D.
    - N represents the numerator with sign of the fraction
    - D represents the denominator. It must always be >0. If 
      it is not passed, it assumes the default value of 1. 

The __init__ initializes the following private attributes:
    - __sign: a string of a single character that represents 
      the sign of the fraction. It can assume only values '+' or '-'
    - __num: a positive (>=0) integer that represents the numerator
    - __den: a positive integer, different from 0 (i.e. >0), that 
      represents the denominator 

NB!! The __init__ checks that N and D are integers, and that D>0

In case the parameters do not respect these conditions, all the attributes for sign, numerator, and denominator must be initialized to None 

The class implements several methods.
    - Write a method get that returns sign, numerator, and denominator as a tuple of type (str, int, int). E.g. fraction +1/10
      will be returned as the tuple ('+',1,10), while the fraction -3/5 will be returned as ('-', 3, 5)
    - Write a method value that takes as parameter an integer d and calculates the value of 
      the fraction and returns it as a float, rounded with the round function at d decimals.
    - Write a method reduce that modifies the fraction by reducing it to the lowest terms. 
      Hint: you can use the gcd function from the math module. For testing purposes, the method must also return self
    - Write the magic method __eq__ that checks if the fraction is equal to another fraction taken 
      as a parameter. Two fractions are equal if their reduced forms are equal. Attention: the method must not 
      reduce or modify the two objects. Do not use the value function and in general do not compare the float values of the fractions.
    - Write the magic method __str__ that returns a string representation of the fraction. The string 
      is in the form SN/D (e.g. +1/3, -20/40), without spaces
    - Write the magic method __add__ that adds the fraction on which is called to another. 
      The return value must be a new fraction, reduced to the lowest terms. Attention: the method must not 
      reduce or modify the two original objects. If the resulting numerator is 0, return the reduced fraction with numerator 0 and the reduced denominator.
"""

import math

class Fraction():
    def __init__(self, N: int, D: int):
        if isinstance(N, int):
            self.__sign = '+' if N >= 0 else '-'
            self.__num = N
        else:
            self.__sign = None
            self.__num = None
            self.__den = None
        
        if isinstance(D, int):
            self.__den = D if D is not None and D > 0 else 1
        else:
            self.__sign = None
            self.__num = None
            self.__den = None

    def get(self) -> tuple:
        return (self.__sign, self.__num, self.__den)
    
    def value(self, d: int):
        return round((self.__num / self.__den), d)

    def reduce(self):
        gcd = math.gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd

        return self
    
    def __eq__(self, f):
        gcd = math.gcd(self.__num, self.__den)
        num = self.__num // gcd
        den = self.__den // gcd

        return (num // den) == f

    def __str__(self):
        str_list = [self.__sign, str(self.__num), '/', str(self.__den)]
        return "".join(str_list)
    
    def __add__(self, f):
        gcd_fraction_1 = math.gcd(self.__num, self.__den)
        gcd_fraction_2 = math.gcd(f._Fraction__num, f._Fraction__den)

        numerator_1 = self.__num // gcd_fraction_1
        denominator_1 = self.__den // gcd_fraction_1

        numerator_2 = f._Fraction__num // gcd_fraction_2
        denominator_2 = f._Fraction__den // gcd_fraction_2

        common_denominator = denominator_1 * denominator_2

        factor_1 = numerator_1 * (common_denominator // denominator_1)
        factor_2 = numerator_2 * (common_denominator // denominator_2)

        factor = factor_1 + factor_2

        gcd_fraction_3 = math.gcd(factor, common_denominator)

        numerator_3 = factor // gcd_fraction_3 
        common_denominator //= gcd_fraction_3 

        return Fraction(numerator_3, common_denominator)
    
print(Fraction(6,300) == Fraction(3,150))