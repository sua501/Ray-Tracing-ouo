from color import Color
from hittable import HitRecord
from material import Material
from ray import Ray
from vec import Vec


class Glass(Material):
    def __init__(self, ir):
        self.ir = ir

    def scatter(self, r: Ray, rec: HitRecord, color: Color, scattered: Ray):
        ratio = 1/self.ir if rec.front_face else self.ir
        unit_dirction = r.direction.unit_vector()
        refracted = Vec.refract(unit_dirction, rec.normal, ratio)
        scattered = Ray(rec.point, refracted)
        scattered.set(rec.point, refracted)
        color.set(Color(1, 1, 1))
        return True
