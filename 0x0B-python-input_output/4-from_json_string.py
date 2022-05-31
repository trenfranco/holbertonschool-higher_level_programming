#!/usr/bin/python3
"""JSON to py data st"""


import json


def from_json_string(my_str):
    strr = json.loads(my_str)
    return strr
