#!/usr/bin/python3
"""101-locked_class module"""


class LockedClass:
    """LockedClass class
    This class prevents user from dynamic attributes"""

    __slots__ = ['first_name']
