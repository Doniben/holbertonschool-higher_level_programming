#!/usr/bin/python3


class Base:
    """ FIRST CLASS """
    __nb_objects = 0
    """ private class attribute """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        """ assign the public instance attribute id with it value """
        else:
            __nb_objects += 1
        self.id = Base.__nb_objects
        """ assign the new value to the public instance attribute id """
