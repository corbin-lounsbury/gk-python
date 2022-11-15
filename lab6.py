# Instructions
# 1. Create a try block
# 2. Create an except block
# 3. Create an else block
# 4. Create a finally block

try:
    myNum = int(input("Please enter a number: "))

except Exception as errorMessage:
    print(f"You didn't enter a valid number. Error message {errorMessage}")

else:
    print(f"The number you entered is {myNum}")

finally:
    print("The end!")