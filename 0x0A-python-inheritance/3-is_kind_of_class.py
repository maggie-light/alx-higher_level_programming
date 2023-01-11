#!/usr/bin/python3
"""Define a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """checking if an object is an instance or inherited instance of a class.

    Args:
    obj (any): The obj to check.
    a_class (type): The class to match the type of obj to.
    Return:
    if obj is an instance or inherited instance of a_class - True.
    Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
