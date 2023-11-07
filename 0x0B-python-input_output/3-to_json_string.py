#!/usr/bin/python3
"""Defines a JSON string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of the my_obj string"""
    return json.dumps(my_obj)
