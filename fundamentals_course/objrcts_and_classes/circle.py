from math import pi


class Circle:
    __pi = pi

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return round(Circle.__pi * self.diameter, 1)

    def calculate_area(self):
        return round(Circle.__pi * self.diameter * self.diameter / 4, 1)

    def calculate_area_of_sector(self, angle):
        return Circle.calculate_area(self) * (angle / 360)
        # return (Circle.__pi * self.diameter * self.diameter / 4) * (angle / 360)


# Test code
circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
