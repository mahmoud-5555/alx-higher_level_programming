#!/usr/bin/python3
"""this 2-is_same_class_module"""


def is_same_class(obj, a_class):
    """
        this  function that returns True if the object
        is exactly an instance of the specified class
    """
    if obj == None:
        return isinstance(obj, a_class)

    return isinstance(obj, a_class) and a_class is not object
