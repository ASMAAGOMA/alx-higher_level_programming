#!/usr/bin/python3
"""Defines a class checks the function"""


def inherits_from(obj, a_class):
    """Checks the object

    Args:
    obj (any): The object
    a_class (type): The class
    Returns: True or false

    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
