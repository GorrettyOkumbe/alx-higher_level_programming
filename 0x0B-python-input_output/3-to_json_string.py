#!/usr/bin/python3
"""json module"""
from json import dumps


def to_json_string(my_obj):
    """writes to json string"""
    return dumps(my_obj)
