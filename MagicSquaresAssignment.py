# Author: Andy Hung - 955587
# Course code: ICS4U0-1
# Date of submission: 10/25/2024
# Program: Magic Squares Assignment 
# Description: Take an input N which can be any prime number from 5 to 19 and output a
# magic square of N x N, the magic sum, a magic square of a matrix containing numbers 1
# to N plus a matrix of sucessive products of N, and a check to see if that magic square is magic 
# VARIABLE DICTIONARY:
#   arr1 (list) = 1d array of 1 to N shuffled
#   MS1 (list) = 2d array containing numbers 1 to N shuffled and shifted each row 
#   MS2 (list) = 2d array containing successive products of N shuffled and shifted each row
#   MS3 (list) = 2d array of M1 + M2 
#   MagicSum (int) = used to display the magic sum
#   FCheck (bool) = used to check if user input has factors besides 1 and N
#   InputPN (int) = user's input of a prime number between 5 and 19 

import random
arr1 = []
MS1 = []
MS2 = []
MS3 = []
MagicSum = 0
FCheck = False
"""
Precondition: accepts an array
Postcondition: appends arrays containing 1 to N shuffled and shifted each row into MS1,
appends arrays of succesive products N shuffled and shifted each row into MS2, returns 0 
"""
def MagicSquare(arr1):
    arr2 = []
    random.shuffle(arr1)
   
    for i in range(InputPN):
        arr2.append(InputPN*i)
   
    random.shuffle(arr2)
   
    for i in range(len(arr1)):
        MS1.append(arr1)
        newarr = []
        for j in range(len(arr1)):
            newarr.append(arr1[(j - 2) % InputPN])
        arr1 = newarr
    
    for i in range(len(arr2)):
        MS2.append(arr2)
        newarr = []
        for j in range (len(arr2)):
            newarr.append(arr2[(j - 3) % InputPN])
        arr2 = newarr
    return 0
"""
Precondition: accepts two matricies of numbers 
Postcondition: appends arrays cotaining each value in matrix A plus the corresponding value
in matrix B to MS3, returns 0 
"""
def add(A, B):
    for i in range(len(A)):
        newarr = []
        for j in range(len(A)):
            x = A[i][j] + B[i][j]
            newarr.append(x)  
        MS3.append(newarr)
    return 0
"""
Precondition: accepts a matrix of numbers 
Postcondition: prints the sum of each row, column and diagonal, prints a message depending
on if each row, column and diagonal add up to the magic sum, returns 0 
"""
def isMagic(MS):
    print() 
    for i in range(len(MS)):
        RSum = 0
        for j in range(len(MS)):
            RSum += MS[i][j]
        print("The sum of row #%d is %d" % (i + 1, RSum))
        
    for i in range(len(MS)):
        CSum = 0
        for j in range(len(MS)):
            CSum += MS[j][i]
        print("The sum of column #%d is %d" % (i + 1, CSum))
        
    DSum1 = 0
    for i in range(len(MS)):
        DSum1 += MS[i][i]
    print("The sum of the first diagonal is", DSum1)
    
    DSum2 = 0
    for i in range(len(MS)):
        DSum2 += MS[i][len(MS)-i-1]
    print("The sum of the second diagonal is", DSum2)
    
    if (RSum != MagicSum) or (CSum != MagicSum) or (DSum1 != MagicSum) or (DSum2 != MagicSum):
        print("This square is not magic!")
    else:
        print("This square is magic!")
    return 0 

InputPN  = int(input("Please input a prime number from 5 to 19: "))
print() 

for i in range(2, InputPN):
    if (InputPN % i) == 0:
        FCheck = True
        break

if FCheck:
    print("Input is not a prime number from 5 to 19, please try again.")
elif (InputPN < 5) or (InputPN > 19):
    print("Input is not a prime number from 5 to 19, please try again.")
else: 
    for i in range(InputPN):
        arr1.append(i + 1)
   
    MagicSquare(arr1)
    add(MS1, MS2)
   
    for i in range(len(MS1)): 
        print(MS1[i])
    print()

    for i in range((InputPN**2 + 1)):
        MagicSum += i
    MagicSum = (MagicSum / InputPN)
    print("The magic sum is", MagicSum, "\n")

    for i in range(len(MS3)):
        print(MS3[i])
    
    isMagic(MS3)
