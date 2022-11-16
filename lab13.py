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

customer1 = Customer("Corbin", 32, "Janitor", 7125938)

customer2 = Customer("Mike", 57, "CPA", 687564)

customer1.printStats()
customer2.printStats()