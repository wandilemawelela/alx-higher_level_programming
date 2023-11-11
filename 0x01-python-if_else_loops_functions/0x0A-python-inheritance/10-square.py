#!/usr/bin/python3
"""Defines a Square ckass that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiation with size"""
    def __init__(self, size):
        super().__init__(size, size)
