#!/usr/bin/python3
"""this 8-Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        this rectangle calss that inherite form BaseGeometry class
        the calss check the values of that enter by ueser to the
        constructor using the function <integer_validator>
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height
