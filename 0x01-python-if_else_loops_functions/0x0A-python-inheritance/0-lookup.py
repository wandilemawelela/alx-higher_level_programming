#!/usr/bin/python3
"""Defines an obj attribute lookup function"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    attributes = []
    methods = []

    for attr in dir(obj):
        if not callable(getattr(obj, attr)):
            attributes.append(attr)

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)

    return attributes + methods
