# Instructions

# 1. Create the class Car

# 2. Add a class/static variable

# 3. Create a class/static attributes

# 4. Create a class method

# 5. create a static method using @staticmethod

# 6. Instantiate an object

# 7. Print the static variable, class method, and static method of an object


class Car:
    def __init__(self, make, model, year, color, msrp):
        self.make = make
        self.model = model
        self.year = int(year)
        self.color = color
        self.msrp = float(msrp)

    def yearMade(self):
        print (f"This car was made in {self.year}")

    @staticmethod
    def calculateAge(thisYear, carYear):
        print(f"This car is {(thisYear-carYear)} years old")

    @staticmethod
    def calculateDepreciation(thisYear, carYear, msrp):
        firstYearDeprec = msrp * .20
        firstYearVlaue = msrp - firstYearDeprec
        deprecValue = .15
        numYears = (thisYear-carYear) - 1
        deprecTotal = firstYearVlaue - (firstYearVlaue * (numYears * deprecValue))

        print(f"This car's estimated value after {(thisYear-carYear)} years depreciation is ${deprecTotal:.2f}")



thisCar = Car("Ford", "F150", 2019, "white", 60000)

print(f"This is a {thisCar.color} {thisCar.make} {thisCar.model}. Original price when new was {thisCar.msrp}")

thisCar.yearMade()

thisCar.calculateAge(2022, thisCar.year)
thisCar.calculateDepreciation(2022, thisCar.year, thisCar.msrp)