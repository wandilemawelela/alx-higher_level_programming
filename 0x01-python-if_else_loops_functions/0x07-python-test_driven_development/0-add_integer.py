#!/usr/bin/python3
"""
This is the Add Interger module

This modules hass the add_integer() fuction
that adds together 2 int or float data types
and returns an int.
"""


def add_integer(a, b=98):
    """Returns the sum of two ints or floats as an int.
    Otherwise it raises a TypeError for an incorrect arg
    type.
    """

    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + int(b)

    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
