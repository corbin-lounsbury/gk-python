# Instructions
# Use Counter on your name

from collections import Counter

name = str(input("Please enter your name: "))

nameCounter = Counter(name)

print(nameCounter)