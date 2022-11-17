import os
import fileinput

currentDir = os.getcwd()
testFile = currentDir + "\\mod3-misclabs\\test.txt"

for line in fileinput.input(files=testFile):
    if line.startswith("hi"):
        print(line)