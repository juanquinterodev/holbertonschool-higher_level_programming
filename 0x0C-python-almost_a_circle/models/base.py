#!/usr/bin/python3
"""Module Base
"""


import json
import os


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
            Args:
                id (int): id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string of list_dictionaries
            Args:
                list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string of list_objs to a file
            Args:
                cls: belonging class
                list_objs: instances who inherits of Base - example:
                            Rectangle or Square instances
        """
        filename = '{}.json'.format(cls.__name__)
        dic = []

        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))

        with open(filename, 'w', encoding='utf-8') as new:
            new.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """JSON string
            Args:
                json_string: list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes already set
            Args:
                cls: belonging class
                **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(36916, 36916)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(36916)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """list of instances
            Args:
                cls: belonging class
        """
        filename = '{}.json'.format(cls.__name__)
        instances = []

        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as new:
                content = cls.from_json_string(new.read())
            for i in content:
                instances.append(cls.create(**i))
            return instances
        else:
            return []
