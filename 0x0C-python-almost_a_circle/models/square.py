#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string rep of a square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Public getter for size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value
