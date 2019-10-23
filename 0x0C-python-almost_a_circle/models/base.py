#!/usr/bin/python3
""" import json module """
import json
import os
import csv


class Base:
    """ PATERN CLASS """
    __nb_objects = 0
    """ private class attribute """

    def __init__(self, id=None):
        """ assign the new value to the public instance attribute id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method to send list dictionaries to the json string """
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

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        n_list = []

        if not json_string or json_string is None:
            return n_list

        n_list = json.loads(json_string)
        return n_list

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == "Rectangle":
            new_ins = cls(10, 5)
        elif cls.__name__ == "Square":
            new_ins = cls(10)

        new_ins.update(**dictionary)

        return new_ins

    @classmethod
    def load_from_file(cls):
        '''return a list of instances'''

        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json') as _file:
                to_json = _file.read()
            dict_list = Base.from_json_string(to_json)
            obj_list = list()
            for sutanito in dict_list:
                obj_list.append(cls.create(**sutanito))
            return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save in CSV file'''

        if cls.__name__ == 'Rectangle':
            _file = 'Rectangle.csv'
            headers = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            _file = 'Square.csv'
            headers = ['id', 'size', 'x', 'y']
        with open(_file, 'w') as fil:
            csv_writer = csv.DictWriter(fil, fieldnames=headers)
            csv_writer.writeheader()
            for row in list_objs:
                dict_row = row.to_dictionary()
                csv_writer.writerow(dict_row)

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes from csv'''

        if cls.__name__ == 'Rectangle':
            _file = 'Rectangle.csv'
        elif cls.__name__ == 'Square':
            _file = 'Square.csv'
        list_csv = []
        dict_csv = {}
        with open(_file) as f:
            dic_reader = csv.DictReader(f)
            for row in dic_reader:
                for key, value in row.items():
                    dict_csv[key] = int(value)
                list_csv.append(cls.create(**dict_csv))
            return list_csv
