# Instructions
# 1. Write a program to implement methods from the inspect module.
# 2. Create a class, function, and import a module 
# 3. use different methods from the inspect module to check for class, method in the class, function, module, and built-in method from the module.
# 4. Print the resulting values

import inspect
import os

class Customer:
    animalClass = "Human"
    def __init__(self, name, age, occupation, rewardsNumber):
        self.name = name
        self.age = int(age)
        self.occupation = occupation
        self.rewardsNumber = str(rewardsNumber)
    
    def printStats(self):
        print(self.name)
        print(self.animalClass)
        print(self.age)
        print(self.occupation)
        print(self.rewardsNumber)

def inspectThings(*args):
    for thing in args:
        print(f"Inspecting {thing}")
        print(f"Is is a module? {inspect.ismodule(thing)}")
        print(f"Is it a class? {inspect.isclass(thing)}")
        print(f"Is it a function? {inspect.isfunction(thing)}")


customer1 = Customer("Corbin", 32, "Janitor", 8675309)

customer2 = Customer("Mike", 57, "CPA", 687564)

inspectThings(os,Customer,Customer.printStats,os.chmod, inspectThings, customer1, customer2)