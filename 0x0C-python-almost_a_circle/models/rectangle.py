#!/usr/bin/python3
"""this is the module Rectangle"""
from base import Base


class Rectangle(Base):
    """
    This class represents a rectangle, inherits from Base.//class
    wihthout Error handling
    """
    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        if not isinstance(x, int):
            raise TypeError('x must be an integer')

        if not isinstance(y, int):
            raise TypeError('y must be an integer')

        if x < 0:
            raise ValueError('x must be >= 0')

        if y < 0:
            raise ValueError('y must be >= 0')

        self.__x, self.__y = x, y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @property 
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """function that return string represention for the instanse"""
        s = "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    # def __del__(self):
    #     print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        new_square = Rectangle(size, size)
        return new_square

    def display(self):
        """functoun that display the shape"""
        res = ''
        if (self.__width == 0 or self.__height == 0):
            return ''
        
        res = '\n' *self.__y

        for i in range(self.__height):

            if (i < self.__height - 1):
                res += self.__x * ' ' + str(self.print_symbol) * (self.__width) + '\n'
            else:
                res += self.__x * ' ' + str(self.print_symbol) * (self.__width)
        return res

    def update(self, *args, **kwargs):
        """function that update the values of the shape"""
        if(len(args) > 5):
            raise ValueError("Too many arguments supplied.")
    
        elif(len(args) == 0 and len(kwargs) == 0):
            raise ValueError("No argument supplied.")
        
        for i, arg in enumerate(args):
            setattr(self,f"attribute{i + 1}", arg)
        
        for key, value in kwargs.items():
            setattr(self, key, value)
