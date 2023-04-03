#!/usr/bin/python3
""" Defines rectangle class"""

class Rectangle:
    """rectangle class"""
    
    """public class attribute"""
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """class constructor or instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        
    @property
    def width(self):
        """getter for private instance width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
            
    @property
    def height(self):
        """getter for private instance height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """area of rectangle"""
        return self.__width * self.__height
    
    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of recatangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string +=  "\n" .join(self.print_symbol * self.__width for i in range(self.__height))
        return string
    
    def __repr__(self):
        """return object function representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    def __del__(self):
        """prints bye when an instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return bigger rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if area(rect_1) >= area(rect_2):
            return rect_1
        return rect_2
