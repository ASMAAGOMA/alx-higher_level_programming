#!/usr/bin/python3

"""Defines a Rectengle"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):

        """Initialize a Rectangle

        Args:
        width (int): The width of the rectengle
        height (int): The height of the rectengle
        """
        self.__width = width
        self.__height = height

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
