#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of private attribute width"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """gets the private attribute height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets private attribute height"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """gets private attribute x"""

        return self.__x

    @x.setter
    def x(self, value):
        """sets private attribute x"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """gets private attribute y"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets the private attr y to value"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """computes area of arectangle"""

        return self.width * self.height

    def display(self):
        """displays Rectangle instances using #"""
        for i in range(self.height):
            print('#' * self.width)

    def __str__(self):
        """returns string info of the rectangle"""

        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)
