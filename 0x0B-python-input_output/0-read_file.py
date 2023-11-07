#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Prints the contents of a text file to stdout"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
