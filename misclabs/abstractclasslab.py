# Instructions

# 1. Write a program to implement abastract base class

# 2. Create an abstract class with an abstract method

# 3. Create separate classes for different shares and print the number of sides

# 4. Print the results

from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def howManySides(self):
        pass

class Square(Shape):
    def howManySides(self):
        print("Squares have 4 sides")

class Dodecagon(Shape):
    def howManySides(self):
        print("Dodecagons have 12 sides")

class Circle(Shape):
    def howManySides(self):
        print("Circles don't have any sides")

shape1 = Square()
shape1.howManySides()

shape2 = Square()
shape2.howManySides()

shape3 = Square()
shape3.howManySides()