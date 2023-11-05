#!/usr/bin/python3
class LockedClass:
    __slots__ = ('_first_name',)

    def __init__(self):
        self._first_name = None

    def __setattr__(self, name, value):
        if name != '_first_name':
            raise AttributeError
        self.__dict__[name] = value
