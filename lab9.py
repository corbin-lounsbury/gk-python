number = int(input("Please enter a number: "))

def outerFunc(outerVar):
    def innerFunc():
        print(f"You entered {outerVar}. The square is {(outerVar**2)}")
        outerVar**2
    return innerFunc

callerFunc = outerFunc(number)

callerFunc()