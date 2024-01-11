#!/usr/bin/python3
"""FILE WRITER"""


def write_file(filename="", text=""):
    """function that overwrite of the file"""
    with open(filename, 'a', encoding="UTF8") as myfile:
        myfile.write(text)
    return len(text)
