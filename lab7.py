# Instructions
# 1. Create a string with all 1s in it
# 2. Replace the 1s with the work "one"
# 3. Print results

import re

oneString = input("Please enter a series of 1's")

ones = re.sub(r"1", "one", oneString)

print(ones)