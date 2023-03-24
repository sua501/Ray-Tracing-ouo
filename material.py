from color import Color
# from hittable import HitRecord
from ray import Ray


class Material:
    # def scatter(self, r: Ray, rec: HitRecord, color: Color, scattered: Ray):
    def scatter(self, r: Ray, rec, color: Color, scattered: Ray):
        pass
