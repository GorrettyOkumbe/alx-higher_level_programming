#!/usr/bin/python3
"""5-save to json module"""
from json import dump


def save_to_json_file(my_obj, filename):
    """saves to a json file"""

    with open(filename, 'w') as file:
        return dump(my_obj, file)
