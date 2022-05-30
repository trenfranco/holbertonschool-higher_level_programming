#!/usr/bin/python3
"""checks if object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Returns True or False"""
    return type(obj) != a_class and isinstance(obj, a_class)
