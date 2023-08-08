#!/usr/bin/python3

"""Defines a Rectengle"""


class Rectangle:
    """Represents a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle
        Args:
        width (int): The width of the rectengle
        height (int): The height of the rectengle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectengle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectengle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the erea of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the parameter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rec = ""
        for i in range(self.__height):
            rec += "#" * self.__width
            rec += '\n'
        return rec[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
