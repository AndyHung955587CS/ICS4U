# Author: Andy Hung 
# Course code: ICS4U0-1
# Date of submission: 12/20/2024
# Program: poly, Polygon Object (Part 2)
# Description: Class file that outlines many functions to be used in the
# driver file 
# FUNCTION DICTIONARY:
#   class Point:
#       __init__ = declares x and y points as floats 
#       valid = validates x and y, makes sure it is properly formatted
#       with ints or floats and it's not at the end of the file 
#       __str__ = returns point (x,y) expressed this way as string, as in: (4,5)
#       distance = formula for the distance between two points 
#       get_x = getter method for x 
#       get_y = getter method for y 
#   class Polygon:
#       _init__ = declares variable for number of sides and head node 
#       add_point = traversal to generate points as float 
#       __str__ = traversal to generate points seperate by "->" as string 
#       distances = traversal to calculate all distances and append them into
#       self.__distances 
#       perimeter = loops through self.__distances to calculate perimeter 
#       is_regular = compares perimeter against distance to number of sides to
#       see if the polygon is regular or irregular 
#       area = traversal to calculate area 
#       draw = traveral to draw the polygon using turtle, all points are mutiplied
#       by 25 otherwise it would be too small on turtle display 

import math 
import turtle 

class Point:
    def __init__(self, x: float = None, y: float = None):
        self.__x = x
        self.__y = y
        self.next = None
        
    def valid(self): 
        val = True 
        if self.__x == None or self.__y == None:
            val = False
        return val
    
    def __str__(self):
        if self.valid():
            return f"({self.__x},{self.__y})"
        return "Not Valid"
    
    def distance(self, p2):
        return math.sqrt((self.__x - p2.__x)**2 + (self.__y - p2.__y)**2)
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
class Polygon:
    def __init__(self):
        self.__sides = 0  
        self.__head = None  

    def add_point(self, x: float, y: float):
        if not self.__head:
            self.__head = Point(x, y)
            return
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = Point(x, y)
        self.__sides += 1

    def __str__(self):
        if not self.__head:
            return ""
        result = self.__head.__str__()
        current = self.__head
        while current.next:
            result += " -> " + current.next.__str__()
            current = current.next
        return result
    
    def distances(self):
        self.__distances = []
        if not self.__head: 
            return self.__distances  
        current = self.__head
        while current.next:
            self.__distances.append(current.distance(current.next))
            current = current.next
        self.__distances.append(current.distance(self.__head))  
        return self.__distances
    
    def perimeter(self):
        temp = 0
        for i in self.__distances: 
            temp += i
        return temp 
    
    def is_regular(self):
        if self.perimeter() == (self.__distances[1] * self.__sides):
            return True
        return False
        
    def area(self):
        temp = 0
        if self.is_regular():
            temp = (self.perimeter()**2)/(4 * math.tan(180/self.__sides))
            return temp
        else:
            if not self.__head: 
                return   
            current = self.__head
            first_point = current  
            while current.next:
                temp += current.get_x() * current.next.get_y()
                temp -= current.get_y() * current.next.get_x()
                current = current.next
            temp += current.get_x() * first_point.get_y()
            temp -= current.get_y() * first_point.get_x()
            temp = (temp/2)
            return abs(temp)
        
    def draw(self):
        turtle.bgcolor("gray80")
        turtle.hideturtle() 
        turtle.penup()
        if not self.__head:
            return  
        current = self.__head
        turtle.goto(current.get_x() * 25, current.get_y() * 25)  
        turtle.pendown()  
        while current.next:
            next_point = current.next
            turtle.goto(next_point.get_x() * 25, next_point.get_y() * 25)  
            current = next_point
        turtle.goto(self.__head.get_x() * 25, self.__head.get_y() * 25)
        turtle.done()
