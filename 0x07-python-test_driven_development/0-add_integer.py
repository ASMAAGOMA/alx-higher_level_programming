#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
    a (int or float): first num
    b (int or float): second num

    Returns:
    int: the sum

    Raises:
    TypeError: a must be an integer or b must be an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
