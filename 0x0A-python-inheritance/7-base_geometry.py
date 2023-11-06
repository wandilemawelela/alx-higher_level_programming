#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Proviced a simple public instance method that
    raises an Exception with the message area() is not
    implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    """Validates the value parameter"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
