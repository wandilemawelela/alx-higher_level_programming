#!/usr/bin/python3
"""
This is a Sqaure module.

This module provides a private instance attribute
size if it is of the type integer and is greater
than or equal to zero.

"""


class Square:
    """
    A very simple Square class that provides calculates
    the area of a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
