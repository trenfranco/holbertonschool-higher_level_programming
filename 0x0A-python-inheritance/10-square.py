#!/usr/bin/python3
"""New class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """New class inhereted form rect"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)

