from dataclasses import dataclass, make_dataclass

@dataclass
class Car:
    make : str
    model : str
    year : int
    color : str
    msrp : float

myCar = Car("Ford", "F150", 2019, "white", 59999)

print(myCar.__dict__)

Employee = make_dataclass("Employee", [("name", str),("age", int), ("job", str)])

myEmployee = Employee("Corbin", 32, "Janitor")

print(myEmployee.__dict__)