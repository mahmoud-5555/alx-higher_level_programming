#!/usr/bin/python3
"""this 7-base_geometry module """


class BaseGeometry:
    """this is BaseGeometry class"""

    def area(self):
        """the plany method in the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator"""
        if type(name) is not str:
            raise TypeError('parameter name must be a string')
        if name == '':
            raise ValueError('name cannot be empty')
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
