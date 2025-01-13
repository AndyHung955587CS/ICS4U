# Author: Andy Hung 
# Course code: ICS4U0-1
# Date of submission: 12/20/2024
# Program: driver, Polygon Object (Part 2)
# Description: Using the poly class file and a2.txt which contains points
# of a polygon in one line: print out the points, perimeter, area, if it is
# regular or irregular and display the polygon using turtle 
# VARIABLE / FUNCTION DICTIONARY:
#  getNumeric = accepts string in the format "(x,y)" returns returns points
#  x and y as float  
#  polydata (str) = a2.txt read as string 
#  polypoint (list) = list of points seperated by a comma 
#  myPoly (poly.Polygon) = polygon object printed as a linked list
#  distances (list) = runs distances function on polygon object
#  perimeter (float) = runs perimeter function on polygon object
#  check (bool) = runs is_regular function on polygon object
#  area (float) = runs area function on polygon object

from poly import *

def getNumeric(S: str):
    point = S[1:-1].split(",")
    x = float(point[0])
    y = float(point[1]) 
    return (x, y)

fh = open("a2.txt", "r") 
polydata = fh.readline().strip()
polypoint = polydata.split(", ")  
myPoly = Polygon() 

for token in polypoint: 
    x, y = getNumeric(token) 
    myPoly.add_point(x, y) 

print("Here are points in a polygon:", myPoly)

distances = myPoly.distances()
perimeter = myPoly.perimeter()
check = myPoly.is_regular()
area = myPoly.area()
if check == True:
    print("This is a regular polygon.")
else:
    print("This is an irrgeular polygon.") 
print("Distances between each point:", distances)
print("The perimeter of this polygon is", perimeter)
print("The area of this polygon is", area)
myPoly.draw()
