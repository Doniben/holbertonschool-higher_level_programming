#!/usr/bin/python3
import json


class Base:
    """ PATERN CLASS """
    __nb_objects = 0
    """ private class attribute """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        """ assign the new value to the public instance attribute id """

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Returning json representation of the dictionaries list """
        file_name = cls.__name__ + ".json"
        n_list = []
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write(n_list)

            for i in list_objs:
                n_list.append(i.to_dictionary())

            str_json = ""
            str_json = cls.to_json_string(n_list)

            f.write(str_json)
