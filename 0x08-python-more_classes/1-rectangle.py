#!/usr/bin/python3

"""class Rectangle"""

class Rectangle:

    """A class to represent a rectangle."""
    
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("Width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
