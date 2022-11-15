# Instructions
# 1. Create a closure that takes one argument and returns and squares it
#       a. Create your outer function
#       b. Create your inner function
#       c. Create your calling function

number = int(input("Please enter a number: "))

def outerFunc(outerVar):
    def innerFunc():
        print(f"You entered {outerVar}. The square is {(outerVar**2)}")
        outerVar**2
    return innerFunc

callerFunc = outerFunc(number)

callerFunc()