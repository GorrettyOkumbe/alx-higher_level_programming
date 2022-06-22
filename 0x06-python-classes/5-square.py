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

    @property
    def size(self):
        """
        Getter Method: gets the value of __size
        Args: magic self ref object
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter Method: sets size to value
        Args: value
        Raises:
            TypeError: value must be int
            ValueError: value must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public Instance Method:
                    Calculates area of a square
        Returns:area of current square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints a square using '#' to the stdout
        """
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
