#!/usr/bin/python3
"""Defines an object instance lookup function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
