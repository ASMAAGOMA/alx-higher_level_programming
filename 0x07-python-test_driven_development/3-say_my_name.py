#!/usr/bin/python3
"""function that prints My name """


def say_my_name(first_name, last_name=""):
    """function that prints My name
    Args:
    first_name (str): The first name
    last_name (str): The last name
    Raises:
    TypeError: if not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
