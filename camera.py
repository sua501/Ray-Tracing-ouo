import math
import random
import sys
from ray import Ray
from vec import Vec


class Camera:
    def __init__(self, vfov, ratio,
                 lookform: Vec,
                 lookat: Vec,
                 vup: Vec):
        w = (lookform-lookat).unit_vector()
        u = vup.cross(w).unit_vector()
        v = w.cross(u).unit_vector()

        theta = math.radians(vfov)
        h = math.tan(theta / 2)
        self.viewport_h = 2*h
        self.viewport_w = self.viewport_h * ratio
        self.origin = lookform
        self.u = u * self.viewport_w
        self.v = v * self.viewport_h
        self.left_bottom = self.origin - 0.5*self.u - 0.5*self.v - w

    def get_ray(self, i, j):
        return Ray(self.origin, self.left_bottom + self.u *
                   j + self.v*i-self.origin)
