#!/usr/bin/python3
""" Myint """


class myint(int):
    """this myint calss that make the opratetor negtive or invers"""
    def __eq__(self, a, b):
        return not int.__eq__(a, b)

    def __ne__(self, a, b):
        return int.__eq__(a, b)
