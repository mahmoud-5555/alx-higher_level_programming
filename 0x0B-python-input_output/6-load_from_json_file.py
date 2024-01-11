#!/usr/bin/python3
"""json"""
import json


def load_from_json_file(filename):
    """
        function that convert json_string
        from the file to python opject
    """
    with open(filename, 'r', encoding='UTF8') as file:
        data = json.load(file)
