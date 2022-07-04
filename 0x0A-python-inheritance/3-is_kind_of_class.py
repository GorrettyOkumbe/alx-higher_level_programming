#!/usr/bin/python3
"""3-iskind of class"""


def is_kind_of_class(obj, a_class):
    """
    Args:obj, a_class
    Returns True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
