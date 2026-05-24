from abc import ABC, abstractmethod
import math

class Person:
    def __init__(self):
        self._age = 0
    def set_age(self, age):
        if age < 0 or age > 130:
            raise ValueError("Некорректный возраст")
        self._age = age
    def get_age(self):
        return self._age
p = Person()
age = int(input("Введите возраст: "))
try:
    p.set_age(age)
    print(p.get_age())
except ValueError as e:
    print(e)



class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "I'm an animal"
class Dog(Animal):
    def speak(self):
        return ("WOOF!!")
class Cat(Animal):
    def speak(self):
        return ("MEOW!!")
dog = Dog("Scooby")
cat = Cat("Belka")
print(dog.name, dog.speak())
print(cat.name, cat.speak())



class Vehicle:
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is driving"
car = Car()
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"
bike = Bicycle()

def move(vehicle):
    return vehicle.move()

print(car.move())
print(bike.move())



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rect = Rectangle(15,7)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
circle = Circle(6)
print(rect.area())
print(circle.area())