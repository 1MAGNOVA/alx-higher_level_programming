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
        """setter: the value of attribute width"""
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
        """setter: the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """solves and returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """solves and returns the perimeter of a rectangle"""
        if (self.__width) == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        total = ""
        if self.__height == 0 or self.width == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i is not self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
