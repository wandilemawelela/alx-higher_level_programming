#!/usr/bin/python3
"""Defines the class MyList"""


class MyList(list):
    """MyList subclass that prints the list that is sorted."""
    def print_sorted(self):
        print(sorted(self))
