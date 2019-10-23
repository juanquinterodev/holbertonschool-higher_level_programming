#!/usr/bin/python3
"""Module to inherit from Base
"""


from .base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructors
            Args:
                width (int): rectangle width
                height (int): rectangle height
                x (int): space left
                y (int): space above
                id (int): unique id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """X getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """X setter
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle with #
        """
        for s in range(self.__y):
            print()
        for r in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """an argument to each attribute or a key/value
            argument to attributes
            Args:
                *args: pointer to a argument list
                **kwargs: double pointer to a dictionary: key/value
        """
        if args:
            for arg, obj in zip(args, range(5)):
                if obj is 0:
                    self.id = arg
                if obj is 1:
                    self.width = arg
                if obj is 2:
                    self.height = arg
                if obj is 3:
                    self.x = arg
                if obj is 4:
                    self.y = arg
                if obj is None:
                    break
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
