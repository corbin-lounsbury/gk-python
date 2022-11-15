# Instructions
# 1. Create a lambda expression that prints out your argument and your argument added by 2
#   a. Use a variable that holds the lambda expression
#   b. Print the results

inArg = int(input("input a number "))

lambVar = lambda: print (f"{inArg} and {(inArg+2)}")

print(lambVar())