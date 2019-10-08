#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        getter width
        """
        return self.__width

    @property
    def height(self):
        """
        getter height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter height
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of Rectangle
        """
        return self.__height * self.width

    def perimeter(self):
        """
        Perimeter of Rectangle
        """
        if (self.__height == 0 or self.width == 0):
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """
        String Representation
        """
        tmp = ""
        for i in range(self.__height):
            if self.__width <= 0:
                tmp = " \n"
                break
            tmp = "{}{}\n".format(tmp, str(self.print_symbol) * self.__width)
        return tmp[:-1]

    def __repr__(self):
        """
        Representation of Rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest instance of Rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

     @classmethod
    def square(cls, size=0):
        """
        Create square
        """
        return cls(size, size)