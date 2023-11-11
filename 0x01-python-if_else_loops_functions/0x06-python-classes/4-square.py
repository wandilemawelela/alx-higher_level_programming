#!/usr/bin/python3
"""
This is the Square module.

This module provides a simple Square class with initialize size.
The method area returns size of area of the square.
"""


class Square:
    """Defines a square by size and can compute area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
