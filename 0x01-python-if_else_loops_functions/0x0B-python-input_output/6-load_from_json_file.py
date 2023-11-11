#!/usr/bin/python3
"""Defines a load from json function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file” """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
