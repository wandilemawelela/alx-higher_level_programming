#!/usr/bin/python3
def lookup(obj):
    attributes = []
    methods = []

    for attr in dir(obj):
        if not callable(getattr(obj, attr)):
            attributes.append(attr)

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)

    return attributes + methods
