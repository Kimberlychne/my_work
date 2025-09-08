import math

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def describe(self):
        print(f"Rectangle {self.width} by {self.height} has area {self.area():.2f}")

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
      
    def area(self):
        return math.pi * self.radius ** 2

    def describe(self):
        print(f"circle with radius {self.radius} has area {self.area():.2f}")

class Triangle:
    def __init__(self, height: float, base: float):
        self.height = height
        self.base = base

    def area(self):
        return (self.height * self.base) / 2

    def describe(self):
        print(f"Triangle with base {self.base} and height {self.height} has.area {self.area():.2f}")

