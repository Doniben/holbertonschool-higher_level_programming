#!/usr/bin/python3
""" import patern class """
from models.base import Base


class Rectangle(Base):
    """ DEFINES INHERITANCE CLASS """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes values for the rectangle """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieves the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ Retrieves the width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieves the x """

        return self.__x

    @x.setter
    def x(self, value):
        """ Retrieves the x """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieves the y """

        return self.__y

    @y.setter
    def y(self, value):
        """ Retrieves the y """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the rectangles area """

        return self.width * self.height

    def display(self):
        """Printing the instance to stdout with #"""

        print("\n" * self.y, end="")
        for i in range(self.height):
                print(" " * self.x, end="")
                print("#" * self.width)

    def __str__(self):
        """ Retrieves the str """

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Retrieves the args """

        count_args = 0
        list_args = ["id", "width", "height", "x", "y"]
        for each_arg in args:
            setattr(self, list_args[count_args], each_arg)
            count_args += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle """

        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
