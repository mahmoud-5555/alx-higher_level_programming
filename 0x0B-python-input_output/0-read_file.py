#!/usr/bin/python3
"""FILE READER"""


def read_file(filename=""):
    """
        function that print the contest that inside the file
    """
    with open(filename, 'r+', encoding='UTF8') as myfile:
        print(myfile.read())
