import math

width = float(input("Enter the width of the tire in mm (ex 205):"))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60):"))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15):"))

val_1 = 10000000000
val_2 = 2540

sval_1 = width * aspect_ratio + val_2 * diameter
sval_2 = math.pi * pow(width, 2) * aspect_ratio * sval_1
tire_volume = sval_2 / val_1
print(f"The approximate volume is {tire_volume:.2f} liters")