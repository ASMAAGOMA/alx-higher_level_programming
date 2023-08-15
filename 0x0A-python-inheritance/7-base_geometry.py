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
