#!/usr/bin/python3


"""Square module"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """
        Sets and gets the value of private position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        Prints the square using # at correct position
        """
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
