#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """function that prints a square with the character #
    Args:
    size (int): The size of the square
    Raisea:
    TypeError: if not integer
    ValueError: if less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
