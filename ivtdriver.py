# Author: Andy Hung 
# Course code: ICS4U0-1
# Date of submission: 1/22/2025
# Program: Ivt driver, Final Project: The IVT Theorem
# Description: Driver to run the ivt class, returns an estimate using the ivt theorem
# of where the 0 might be based on a polynomial and two guesses (x1, x2) as to where the 0 might be 
# VARIABLE DICTIONARY:
#   P (Polynomial.Polynomial) = coefficients (numbers in an array) of a polynomial
#   x1 (float) = first guess  
#   x2 (float) = second guess
#   polyFinal (IVT.IVT) = the polynomial ran through the ivt class
#   zero (float) = x0 where f(x0) = 0

from Polynomial import *
from IVT import * 

try: # Tries for an error 
    P = Polynomial([1, 2, 3, 4, 5, 6]) # input for coefficients of a polynomial
    x1 = -1.6 # input for the first guess
    x2 = -1.3 # input for the second guess 

    polyFinal = IVT(P)
    zero = polyFinal.findZero(x1, x2)

    if type(zero) == str:
        print(zero)
    else:
        print("The zero of the interval (%f,%f) is %f." % (x1, x2, zero))
except: # Catches an error if any input for P, x1 and x2 aren't int or float 
    print("Input must be a number.")