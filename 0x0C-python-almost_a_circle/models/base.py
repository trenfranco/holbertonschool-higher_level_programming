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
        a = json.dumps(list_dictionaries)
        return a
