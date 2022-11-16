import datetime

class Customer:
    animalClass = "Human"
    def __init__(self, name, birthYear, occupation, rewardsNumber):
        self.name = name
        self.birthYear = int(birthYear)
        self.occupation = occupation
        self.rewardsNumber = str(rewardsNumber)
    
    def printStats(self):
        print(self.name)
        print(self.animalClass)
        print(self.age)
        print(self.occupation)
        print(self.rewardsNumber)

    @staticmethod
    def calculateAge(self):
        today = datetime.date.today()
        age = today.year - self.birthYear
        return age

    @classmethod
    def isAdult(cls,age):
        return age > 17

class Car:
    def __init__(self, make, model, year, color, msrp):
        self.make = make
        self.model = model
        self.year = int(year)
        self.color = color
        self.msrp = float(msrp)



person = Customer("Corbin", 1990, "janitor", 398457)

personAge = person.calculateAge(person)

isAdult = person.isAdult(personAge)

thisCar = Car("Ford", "F150", 2019, "white", 59999)

print(thisCar.__dict__)