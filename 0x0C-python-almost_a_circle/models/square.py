#!/usr/bin/python3
"""New class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding str"""
        return (f"[Square] ({self.id}) {self.x}/{self.y}" +
                f" - {self.width}")
