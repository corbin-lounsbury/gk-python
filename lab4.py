gemList = ["garnet", "bizmuth", "ruby", "sapphire", "diamond", "peridot", "spinel"]

print("Starting for loop")
for gem in gemList:
    print(f"The current gem is {gem}")
    if gem == "diamond":
        print("Shine bright like a diamond!")

print("Starting while loop")
i = 0
while True:
    print(f"The current gem is {gemList[i]}")
    if gemList[i] == "diamond":
        break
    else:
        i+=1

print("Diamonds are forever")
