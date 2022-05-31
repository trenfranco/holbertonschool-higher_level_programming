#!/usr/bin/python3
"""Class to JSON"""


import json


def class_to_json(obj):
    """class_to_json"""
    return obj.__dict__
