# Author: Andy Hung - 955587
# Course code: ICS4U0-1
# Date of submission: 12/9/2024
# Program: Class file, outlines point and polygon classes / objects 

class point:
    def __init__(self, x: float = None, y: float = None):
        # default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None
        
    def valid(self): 
        # a validator is needed mostly for when we go to the end of the file, but
        # also to assure us that the point is properly formatted with either
        # ints or floats.
        val = True 
        if self.__x == None or self.__y == None:
            val = False
        return val

    def __str__(self):
        # point (x, y) expressed this way as string, as in: (4, 5)
        if self.valid():
            return f"({self.__x},{self.__y})"
        return "Not Valid"
    
class Polygon:
    def __init__(self):
        # set basic properties to default values
        self.__sides = 1
        self.__vertices = 1
        self.__head = point() # a null point with a null Next field

    def add_point(self, x: float, y: float):
        # initialize a point object V
        if not self.__head.valid():
            self.__head = point(x, y)
            return
        V = self.__head # if it is the first point, create the object with variable V make head.next point to V
        while not V.next is None:
            V = V.next # if it is any other point, V.next points to it, and V traverses to that point
        V.next = point(x, y)
        self.__sides += 1 # count for the sides 
        self.__vertices += 1 # count for the sides 
        
    def __str__(self):
        # use of traversal to generate the entire set of points separated by "->" as string
        # uses point's __str__ function 
        if not self.__head.valid():
            return ""
        result = self.__head.__str__() 
        current = self.__head
        while current.next is not None:
            result += " -> " + current.next.__str__()  
            current = current.next
        return result
