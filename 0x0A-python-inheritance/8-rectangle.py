#!/usr/bin/python3
"""Defines the Rectangle class"""
BaseGeometry = import('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class"""

    def init(self, width, height):
        """Intialize a new Rectangle.

        Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
