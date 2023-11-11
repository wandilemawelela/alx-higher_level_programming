#!/usr/bin/python3
"""Defines a BaseGeometry class with a single public instance method"""


class BaseGeometry:
    """Proviced a simple public instance method that
    raises an Exception with the message area() is not
    implemented"""
    def area(self):
        raise Exception("area() is not implemented")
