from abc import ABC, abstractmethod
import math

# TODO: Implement the Shape class
class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError


class Rectangle(Shape):
    # TODO: Initialise the constructor
    def __init__(self, length, width):
        self.lenght = length
        self.width = width


    # TODO: Implement the `area` function
    def area(self):
        return self.lenght * self.width
        

    # TODO: Implement the `perimeter` function
    def perimeter(self):
        return 2 * (self.lenght + self.width)



# TODO: Implement the Circle class along with the incomplete functions
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return (math.pi * (self.radius ** 2))


    def perimeter(self):
        return 2 * (math.pi * self.radius)



# Example usage
rectangle = Rectangle(5, 4)
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 20
print("Rectangle perimeter:", rectangle.perimeter())  # Output: Rectangle perimeter: 18

circle = Circle(3)
print("Circle area:", circle.area())  # Output: Circle area: 28.274333882308138
print("Circle perimeter:", circle.perimeter())  # Output: Circle perimeter: 18.84955592153876
