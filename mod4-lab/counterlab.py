# Instructions
# Use Counter on your name

name = str(input("Please enter your name: "))

uniqueItems = {}
for item in name:
    if item in uniqueItems:
        uniqueItems[item] = uniqueItems[item]+1
    else:
        uniqueItems[item] = 1

print(uniqueItems)

from collections import Counter
nameCounter = Counter(name)
print(nameCounter)