#!/usr/bin/python3
"""Defines a new append write function"""


def append_write(filename="", text=""):
    """Appends to a new file then returns the lenght"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
