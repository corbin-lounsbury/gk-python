# Instructions
# 1. Create a list that contains anything you wish, plust the list item "diamond" anywhere you wish to place it.
# 2. Loop through the list and print every value.
# 3. If the program comes across "diamond", have it print "Shine bright like a diamond".
# 4. Using the same list, create a while loop that keeps looping and printing values until it reaches "diamond".
# 5. Have your program break out of the list and print "Diamonds are forever". 

gemList = ["garnet", "bismuth", "ruby", "sapphire", "diamond", "peridot", "spinel"]

print("Starting for loop")
for gem in gemList:
    print(f"The current gem is {gem}")
    if gem == "diamond":
        print("Shine bright like a diamond!")

print("Starting while loop")
i = 0
while i < len(gemList):
    print(f"The current gem is {gemList[i]}")
    if gemList[i] == "diamond":
        break
    else:
        i+=1

print("Diamonds are forever")
