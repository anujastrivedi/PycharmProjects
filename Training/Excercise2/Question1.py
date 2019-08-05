# Create a Circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = round(math.pi * (self.radius ** 2), 2)
        print(f"Area of Circle : {area}")

    def get_circumference(self):
        circumference = round(2 * math.pi * self.radius, 2)
        print(f"Circumference of Circle : {circumference}")


circle = Circle(10)
circle.get_area()
circle.get_circumference()
