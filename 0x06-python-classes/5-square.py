#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
The methods Getter and Setter set properties for size.
Th method area returns size of area of the square.
The method my_print prints the square using "#".
"""


class Square:
    """Defines a square by size, which defaults 0.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
