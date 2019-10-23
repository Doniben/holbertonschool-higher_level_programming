#!/usr/bin/python3
""" Module Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes values """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ initializes str """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Retrieves size """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Uses args """
        count_args = 0
        list_args = ["id", "size", "x", "y"]
        for each_arg in args:
            setattr(self, list_args[count_args], each_arg)
            count_args += 1
        for key, value in kwargs.items():
            if key == "size":
                self.width = value
                self.height = value
            else:
                setattr(self, key, value)

    def to_dictionary(self):
        """ sends to dictionary """
        square_dictionary = dict(id=self.id,
                                 size=self.size,
                                 x=self.x,
                                 y=self.y)
        return square_dictionary
