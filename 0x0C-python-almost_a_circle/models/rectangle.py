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
        self.__width = value

    """Public getter and setter for width"""
    @property
    def height(self):
        return self__height

    @height.setter
    def height(self, value):
        self.__height = value

    """Public getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """Public getter and setter for y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
