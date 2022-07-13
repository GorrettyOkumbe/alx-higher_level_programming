#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""

        super().__init__(size, size, x, y)

    def __str__(self):
        """string rep of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
