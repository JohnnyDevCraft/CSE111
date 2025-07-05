import math
from datetime import datetime

class Tire:
    DIAMETER_REQ = "Enter the diameter of the wheel in inches (ex 15):"
    WIDTH_REQ = "Enter the width of the tire in mm (ex 205):"
    ASPECT_RATIO_REQ = "Enter the aspect ratio of the tire (ex 60):"

    VAL_1 = 10000000000
    VAL_2 = 2540

    def __init__(self):
        self.diameter = 0.0
        self.width = 0.0
        self.aspect_ratio = 0.0
        self.date = datetime.now(tz=None).strftime("%Y-%m-%d")

    def calculate_volume(self):

        sval_1 = self.width * self.aspect_ratio + self.VAL_2 * self.diameter
        sval_2 = math.pi * pow(self.width, 2) * self.aspect_ratio * sval_1
        tire_volume = sval_2 / self.VAL_1
        return float(tire_volume).__round__(2)

    def set_diameter(self, diameter):
        self.diameter = diameter

    def set_width(self, width):
        self.width = width

    def set_aspect_ratio(self, aspect_ratio):
        self.aspect_ratio = aspect_ratio

    def get_diameter(self):
        return self.diameter

    def get_width(self):
        return self.width

    def get_aspect_ratio(self):
        return self.aspect_ratio

    def get_date(self):
        return self.date

    def __str__(self):
        return f"{self.date},{self.diameter:.2f},{self.width:.2f},{self.aspect_ratio:.2f},{self.calculate_volume():.2f}"

    def get_volume_str(self):
        return f"Date: {self.date}\nThe approximate volume is {self.calculate_volume():.2f} liters"

    def load_from_csv_line(self, line):
        parts = line.split(',')
        if len(parts) > 0:
            self.date = datetime.fromisoformat(parts[0]).strftime("%Y-%m-%d")
            self.diameter = float(parts[1])
            self.width = float(parts[2])
            self.diameter = float(parts[1])
            self.width = float(parts[2])
            self.aspect_ratio = float(parts[3])
        else:
            raise ValueError("Invalid CSV line format")

    def __iter__(self):
        return iter([self.date, self.diameter, self.width, self.aspect_ratio, self.calculate_volume()])

    @staticmethod
    def headers():
        return iter(["Date","Diameter", "Width", "Aspect Ratio", "Volume"])