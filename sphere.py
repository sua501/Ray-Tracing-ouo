from hittable import Hittable, HitRecord
from material import Material
from ray import Ray


class Sphere(Hittable):
    def __init__(self, center, radius, matt: Material):
        self.matt = matt
        self.center = center
        self.radius = radius

    def hit(self, tmin, tmax, r: Ray, record: HitRecord):
        oc = r.start_point-self.center
        a = r.direction.length_square()
        h = r.direction.dot(oc)
        c = oc.length_square()-self.radius**2
        d = h**2-a*c
        if d < 0:
            return False
        t = (-h - d**0.5)/a
        if t < tmin or t > tmax:
            return False
        record.t = t
        record.point = r.at(record.t)
        record.set_face_normal(r, (record.point - self.center).unit_vector())
        record.matt = self.matt
        return True
