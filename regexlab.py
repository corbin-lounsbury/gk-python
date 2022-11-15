

import re

# 1. Write a program to extract all the numbers from "hello 12 hi 89 how 34"

wholeString = "hello 12 hi 89 how 34"

numString= re.split(r"[A-Za-z]", wholeString)

print(numString)


# 2. Write a program to split the string only at the first occurrence of a digit from "hello 12 hi 89 how 34"
firstNumString = re.split(r'\d', wholeString, 1)

print(firstNumString)

# 3. Write a program to replace 'o' with '2' in thi string only once "hello 12 hi 19 how 14"
wholeString = "hello 12 hi 19 how 14"

replace2O = re.sub(r'o', "2", wholeString, 1)

print(replace2O)

# 4. Write a program to return the first occurrence of a 2-digit number in the following string "hello 12 hi 19 how 14"
findNum = re.search(r"[0-9][0-9]", wholeString)

print(findNum)