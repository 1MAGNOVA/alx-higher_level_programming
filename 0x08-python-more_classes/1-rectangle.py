#!/usr/bin/python3
"""defines a class rectangle with  attributes width, height"""


class Rectangle:
    """ contains attributes: width, height as @properties"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle props"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """this gets the private instance for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this sets the value of attribute width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this gets the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this sets the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
