#!/usr/bin/python3
"""FILE WRITER"""
import json


def to_json_string(my_obj):
    """Converts a Python object into a JSON string."""
    return json.dumps(my_obj)
