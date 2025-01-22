# Author: Andy Hung 
# Course code: ICS4U0-1
# Date of submission: 1/22/2025
# Program: Polynomial object/class, Final Project: The IVT Theorem
# Description: Calculates the order, f(x) of a given value x, and expresses itself as string
# FUNCTION DICTIONARY:
#    class Polynomial
#    __init__ = declares a copy of the polynomial input expressed as
#    coefficients (int or float) in an array (cuts any leading zeroes) 
#    get_order = returns the order of the polynomial
#    f = Returns f(x) for a given x value 
#    __str__ = returns the polynomial as string

class Polynomial:
    def __init__(self, arr):
        self.__coefficients = []
        for i in arr:
            if not (i == 0 and (len(self.__coefficients)) == 0):
                self.__coefficients.append(i)  
                
    """
    Precondition: Accepts an array of numbers (coefficients of a polynomial)
    Postcondtion: Returns the order of the polynomial as string
    """
    def get_order(self):
        return ("The order of this polynomial is %d" % (len(self.__coefficients) - 1))
    
    """
    Precondition: Accepts x (int or float)
    Postcondtion: Returns f(x) as float 
    """
    def f(self, x):
        result = 0
        for i in range(len(self.__coefficients)):
            result += self.__coefficients[i] * x ** (len(self.__coefficients) - i - 1)
        return result
    
    """
    Precondition: Accepts an array of numbers (coefficients of a polynomial)
    Postcondtion: Returns the polynomial as string 
    """   
    def __str__(self):
        result = ""
        for i in range(len(self.__coefficients)):
            result += str(self.__coefficients[i]) + "x^" + str(len(self.__coefficients) - i - 1)
            if not i == len(self.__coefficients) - 1:
                result += " + " 
        return result