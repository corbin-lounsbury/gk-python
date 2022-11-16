class Human:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.isMammal = True
    def displayStats(self):
        print("Name: " + self.name)
        print("Health: " + str(self.health))

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