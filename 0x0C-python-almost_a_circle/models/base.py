#!/usr/bin/python3
"""this is the module doc"""


class Base:
    """
    This is a base class.
    attributes:
    __nb_opjects: number of opjects
    id: the id of the instance
    """
    __nb_opjects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_opjects += 1
            self.id = Base.__nb_opjects
