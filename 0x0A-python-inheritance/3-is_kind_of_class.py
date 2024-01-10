#!/usr/bin/python3
"""this 3-is_kind_of_class.py_module"""


def is_kind_of_class(obj, a_class):
    """
        rite a function that returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class; otherwise False.
     """
    return isinstance(obj, a_class) and type(obj) is not a_class
