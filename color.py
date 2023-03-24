import sys
from vec import Vec


class Color(Vec):
    def __init__(self, r, g, b):
        super().__init__(r, g, b)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def set(self, color):
        self.x = color.x
        self.y = color.y
        self.z = color.z

    def __str__(self):
        try:
            r = int(self.r ** 0.5 * 255)
            g = int(self.g ** 0.5 * 255)
            b = int(self.b ** 0.5 * 255)
            return f"{r} {g} {b}"
        except:
            print(f'Error {self.r} {self.g} {self.b}', file=sys.stderr)
