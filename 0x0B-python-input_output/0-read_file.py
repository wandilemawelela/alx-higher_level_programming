#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Prints the contents of a text file to stdout"""
    line_number = 0

    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            line_number += 1
            print('{}'.format(a_line.strip()))
