#!/usr/bin/python3

class Base:
    """A class representing a base object"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object

        Args:
            id (int, optional): An identifier for the object. If not provided,
            it is auto-generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
