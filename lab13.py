# Instructions

# 1. Create a class customer

# 2. Create class attributes

# 3. Create object attributes

# 4. Instantiate an object with its unique attributes

# 5. Print the results

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

customer1 = Customer("Corbin", 32, "Janitor", 8675309)

customer2 = Customer("Mike", 57, "CPA", 687564)

customer1.printStats()
customer2.printStats()