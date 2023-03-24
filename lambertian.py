from color import Color
from material import Material
from ray import Ray
from hittable import HitRecord
from vec import Vec


class Lambertian(Material):
    def __init__(self, color: Color):
        self.albedo = color

    def scatter(self, r: Ray, rec: HitRecord, color: Color, scattered: Ray):
        direction = rec.normal + Vec.random_in_unit_sphere().unit_vector()
        scattered.set(rec.point, direction)
        color.set(self.albedo)
        return True
