from vec import Vec


class Ray:
    def __init__(self, x: Vec, y: Vec):
        self.start_point = x
        self.direction = y.unit_vector()

    def at(self, t):
        return self.start_point + t*self.direction

    def set(self, start_point: Vec, direction: Vec):
        self.start_point = start_point
        self.direction = direction


if __name__ == "__main__":
    ray1 = Ray(Vec(0, 0, 0), Vec(1, 2, 3))
    print(ray1.at(10))
