# Instructions
# 1. Write a program to look through each line in the file. 
# 2. Create a file
# 3. Check if any line starts with "hi", if so, print hello in the console, else print the line

import os
import fileinput

currentDir = os.getcwd()
testFile = currentDir + "\\mod3-misclabs\\test.txt"

for line in fileinput.input(files=testFile):
    if line.startswith("hi"):
        print("Hello")
    else:
        print(line)