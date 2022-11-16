from abc import ABC, abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def whatMake(self):
        pass

class Mustang(Car):
    def whatMake(self):
        print("Ford makes this")

class Corvette(Car):
    def whatMake(self):
        print("Chevy makes this")

class Aventador(Car):
    def whatMake(self):
        print("Lamborghini makes this")


car1 = Mustang()
car1.whatMake()

car2 = Corvette()
car2.whatMake()

car3 = Aventador()
car3.whatMake()