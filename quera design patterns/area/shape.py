from interfaces import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area_with(self, calculator):
        return calculator.calculate_circle_area(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area_with(self, calculator):
        return calculator.calculate_rectangle_area(self)
        


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area_with(self, calculator):
        return calculator.calculate_triangle_area(self)