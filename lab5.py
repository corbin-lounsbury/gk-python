# instructions
# 1. Using deque, create a stack that adds the first 6 letters alphabetically (use appendleft() )
# 2. Remove each letter from the stack (use popleft() and print() )
# 3. When there are no more letters, print "No more letters in the stack".

from collections import deque

letterList = ["A", "B", "C", "D", "E", "F", "G"]

letterStack = deque()

print("Adding letters")
for letter in letterList:
    letterStack.appendleft(letter)
    print(letterStack)

print("Removing letters")

i=0
while i < len(letterStack):
    letterStack.popleft()
    if len(letterStack) > 0:
        print(letterStack)
    else:
        print(" No more letters in the stack!")