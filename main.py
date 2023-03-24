from camera import Camera
from color import Color
from glass import Glass
from lambertian import Lambertian
from metal import Metal
from vec import Vec
from ray import Ray
from sphere import Sphere
from hittable import HittableList, HitRecord
import random
import math
import sys

MAX_DEPTH = 10
SAMPLES_PER_PIXEL = 1
RATIO = 4/3


def random_scene():
    world = HittableList()
    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    world.append(Sphere(Vec(0, -10000, 0), 10000, material_ground))
    for i in range(-11, 11):
        for j in range(-11, 11):
            material = 0
            if random.choice([0, 1]) == 0:
                material = Lambertian(
                    Color(random.random(), random.random(), random.random()))
            else:
                material = Metal(
                    Color(random.random(), random.random(), random.random()))
            x = i + random.random()*0.9
            y = 0.2
            z = j + random.random()*0.9
            world.append(Sphere(Vec(x, y, z), 0.2, material))
    world.append(Sphere(Vec(0, 1, 0), 1, Lambertian(Color(0.4, 0.2, 0.1))))
    world.append(Sphere(Vec(-4, 1, 0), 1, Lambertian(Color(0.7, 0.6, 0.5))))
    world.append(Sphere(Vec(4, 1, 0), 1, Metal(Color(0.8, 0.2, 0.1))))
    return world


camera = Camera(90, RATIO, Vec(13, 2, 3), Vec(0, 0, 0), Vec(0, 1, 0))


image_height = 300
image_witdh = int(image_height * RATIO)

world = random_scene()

material_ground = Lambertian(Color(0.8, 0.8, 0.0))
# material_center = Glass(1.2)  # Color(0.7, 0.3, 0.3))
# material_left = Glass(1.4)  # Color(0.8, 0.8, 0.8))
# material_right = Metal(Color(0.8, 0.6, 0.2))
# world.append(Sphere(Vec(0, 0, -1), 3, material_center))
# world.append(Sphere(Vec(-1, 0, -1), 0.5, material_left))
# world.append(Sphere(Vec(1, 0, -1), 0.5, material_right))
# world.append(Sphere(Vec(0, -100.5, -1), 100, material_ground))

print("P3")
print(image_witdh, image_height)
print("255")


def ray_color(r: Ray, depth):
    if depth <= 0:
        return Color(0, 0, 0)
    rec = HitRecord(Vec(0, 0, 0), Vec(0, 0, 0), -1, material_ground)
    if world.hit(0.001, math.inf, r, rec) == True:
        scattered = Ray(Vec(1, 1, 1), Vec(1, 1, 1))
        att = Color(1, 1, 1)
        if rec.matt.scatter(r, rec, att, scattered) == True:
            c = ray_color(scattered, depth - 1)
            return Color(att.r * c.r, att.g * c.g, att.b * c.b)
        return Color(0, 0, 0)

    else:
        t = (r.direction.unit_vector().y+1)*0.5
        return (1-t)*Color(1, 1, 1) + t*Color(0.5, 0.7, 1)
    # 밤 return (1-t)*Color(4/16, 4/16, 8/16) + t*Color(1/16, 2/16, 5/16)
    # 낮 return (1-t)*Color(1, 1, 1) + t*Color(0.5, 0.7, 1)
    # 노을 return (1-t)*Color(15/16, 4/16, 3/16) + t*Color(3/16, 2/16, 5/16)
    # 무지개공 return (Color(1, 1, 1) + rec.normal) / 2


for i in range(image_height - 1, -1, -1):
    print(f'\r{i}   ', end='', file=sys.stderr)
    for j in range(image_witdh):
        c = Color(0, 0, 0)
        for _ in range(SAMPLES_PER_PIXEL):
            u = (i + random.random()) / (image_height-1)
            v = (j + random.random()) / (image_witdh-1)
            r = camera.get_ray(u, v)
            c += ray_color(r, MAX_DEPTH)

        c /= SAMPLES_PER_PIXEL
        print(c)  # ray_color(r, MAX_DEPTH))
