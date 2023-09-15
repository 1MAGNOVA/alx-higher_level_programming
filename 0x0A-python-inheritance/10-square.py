#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """Square class inherits from Rectangle which inherits Base_Geometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area with size"""

        return self.__size ** 2
