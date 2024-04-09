import math
import unittest


class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        area = math.pi * radius ** 2
        return area

    @staticmethod
    def triangle_area(side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Длины не могут быть отрицательными")
        if ShapeCalculator.is_right_triangle(side1, side2, side3):
            sides = [side1, side2, side3]
            sides.remove(max(sides))
            area = sides[0] * sides[1] / 2
        else:
            s = (side1 + side2 + side3) / 2
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        max_side = max(sides)
        sides.remove(max_side)
        return math.isclose(max_side ** 2, sides[0] ** 2 + sides[1] ** 2, rel_tol=1e-9)

    @staticmethod
    def universal_area(*sides):
        if len(sides) == 1:
            return ShapeCalculator.circle_area(sides[0])
        if len(sides) == 3:
            return ShapeCalculator.triangle_area(sides[0], sides[1], sides[2])
        else:
            return None

    # Юнит-тесты


class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self): # Площадь круга
        self.assertAlmostEqual(ShapeCalculator.circle_area(5), 78.54, places=2)

    def test_triangle_area(self): # Площадь треугольника
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self): # Площадь прямоугольного треугольника
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6)

    def test_universal_area(self): # Площадь неизвестной фигуры
        self.assertAlmostEqual(ShapeCalculator.universal_area(5), 78.54, places=2)
        self.assertAlmostEqual(ShapeCalculator.universal_area(3, 4, 5), 6)


if __name__ == "__main__":
    unittest.main()
