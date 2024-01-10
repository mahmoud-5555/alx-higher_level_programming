#!/usr/bin/python3
"""this my_list_module"""


class MyList(list):
    """A class that inherits from the built-in list class."""
    def __init__(self, *args, **kwargs):
        """ Call to parent constructor"""
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        print(sorted(self))
