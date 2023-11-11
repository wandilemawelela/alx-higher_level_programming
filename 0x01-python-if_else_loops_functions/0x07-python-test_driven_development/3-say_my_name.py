#!/usr/bin/python3
"""
This is the Say My Name module

This module has the say_my_name() fuction
that takes in a first_name and a last_name
as parameters the prints out "My name is "
and the values passed to the parameters.
"""


def say_my_name(first_name, last_name=""):
    """Prints the value passed in the parameters of
    the say_my_name fucntion. Otherwise raises a
    TypeError is any of the parameters is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
