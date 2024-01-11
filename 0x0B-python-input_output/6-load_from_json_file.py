#!/usr/bin/python3
"""json"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding='UTF8') as file:
        data = json.load(file)
