#!/usr/bin/python3
"""Add a new attribute to an object if possible."""


def add_attribute(obj, attr_name, attr_value):

    """Add a new attribute to an object if possible.

    Args:
    obj: The object to which the attribute should be added.
    attr_name (str): The name of the attribute.
    attr_value: The value to assign to the attribute.

    Raises:
    TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
