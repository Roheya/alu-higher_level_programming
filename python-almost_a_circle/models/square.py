#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self): return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        attrs = ["id", "size", "x", "y"]
        for i, val in enumerate(args):
            setattr(self, attrs[i], val)
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
