#!/usr/bin/python3
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
    if type(a) not in(int, float):
        raise TypeError("a must be an integer")
    if type(b) not in(int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
