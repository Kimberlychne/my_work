
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def describe(self):
        return f"Rectangle: length={self.length}, width={self.width}, area={self.area():.2f}"


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def describe(self):
        return f"Circle: radius={self.radius}, area={self.area():.2f}"


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def describe(self):
        return f"Triangle: base={self.base}, height={self.height}, area={self.area():.2f}"
