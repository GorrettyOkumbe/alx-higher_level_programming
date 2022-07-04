#!/usr/bin/python3
"""2-is_same"""


def is_same_class(obj, a_class):
    """Args: obj
            a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
