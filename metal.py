from color import Color
from material import Material
from ray import Ray
from hittable import HitRecord
from vec import Vec


class Metal(Material):
    def __init__(self, color: Color):
        self.albedo = color

    def scatter(self, r: Ray, rec: HitRecord, color: Color, scattered: Ray):
        reflected = Vec.reflect(r.direction.unit_vector(), rec.normal)
        scattered.set(rec.point, reflected)
        color.set(self.albedo)
        return scattered.direction.dot(rec.normal) > 0
