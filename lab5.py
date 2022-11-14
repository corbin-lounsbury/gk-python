from collections import deque

letterList = ["A", "B", "C", "D", "E", "F", "G"]

letterStack = deque()

print("Adding letters")
for letter in letterList:
    letterStack.append(letter)
    print(letterStack)

print("Removing letters")

i=0
while i < len(letterStack):
    letterStack.popleft()
    if len(letterStack) > 0:
        print(letterStack)
    else:
        print(" No more letters in the stack!")