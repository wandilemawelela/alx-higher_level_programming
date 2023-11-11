#!/usr/bin/python3
"""Defines a new write file function"""


def write_file(filename="", text=""):
    """"Writes a file the returns its lenght"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
