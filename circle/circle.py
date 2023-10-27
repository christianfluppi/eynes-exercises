import math


class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f"El radio del círculo debe ser un número mayor que 0 (cero) y positivo. Radio: {radius}")
        self.radius = radius

    def get_radius(self): return self.radius

    def set_radius(self, radius):
        if radius <= 0: 
            raise ValueError(f"El radio del círculo debe ser mayor que 0 (cero) y positivo. Radio: {radius}")
            self.radius = radius

    def get_area(self): return math.pi * self.radius ** 2

    def get_perimeter(self): return 2 * math.pi * self.radius

    def __mul__(self, n):
        if n <= 0: 
            raise ValueError("El número de multiplicación debe ser mayor que cero.")
        return Circle(self.radius * n)

    def __str__(self): return f"Círculo con radio: {self.radius}"
