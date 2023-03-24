from material import Material
from ray import Ray
from vec import Vec


class HitRecord:
    def __init__(self, point: Vec, normal: Vec, t, matt: Material):
        self.matt = matt
        self.point = point
        self.normal = normal
        self.t = t
        self.front_face = False

    def set_face_normal(self, r: Ray, normal: Vec):
        self.front_face = r.direction.dot(normal) < 0
        if self.front_face == False:
            self.normal = -1*normal
        else:
            self.normal = normal


class Hittable:
    def hit(self, tmin, tmax, r: Ray, record: HitRecord):
        pass


class HittableList(list[Hittable]):
    def hit(self, tmin, tmax, r: Ray, record: HitRecord):
        hit_anything = False
        closest = tmax

        for object in self:
            if object.hit(tmin, closest, r, record) == True:
                hit_anything = True
                closest = record.t

        return hit_anything
