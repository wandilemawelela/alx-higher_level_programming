#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int, optional): The x-coordinate of the rectangle's position.
        Default is 0.
        - y (int, optional): The y-coordinate of the rectangle's position.
        Default is 0.
        - id (int, optional): The unique identifier. Default is None.
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Public getter and setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_positive_integer("width", value)
        self.__width = value

    """Public getter and setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_positive_integer("height", value)
        self.__height = value

    """Public getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_non_negative_integer("x", value)
        self.__x = value

    """Public getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, attribute_name, value):
        """
        Validate that the given value is a positive integer.

        Parameters:
        - attribute_name (str): The name of the attribute being validated.
        - value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer.")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0.")

    def validate_non_negative_integer(self, attribute_name, value):
        """
        Validate that the given value is a non-negative integer.

        Parameters:
        - attribute_name (str): The name of the attribute being validated.
        - value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer.")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0.")

    def area(self):
        """
        Public area method to return the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the Rectangle instance with '#' characters,
        considering the offset x and y.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """"Return value for str()"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                              self.x,
                                                              self.y,
                                                              self.width,
                                                              self.height)
