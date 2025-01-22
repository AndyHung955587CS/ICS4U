# Author: Andy Hung 
# Course code: ICS4U0-1
# Date of submission: 1/22/2025
# Program: Poly driver, Final Project: The IVT Theorem
# Description: Driver to test the polynomial class 
# VARIABLE / FUNCTION DICTIONARY:
#   P (Polynomial.Polynomial) = coefficients (numbers in an array) of a polynomial
#   x1 (int) = first guess  
#   x2 (int) = second guess 

from Polynomial import *
from IVT import *

P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])
x1 = -1
x2 = 1

print(P)

for i in range(10):
    print(i, P.f(i))
print(P.get_order())

print(x1, P.f(x1))
print(x2, P.f(x2))