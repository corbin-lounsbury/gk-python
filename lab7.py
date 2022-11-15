# Instructions
# 1. Create a string with all 1s in it
# 2. Replace the 1s with the work "one"
# 3. Print results

import re

oneString = input("Please enter a series of 1's")

ones = re.findall(r"1", oneString)

newOnes = []
oneCount = 0

for i, one in enumerate(ones):
    if one == "1":
        print("Found a 1, converting to one")
        newOnes.append("one")
        oneCount +=1
    else:
        print(f"Not a 1, leavings as is")
        newOnes.append(one)

print(f"I found {oneCount} instances of the number 1")

result = "".join(newOnes)
print(result)