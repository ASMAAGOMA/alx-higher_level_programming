#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents the sqaure"""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
        size(int):The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
