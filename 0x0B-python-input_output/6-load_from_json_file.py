#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """new obj"""
    with open(filename) as txt:
        a = json.load(txt)
