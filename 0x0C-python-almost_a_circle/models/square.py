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

    @property
    def size(self):
        """getter prop"""
        return self.width

    @size.setter
    def size(self, value):
        """setter prop"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update to square"""
        if len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.width = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    self.id = v

    def to_dictionary(self):
        """dict returns representation"""
        a = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
        return a
