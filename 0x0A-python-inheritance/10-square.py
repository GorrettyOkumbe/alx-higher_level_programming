#!/usr/bin/python3
"""10-square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """constructor"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
