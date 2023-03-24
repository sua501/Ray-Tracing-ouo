import random


class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return type(self)(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return type(self)(x, y, z)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return type(self)(x, y, z)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return type(self)(x, y, z)

    def dot(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x+y+z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return type(self)(x, y, z)

    def length(self):
        return (self.x**2+self.y**2+self.z**2)**0.5

    def length_square(self):
        return (self.x**2+self.y**2+self.z**2)

    def unit_vector(self):
        return self / self.length()

    @staticmethod
    def random():
        return Vec(random.random(), random.random(), random.random())

    @staticmethod
    def random_unit_vec():
        return Vec(random.random(), random.random(), random.random()).unit_vector()

    @staticmethod
    def random_in_unit_sphere():
        while True:
            x = Vec.random()
            if x.length() < 1:
                return x

    @staticmethod
    def reflect(direction, normal):
        return direction - direction.dot(normal)*2*normal.unit_vector()

    @staticmethod
    def refract(uv, n, etai_over_etat):
        cos_theta = min(-uv.dot(n), 1)
        r_out_perp = etai_over_etat * (uv+n*cos_theta)
        r_out_parallel = abs(1-r_out_perp.length_square())**0.5*n*-1
        return r_out_perp+r_out_parallel

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"


if __name__ == '__main__':
    v = Vec.random_in_unit_sphere()
    print(v, v.length())
