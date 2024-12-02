from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.radius


class Triangle(Shape):

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass