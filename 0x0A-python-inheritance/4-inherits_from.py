#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """args: obj
            a_class
        Returns: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
