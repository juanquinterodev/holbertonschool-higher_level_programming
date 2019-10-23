#!/usr/bin/python3
"""Module to inherit from Rectangle
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor
            Args:
                size (int): square size
                x (int): space left
                y (int): space above
                id (int): id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """attributes
            Args:
                *args: pointer to argument list
                **kwargs: double pointer to a dictionary: key/value
        """
        if args:
            for arg, obj in zip(args, range(4)):
                if obj is 0:
                    self.id = arg
                if obj is 1:
                    self.size = arg
                if obj is 2:
                    self.x = arg
                if obj is 3:
                    self.y = arg
                if obj is None:
                    break
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
