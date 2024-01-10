#!/usr/bin/python3
""" my module """

def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if it's possible."""
    if hasattr(obj, '__dict__') and not hasattr(obj, attr_name):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
