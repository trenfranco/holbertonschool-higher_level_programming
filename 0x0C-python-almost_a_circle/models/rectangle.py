#!/usr/bin/python3
"""New class"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/" +
                f"{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        size = len(args)
        if size > 0:
            if size > 0:
                self.id = args[0]
            if size > 1:
                self.__width = args[1]
            if size > 2:
                self.__height = args[2]
            if size > 3:
                self.__x = args[3]
            if size > 4:
                self.__y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v
                if k == "id":
                    self.id = v

    def to_dictionary(self):
        """returns a dict"""
        a = dict()
        a = {'x': self.x, 'y': self.y, 'id': self.id,
             'height': self.height, 'width': self.width}
        return a
