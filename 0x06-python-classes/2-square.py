#!/usr/bin/python3


"""Square module"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """
        constractor:
        Args:
            size: length of the square
        Raises:
            ValueError: if size < 0
            TypeError: if size not int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
