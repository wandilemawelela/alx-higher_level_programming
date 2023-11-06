#!/usr/bin/python3
"""Defines the class MyList"""


class MyList(list):
    """MyList subclass that prints the list that is sorted."""
    def __init__(self):
        """Init object"""
        super().__init__()

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
