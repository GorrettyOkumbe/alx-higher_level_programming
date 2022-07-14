#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """My base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            "[]"
