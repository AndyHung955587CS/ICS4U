# Author: Andy Hung 
# Course code: ICS4U0-1
# Date of submission: 1/22/2025
# Program: Ivt object/class, Final Project: The IVT Theorem 
# Description: Calculates the 0 based off of two guesses (x1, x2), can return string
# statement if input is faulty 
# FUNCTION DICTIONARY:
#   class IVT:
#      __init__ = declares a copy of the polynomial input expressed as
#      coefficients (int or float) in an array
#      findZero = returns the 0 or if there's faulty input return a message 

from Polynomial import *

class IVT:
    def __init__(self, P):
        self.__polynomial = P
        
    """
    Accepts two guesses x1 and x2 (int or float)
    Returns the 0 (float) or string message 
    """
    def findZero(self, x1, x2):
        if (x1 == x2):
            return "The two guesses can't be equal in value."
        elif self.__polynomial.f(x1) * self.__polynomial.f(x2) > 0:
            return "No solution exists."
        
        left = x1
        right = x2
        
        while right - left >= 0.0004:
            avg = (right + left)/2
            result = self.__polynomial.f(avg)
            if result > 0:
                right = avg
            elif result < 0:
                left = avg
            else:
                return avg
        return (left + right)/2