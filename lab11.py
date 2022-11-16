# Instructions

# 1. Create superclass Human

# 2. Create subclass Student

# 3. Have Student inherit from superclass Human

# 4. Create an instance 

# 5. Print the results


class Human:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.animalClass = "Mammal"
    
    def displayStats(self):
        print("Name: " + self.name)
        print(f"Health: {self.health}")
        print(f"Class in the animal Kingdom: {self.animalClass}")

class Student(Human):
    def __init__(self, name):
        super(Student, self).__init__(name)
        self.subjectsLearned = []
    
    def learnSubject(self, subject):
        self.subjectsLearned.append(subject)
    
    def displayLearnedSubjects(self):
        print(f"You know the following subjects{self.subjectsLearned}")
        

studentName = input("Please enter the student name: ")

studentObj = Student(studentName)

studentObj.displayStats()

studentObj.learnSubject("math")

studentObj.displayLearnedSubjects()