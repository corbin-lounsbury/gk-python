myList = [1,2,3]
myTuple = (1,2,3)
myDict = {"1":"one", "2":"two", "3":"three" }
mySet = set({1,2,3})

print("Printing data types")
print("myList is:", type(myList))
print("myTuple is:", type(myTuple))
print("myDict is:", type(myDict))
print("mySet is:", type(mySet))

print("Printing contents")
print(myList)
print(myTuple)
print(myDict)
print(mySet)

print("Adding data")
myList.append(4)
myDict["4"]="four"
mySet.add(4)

print("Printing contents with new data")
print(myList)
print(myTuple)
print(myDict)
print(mySet)