import math

class Circle():
    def __init__(self,radius):
        if radius <= 0:
            raise ValueError(f"El radio del círculo debe ser un número mayor que 0 (cero) y positivo. Radio: {radius}")
        self.radius = radius

    
    def get_radius(self):
        return self.radius
    

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError(f"El radio del círculo debe ser un número mayor que 0 (cero) y positivo. Radio: {radius}")
        self.radius = radius


    def get_area(self):
        return 3.14159 * self.radius ** 2