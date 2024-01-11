#!/usr/bin/python3
"""FILE WRITER"""

def append_write(filename="", text=""):
    """function that overwrite of the file"""
    with open(filename, 'a', encoding="UTF8") as myfile:
        myfile.write(text)
    return len(text)
