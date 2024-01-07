#!/usr/bin/python3

"""	0_add_integer
	this module has adds two integers
    function that return the sumation of
    two intgers
"""


def add_integer(a, b=98):
    """	this is function that add two intgers
    	Args: a,b inegers values
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
        

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    b = int(b)
    a = int(a)
    return a + b
	