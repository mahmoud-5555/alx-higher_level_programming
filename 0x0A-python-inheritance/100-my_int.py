#!/usr/bin/python3
""" Myint """


class MyInt(int):
    """this myint calss that make the opratetor negtive or invers"""
    def __eq__(self, b):
        return not int.__eq__(self, b)

    def __ne__(self, b):
        return int.__eq__(self, b)
