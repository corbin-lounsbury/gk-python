'''# Instructions
# Use Counter on your name'''

from collections import Counter

NAME = str(input("Please enter your name: "))

nameCounter = Counter(NAME)

print(nameCounter)
