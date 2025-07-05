import math

class Tire:
    def __init__(self, width, aspect_ratio, diameter):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.diameter = diameter

    def volume(self):
        val_1 = 10000000000
        val_2 = 2540
        sval_1 = self.width * self.aspect_ratio + val_2 * self.diameter
        sval_2 = math.pi * (self.width ** 2) * self.aspect_ratio * sval_1
        return sval_2 / val_1

    def __str__(self):
        return f"Tire(width={self.width}, aspect_ratio={self.aspect_ratio}, diameter={self.diameter})"