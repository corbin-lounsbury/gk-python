# Instructions
# 1. Write a program to count unique objects in a dataset using different ways
# 2. Use for loop, counter variable, and get method
# 3. Use for loop and counter variable
# 4. Use defaultdict
# 5. finally import counter method from collections module to countt unique objects

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