#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Defines a class BaseGeometry"""

    def area(self):
        """Area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer_validator

        Args:
        name (string): The name
        value (int): The value

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Defines the Rectangle class"""


class Rectangle(BaseGeometry):
    """Defines the Rectangle class"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self._Rectangle__width = width
        self.integer_validator("height", height)
        self._Rectangle__height = height

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
