#!/usr/bin/python3
"""
Square is a special Rectangle
methods:
def __init__(self, size, x=0, y=0, id=None):
def __str__(self):
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of Square class attributes
        :param size:
        :param x:
        :param y:
        :param id:
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the formatted string representation
        of the square class
        :return:
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.__height)

    @property
    def size(self):
        """
        returns the height of the square
        :return:
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Assigning with and height to the same value
        :return:
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Square updates
        using args and kwargs
        """
        new_args = [self.id, self.size, self.x, self.y]
        if len(args) == 0 or args is None:
            if len(kwargs) == 0:
                return
            else:
                try:
                    new_args[0] = kwargs['id']
                except KeyError:
                    pass
                try:
                    new_args[1] = kwargs['size']
                except KeyError:
                    pass
                try:
                    new_args[2] = kwargs['x']
                except KeyError:
                    pass
                try:
                    new_args[3] = kwargs['y']
                except KeyError:
                    pass
        else:
            for i in range(len(args)):
                new_args[i] = args[i]
        self.__init__(new_args[1],
                      new_args[2],
                      new_args[3],
                      new_args[0])

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        :return:
        """
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}
