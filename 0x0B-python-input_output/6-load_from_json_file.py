#!/usr/bin/python3
"""6-load from json module"""
from json import load


def load_from_json_file(filename):
    """load from json"""
    with open(filename) as file:
        return load(file)
