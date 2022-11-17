list1 =[1,2,3,4,5,6,7,8]

# 1. Write a program to filter only the even numbers from the list using a lambda function
evenNums = filter(lambda num: num % 2 == 0, list1)

print(list(evenNums))

# 2. Write a program to create a list with the square of items that are present in the existing list using list comprehension

squareList = [num**2 for num in list1]

print(squareList)

# 3. Write a program to create a generator using generator expression and iterate through the generator to print the items.

myGenerator = (print(num) for num in list1)

for num in myGenerator: 
    next(myGenerator)

# 4. Write a program to create your own function to implement decorator and closure

# Decorator
def squareDec(inputFunc):
    def innerFunc():
        squareList = [num**2 for num in list1]
        print(squareList)
        inputFunc()
    return innerFunc

@squareDec
def SquareFunc():
    print("Squaring the list inside a decorator")

SquareFunc()

#closure
def outerFunc(outerVar):
    def innerFunc():
        print("Printing evens again in a closure")
        evenNums = filter(lambda num: num % 2 == 0, outerVar)
        print(list(evenNums))
    return innerFunc

callerFunc = outerFunc(list1)

callerFunc()
