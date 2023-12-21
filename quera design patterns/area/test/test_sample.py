import unittest
from shape import *
from area_calculator import *


class TestVisitorPattern(unittest.TestCase):

    def test_circle_initialization(self):
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)

    def test_circle_area(self):
        circle = Circle(5)
        calculator = AreaCalculator()
        self.assertEqual(circle.calculate_area_with(calculator), math.pi * 25)