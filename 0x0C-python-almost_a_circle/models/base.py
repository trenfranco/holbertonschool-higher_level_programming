#!/usr/bin/python3
"""New class"""


import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionaries to json string"""
        if list_dictionaries is None or list_dictionaries is {}:
            a = "[]"
        else:
            a = json.dumps(list_dictionaries)
        return a

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        a = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                a.append(i.to_dictionary())
        if a == []:
            a = "[]"
        else:
            a = cls.to_json_string(a)
        with open(filename, 'w') as txt:
            txt.write(a)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None:
            a = []
        else:
            a = json.loads(json_string)
        return a
