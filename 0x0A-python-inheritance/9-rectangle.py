#!/usr/bin/python3
"""Defines a new Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry and instantes with width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """Area mathod to calculate the area"""
    def area(self):
        return self.__width * self.__height

    """Return value for str()"""
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
