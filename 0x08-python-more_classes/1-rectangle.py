#!/usr/bin/python3
"""0-rectangle module"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """constructor instance method
        Args: width
              height
        """

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method
        Args: value
        Raises: TypeError
                    height must be an integer
                ValueError:
                    height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter method
        Returns self.__width"""
        return self.__width

    @width.setter
    def width(self, value):
        """height setter method
        Args: value
        Raises: TypeError: height must be an integer
                ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
