"""
Практическая работа №16
Вариант 30 — Блок 2
Базовый класс "Фигура", классы "Прямоугольник" и "Квадрат"
"""


class Figure:
    """Базовый класс фигуры."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Rectangle(Figure):
    """Класс прямоугольника."""

    pass


class Square(Figure):
    """Класс квадрата."""

    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return 4 * self.width


# Тестовый запуск
rectangle = Rectangle(10, 5)
print("Прямоугольник")
print("Площадь:", rectangle.area())
print("Периметр:", rectangle.perimeter())

print()

square = Square(7)
print("Квадрат")
print("Площадь:", square.area())
print("Периметр:", square.perimeter())
