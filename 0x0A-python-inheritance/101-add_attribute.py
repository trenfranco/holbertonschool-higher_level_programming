#!/usr/bin/python3
"""ex 101"""


def add_attribute(obj, name, value):
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
